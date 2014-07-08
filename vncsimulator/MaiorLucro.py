from pulp import *

conjuntos = ["vm", "cap"]

supply = {"vm": 1000,
          "cap": 4000}

Bars = ["x1", "x2", "x3", "x4", "x5"]

demand = {"x1":500,
          "x2":900,
          "x3":1800,
          "x4":200,
          "x5":700,}

costs = [   #Bars
         #1 2 3 4 5
         [2,4,5,2,1],#A   conjuntos
         [3,1,3,2,3] #B
         ]

# The cost data is made into a dictionary
costs = makeDict([conjuntos,Bars],costs,0)

# Creates the 'prob' variable to contain the problem data
prob = LpProblem("Maior Lucro",LpMaximize)

# Creates a list of tuples containing all the possible routes for transport
Routes = [(w,b) for w in conjuntos for b in Bars]

# A dictionary called 'Vars' is created to contain the referenced variables(the routes)
vars = LpVariable.dicts("Route",(conjuntos,Bars),0,None,LpInteger)


##### The objective function is added to 'prob' first
#prob += lpSum([vars[w][b]*costs[w][b] for (w,b) in Routes]), "Sum_of_Transporting_Costs"

##### The supply maximum constraints are added to prob for each supply node (warehouse)
#for w in conjuntos:
   # prob += lpSum([vars[w][b] for b in Bars])<=supply[w], "Sum_of_Products_out_of_Warehouse_%s"%w

# The demand minimum constraints are added to prob for each demand node (bar)
#for b in Bars:
    #prob += lpSum([vars[w][b] for w in conjuntos])>=demand[b], "Sum_of_Products_into_Bar%s"%b
                   


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
