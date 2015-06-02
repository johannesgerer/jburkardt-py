#! /usr/bin/env python
#
def euler ( n ):

#*****************************************************************************80
#
## EULER returns the N-th row of Euler's triangle.
#
#  Discussion:
#
#    E(N,K) counts the number of permutations of the N digits that have
#    exactly K "ascents", that is, K places where the Ith digit is
#    less than the (I+1)th digit.
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
#  Parameters:
#
#    Input, integer N, the row of Euler's triangle desired.
#
#    Output, integer A[0:N], the N-th row of Euler's
#    triangle, A(K+1) contains the value of E(N,K).  Note
#    that A(1) should be 1 and A(N+1) should be 0.
#
  import numpy as np

  a = np.zeros ( n + 1 )

  a[0] = 1

  if ( 0 < n ):
    a[1] = 0
    for irow in range ( 2, n + 1 ):
      a[irow] = 0
      for k in range ( irow - 1, 0, -1 ):
        a[k] = ( k + 1 ) * a[k] + ( irow - k ) * a[k-1]
      a[0] = 1

  return a

def euler_test ( ):

#*****************************************************************************80
#
## EULER_TEST tests EULER.
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
  nmax = 9

  print ''
  print 'EULER_TEST'
  print '  EULER gets rows of Euler\'s triangle.'
  print ''

  for n in range ( 0, nmax + 1 ):
    ieuler = euler ( n )
    for i in range ( 0, n + 1 ):
      print '  %d' % ( ieuler[i] ),
    print ''
#
#  Terminate.
#
  print ''
  print 'EULER_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  euler_test ( )
  timestamp ( )

