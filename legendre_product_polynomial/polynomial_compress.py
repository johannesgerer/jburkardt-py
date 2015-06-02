#!/usr/bin/env python

def polynomial_compress ( o1, c1, e1 ):

#*****************************************************************************80
#
## POLYNOMIAL_COMPRESS compresses a polynomial.
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
#    Input, integer O1, the "order" of the polynomial.
#
#    Input, real C1(O1), the coefficients.
#
#    Input, integer E1(O1), the indices of the exponents.
#        
#    Input, integer O2, the "order" of the compressed polynomial.
#
#    Input, real C2(O2), the coefficients of the compressed polynomial.
#
#    Input, integer E2(O2), the indices of the exponents of the 
#    compress polynomial.
#
  import numpy as np

  r8_epsilon_sqrt = 0.1490116119384766E-07
#
#  Add coefficients associated with the same exponent.
#
  get = 0
  put = 0

  c2 = np.zeros ( o1, dtype = np.float64 )
  e2 = np.zeros ( o1, dtype = np.int32 )

  while ( get < o1 ):
    get = get + 1

    if ( 0 == put ):
      put = put + 1
      c2[put-1] = c1[get-1]
      e2[put-1] = e1[get-1]
    else:
      if ( e2[put-1] == e1[get-1] ):
        c2[put-1] = c2[put-1] + c1[get-1]
      else:
        put = put + 1
        c2[put-1] = c1[get-1]
        e2[put-1] = e1[get-1]

  o2 = put
#
#  Clear out zeros and tiny coefficients.
#
  get = 0
  put = 0

  while ( get < o2 ):
    if ( r8_epsilon_sqrt < abs ( c2[get] ) ):
      c2[put] = c2[get]
      e2[put] = e2[get]
      put = put + 1
    get = get + 1

  o2 = put

  return o2, c2, e2

def polynomial_compress_test ( ):

#*****************************************************************************80
#
## POLYNOMIAL_COMPRESS_TEST tests POLYNOMIAL_COMPRESS.
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

  print ''
  print 'POLYNOMIAL_COMPRESS_TEST'
  print '  POLYNOMIAL_COMPRESS compresses a polynomial.'

  m = 3
  o = 10
  c = np.array ( [ 7.0, - 5.0, 5.0, 9.0, 11.0, 3.0, 6.0, 0.0, - 13.0, 1.0E-20 ], \
    dtype = np.float64 )
  e = np.array ( [ 1, 2, 2, 4, 5, 5, 5, 12, 33, 35 ], dtype = np.int32 )

  print ''
  title = '  Uncompressed polynomial ='
  polynomial_print ( m, o, c, e, title )

  o2, c2, e2 = polynomial_compress ( o, c, e )
  print ''
  title = '  Compressed polynomial ='
  polynomial_print ( m, o2, c2, e2, title )

  print ''
  print 'POLYNOMIAL_COMPRESS_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp

  timestamp ( )
  polynomial_compress_test ( )
  timestamp ( )
