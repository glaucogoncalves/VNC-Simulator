##########
#Main file of VNC simulator
##########
from igraph import *
from random import *
import csv


from algorithms import shpalg
from topo import fixed
#from matplotlib.pyplot import *
import matplotlib.pyplot as plt

###Function to allocate the created network###
def allocate(subPhyNet,phyNet):
    usedEdges = [(subPhyNet.vs[i[0]]["name"],subPhyNet.vs[i[1]]["name"]) for i in subPhyNet.get_edgelist()]
    for e in usedEdges:
        phyNet.es[phyNet.get_eid(e[0],e[1])]["nvlinks"] = phyNet.es[phyNet.get_eid(e[0],e[1])]["nvlinks"] + 1
    return phyNet

def deallocate(subPhyNet,phyNet1):
    usedEdges = [(subPhyNet.vs[i[0]]["name"],subPhyNet.vs[i[1]]["name"]) for i in subPhyNet.get_edgelist()]
    for e in usedEdges:
        phyNet.es[phyNet.get_eid(e[0],e[1])]["nvlinks"] = phyNet.es[phyNet.get_eid(e[0],e[1])]["nvlinks"] -1
    return phyNet



###Parameters###
numberOfPhyNodes = 50 
numberOfVirtualNodes = [3, 4, 5, 6, 7,9,10,12,15]
#numberOfVirtualNodes = range(3,50)
#numberOfVirtualNodes = [3, 4, 5, 6, 7]
numberOfVirtualNetsToBeCreated = 500
seed(1224)

###Variables###
numberOfCreatedVNets = 0

###Initializing Metrics###
numberOfUsedLinks = 0
virtualLinksPerPhyLink = [] #list

meanLoadLinks = [] 
maximumLoadLinks = []
minimumLoadLinks = []
unusedLinks = []
optimisticMeanLoadLinks = []
exceedingLoad = []
listPhynet = []
#1)generate a physical topology
phyNet = Graph.Erdos_Renyi(numberOfPhyNodes, 0.5)


phyNet.es["nvlinks"] = 0

for i in numberOfVirtualNodes: 
    #phyNet = fixed.generate()
    numberOfPhyNodes = phyNet.vcount()
    phyNet.vs["name"] = range(0,numberOfPhyNodes)
    
    #plot(phyNet, edge_label=phyNet.es["nvlinks"])
    
    for numberOfCreatedVNets in range(0,numberOfVirtualNetsToBeCreated):
        #2)select some vertices to be connected    
        listOfNodes=sample(range(0,phyNet.vcount()),i)
        #3)try to create a network connecting the nodes (the algorithm goes here)
        subPhyNet = shpalg.create(phyNet,listOfNodes)
        phyNet = allocate(subPhyNet,phyNet)
        listPhynet.append(phyNet)
    for j in listPhynet:
        phyNet = deallocate(j,phyNet) ## modifiquei essa linha e coloquei a phyNet recebendo a funcao
        #testando o conteudo da lista.
               
#4)Compute the metrics
    #Mean load of physical links
    meanLoadLinks.append(round(sum(phyNet.es["nvlinks"])/float(phyNet.ecount()),3))
    #Maximum load of physical links
    maximumLoadLinks.append(max(phyNet.es["nvlinks"]))
    #Minimum load of physical links
    minimumLoadLinks.append(min(phyNet.es["nvlinks"]))
    #Number of links not used
    soma = sum([1 for i in phyNet.get_edgelist() if phyNet.es[phyNet.get_eid(i[0],i[1])]["nvlinks"] == 0 ])
    unusedLinks.append((soma/float(phyNet.ecount()))*100)
    
print (meanLoadLinks)
for i in numberOfVirtualNodes:
    optimisticMeanLoadLinks.append(((i-1)*numberOfVirtualNetsToBeCreated)/float(phyNet.ecount()))

for i in range(0,len(numberOfVirtualNodes)):
    exceedingLoad.append(((meanLoadLinks[i]/optimisticMeanLoadLinks[i]) - 1)*100 )
print (exceedingLoad)
#plt.hist(b,bins=5, color='red',alpha=0.2,label='vermelhos')
#plt.plot(numberOfVirtualNodes,meanLoadLinks)
#plt.title('Experiment A/1/1213 - Mean load of physical links', fontsize=20,fontweight='bold')
#plt.xlabel('Number     of Virtual Nodes per Virtual Network',fontsize=15)
#plt.ylabel('Mean load of physical links',fontsize=15)
#plt.legend()
plt.show()

plt.close('all')

# Four axes, returned as a 2-d arrayaxarr[0, 0].plot(numberOfVirtualNodes, meanLoadLinks)
f, axarr = plt.subplots(2, 2)
axarr[0, 0].plot(numberOfVirtualNodes, meanLoadLinks)
axarr[0, 0].set_title('Experiment 05/2014 - Mean load of a link')
axarr[0, 1].plot(numberOfVirtualNodes, maximumLoadLinks)
axarr[0, 1].set_title('Experiment 05/2014 - Maximum load of a link')
axarr[1, 0].plot(numberOfVirtualNodes, minimumLoadLinks)
axarr[1, 0].set_title('Experiment 05/2014 - Minimum load of a link')
axarr[1, 1].plot(numberOfVirtualNodes, unusedLinks)
axarr[1, 1].set_title('Experiment 05/2014 - Number of links not used')
# Fine-tune figure; hide x ticks for top plots and y ticks for right plots
#plt.setp([a.get_xticklabels() for a in axarr[0, :]], visible=False)
#plt.setp([a.get_yticklabels() for a in axarr[:, 1]], visible=False)

fileExp = open("Experimento.txt", "a")
lista = [numberOfVirtualNodes,meanLoadLinks,maximumLoadLinks,minimumLoadLinks,unusedLinks]

fileExp.writelines(['\n','\n',"Nos", '\t',"metrica1", '\t', "metrica2", '\t',"metrica3", '\t',"metrica4",'\n'])

aux = ''
tamanho = len(numberOfVirtualNodes)
i = 0
while i < len(numberOfVirtualNodes)-1:
    aux = aux+ str(numberOfVirtualNodes[i])+'\t'+str(meanLoadLinks[i])+'\t''\t'+str(maximumLoadLinks[i])+ '\t''\t'+str(minimumLoadLinks[i])+'\t''\t'+str(unusedLinks[i])+'\n'
    i = i+1

print aux
fileExp.writelines(aux)
fileExp.close()

print(meanLoadLinks)
print(maximumLoadLinks)
print(minimumLoadLinks)
print(unusedLinks)

plt.show()
