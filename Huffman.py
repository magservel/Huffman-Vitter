from Tree import Tree


class Huffman:
    def __init__(self, s_input):
        if s_input is None:
            raise Exception('A string is needed for Huffman algo initialization')
        self.s_input = s_input
        self.tree = Tree(s_input)

    def compress(self):
        return self.s_input

    def decompress(self):
        return self.s_input


