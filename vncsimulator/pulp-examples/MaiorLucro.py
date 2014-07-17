"""
The Largest Profit Problem for the PuLP Modeller

Authors: Felipe Fernandes, Dr Glauco Goncalves 2014
"""
from random import randint
from pulp import *

V=10 #number of virtual machines
M=2 #number of servers
profit=[randint(20,100) for i in range(0,V)]
print("Profit:%s"%profit)
demand=[randint(10,50) for i in range(0,V)]
print("Demands:%s"%demand)
capacity=[randint(40,50) for i in range(0,M)]
print("Capacities:%s"%capacity)

vms = [ "vm%s"%i for i in range(1,V+1) ]
servers = [ "s%s"%i for i in range(1,M+1) ]

p = dict(zip(vms,profit))
d = dict(zip(vms,demand))
C = dict(zip(servers,capacity))

# Creates the 'prob' variable to contain the problem data
prob = LpProblem("Maior Lucro",LpMaximize)

# Creates a list of tuples containing all the possible 
Possible = [(vm,server) for vm in vms for server in servers]

# A dictionary called 'Vars' is created to contain the referenced variables
vars = LpVariable.dicts("x",(vms,servers),0,1,LpInteger)

##### The objective function is added to 'prob' first
prob += lpSum([p[vm]*vars[vm][server] for (vm,server) in Possible]), "Sum of profit of vms"


for server in servers:
    prob += lpSum([d[vm]*vars[vm][server] for vm in vms])<=C[server], "Sum_of_VM_demands_on_Server_%s"%server

for vm in vms:
    prob += lpSum([vars[vm][server] for server in servers])<=1, "Allocation_Constraint_of_VM_%s"%vm

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