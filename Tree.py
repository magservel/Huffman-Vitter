from Leaf import Leaf
from collections import Counter


class Tree:
    def __init__(self, s_input):
        self.root = Leaf(is_root=True)
        self.lone_leaves = []
        self.adopted_leaves = []

        for char, weight in Counter(s_input):
            self.lone_leaves.append(Leaf(is_root=False, weight=weight, char=char))
