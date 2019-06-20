from pygraphviz import *
from collections import Counter


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
    Пример: {'Home': {'Home': 'fine', 'Work': 'Go'}, 'Work': None}
    '''
    for startNode in nodesDictionary:
        if nodesDictionary.get(startNode) == None:
            return False

    return True 

def checkDeterm(nodesDictionary):
    '''
    Если граф не детерменированный возвращает False
    {"Work":{"Home":"1","Basic":"1"},"Home":null,"Basic":null}
    '''
    for startNode in nodesDictionary:
        arrayValue = []
        endNodes = nodesDictionary.get(startNode)
        if endNodes:
            for endNode in endNodes:
                arrayValue.append(endNodes.get(endNode))
        duplicate = [arrayValue[i] for i in range(len(arrayValue)) if i == arrayValue.index(arrayValue[i])]
        if len(duplicate) != 0:
            return False
    return True 


if __name__ == '__main__':
    nodesDictionary = {'Home': {'Home': 'fine', 'Work': 'Go'}, 'Work': None}

    nodesDictionary1 = {'Home': {'Home': 'fine', 'Work': 'Go'}, 'Work': {'Home': 'lai'}}
    
    nodesDictionary2 = {"Work": {"Home": "1", "Basic": "1"}, "Home": None, "Basic": None}

    print(checkDeterm(nodesDictionary2))

    #print(fulnessCheck(nodesDictionary))
    #print(fulnessCheck(nodesDictionary1))

