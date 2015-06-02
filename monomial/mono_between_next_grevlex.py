#!/usr/bin/env python

def mono_between_next_grevlex ( m, n1, n2, x ):

#*****************************************************************************80
#
## MONO_BETWEEN_NEXT_GREVLEX: grevlex next monomial, degree between N1 and N2.
#
#  Discussion:
#
#    We consider all monomials in an M-dimensional space, with total
#    degree N between N1 and N2, inclusive.
#
#    For example:
#
#    M = 3
#    N1 = 2
#    N2 = 3
#
#    #  X(1)  X(2)  X(3)  Degree
#      +------------------------
#    1 |  0     0     2        2
#    2 |  0     1     1        2
#    3 |  1     0     1        2
#    4 |  0     2     0        2
#    5 |  1     1     0        2
#    6 |  2     0     0        2
#      |
#    7 |  0     0     3        3
#    8 |  0     1     2        3
#    9 |  1     0     2        3
#   10 |  0     2     1        3
#   11 |  1     1     1        3
#   12 |  2     0     1        3
#   13 |  0     3     0        3
#   14 |  1     2     0        3
#   15 |  2     1     0        3
#   16 |  3     0     0        3
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
#    Input, integer N1, N2, the minimum and maximum degrees.
#    0 <= N1 <= N2.
#
#    Input, integer X[M], the current monomial.
#    The first element is X = [ 0, 0, ..., 0, N1 ].
#    The last is [ N2, 0, ..., 0, 0 ].
#
#    Output, integer X[M], the next monomial.
#
  from i4vec_sum import i4vec_sum
  from mono_next_grevlex import mono_next_grevlex

  if ( n1 < 0 ):
    print ''
    print 'MONO_BETWEEN_NEXT_GREVLEX - Fatal error!'
    print '  N1 < 0.'
    sys.exit ( 'MONO_BETWEEN_NEXT_GREVLEX - Fatal error!' )

  if ( n2 < n1 ):
    print ''
    print 'MONO_BETWEEN_NEXT_GREVLEX - Fatal error!'
    print '  N2 < N1.'
    sys.exit ( 'MONO_BETWEEN_NEXT_GREVLEX - Fatal error!' )

  if ( i4vec_sum ( m, x ) < n1 ):
    print ''
    print 'MONO_BETWEEN_NEXT_GREVLEX - Fatal error!'
    print '  Input X sums to less than N1.'
    sys.exit ( 'MONO_BETWEEN_NEXT_GREVLEX - Fatal error!' )

  if ( n2 < i4vec_sum ( m, x ) ):
    print ''
    print 'MONO_BETWEEN_NEXT_GREVLEX - Fatal error!'
    print '  Input X sums to more than N2.'
    sys.exit ( 'MONO_BETWEEN_NEXT_GREVLEX - Fatal error!' )

  if ( n2 == 0 ):
    return x

  if ( x[0] == n2 ):
    x[0] = 0
    x[m-1] = n1
  else:
    x = mono_next_grevlex ( m, x )

  return x

def mono_between_next_grevlex_test ( ):

#*****************************************************************************80
#
## MONO_BETWEEN_NEXT_GREVLEX_TEST tests MONO_BETWEEN_NEXT_GREVLEX.
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
  print 'MONO_BETWEEN_NEXT_GREVLEX_TEST'
  print '  MONO_BETWEEN_NEXT_GREVLEX can list the monomials'
  print '  in M variables, of total degree N between N1 and N2,'
  print '  in grevlex order, one at a time.'
  print ''
  print '  We start the process with (0,0,...,0,N1).'
  print '  The process ends with (N2,0,...,0,0)'

  n1 = 2;
  n2 = 3;

  print ''
  print '  Let M =   %d' % ( m )
  print '      N1 =  %d' % ( n1 )
  print '      N2 =  %d' % ( n2 )
  print ''

  x = np.array ( [ 0, 0, n1 ], dtype = np.int32 )
 
  i = 1;

  while ( True ):

    print '  %2d    ' % ( i ),
    for k in range ( 0, m ):
      print '%2d' % ( x[k] ),
    print ''

    if ( x[0] == n2 ):
      break

    x = mono_between_next_grevlex ( m, n1, n2, x )
    i = i + 1

  print ''
  print 'MONO_BETWEEN_NEXT_GREVLEX_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp

  timestamp ( )
  mono_between_next_grevlex_test ( )
  timestamp ( )
