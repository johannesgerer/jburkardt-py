#!/usr/bin/env python

def mono_total_next_grlex ( m, n, x ):

#*****************************************************************************80
#
## MONO_TOTAL_NEXT_GRLEX: grlex next monomial, total degree equal to N.
#
#  Discussion:
#
#    We consider all monomials in an M-dimensional space, with total
#    degree N.
#
#    For example:
#
#    M = 3
#    N = 3
#
#    #  X(1)  X(2)  X(3)  Degree
#      +------------------------
#    1 |  0     0     3        3
#    2 |  0     1     2        3
#    3 |  0     2     1        3
#    4 |  0     3     0        3
#    5 |  1     0     2        3
#    6 |  1     1     1        3
#    7 |  1     2     0        3
#    8 |  2     0     1        3
#    9 |  2     1     0        3
#   10 |  3     0     0        3
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the spatial dimension.
#
#    Input, integer N, the total degree.
#    0 <= N1 <= N2.
#
#    Input, integer X[M], the current monomial.
#    The first element is X = [ 0, 0, ..., 0, N ].
#    The last is [ N, 0, ..., 0, 0 ].
#
#    Output, integer X[M], the next monomial.
#
  from i4vec_sum import i4vec_sum
  from mono_next_grlex import mono_next_grlex
  from sys import exit

  if ( n < 0 ):
    print ''
    print 'MONO_TOTAL_NEXT_GRLEX - Fatal error!'
    print '  N < 0.'
    exit ( 'MONO_TOTAL_NEXT_GRLEX - Fatal error!' )

  if ( i4vec_sum ( m, x ) != n ):
    print ''
    print 'MONO_TOTAL_NEXT_GRLEX - Fatal error!'
    print '  Input X sums is not N.'
    exit ( 'MONO_TOTAL_NEXT_GRLEX - Fatal error!' )

  if ( n == 0 ):
    return x

  if ( x[0] == n ):
    x[0] = 0
    x[m-1] = n
  else:
    x = mono_next_grlex ( m, x )

  return x

def mono_total_next_grlex_test ( ):

#*****************************************************************************80
#
## MONO_TOTAL_NEXT_GRLEX_TEST tests MONO_TOTAL_NEXT_GRLEX.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 October 2014
#
#  Author:
#
#    John Burkardt
#
  from i4vec_uniform_ab import i4vec_uniform_ab
  import numpy as np

  m = 3

  print ''
  print 'MONO_TOTAL_NEXT_GRLEX_TEST'
  print '  MONO_TOTAL_NEXT_GRLEX can list the monomials'
  print '  in M variables, of total degree N,'
  print '  in grlex order, one at a time.'
  print ''
  print '  We start the process with (0,0,...,0,N).'
  print '  The process ends with (N,0,...,0,0)'

  n = 3;

  print ''
  print '  Let M =   %d' % ( m )
  print '      N =   %d' % ( n )
  print ''

  x = np.array ( [ 0, 0, n ], dtype = np.int32 )
 
  i = 1;

  while ( True ):

    print '  %2d    ' % ( i ),
    for k in range ( 0, m ):
      print '%2d' % ( x[k] ),
    print ''

    if ( x[0] == n ):
      break

    x = mono_total_next_grlex ( m, n, x )
    i = i + 1

  print ''
  print 'MONO_TOTAL_NEXT_GRLEX_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp

  timestamp ( )
  mono_total_next_grlex_test ( )
  timestamp ( )
