#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "liblzg/src/include/lzg.h"

int main(int argc, char** argv)
{
	if(argc != 2){
		printf("%s INPUT\n", argv[0]);
		return 1;
	}

	char* input = argv[1];

	lzg_uint32_t maxEncSize = LZG_MaxEncodedSize(strlen(input));

	printf("Worst-case enc size: %d\n", maxEncSize);

	unsigned char* encStr = (unsigned char*) malloc(maxEncSize);
	lzg_uint32_t encSize = LZG_Encode(input, strlen(input), encStr, maxEncSize, NULL);

	printf("Actual enc size: %d\n", encSize);
	printf("Result:\n");
	int i=0;
	for(i=0; i<encSize; i++){
		printf("%02x ", encStr[i]);
	}
	printf("\n");

	return 0;
}
