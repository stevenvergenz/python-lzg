from __future__ import print_function

from lzg.lzg import LZG


def test():
    coder = LZG()

    test_data = 'abcdefghijlkmnopqrstuvwxyz' * 100

    print('Original ({} length): "{}"'.format(len(test_data), test_data[:50] + '...'))

    compressed = coder.compress(test_data)
    print('Compressed ({} length): "{}"'.format(len(compressed),
                                                compressed if len(compressed) <= 50 else compressed[:50]))

    decompressed = coder.decompress(compressed)
    print('Decompressed ({} length): "{}"'.format(len(decompressed),
                                                  decompressed if len(decompressed) <= 50 else decompressed[
                                                                                               :50] + '...'))


if __name__ == '__main__':
    test()
