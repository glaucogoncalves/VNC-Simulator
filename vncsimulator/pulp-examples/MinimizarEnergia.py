"""
The Minimize Energy Problem for the PuLP Modeller

Authors: Felipe Fernandes, Dr Glauco Goncalves 2014
"""
from random import randint
from pulp import *

V=5 #number of virtual machines
M=2 #number of servers
profit=[randint(20,100) for i in range(0,V)]
print("Profit:%s"%profit)
demand=[randint(10,50) for i in range(0,V)]
print("Demands:%s"%demand)
capacity=[randint(40,50) for i in range(0,M)]
print("Capacities:%s"%capacity)
energycost=[randint(60,100) for i in range(0,M)]
print("Energy Cost:%s"%energycost)

#demand=[10,30,10,10,20]
#capacity=[80,30]

vms = [ "vm%s"%i for i in range(1,V+1) ]
servers = [ "s%s"%i for i in range(1,M+1) ]

p = dict(zip(vms,profit))
d = dict(zip(vms,demand))
C = dict(zip(servers,capacity))
w = dict(zip(servers,energycost))

# Creates the 'prob' variable to contain the problem data
prob = LpProblem("Minimize Energy",LpMaximize)

# Creates a list of tuples containing all the possible 
Possible = [(vm,server) for vm in vms for server in servers]

# A dictionary called 'Vars' is created to contain the referenced variables
Xvars = LpVariable.dicts("x",(vms,servers),0,1,LpInteger)
Yvars = LpVariable.dicts("y",servers,0,1,LpInteger)

##### The objective function is added to 'prob' first
lst1 =[p[vm]*Xvars[vm][server] for (vm,server) in Possible]
lst2 =[w[server]*(1-Yvars[server]) for server in servers]  
prob += lpSum(lst1+lst2), "Total Profit"

for server in servers:
    prob += lpSum([d[vm]*Xvars[vm][server] for vm in vms])<=Yvars[server]*C[server], "Sum_of_VM_demands_on_Server_%s"%server

for vm in vms:
    prob += lpSum([Xvars[vm][server] for server in servers])<=1, "Allocation_Constraint_of_VM_%s"%vm

#prob += lpSum([Yvars[server] for server in servers])<=M, "Sanity check"
# The problem data is written to an .lp file
prob.writeLP("MinimizarEnergia.lp")

# The problem is solved using PuLP's choice of Solver
prob.solve()

# The status of the solution is printed to the screen
print "Status:", LpStatus[prob.status]

# Each of the variables is printed with it's resolved optimum value
for v in prob.variables():
    print v.name, "=", v.varValue

# The optimised objective function value is printed to the screen    
print "Total Profit = ", value(prob.objective)