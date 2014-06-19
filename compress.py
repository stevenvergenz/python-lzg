import sys
from lzg.lzg import LZG

def main(args):

	if len(args) != 2:
		print args[0], 'INPUTFILE'
		return

	ifp = open(args[1], 'r')
	data = ifp.read()



if __name__ == '__main__':
	main(sys.argv)
