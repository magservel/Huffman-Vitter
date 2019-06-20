from Huffman import Huffman

if __name__ == '__main__':
    sinput = 'Hello this is a test, how are you ?'

    huffman = Huffman(sinput)
    # Compress input
    compressed_input = huffman.compress()
    print(compressed_input)

    # Decompress input
    decompressed_input = huffman.decompress()
    print(decompressed_input)

