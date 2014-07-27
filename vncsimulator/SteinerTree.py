"""
The Minimum Cost Steiner Tree Problem for the PuLP Modeller

Authors: Felipe Fernandes, Dr Glauco Goncalves 2014
"""
from random import randint
from igraph import *
from pulp import *
from topo import fixed
from random import sample

G = fixed.generate()
G.es["nvlinks"] = 1

print(G)

#vms = [ "vm%s"%i for i in range(1,V+1) ]
#servers = [ "s%s"%i for i in range(1,M+1) ]
N = ["n%s"%i for i in range(0,G.vcount())]
A = ["e"+str(i) for i in G.get_edgelist()]
T = ["n2","n6","n8"]
c = dict(zip(A,G.es["nvlinks"]))

Aquote = [] # the set A'
for (i,j) in G.get_edgelist():
    Aquote.extend(["e"+str((i,j)),"e"+str((j,i))])


caux = [] #c' vector
for i in G.es["nvlinks"]:
    caux.extend([i,i])
cquote = dict(zip(Aquote,caux))

deltaplus = {}
for i in N:
    laux = []
    for e in Aquote: 
        if e.find("e("+i[1:]) != -1:
            laux.extend([e])
    deltaplus[i]=laux

deltaminus = {}
for i in N:
    laux = []
    for e in Aquote: 
        if e.find(", "+i[1:]+")") != -1:
            laux.extend([e])
    deltaminus[i]=laux
    
r = T[-1]
Tquote = T[0:-1]
    
# Creates the 'prob' variable to contain the problem data
prob = LpProblem("Minimum Cost Steiner Tree",LpMinimize)

# Creates a list of tuples containing all the possible 
#Possible = [(vm,server) for vm in vms for server in servers]

# A dictionary called 'Vars' is created to contain the referenced variables
#varsX = LpVariable.dicts("x",Aquote,0,1,LpInteger)
varsX = LpVariable.dicts("x",A,0,1,LpInteger)
varsF = LpVariable.dicts("f",(Tquote,Aquote),0,None,LpContinuous)

##### The objective function is added to 'prob' first
#prob += lpSum([cquote[e]*varsX[e] for e in Aquote]), "Sum of edge costs"
prob += lpSum([c[e]*varsX[e] for e in A]), "Sum of edge costs"

for i in N:
    for t in Tquote:
        if i == t:
            termo1 = [varsF[t][edge] for edge in deltaplus[i]]
            termo2 = [-1*varsF[t][edge] for edge in deltaminus[i]]
            prob += lpSum(termo1+termo2)==1, "Sum_of_Flow_"+str(t)+"_on_node_"+str(i)
        elif i == r:
            termo1 = [varsF[t][edge] for edge in deltaplus[i]]
            termo2 = [-1*varsF[t][edge] for edge in deltaminus[i]]
            prob += lpSum(termo1+termo2)==-1, "Sum_of_Flow_"+str(t)+"_on_node_"+str(i)
        else:
            termo1 = [varsF[t][edge] for edge in deltaplus[i]]
            termo2 = [-1*varsF[t][edge] for edge in deltaminus[i]]
            prob += lpSum(termo1+termo2)==0, "Sum_of_Flow_"+str(t)+"_on_node_"+str(i)    

for e in A:
    i,j = e.replace("e(","").replace(")","").replace(" ","").rsplit(",")
    for s in Tquote:
        for t in Tquote:
            if s != t:
                prob += lpSum([varsF[s][e],varsF[t]["e("+j+", "+i+")"]])<=varsX[e], "No_Contraditory_Flows_from_"+str(s)+"_and_from_"+str(t)+"_over_"+str(e)

#prob += varsX["e(1, 2)"] == 1
#prob += varsX["e(1, 3)"] == 1
#prob += varsF["n1"]["e(1, 3)"] == 1
#prob += varsF["n2"]["e(2, 1)"] == 1
#prob += varsF["n2"]["e(1, 3)"] == 1


# The problem data is written to an .lp file
prob.writeLP("Steiner Tree.lp")

# The problem is solved using PuLP's choice of Solver
prob.solve()

# The status of the solution is printed to the screen
print "Status:", LpStatus[prob.status]

# Each of the variables is printed with it's resolved optimum value
for v in prob.variables():
    print v.name, "=", v.varValue

# The optimised objective function value is printed to the screen    
print "Steiner cost = ", value(prob.objective)
