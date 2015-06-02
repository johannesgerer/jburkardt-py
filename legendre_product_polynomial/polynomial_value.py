#!/usr/bin/env python

def polynomial_value ( m, o, c, e, nx, x ):

#*****************************************************************************80
#
## POLYNOMIAL_VALUE evaluates a polynomial.
#
#  Discussion:
#
#    The polynomial is evaluated term by term, and no attempt is made to
#    use an approach such as Horner's method to speed up the process.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, int M, the spatial dimension.
#
#    Input, integer O, the "order" of the polynomial.
#
#    Input, real C[O], the coefficients of the scaled polynomial.
#
#    Input, integer E[O], the indices of the exponents of 
#    the scaled polynomial.
#
#    Input, integer NX, the number of evaluation points.
#
#    Input, real X[M*NX], the coordinates of the evaluation points.
#
#    Output, real V[NX], the value of the polynomial at X.
#
  from mono_unrank_grlex import mono_unrank_grlex
  from mono_value import mono_value
  import numpy as np

  p = np.zeros ( nx, dtype = np.float64 )

  for j in range ( 0, o ):
    f = mono_unrank_grlex ( m, e[j] )
    v = mono_value ( m, nx, f, x )
    for k in range ( 0, nx ):
      p[k] = p[k] + c[j] * v[k]

  return p

def polynomial_value_test ( ):

#*****************************************************************************80
#
## POLYNOMIAL_VALUE_TEST tests POLYNOMIAL_VALUE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 October 2014
#
#  Author:
#
#    John Burkardt
#
  from polynomial_print import polynomial_print
  import numpy as np

  m = 3
  o = 6
  c = np.array ( [ 7.0, - 5.0, 9.0, 11.0, 0.0, - 13.0 ], dtype = np.float64 )
  e = np.array ( [ 1, 2, 4, 5, 12, 33 ], dtype = np.int32 )
  nx = 2
  x = np.array ( [ 1.0, 2.0, 3.0, \
                  -2.0, 4.0, 1.0 ], dtype = np.float64 );

  print ''
  print 'POLYNOMIAL_VALUE_TEST'
  print '  POLYNOMIAL_VALUE evaluates a polynomial.'

  print ''
  title = '  P(X) = '
  polynomial_print ( m, o, c, e, title )

  p = polynomial_value ( m, o, c, e, nx, x )

  print ''
  for j in range ( 0, nx ):
    print '  P(%f,%f,%f) = %g' % ( x[0+j*m], x[1+j*m], x[2+j*m], p[j] )

  print ''
  print 'POLYNOMIAL_VALUE_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp

  timestamp ( )
  polynomial_value_test ( )
  timestamp ( )
