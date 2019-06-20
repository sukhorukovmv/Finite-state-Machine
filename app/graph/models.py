from pygraphviz import *


def createGraph(nodesDictionary):
    print(nodesDictionary)
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
    Graph.draw('app/static/img/result.png', prog="dot") # draw to png using circo

def fulnessCheck(nodesDictionary):
    '''
    Принимает граф в виде словаря
    Если граф не прошел проверку на полноту вернет False иначе вернет True
    '''
    for startNode in nodesDictionary:
        if nodesDictionary.get(startNode) == None:
            return False

    return True 

if __name__ == '__main__':
    nodesDictionary = {'Home': {'Home': 'fine', 'Work': 'Go'}, 'Work': None}

    nodesDictionary1 = {'Home': {'Home': 'fine', 'Work': 'Go'}, 'Work': {'Home': 'lai'}}

    print(fulnessCheck(nodesDictionary))
    print(fulnessCheck(nodesDictionary1))

