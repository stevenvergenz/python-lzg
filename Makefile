all: lzg test

lzg:
	cd ./liblzg/src && $(MAKE)

test: testlzg.o
	gcc testlzg.o -L./liblzg/src/lib -llzg -o testlzg

testlzg.o: testlzg.c
	gcc -c testlzg.c

clean:
	rm -rf *o testlzg
