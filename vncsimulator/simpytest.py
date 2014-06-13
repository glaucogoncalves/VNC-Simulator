import simpy 
from random import expovariate, seed, sample

## Model components ------------------------
class Source(object):

    def __init__(self,env):
        self.env = env

    """ Source generates virtual networks"""        
    def generate(self,mon):
        while 1:
            vn = VirtualNetwork(3,self.env,mon) #<=== Change this to randomize the size of virtualnetwork
            t = expovariate(1.0/meanTimeBtwVNArrivals) #generate time to produce a new Virtual Network
            yield self.env.timeout(t)

class VirtualNetwork(object):    

    def __init__(self,qty,env,mon):
        self.env=env
        #global phyNet
        #generate the number of virtual nodes 
        #self.nodes = sample(range(0,phyNet.vcount()),qty)
        self.nodes = sample(range(0,10),qty)
        self.env.process(self.arrival(mon))
    
    """ Virtual Network arrives, is allocated and leaves """           
    def arrival(self,M):
        print("VN arrived",str(self.env.now))
        global phyNet
        #create the virtual network
        #allocate the virtual network
        phyNet = phyNet + len(self.nodes)
        lf = expovariate(1.0/meanLifeVNTime) #generate the VN lifetime
        M[0].append(lf)
        M[1].append(phyNet)
        print phyNet
        print lf
        yield self.env.timeout(lf)
        #remove the virtual network
        phyNet = phyNet - len(self.nodes)
        M[1].append(phyNet)
        print("VN died",str(self.env.now))
 
## Model  ----------------------------------
def model():                            
    #generate physical network
    global phyNet
    phyNet = 0
    #initialize monitors  
    lfM = [] #Monitors the lifetime
    pNM = [] #Monitors phyNet
    
    env = simpy.Environment()
    s = Source(env)
    env.process(s.generate(mon=(lfM,pNM)))         
    env.run(until=simDuration)
    return (sum(lfM)/float(len(lfM)),sum(pNM)/float(len(pNM)),len(lfM),len(pNM))

## Experiment parameters -------------------------------
simDuration = 2000.0  # time to stop simulation (minutes)
meanTimeBtwVNArrivals = 6.0   # mean time between arrivals of virtual networks (minutes)
meanLifeVNTime = 20.0     # mean lifetime of virtual networks (minutes)
theSeed = 393939

## Experiment/Result  ----------------------------------

o=[]
ta=[]
tmaxf=[]
tmedf=[]
seed(theSeed)
for Sd in range(1):
    result = model()
    o.append(float(result[0]))
    ta.append(float(result[1]))
    tmaxf.append(float(result[2]))
    tmedf.append(float(result[3]))
    #print "Total de atendimentos=",result[4]

print "Relatorio"
print "Mean Lifetime",(sum(o) / float(len(o)))
print "Physical Network Ocupation",(sum(ta) / float(len(ta)))
print "Number of Virtual Networks created",(sum(tmedf) / float(len(tmedf)))
print "Number of triggered events",(sum(tmaxf) / float(len(tmaxf)))