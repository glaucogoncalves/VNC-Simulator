from igraph import Graph
import matplotlib.pyplot as plt
import numpy as np

from igraph import *
from random import *


#Parameters
caplinkbase=10000
k=6
capacity=50

#Create Core
g = Graph()
g.empty(directed = False)
g.add_vertices(g, (k/2)*2, type="core", cap=0, color="black", hyperedge=1)

#Create Pods
cnt=len(V(g))
for p in range(1,k): 
    ##Create Aggregation
    g.add_vertices(g, k/2, type="aggregation", cap=0, color="black", hyperedge=1)
    links= False
    c=0

    for l in range(1,(k/2)*2):
        c=c+1
        a= int(l/(k/2))
        links = c(links, cnt+a,c)
        
        g.add_edges(g, matrix(links,ncol=2),capacity=caplinkbase*(k/2)*(k/2))
        cnt=len(V(g))
        ##Create Edge
        g.add_vertices(g, k/2, type="edge", cap=0, color="black", hyperedge=1)
        links=False
        c=0
    for i in range(1,(k/2)): 
        e=cnt+i
        for j in range(1,(k/2)):
            a=(cnt-k/2)+j
            links = c(links, e,a)
        
    
    g.add_edges(g, matrix(links,ncol=2),capacity=caplinkbase*(k/2))
    cnt=len(V(g))
    ##Create Servers
    g.add_vertices(g, (k/2)*2, type="server", cap=sample(capacity,1), color="red")
    links= False
    c=0
    for i in range(1,(k/2)*2):
        s=cnt+i
        e=cnt-(k/2)+ int(i/(k/2))
        print
        links = c(links,s,e)
    
    g.add_edges(g, matrix(links,ncol=2),capacity=caplinkbase)
    cnt=len(V(g))

plot(g)

