class Leaf(object):

    def __init__(self, is_root=True, weight=0, char=None, parent=None, left_child=None, right_child=None):
        self.is_root = is_root
        self.weight = weight
        self.char = char

        self.parent = parent
        self.left_child = left_child
        self.right_child = right_child

    def __str__(self):
        return "Leaf {0}: is_root={1}, weight={2}, char={3}, parent={4}, left_child={5}, right_child={6}".format(
            self.char, self.is_root, self.weight, self.char, self.parent, self.left_child, self.right_child
        )




