# A template for lab 2 - strong connectivity in graphs - for CSC 349 at Cal Poly
# Reads a file with a list of edges and outputs it to the screen
# Credit: Rodrigo Canaan 

import sys
import math

class node:

	def __init__(self,name,out_edges,in_edges,previsit,postvisit,component):
		self.name = name
		self.out_edges = out_edges
		self.in_edges = in_edges
		self.previsit = previsit
		self.postvisit = postvisit		
		self.component = component


#tarjan's algorithm
#dfs first pass
#keep track of the visited nodes and their 

"""in strong_connectivity, pass in a graph, pass that graph into dfs and
set to variable, pass that variable to sort, return sorted graph
"""
def strong_connectivity(G):
	components = dfs(G)
	sort_component_list(components)
	return components

""" in dfs, pass in the graph 
	for all nodes if undiscovered, call dfs with current graph
"""

def dfs(G: list[node]) -> list[node]:
	"""
	for each node in G, if previsit = -1
	call explore 
	if undiscovered, call explore on it

	in explore, make its previsit = count
	"""
	counter = 0
	node_list = []
	for index in range(len(G)):
		if G[index].previsit == -1:
			node_list = explore(G, index, counter,	node_list)

	return node_list

			#graph		  currentnode  currcount   	node_list
def explore(G: list[node], node: int, count: int, node_list: list[int]):
	G[node].previsit = count
	#using postvisit as lowlink number
	G[node].postvisit = count
	count = count + 1

	for neighbor in G[node].out_edges:
		#if neighbor is not visited, call dfs on that neighbor
		if G[neighbor].previsit == -1:
			node_list = explore(G, neighbor, count,	node_list)
			G[node].postvisit = min(G[node].in_edges, G[node].postvisit)
		
		elif G[neighbor].previsit > -1:
			#if neighbor is already visited, make curren nodes postnum = to that neighbirs postnum
			G[node].postvisit = min(G[neighbor].postvisit, G[node].postvisit)

	if G[node].previsit == G[node].postvisit:
		subcomp = []
		subcomp.append(G[node].name)
			

	node_list.append(G[node].name)

	return	node_list
	

def sort_component_list(components):
	for c in components:
		c.sort()
	components.sort(key = lambda x: x[0])

def read_file(filename):
	with open(filename) as f:
		lines = f.readlines()
		v = int(lines[0])
		if  v == 0:
			raise ValueError("Graph must have one or more vertices")
		G = list(node(name = i, in_edges=[],out_edges=[],previsit= -1, postvisit=-1, component=None) for i in range(v))
		for l in lines[1:]:
			tokens = l.split(",")
			fromVertex,toVertex = (int(tokens[0]),int(tokens[1]))
			G[fromVertex].out_edges.append(toVertex)
			G[toVertex].in_edges.append(fromVertex)
		return G


def main():
	filename = sys.argv[1]
	G = read_file(filename)

	for i in range(len(G)):
		print(f"{G[i].name}, {G[i].out_edges},  {G[i].in_edges}, {G[i].previsit}, {G[i].postvisit}, {G[i].component}")
	components = strong_connectivity(G)
	print(components)
		
		
if __name__ == '__main__':
	main()
