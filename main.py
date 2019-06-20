import Leaf
from Huffman import Huffman

if __name__ == '__main__':
    sinput = 'Hello this is a test, how are you ?'

    # Compress input
    compressed_input = Huffman.compress(sinput)
    print(compressed_input)

    # Decompress input
    decompressed_input = Huffman.decompress(sinput)
    print(decompressed_input)

