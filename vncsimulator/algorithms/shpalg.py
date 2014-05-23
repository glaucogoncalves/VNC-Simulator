from igraph import *
import itertools

def shplist(phyNet,head,tail):
	if tail == []:
		return []
	else:
		ret = []
		ret = phyNet.get_shortest_paths(head,tail,output="epath")
		ret.extend(shplist(phyNet, tail.pop(), tail))
		return ret

def create(phyNet,Vnodes):
	Vnodesaux = list(Vnodes)
	shortestPaths = shplist(phyNet, Vnodesaux.pop(), Vnodesaux)
	#transform shortestPaths in a list of links(edges)
	shortestPaths = list(itertools.chain(*shortestPaths))
	#for each edge in phyNet: check if the edge is on the list of links, if so mantain, if not remove the edge
	phyNetaux = phyNet.subgraph_edges(shortestPaths)
	return phyNetaux