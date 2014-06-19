import sys
from lzg import LZG

def main(args):
	
	coder = LZG()

	if len(args) != 2:
		args.append('hello world!')

	print 'Original ({} length): {}'.format(len(args[1]), args[1])
	compressed = coder.compress(args[1])
	print 'Compressed ({} length): {}'.format(len(compressed), compressed)


if __name__ == '__main__':
	main(sys.argv)
