from flask import url_for
from pygraphviz import *


def createGraph(nodesDictionary):
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
    return Graph


def drawGraph(Graph):
    Graph.draw('app/static/img/result.png', prog="twopi") # draw to png using circo
#    Graph.draw(url_for('static', filename='img/result.png'), prog="twopi") # draw to png using circo
