#include <bits/stdc++.h>
using namespace std;

//137 => 164 (0x89 => 0xa4)
#define HIDWORD(x) ((unsigned int)((x)>>32))

vector <int> st;

int main() {
	int state = 1618033988;
	
	for (long long i=0; i<(1LL<<31); i++) {
		st.push_back(state);
		state = (1103515245 * state + 12345) & 0x7FFFFFFF;
	}
	long long v17 = 1LL, v13;
	int now = 0;
	int ch;
	while((ch = getchar()) != -1) {
		int v8 = 1103515245 * st[now] + 12345;
		now = (now+1) & 0x7fffffff;
		//state = v8 & 0x7FFFFFFF;
		
		//if((((unsigned char)v8) ^ png[j]) != enc[j])
		//	break;
		
		putchar((((unsigned char)v8) ^ ch));
		now = (now+1) & 0x7fffffff;
		state = st[now];
	//	state = (1103515245 * state + 12345) & 0x7FFFFFFF;
		int v9 = state;
		int v10 = state - 1000 * ((unsigned int)((unsigned long long)(274877907LL * state) >> 32) >> 6);
		int v11 = v10 * HIDWORD(v17) + (v10 >> 31) * v17;
		unsigned long long v12 = (unsigned int)v17 * (unsigned long long)(unsigned int)v10;
		v12 = ((v12 & 0xffffffff00000000) + ((long long)v11 << 32)) +  (v12 & 0xffffffff);
		if ( v12 )
		{
			now = (now + v12) & 0x7fffffff;
			/*
			v13 = v12 - 1LL;
			do
			{
				v9 = (1103515245 * v9 + 12345) & 0x7FFFFFFF;
				--v13;
			}
			while ( (HIDWORD(v13) & (unsigned int)v13) != -1 );
			state = v9;*/
		}
		++v17;
	}
}
