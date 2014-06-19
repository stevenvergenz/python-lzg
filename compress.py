import sys, base64, array
from lzg.lzg import LZG

def main(args):

	if len(args) != 2:
		print args[0], 'INPUTFILE'
		return

	ifp = open(args[1], 'r')
	jsondata = ifp.read()

	comp = LZG(level=8)
	payload = comp.compress(jsondata)
	b64payload = base64.b64encode( array.array('B', payload).tostring() )
	print b64payload
	utf16payload = ''
	

if __name__ == '__main__':
	main(sys.argv)
