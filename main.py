from Huffman import Huffman

if __name__ == '__main__':
    sinput = 'Hello this is a test, how are you ?'

    huffman = Huffman()
    huffman.build_tree()
    # Compress input
    compressed_input = huffman.compress(sinput)
    print(compressed_input)

    # Decompress input
    decompressed_input = huffman.decompress(sinput)
    print(decompressed_input)

