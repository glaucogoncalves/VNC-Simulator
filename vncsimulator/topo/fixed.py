'''
Created on 15/05/2014

@author: Felipe_Fernandes
'''
from igraph import Graph

def generate():
    g = Graph()
    g.add_vertices(10)
    g.add_edges([(0,1),(0,2),(1,2),(1,3),(1,4),(2,5),(2,6),(3,4),(4,5),(4,8),(5,6),(5,7),(5,8),(6,7),(7,8),(8,9),(9,3)])
    return g
