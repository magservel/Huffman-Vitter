class Leaf(object):

    def __init__(self, is_root=True, weight=0, char=None, parent=None, left_child=None, right_child=None):
        if is_root == bool(parent):
            raise Exception('Leaf needs to be root xor to have parent')

        self.is_root = is_root
        self.weight = weight
        self.char = char

        self.parent = parent
        self.left_child = left_child
        self.right_child = right_child





