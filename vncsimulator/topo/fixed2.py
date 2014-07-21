'''
Created on 15/05/2014

@author: Felipe_Fernandes
'''
from igraph import Graph

def generate():
    g = Graph()
    g.add_vertices(5)
    g.add_edges([(0,1),(1,2),(2,3),(3,4),(4,0)])
    return g
