from typing import TypeVar, Generic, List, Tuple

T = TypeVar('T')

class Vertex(Generic[T]):

    def __init__(self, name: T) -> None:
        self.name : T = name
    
    def display(self) -> str:
        return f"Vertex({self.name})"
    
    def __eq__(self, other):
        return isinstance(other, Vertex) and self.name == other.name

    def __hash__(self):
        return hash(self.name)


class Graph(Generic[T]):
    
    def __init__(self) -> None:
        self.vertices: List[Vertex[T]] = []
        self.edges: List[Tuple[Vertex[T], Vertex[T], float]] = []
    
    def add_edge(self, u: Vertex[T], v: Vertex[T], weight: float) -> None:
        if u not in self.vertices:
            self.vertices.append(u)
        if v not in self.vertices:
            self.vertices+=[v]
        self.edges.append((u, v, weight))


