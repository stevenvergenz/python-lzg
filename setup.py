from distutils.core import setup, Extension

liblzg = Extension('liblzg',
                    include_dirs = ['liblzg/src/include'],
                    sources = [
                        'liblzg/src/lib/checksum.c',
                        'liblzg/src/lib/decode.c',
                        'liblzg/src/lib/encode.c',
                        'liblzg/src/lib/version.c',
                    ])

setup (
    name = 'python-lzg',
    version = '1.0',
    description = 'liblzg for python',
    ext_modules = [liblzg]
)