from pygraphviz import *
import json
from collections import namedtuple

x =  '{ "Home": {"Home": "cicle", "Work": "Go"}, "Work": {"Bed": "Sleep", "Home": "Rest"}, "Bed": {"Work": "Name"}, "Pro": {"Bed": null}, "Alone": null}'
nodesDictionary = json.loads(x)
Graph = AGraph(directed=True)

for startNode in nodesDictionary:
    Graph.add_node(startNode)
    Graph.get_node(startNode).attr['label'] = startNode
    endNodes = nodesDictionary.get(startNode)
    if endNodes:
        for endNode in endNodes:
            Graph.add_edge(startNode, endNode)
            edge = Graph.get_edge(startNode, endNode)
            edge.attr['label'] = endNodes.get(endNode) 

print(Graph.string()) # print to screen
Graph.draw('example.png',prog="twopi") # draw to png using circo
print("example.png")

print(nodesDictionary)
