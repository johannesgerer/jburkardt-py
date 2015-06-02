#!/usr/bin/env python

def polynomial_print ( m, o, c, e, title ):

#*****************************************************************************80
#
## POLYNOMIAL_PRINT prints a polynomial.
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
#    Input, integer O, the "order" of the polynomial, that is,
#    simply the number of terms.
#
#    Input, real C(O), the coefficients.
#
#    Input, integer E(O), the indices of the exponents.
#        
#    Input, string TITLE, a title.
#
  from mono_unrank_grlex import mono_unrank_grlex
  import sys

  sys.stdout.write ( title )
  sys.stdout.write ( '\n' )

  if ( o == 0 ):
    sys.stdout.write ( '      0.' )
  else:
    for j in range ( 0, o ):
      sys.stdout.write ( '    ' )
      if ( c[j] < 0 ):
        sys.stdout.write ( '- ' )
      else:
        sys.stdout.write ( '+ ' )
      sys.stdout.write ( repr ( abs ( c[j] ) ) )
      sys.stdout.write ( ' * x^(' )
      f = mono_unrank_grlex ( m, e[j] )
      for i in range ( 0, m ):
        sys.stdout.write ( repr ( f[i] ) )
        if ( i < m - 1 ):
          sys.stdout.write ( ',' )
        else:
          sys.stdout.write ( ')' )
      if ( j == o - 1 ):
        sys.stdout.write ( '.' )
      sys.stdout.write ( '\n' )

  return

def polynomial_print_test ( ):

#*****************************************************************************80
#
## POLYNOMIAL_PRINT_TEST tests POLYNOMIAL_PRINT.
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
  import numpy as np

  print ''
  print 'POLYNOMIAL_PRINT_TEST'
  print '  POLYNOMIAL_PRINT prints a polynomial.'

  m = 3
  o = 6
  c = np.array ( [ 7.0, - 5.0, 9.0, 11.0, 0.0, - 13.0 ], dtype = np.float64 )
  e = np.array ( [ 1, 2, 4, 5, 12, 33 ], dtype = np.int32 )
  title = '  P1(X) ='

  print ''
  polynomial_print ( m, o, c, e, title )

  print ''
  print 'POLYNOMIAL_PRINT_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp

  timestamp ( )
  polynomial_print_test ( )
  timestamp ( )
