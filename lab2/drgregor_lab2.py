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
#keep track of the visited nodes and their lowlink value

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

def dfs(G: list[node]) -> list[list[int]]:
	"""
	for each node in G, 
	if previsit = -1 (undiscvered)
	call explore  
	"""
	counter = [0]
	stack = []
	node_list = []
	on_stack = [False] * len(G)

	for i in range(len(G)):
		if G[i].previsit == -1:
			explore(G, i, counter, stack, on_stack, node_list)

	return node_list


"""
in explore, 
make the current nodes pre and postvisit = to the counter
add 1 to count 

if the current nodes out edges is empty,
add it to the list and return that list

for each of the nodes neighbor, 
if it is undiscovered, call explore on that neighbor
if its already discovered, make the current nodes postvisit = to that neighbors post visit

"""
def explore(G: list[node], node: int, counter: list[int], stack: list[int], on_stack: list[bool], node_list: list[list[int]]):
	G[node].previsit = G[node].postvisit = counter[0]
	#using postvisit as lowlink number
	counter[0] += 1
	stack.append(node)
	on_stack[node] = True

	for neighbor in G[node].out_edges: 
		#if neighbor is not visited, call dfs on that neighbor
		#print(f"current node {G[node].name}, neighbor {G[neighbor].name}")
		if G[neighbor].previsit == -1:
			explore(G, neighbor, counter, stack, on_stack, node_list)
			G[node].postvisit = min(G[node].postvisit, G[neighbor].postvisit)
			#print(f"current {G[node].name} previsit and post visit: {G[node].previsit}, {G[node].postvisit}")

		elif on_stack[neighbor]: 
			#if neighbor is already visited, make current nodes postnum = to that neighbirs postnum
			G[node].postvisit = min(G[neighbor].postvisit, G[node].postvisit)
			#print(f"current nodes previsit and post visit: {G[node].previsit}, {G[node].postvisit}")


	if G[node].previsit == G[node].postvisit:
		subcomp = []
		while True:
			n = stack.pop()
			on_stack[n] = False
			subcomp.append(G[n].name)
			if n == node:
				break
		node_list.append(subcomp)


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

	#for i in range(len(G)):
		#print(f"{G[i].name}, {G[i].out_edges},  {G[i].in_edges}, {G[i].previsit}, {G[i].postvisit}, {G[i].component}")
	components = strong_connectivity(G)
	print(components)
		
		
if __name__ == '__main__':
	main()
