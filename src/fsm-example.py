from pygraphviz import *

A=AGraph(directed=True)

# set some default node attributes
A.node_attr['style']='filled'

A.node_attr['shape']='circle'
A.node_attr['fixedsize']='true'
A.node_attr['fontcolor']='red'

A.add_node('work')
A.add_node('home')
A.add_node('bed')

A.get_node('home').attr['label'] = 'home'
A.get_node('work').attr['label'] = 'work'
A.get_node('bed').attr['label'] = 'bed'

A.add_edge('work','home')
edge = A.get_edge('work','home')
edge.attr['label'] = 'time to go'

A.add_edge('home','work')
edge = A.get_edge('home','work')
edge.attr['label'] = 'time to go'

A.add_edge('home','bed')
edge = A.get_edge('home','bed')
edge.attr['label'] = 'sleep'

A.add_edge('bed','home')
edge = A.get_edge('bed','home')
edge.attr['label'] = 'wake'


print(A.string()) # print to screen
A.draw('fsm-example.png',prog="twopi") # draw to png using circo
print("fsm-example.png")