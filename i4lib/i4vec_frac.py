#! /usr/bin/env python
#
def i4vec_frac ( n, a, k ):

#*****************************************************************************80
#
#% I4VEC_FRAC searches for the K-th smallest entry in an N-vector.
#
#  Discussion:
#
#    Hoare's algorithm is used.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 May 2015
#
#  Author:
#
#    John Burkardt.
#
#  Parameters:
#
#    Input, integer N, the number of elements of A.
#
#    Input, integer A(N), the array to search.
#
#    Input, integer K, the fractile to be sought.  If K = 1, the minimum
#    entry is sought.  If K = N, the maximum is sought.  Other values
#    of K search for the entry which is K-th in size.  K must be at
#    least 1, and no greater than N.
#
#    Output, integer FRAC, the value of the K-th fractile of A.
#
  from sys import exit

  if ( n <= 0 ):
    print ''
    print 'I4VEC_FRAC - Fatal error!'
    print '  Illegal nonpositive value of N = %d' % ( n )
    exit ( 'I4VEC_FRAC - Fatal error!' )

  if ( k <= 0 ):
    print ''
    print 'I4VEC_FRAC - Fatal error!'
    print '  Illegal nonpositive value of K = %d' % ( k )
    exit ( 'I4VEC_FRAC - Fatal error!' )

  if ( n < k ):
    print ''
    print 'I4VEC_FRAC - Fatal error!'
    print '  Illegal N < K, K = %d' % ( k )
    exit ( 'I4VEC_FRAC - Fatal error!' )

  left = 1
  iryt = n

  while ( True ):

    if ( iryt <= left ):
      frac = a[k-1]
      break

    x = a[k-1]
    i = left
    j = iryt

    while ( True ):

      if ( j < i ):
        if ( j < k ):
          left = i
        if ( k < i ):
          iryt = j
        break
#
#  Find I so that X <= A(I)
#
      while ( a[i-1] < x ):
        i = i + 1
#
#  Find J so that A(J) <= X
#
      while ( x < a[j-1] ):
        j = j - 1

      if ( i <= j ):

        temp   = a[i-1]
        a[i-1] = a[j-1]
        a[j-1] = temp

        i = i + 1
        j = j - 1

  return frac

def i4vec_frac_test ( ):

#*****************************************************************************80
#
#% I4VEC_FRAC_TEST tests I4VEC_FRAC
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 May 2015
#
#  Author:
#
#    John Burkardt
#
  from i4vec_print import i4vec_print
  from i4vec_uniform_ab import i4vec_uniform_ab

  n = 10
  b = 1
  c = 2 * n
  seed = 123456789

  print ''
  print 'I4VEC_FRAC_TEST'
  print '  I4VEC_FRAC: K-th smallest integer vector entry.'
  print '  Using initial random number seed = %d' % ( seed )

  a, seed = i4vec_uniform_ab ( n, b, c, seed )

  i4vec_print ( n, a, '  The array to search:' )

  print ''
  print '  Fractile    Value'
  print ''

  nh = ( n // 3 )

  for k in range ( 1, n + 1, nh ):

    afrac = i4vec_frac ( n, a, k )

    print '  %6d  %6d' % ( k, afrac )
#
#  Terminate.
#
  print ''
  print 'I4VEC_FRAC_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4vec_frac_test ( )
  timestamp ( )
