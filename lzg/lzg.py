from ctypes import *

CLIB = CDLL('./liblzg/src/lib/liblzg.so')



class LZG:


	def __init__(self, level=5, fast=True):
	
		self.config = {'level':level, 'fast':fast}

	def compress(self, rawtext):

		class Config(Structure):
			_fields_ = [('level',c_int32), ('fast',c_int)]

		# initialize stuff
		config = Config(level=self.config['level'], fast=self.config['fast'])

		# get the worst-case on encoded size
		maxEncSize = CLIB['LZG_MaxEncodedSize'](len(rawtext))
		print maxEncSize
		cout = create_string_buffer(maxEncSize+1)

		# uchar* in, uint32 insize, uchar* out, uint32 outsize, config
		encsize = CLIB['LZG_Encode'](rawtext, len(rawtext), cout, len(cout), config)
		print encsize
		
		return rawtext

	def decompress(self, enctext):
		return enctext
