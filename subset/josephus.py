#!/usr/bin/env python
#
def josephus ( n, m, k ):

#*****************************************************************************80
#
## JOSEPHUS returns the position X of the K-th man to be executed.
#
#  Discussion:
#
#    The classic Josephus problem concerns a circle of 41 men.
#    Every third man is killed and removed from the circle.  Counting
#    and executing continues until all are dead.  Where was the last
#    survivor sitting?
#
#    Note that the first person killed was sitting in the third position.
#    Moreover, when we get down to 2 people, and we need to count the
#    "third" one, we just do the obvious thing, which is to keep counting
#    around the circle until our count is completed.
#
#    The process may be regarded as generating a permutation of
#    the integers from 1 to N.  The permutation would be the execution
#    list, that is, the list of the executed men, by position number.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    W W Rouse Ball,
#    Mathematical Recreations and Essays,
#    Macmillan, 1962, pages 32-36.
#
#    Donald Knuth,
#    The Art of Computer Programming,
#    Volume 1, Fundamental Algorithms,
#    Addison Wesley, 1968, pages 158-159.
#
#    Donald Knuth,
#    The Art of Computer Programming,
#    Volume 3, Sorting and Searching,
#    Addison Wesley, 1968, pages 18-19.
#
#  Parameters:
#
#    Input, integer N, the number of men.
#    N must be positive.
#
#    Input, integer M, the counting index.
#    M must not be zero.  Ordinarily, M is positive, and no greater than N.
#
#    Input, integer K, the index of the executed man of interest.
#    K must be between 1 and N.
#
#    Output, integer X, the position of the K-th man.
#    X will be between 1 and N.
#
  from sys import exit
  from i4_modp import i4_modp

  if ( n <= 0 ):
    print ''
    print 'JOSEPHUS - Fatal error!'
    print '  N <= 0.'
    exit ( 'JOSEPHUS - Fatal error!' )

  if ( m == 0 ):
    print ''
    print 'JOSEPHUS - Fatal error!'
    print '  M = 0.'
    exit ( 'JOSEPHUS - Fatal error!' )

  if ( k <= 0 or n < k ):
    print ''
    print 'JOSEPHUS - Fatal error!'
    print '  J <= 0 or N < K.'
    exit ( 'JOSEPHUS - Fatal error!' )
#
#  In case M is bigger than N, or negative, get the
#  equivalent positive value between 1 and N.
#  You can skip this operation if 1 <= M <= N.
#
  m2 = i4_modp ( m, n )

  x = k * m2

  while ( n < x ):
    x = ( ( m2 * ( x - n ) - 1 ) // ( m2 - 1 ) )

  return x

def josephus_test ( ):

#*****************************************************************************80
#
## JOSEPHUS_TEST tests JOSEPHUS_NEXT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 May 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'JOSEPHUS_TEST'
  print '  JOSEPHUS solves Josephus problems.'
  print ''
  print '     N     M     K     X'
  print ''

  m = 3
  n = 41
  k = 41
  x = josephus ( n, m, k )
  print '  %4d  %4d  %4d  %4d' % ( n, m, k, x )

  m = -38
  n = 41
  k = 41
  x = josephus ( n, m, k )

  print '  %4d  %4d  %4d  %4d' % ( n, m, k, x )

  m = 3
  n = 41
  k = 40
  x = josephus ( n, m, k )

  print '  %4d  %4d  %4d  %4d' % ( n, m, k, x )

  m = 2
  n = 64
  k = 64
  x = josephus ( n, m, k )

  print '  %4d  %4d  %4d  %4d' % ( n, m, k, x )

  m = 2
  n = 1000
  k = 1000
  x = josephus ( n, m, k )

  print '  %4d  %4d  %4d  %4d' % ( n, m, k, x )
#
#  Terminate.
#
  print ''
  print 'JOSEPHUS_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  josephus_test ( )
  timestamp ( )
