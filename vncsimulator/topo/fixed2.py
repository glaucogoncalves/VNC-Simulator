'''
Created on 15/05/2014

@author: Felipe_Fernandes
'''
from igraph import Graph

def generate():
    g = Graph()
    g.add_vertices(10)
    g.add_edges([(1,2),(2,3),(3,4),(4,5),(5,1)])
    return g
