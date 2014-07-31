import re
from igraph import *
from pulp import *

def find_src_node(text, search):
    result = re.findall('\\b'+'\('+search+','+'\\b', text, flags=re.IGNORECASE)
    if len(result)>0:
        return True
    else:
        return False

def find_dst_node(text, search):
    result = re.findall('\\b'+','+search+'\)', text, flags=re.IGNORECASE)
    if len(result)>0:
        return True
    else:
        return False
    
def create(phyNet,Vnodes):
        G = phyNet

        #costs = [i+1 for i in G.es["nvlinks"]]
        costs = [1 for i in G.es["nvlinks"]]

        #vms = [ "vm%s"%i for i in range(1,V+1) ]
        #servers = [ "s%s"%i for i in range(1,M+1) ]
        N = ["n%s"%i for i in range(0,G.vcount())]
        A = ["e"+str(i).replace(" ", "") for i in G.get_edgelist()]
        T = ["n"+str(i) for i in Vnodes]
        c = dict(zip(A,costs))      

        Aquote = [] # the set A'
        for (i,j) in G.get_edgelist():
            Aquote.extend(["e"+str((i,j)).replace(" ", ""),"e"+str((j,i)).replace(" ", "")])
        
        deltaplus = {}
        for i in N:
            laux = []
            for e in Aquote: 
                if find_src_node(e,i[1:]):
                    laux.extend([e])
            deltaplus[i]=laux
                
        deltaminus = {}
        for i in N:
            laux = []
            for e in Aquote:
                if find_dst_node(e,i[1:]):
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
            i,j = e.replace("e(","").replace(")","").rsplit(",")
            if len(Tquote)>1:
                for s in Tquote:
                    for t in Tquote:
                        if s != t:
                            prob += lpSum([varsF[s][e],varsF[t]["e("+j+","+i+")"]])<=varsX[e], "No_Contraditory_Flows_from_"+str(s)+"_and_from_"+str(t)+"_over_"+str(e)
            else:
                s = Tquote[0]
                prob += lpSum([varsF[s][e]])<=varsX[e], "There_is_a_flow_from_"+str(s)+"_only_if_"+str(e)+"_is_used"
                prob += lpSum([varsF[s]["e("+j+","+i+")"]])<=varsX[e], "There_is_a_flow_from_"+str(s)+"_only_if_"+"e("+j+","+i+")"+"_is_used"

        # The problem data is written to an .lp file
        #prob.writeLP("Steiner Tree.lp")

        # The problem is solved using PuLP's choice of Solver
        prob.solve()
        

        # The status of the solution is printed to the screen
        #print "Status:", LpStatus[prob.status]

        # Each of the variables is printed with it's resolved optimum value
        listAux = []
        for v in prob.variables():
            #print v.name, "=", v.varValue
            if v.name[0] == "x" and v.varValue > 0:
                listAux.append(v.name); 
        
        listAux2 = []
        for i in listAux:
            RetirandoX = (i).replace("x_e(", "")
            RetirandoR = (RetirandoX).replace(")", "")  
            listAux2.append(RetirandoR); 

        c = []
        lst_phynet = []
        for i in listAux2:
            a = (int(i.split(",")[0]))
            b = (int(i.split(",")[1]))
            c += [(a,b)]
            z = G.get_eid(a,b)
            lst_phynet.append(int(z))
        
        phyNetaux = G.subgraph_edges(lst_phynet)
        del(prob)
        return phyNetaux
        # The optimised objective function value is printed to the screen    
        #print "Steiner cost = ", value(prob.objective)