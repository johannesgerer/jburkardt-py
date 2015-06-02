#!/usr/bin/env python

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
#    The combination 0.0^0, if encountered, is treated as 1.0.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    07 April 2015
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
#    Input, integer E(M), the exponents.
#
#    Input, real X(M,N), the point coordinates.
#
#    Output, real V(N), the monomial values.
#
  import numpy as np

  v = np.ones ( n )

  for i in range ( 0, m ):
    if ( 0 != e[i] ):
      for j in range ( 0, n ):
        v[j] = v[j] * x[i,j] ** e[i]

  return v

def monomial_value_test ( ):

#*****************************************************************************80
#
## MONOMIAL_VALUE_TEST tests MONOMIAL_VALUE on sets of data in various dimensions.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 April 2015
#
#  Author:
#
#    John Burkardt
#
  from i4vec_transpose_print import i4vec_transpose_print
  from i4vec_uniform_ab import i4vec_uniform_ab
  from monomial_value import monomial_value
  from r8mat_nint import r8mat_nint
  from r8mat_uniform_ab import r8mat_uniform_ab

  print ''
  print 'MONOMIAL_VALUE_TEST'
  print '  Use monomial_value() to evaluate some monomials'
  print '  in dimensions 1 through 3.'

  e_min = -3
  e_max = 6
  n = 5
  seed = 123456789
  x_min = -2.0
  x_max = +10.0

  for m in range ( 1, 4 ):

    print ''
    print '  Spatial dimension M =  %d' % ( m )

    e, seed = i4vec_uniform_ab ( m, e_min, e_max, seed )
    i4vec_transpose_print ( m, e, '  Exponents:' )
    x, seed = r8mat_uniform_ab ( m, n, x_min, x_max, seed )
#
#  To make checking easier, make the X values integers.
#
    x = r8mat_nint ( m, n, x )
    v = monomial_value ( m, n, e, x )

    print ''
    print '   V(X)         ',
    for i in range ( 0, m ):
      print '      X(%d)' % ( i ),
    print ''
    print ''
    for j in range ( 0, n ):
      print '%14.6g  ' % ( v[j] ),
      for i in range ( 0, m ):
        print '%10.4f' % ( x[i,j] ),
      print ''

  print ''
  print 'MONOMIAL_VALUE_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  monomial_value_test ( )
  timestamp ( )
