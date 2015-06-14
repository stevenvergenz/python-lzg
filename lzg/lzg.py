import os
import ctypes
import ctypes.util

# print(ctypes.util.find_library('lzg'))
# print(ctypes.util.find_library('liblzg'))
# print(ctypes.util.find_library('liblzg.cpython-34m.so'))
# print(ctypes.util.find_library('c'))


from distutils.sysconfig import get_python_lib
python_lib = get_python_lib()
# print(python_lib)

lzg_filepath = os.path.join(python_lib, 'liblzg.cpython-34m.so')
# print(lzg_filepath)
CLIB = ctypes.CDLL(lzg_filepath) # FIXME!


class LZG:
    def __init__(self, level=5, fast=True):

        level = min(max(level, 1), 9)

        self.config = {'level': level, 'fast': fast}

    def compress(self, rawtext):

        class Config(ctypes.Structure):
            _fields_ = [('level', ctypes.c_int32), ('fast', ctypes.c_int)]

        # initialize stuff
        config = Config(level=self.config['level'], fast=self.config['fast'])

        # get the worst-case on encoded size
        maxEncSize = CLIB['LZG_MaxEncodedSize'](len(rawtext))
        cout = ctypes.create_string_buffer(maxEncSize)

        encSize = CLIB['LZG_Encode'](rawtext, len(rawtext), cout, len(cout), ctypes.byref(config))

        ret = []
        for i in range(encSize):
            ret.append(ord(cout[i]))

        return ret

    def decompress(self, encbuf):

        cin = ctypes.create_string_buffer(len(encbuf))
        for i, val in enumerate(encbuf):
            cin[i] = chr(val)

        estDecSize = CLIB['LZG_DecodedSize'](cin, len(cin))
        cout = ctypes.create_string_buffer(estDecSize)
        decSize = CLIB['LZG_Decode'](cin, len(cin), cout, len(cout))

        return ctypes.string_at(cout, decSize)
