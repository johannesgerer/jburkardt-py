#! /usr/bin/env python
#
def monomial_value ( m, n, e, x ):

#*****************************************************************************80
#
## MONOMIAL_VALUE evaluates a monomial.
#
#  Discussion:
#
#    This routine evaluates a monomial of the form
#
#      product ( 1 <= i <= m ) x(i)^e(i)
#
#    where the exponents are nonnegative integers.  Note that
#    if the combination 0^0 is encountered, it should be treated
#    as 1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the spatial dimension.
#
#    Input, integer N, the number of points at which the
#    monomial is to be evaluated.
#
#    Input, integer E(M), the exponents.
#
#    Input, real X(M,N), the point coordinates.
#
#    Output, real V(N), the value of the monomial.
#
  import numpy as np

  v = np.ones ( n )

  for i in range ( 0, m ):
    if ( e[i] != 0 ):
      for j in range ( 0, n ):
        v[j] = v[j] * x[i,j] ** e[i]

  return v

def monomial_value_test ( ):

#*****************************************************************************80
#
## MONOMIAL_VALUE_TEST tests MONOMIAL_VALUE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    18 April 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from i4vec_print import i4vec_print
  from r8mat_transpose_print import r8mat_transpose_print
  from r8mat_uniform_01 import r8mat_uniform_01

  print ''
  print 'MONOMIAL_VALUE_TEST'
  print '  MONOMIAL_VALUE evaluates a monomial at multiple points X.'

  m = 2
  n = 10
  seed = 123456789

  print ''
  print '  Spatial dimension M = %d' % ( m )
  print '  Number of samples to select is N = %d' % ( n )

  x, seed = r8mat_uniform_01 ( m, n, seed )

  r8mat_transpose_print ( m, n, x, '  Random points.' )

  e = np.array ( [ 1, 2 ], dtype = np.int32 )

  i4vec_print ( m, e, '  Monomial exponents:' )

  v = monomial_value ( m, n, e, x )

  print ''
  print '  Monomial values:'
  print ''
  print '   J          X            Y              X*Y^2'
  print ''
  for j in range ( 0, n ):
    print '  %2d:' % ( j ),
    for i in range ( 0, m ):
      print '  %10.4g' % ( x[i,j] ),
    print '    %10.4g' % ( v[j] )
#
#  Terminate.
#
  print ''
  print 'MONOMIAL_VALUE_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  monomial_value_test ( )
  timestamp ( )
