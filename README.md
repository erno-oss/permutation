# permutation
 a simple Python script that calculates all possible permutations of given elements and stores them in the form of a tree structure.
___

The amount of nodes in the last generation can be calculated by: 

*$n$ = the amount of elements*
$$n!$$

$n!$ describes all permutations that have all possible elements in them.

For the example of: [1, 2, 3, 4]

describes $n!$ only all permutations that are constructed in this way:
[1, 2, 3, 4], [2, 3, 1, 4] ..... [4, 3, 2, 1] 

___
The amount of all nodes in a generation can be calculated by:

$$\frac{n!}{(n-k)!}$$

___

The amount of all nodes in the tree can be calculated by:

$n$ = elements
$$\sum^{n}_{k=1} \frac{n!}{(n-k)!}$$

---
amount of elements ($n$) | amount of permutations
--- | ---
4 | 64
8 | 109600
16| 56874039553216

The numbers become very large when $n$ is increased.

---

the objects are displayed in the form:
__parent: ...|value: ...|child: ...|generation: ...|__

attributes | definition
---|---
self.parent | every past node
self.value | current value
self.child | future nodes
self.generation | current generation


```python
def __repr__(self) -> str:
        return f"parent: {self.parent[1:]}|value: {self.value}|child: {self.child}|generation: {self.generation}"
```
The form can be modified in the *__ repr __()* function shown above.
