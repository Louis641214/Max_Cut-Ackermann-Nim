from src.basic_class import Vertex, Graph 
from src.Max_Cut_local_search import max_cut_local_search

def test_max_cut_local_search():

    g = Graph[str]()
    a, b, c, d = Vertex("A"), Vertex("B"), Vertex("C"), Vertex("D")
    
    g.add_edge(a, b, 3.0)
    g.add_edge(b, c, 1.0)
    g.add_edge(b, d, 4.0)
    g.add_edge(d, c, 5.0)
    g.add_edge(a, c, 2.0)

    partition, cut_value = max_cut_local_search(g)


    print("Partition:")
    for vertex in g.vertices:
        print(f"  {vertex.name} -> Group {partition[vertex]}")
    
    print(f"Cut value: {cut_value}")


# ================================
# Main
# ================================

test_max_cut_local_search()