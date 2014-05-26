from igraph import Graph,plot

def add_vertices_with_attrs(graph, n, attrs):
    for i in range(0,n):
        v = graph.vcount()
        graph.add_vertices(1)
        for key, value in attrs.iteritems():
            graph.vs[v][key] = value

def generate(caplinkbase=10000,k=6,capacity=50):
    #Create Core
    g = Graph(directed = False)
    add_vertices_with_attrs(g, (k/2)*2, {"type":"core","cap":0,"color":"black"})
    #Create Pods
    cnt=g.vcount()
    for p in range(1,k): 
        ##Create Aggregation
        add_vertices_with_attrs(g, (k/2), {"type":"aggregation","cap":0,"color":"black"})        
        links=[]
        c=0
        for l in range(1,(k/2)*2):
            c=c+1
            a= int(l/(k/2))
            links = c(links, cnt+a,c)
            g.add_edges(matrix(links,ncol=2),capacity=caplinkbase*(k/2)*(k/2))
            cnt=len(V(g))
            ##Create edge nodes
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

generate()