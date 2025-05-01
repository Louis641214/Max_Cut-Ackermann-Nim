import random
from typing import Dict, Literal, Tuple
from .basic_class import T, Vertex, Graph 

def max_cut_local_search(g: Graph[T]) -> Tuple[Dict[Vertex[T], Literal[0,1]], float]:

    partition = {vertex: random.choice([0, 1]) for vertex in g.vertices} # Randomly assigning vertices to partitions
    
    improved = True
    while improved:
        improved = False
        for vertex in g.vertices:
            current_cut = compute_cut_value(g, partition)
            partition[vertex] = 1 - partition[vertex] # Moving the vertex to the other group
            new_cut = compute_cut_value(g, partition)
            if new_cut > current_cut:
                improved = True
            else:
                partition[vertex] = 1 - partition[vertex]
    return partition, current_cut


def compute_cut_value(g: Graph[T], partition: Dict[Vertex[T], Literal[0,1]]) -> float:
    cut_value = 0
    for u, v, weight in g.edges:
        if partition[u] != partition[v]:
            cut_value += weight
    return cut_value
