from Leaf import Leaf
from collections import Counter


class Tree:
    def __init__(self, s_input):
        self.root = Leaf(is_root=True)
        self.leaves = []

        for char, weight in Counter(s_input).items():
            self.leaves.append(Leaf(is_root=False, weight=weight, char=char))

        self.build_tree()
        print(self)

    def __str__(self):
        for l in self.leaves:
            print(l)
        return 'Done'

    def build_tree(self):
        l1, l2 = self.get_two_lower_leaves()
        new_weight = l1.weight + l2.weight
        new_leaf = Leaf(weight=new_weight, left_child=l1, right_child=l2)
        self.leaves.append(new_leaf)
        l1.parent = new_leaf
        l2.parent = new_leaf
        return

    def get_two_lower_leaves(self):
        # TODO: Code get two lower
        return self.leaves[0], self.leaves[1]

