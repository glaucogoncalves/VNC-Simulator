from pulp import *

conjuntos = ["vm", "cap"]

supply = {"vm": 100,
          "cap": 200}

Vars = ["x1", "x2", "x3", "x4", "x5"]

demand = {"x1":0,
          "x2":1,
          "x3":1,
          "x4":0,
          "x5":1,}

costs = [   #Vars
         #1 2 3 4 5
         [1,1,0,1,0],#A   conjuntos
         [0,0,0,0,0,1] #B
         ]

# The cost data is made into a dictionary
costs = makeDict([conjuntos,Vars],costs,0)

# Creates the 'prob' variable to contain the problem data
prob = LpProblem("Maior Lucro",LpMaximize)

# Creates a list of tuples containing all the possible 
Routes = [(w,b) for w in conjuntos for b in Vars]

# A dictionary called 'Vars' is created to contain the referenced variables
vars = LpVariable.dicts("Route",(conjuntos,Vars),0,None,LpInteger)


##### The objective function is added to 'prob' first
prob += lpSum([vars[w][b]*costs[w][b] for (w,b) in Routes]), "Soma_das_Vars"

for w in conjuntos:
    for b in Vars:
        #####  prob += lpSum([vars[w][c] for c in Vars])*lpSum([vars[d][b] for d in conjuntos])<=demand[b], "Capacidade"%w
        prob += lpSum([vars[w][c] for c in Vars])
        prob *= lpSum([vars[d][b] for d in conjuntos])<=demand[b], "Capacidade"%w


##### The supply maximum constraints are added to prob for each supply node
for w in conjuntos:
    prob += lpSum([vars[w][b] for b in Vars])<= 1, "Maquina virtual"%w

# The problem data is written to an .lp file
prob.writeLP("Maior Lucro.lp")

# The problem is solved using PuLP's choice of Solver
prob.solve()

# The status of the solution is printed to the screen
print "Status:", LpStatus[prob.status]

# Each of the variables is printed with it's resolved optimum value
for v in prob.variables():
    print v.name, "=", v.varValue

# The optimised objective function value is printed to the screen    
print "Maior Lucro = ", value(prob.objective)
