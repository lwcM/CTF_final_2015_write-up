#include <stdio.h>
#include <string.h>
#include <stdlib.h>

unsigned char png[8] = {0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a};
unsigned char enc[8] = {0xa4, 0x49, 0xad, 0x56, 0xd2, 0xa3, 0x51, 0x7b};


int main() {
	for(int i=2147483647; i>=0; i--) {
		if(i % (1<<20)==0)
			printf("process %d\n", i);
		int state = i;
		int v8 = 1103515245 * state + 12345;
		if((((unsigned char)v8) ^ png[0]) != enc[0])
			continue;
		char s[256];
		sprintf(s, "./otp %d test qwe > /dev/null", i);
		system(s);
		FILE *fp = fopen("qwe", "r");
		int j;
		for(j=0; j<8; j++)
		{
			unsigned char c = fgetc(fp);
			if(c != enc[j])
				break;
		}
		fclose(fp);
		if(j == 8)
			printf("%d\n", i);
	}
}
