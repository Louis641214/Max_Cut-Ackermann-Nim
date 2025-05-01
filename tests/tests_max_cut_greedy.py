from src.basic_class import Vertex, Graph 
from src.Max_Cut_Greedy import max_cut_greedy

def test_max_cut_greedy():

    g = Graph[str]()
    a, b, c, d = Vertex("A"), Vertex("B"), Vertex("C"), Vertex("D")
    
    g.add_edge(a, b, 1.0)
    g.add_edge(b, c, 2.0)
    g.add_edge(c, d, 3.0)
    g.add_edge(d, a, 4.0)
    g.add_edge(a, c, 1.5)

    partition, cut_value = max_cut_greedy(g)


    print("Partition:")
    for vertex in g.vertices:
        print(f"  {vertex.name} -> Group {partition[vertex]}")
    
    print(f"Cut value: {cut_value}")


# ================================
# Main
# ================================

test_max_cut_greedy()