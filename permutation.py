"""
This programme calculates all permutations of given elements. In addition,
the permutations are calculated in the form of a tree. the different levels
of the tree are given as generations. Each node of the tree is a vertex object.
"""


class Vertex:

    def __init__(self, parent: list, child: list, value, generation: int) -> None:
        self.parent = parent
        self.child = child
        self.value = value
        self.generation = generation

    def __repr__(self) -> str:
        return f"parent: {self.parent[1:]}|value: {self.value}|child: {self.child}|generation: {self.generation}"


"""
A new vertex is created by this function.
"""


def create_vertex(parent: list, child: list, value: any, generation: int) -> object:
    return Vertex(parent=parent, child=child, value=value, generation=generation)


"""
This function creates a new generation (next tree level).
"""


def new_generation(old_generation: list, generation: int) -> list:
    arr = []
    for old_vertex in old_generation:
        for new_vertex in old_vertex.child:
            def create_child(parent, value):
                return [o for o in elements if o not in parent and o != value]

            new_parnet = old_vertex.parent + [old_vertex.value]
            new_child = create_child(old_vertex.parent + [old_vertex.value], new_vertex)
            new_value = new_vertex

            arr.append(create_vertex(new_parnet, new_child, new_value, generation))
    return arr


"""
This function creates the first layer, or what I like to call it "level_zero".
"""


def level_zero() -> list:
    arr = []
    for e in elements:
        arr.append(create_vertex(["origin"], [x for x in elements if x != e], e, 1))
    return arr


"""
This function builds the tree, starting with the first generation,
all other generations then build on the generation constructed at the beginning.
"""


def tree_constructor() -> None:
    tree.append(level_zero())

    for i in range(len(elements) - 1):
        tree.append(new_generation(tree[-1], i+2))


"""
returns the amount of all vertex summed up.
"""


def all_vertices() -> int:
    return len([vertex for gen in tree for vertex in gen])


"""
The tree is displayed in the console, the display can be modified 
in the class under __repr__().
"""


def print_tree() -> None:
    for generations in tree:
        for all_generations in generations:
            print(all_generations)


"""
vertex objects are stored in this array
"""
tree = []

"""
All elements to be used in the permutation.
"""
elements = [1, 2, 3, 4, 5]

tree_constructor()  # builds the tree.
print_tree()  # prints the tree in the console.

print(all_vertices())