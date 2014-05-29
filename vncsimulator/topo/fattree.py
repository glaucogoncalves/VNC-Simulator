from igraph import Graph,plot
from math import * 
from random import * 

def group(lst, n):
    """group([0,3,4,10,2,3], 2) => [(0,3), (4,10), (2,3)]
    
    Group a list into consecutive n-tuples. Incomplete tuples are
    discarded e.g.
    
    >>> group(range(10), 3)
    [(0, 1, 2), (3, 4, 5), (6, 7, 8)]
    """
    return zip(*[lst[i::n] for i in range(n)]) 

def add_vertices_with_attrs(graph, n, attrs):
    for i in range(0,n):
        v = graph.vcount()
        graph.add_vertices(1)
        for key, value in attrs.iteritems():
            graph.vs[v][key] = value
            
def add_edges_with_attrs(graph, listaArestas, attrs):
    for i in listaArestas:
        graph.add_edge(i[0],i[1])
        e = graph.get_eid(i[0],i[1])
        for key, value in attrs.iteritems():
            graph.es[e][key] = value

def generate(caplinkbase=10000,k=6,capacity=50):
    #Create Core
    g = Graph(directed = False)
    add_vertices_with_attrs(g, (k/2)*2, {"type":"core","cap":0,"color":"black"})
    #Create Pods
    cnt=g.vcount()-1
    for p in range(1,k): 
        ##Create Aggregation
        add_vertices_with_attrs(g, (k/2), {"type":"aggregation","cap":0,"color":"black"})        
        links=[]
        c=0
        for l in range(1,(k/2)*2):
            c=c+1
            a= int(ceil(l/(k/2.0)))
            links = links + [cnt+a,c]
        add_edges_with_attrs(g, group(links,2),{"capacity":caplinkbase*(k/2)*(k/2)})
        
        cnt=g.vcount()-1
        ##Create edge nodes
            
        add_vertices_with_attrs(g, (k/2), {"type":"edge","cap":0,"color":"black","hyperedge":1})
        links=[]
        c=0
        for i in range(1,(k/2)): 
            e=cnt+i
            for j in range(1,(k/2)):
                a=(cnt-k/2)+j
                links = links + [e,a]            
        add_edges_with_attrs(g, group(links,2),{"capacity":caplinkbase*(k/2)})
        cnt=g.vcount()-1
        ##Create Servers
        
        add_vertices_with_attrs(g, (k/2), {"type":"server","cap":sample(range(1,capacity),1),"color":"red"})     
        links= []
        c=0
        for i in range(1,(k/2)*2):
            s=cnt+i
            e=cnt-(k/2)+ int(i/(k/2))
            links = links + [s,e]
            print group(links,2)
        add_edges_with_attrs(g, group(links,2),{"capacity":caplinkbase})
        cnt=g.vcount()-1    
    plot(g)

generate()