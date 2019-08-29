#ALGORITMA PENCARIAN#

import search
from search import *

manchaster_map = UndirectedGraph(dict(
	Manchaster=dict(Liverpool = 30, Sheffield = 40),
	Sheffield = dict(Nottingham = 40),
	Nottingham = dict(Liverpool = 110, Bham = 50, Oxford = 100),
	Liverpool = dict(Shrewburry = 70),
	Shrewburry = dict(Bham = 50, Aberyst = 80, Cardiff = 50),
	Bham = dict(Bristol = 90),
	Aberyst = dict(Cardiff = 120),
	Cardiff = dict(Bristol = 50),
	Bristol = dict(Oxford = 70, Southampton=70),
	Oxford = dict(Southampton = 70)))

#buat objek bernama graph problem
manchaster_problem = GraphProblem('Manchaster', 'Southampton', manchaster_map)

#manchaster_locations = romania_map.locations

#BFS
a=[node.state for node in breadth_first_graph_search(manchaster_problem).path()]
print(a)

#DFS
a=[node.state for node in depth_first_graph_search(manchaster_problem).path()]
print(a)
