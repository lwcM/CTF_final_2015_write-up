#include <bits/stdc++.h>
#include <openssl/sha.h>
using namespace std ;
// template end here
int main(int argc, char** argv)
{
	unsigned char q[ 20 ] , q2[ 30 ] , q3[ 50 ] ;
	int a, b, c, d;
	scanf("%d%d%d%d", &a, &b, &c, &d);
	q[0] = a;
	q[1] = b;
	q[2] = c;
	q[3] = d;
	for ( int i1 = 1 ; i1 < 256 ; i1 ++ )
	for ( int i2 = 1 ; i2 < 256 ; i2 ++ )
	for ( int i3 = 1 ; i3 < 256 ; i3 ++ )
	for ( int i4 = 1 ; i4 < 256 ; i4 ++ )
	{
		q[ 4 ] = i1 ;
		q[ 5 ] = i2 ;
		q[ 6 ] = i3 ;
		q[ 7 ] = i4 ;
		q[ 8 ] = 0 ;
		SHA1(q, 8, q2) ;
		if ( q2[ 0 ] == 0 && q2[ 1 ] == 0 && q2[ 2 ] == 0 )
		{
			for ( int i = 4 ; i < 8 ; i ++ )
			{
				putchar( q[ i ] ) ;
			}
			goto done;
		}
	}
done:
	return 0 ;
}
