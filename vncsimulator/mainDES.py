import simpy 
from random import expovariate, seed, sample, randint
from igraph import *
from algorithms import shpalg
from algorithms import optimal

def allocate(subPhyNet,phyNet):
    usedEdges = [(subPhyNet.vs[i[0]]["name"],subPhyNet.vs[i[1]]["name"]) for i in subPhyNet.get_edgelist()]
    for e in usedEdges:
        phyNet.es[phyNet.get_eid(e[0],e[1])]["nvlinks"] = phyNet.es[phyNet.get_eid(e[0],e[1])]["nvlinks"] + 1
    return phyNet

def deallocate(subPhyNet,phyNet):
    usedEdges = [(subPhyNet.vs[i[0]]["name"],subPhyNet.vs[i[1]]["name"]) for i in subPhyNet.get_edgelist()]
    for e in usedEdges:
        phyNet.es[phyNet.get_eid(e[0],e[1])]["nvlinks"] = phyNet.es[phyNet.get_eid(e[0],e[1])]["nvlinks"] -1
    return phyNet

## Model components ------------------------
class Source(object):

    def __init__(self,env):
        self.env = env

    """ Source generates virtual networks"""        
    def generate(self,mon):
        while 1:
            vn = VirtualNetwork(self.env,mon) #<=== Change this to randomize the size of virtualnetwork
            t = expovariate(1.0/meanTimeBtwVNArrivals) #generate time to produce a new Virtual Network
            yield self.env.timeout(t)

class VirtualNetwork(object):    

    def __init__(self,env,mon):
        global phyNet
        self.env=env
        perc = 0.2
        qty = randint(2,int(phyNet.vcount()*perc))
        self.nodes = sample(range(0,phyNet.vcount()),qty)
        self.env.process(self.arrival(mon))
    
    """ Virtual Network arrives, is allocated and leaves """           
    def arrival(self,M):
        #print("VN arrived",str(self.env.now))
        global phyNet
        global algorithm
        #create the virtual
        if algorithm == 1:
            subPhyNet = shpalg.create(phyNet,self.nodes)
        if algorithm == 2:
            subPhyNet = optimal.create(phyNet,self.nodes)
        
		#allocate the virtual network
        phyNet = allocate(subPhyNet,phyNet)

        lf = expovariate(1.0/meanLifeVNTime) #generate the VN lifetime
        
        #Capturing Metrics
        #M[0] is mLL, M[1] is maxLL, M[2] is minLL, M[3] is nUnL
        M[0].append(round(sum(phyNet.es["nvlinks"])/float(phyNet.ecount()),3))
        M[1].append(max(phyNet.es["nvlinks"]))
        M[2].append(min(phyNet.es["nvlinks"]))
        soma = sum([1 for i in phyNet.get_edgelist() if phyNet.es[phyNet.get_eid(i[0],i[1])]["nvlinks"] == 0 ])
        M[3].append((soma/float(phyNet.ecount()))*100)
        
        yield self.env.timeout(lf)
        #remove the virtual network
        phyNet = deallocate(subPhyNet,phyNet)
        
        #Capturing Metrics
        M[0].append(round(sum(phyNet.es["nvlinks"])/float(phyNet.ecount()),3))
        M[1].append(max(phyNet.es["nvlinks"]))
        M[2].append(min(phyNet.es["nvlinks"]))
        soma = sum([1 for i in phyNet.get_edgelist() if phyNet.es[phyNet.get_eid(i[0],i[1])]["nvlinks"] == 0 ])
        M[3].append((soma/float(phyNet.ecount()))*100)
        #print("VN died",str(self.env.now))
 
## Model  ----------------------------------
def model():                            
    #generate physical network
    global phyNet
    numberOfPhyNodes = 50
    phyNet = Graph.Erdos_Renyi(numberOfPhyNodes, 0.5)
    phyNet.es["nvlinks"] = 0
    phyNet.vs["name"] = range(0,numberOfPhyNodes)
    #phyNet = 0
    #initialize monitors  
    mLL = [] #Monitors the mean load of physical links
    maxLL = [] #Monitors the maximum load of physical links
    minLL = [] #Monitors the minimum load of physical links
    nUnL = [] #Monitors the number of unused links  
    
    env = simpy.Environment()
    s = Source(env)
    env.process(s.generate(mon=(mLL,maxLL,minLL,nUnL)))         
    env.run(until=simDuration)
    return (sum(mLL)/float(len(mLL)),max(maxLL),min(minLL),nUnL[len(nUnL)-1])

## Experiment parameters -------------------------------
simDuration = 2000.0  # time to stop simulation (minutes)
meanTimeBtwVNArrivals = 0.2   # mean time between arrivals of virtual networks (minutes)
meanLifeVNTime = 100.0     # mean lifetime of virtual networks (minutes)
theSeed = 393939
algorithm = 2 #Use 1 for shpalg and 2 for optimal  
## Experiment/Result  ----------------------------------

mLL=[]
maxLL=[]
minLL=[]
nUnL=[]
seed(theSeed)
for Sd in range(1):
    result = model()
    mLL.append(float(result[0]))
    maxLL.append(float(result[1]))
    minLL.append(float(result[2]))
    nUnL.append(float(result[3]))
    print Sd

print "Report"
print "Mean load of physical links",(sum(mLL) / float(len(mLL)))
print "Maximum load of physical links",(sum(maxLL) / float(len(maxLL)))
print "Minimum load of physical links",(sum(minLL) / float(len(minLL)))
print "Percentage of unused links",(sum(nUnL) / float(len(nUnL)))