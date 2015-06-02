#! /usr/bin/env python
#
def r8vec_frac ( n, a, k ):

#*****************************************************************************80
#
## R8VEC_FRAC searches for the K-th smallest entry in an R8VEC.
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
#    30 May 2015
#
#  Author:
#
#    John Burkardt.
#
#  Parameters:
#
#    Input, integer N, the number of elements of A.
#
#    Input, real A(N), the array to search.
#
#    Input, integer K, the fractile to be sought.  If K = 1, the minimum
#    entry is sought.  If K = N, the maximum is sought.  Other values
#    of K search for the entry which is K-th in size.  K must be at
#    least 1, and no greater than N.
#
#    Output, real FRAC, the value of the K-th fractile of A.
#
  from sys import exit

  if ( n <= 0 ):
    print ''
    print 'R8VEC_FRAC - Fatal error!'
    print '  Illegal nonpositive value of N = %d' % ( n )
    exit ( 'R8VEC_FRAC - Fatal error!' )

  if ( k <= 0 ):
    print ''
    print 'R8VEC_FRAC - Fatal error!'
    print '  Illegal nonpositive value of K = %d' % ( k )
    exit ( 'R8VEC_FRAC - Fatal error!' )

  if ( n < k ):
    print ''
    print 'R8VEC_FRAC - Fatal error!'
    print '  Illegal N < K, K = %d' % ( k )
    exit ( 'R8VEC_FRAC - Fatal error!' )

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
        break;
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

def r8vec_frac_test ( ):

#*****************************************************************************80
#
## R8VEC_FRAC_TEST tests R8VEC_FRAC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 May 2015
#
#  Author:
#
#    John Burkardt
#
  from r8vec_print import r8vec_print
  from r8vec_uniform_ab import r8vec_uniform_ab

  n = 10
  ahi = 10.0
  alo = 0.0

  print ''
  print 'R8VEC_FRAC_TEST'
  print '  R8VEC_FRAC: K-th smallest real vector entry;'

  seed = 123456789

  a, seed = r8vec_uniform_ab ( n, alo, ahi, seed )

  r8vec_print ( n, a, '  The real array to search: ' )

  print ''
  print 'Frac   R8VEC_FRAC'
  print ''

  for k in range ( 1, n + 1 ):

    afrac = r8vec_frac ( n, a, k )
    print '  %2d  %6f' % ( k, afrac )
#
#  Terminate.
#
  print ''
  print 'R8VEC_FRAC_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8vec_frac_test ( )
  timestamp ( )
