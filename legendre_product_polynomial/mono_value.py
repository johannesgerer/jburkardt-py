#!/usr/bin/env python

def mono_value ( m, n, f, x ):

#*****************************************************************************80
#
## MONO_VALUE evaluates a monomial.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the spatial dimension.
#
#    Input, integer N, the number of evaluation points.
#
#    Input, integer F[M], the exponents of the monomial.
#
#    Input, real X[M*N], the coordinates of the evaluation points.
#
#    Output, real MONO_VALUE[N], the value of the monomial at X.
#
  import numpy as np

  v = np.zeros ( n, dtype = np.float64 )

  for j in range ( 0, n ):
    v[j] = 1.0
    for i in range ( 0, m ):
      v[j] = v[j] * ( x[i+j*m] ** f[i] )

  return v

def mono_value_test ( ):

#*****************************************************************************80
#
## MONO_VALUE_TEST tests MONO_VALUE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 October 2014
#
#  Author:
#
#    John Burkardt
#
  from mono_print import mono_print
  from mono_upto_random import mono_upto_random
  import numpy as np

  m = 3
  nx = 2
  x = np.array ( [ 1.0, 2.0, 3.0, -2.0, 4.0, 1.0 ], dtype = np.float64 )

  print ''
  print 'MONO_VALUE_TEST'
  print '  MONO_VALUE evaluates a monomial.'

  n = 6

  print ''
  print '  Let M = %d' % ( m )
  print '      N = %d' % ( n )

  seed = 123456789
  test_num = 5

  for test in range ( 0, test_num ):
    f, rank, seed = mono_upto_random ( m, n, seed )
    print ''
    mono_print ( m, f, '  M(X) = ' )
    v = mono_value ( m, nx, f, x )
    for j in range ( 0, nx ):
      print '  M(%g,%g,%g) = %g' % ( x[0+j*m], x[1+j*m], x[2+j*m], v[j] )

  print ''
  print 'MONO_VALUE_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp

  timestamp ( )
  mono_value_test ( )
  timestamp ( )
