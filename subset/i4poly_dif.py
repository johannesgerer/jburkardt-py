#! /usr/bin/env python
#
def i4poly_dif ( na, a, d ):

#*****************************************************************************80
#
## I4POLY_DIF differentiates an I4POLY.
#
#  Discussion:
#
#    The polynomials are in power sum form.
#
#    The power sum form is:
#
#      p(x) = a(0) + a(1)*x + ... + a(n-1)*x^(n-1) + a(n)*x^(n)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer NA, the degree of polynomial A.
#
#    Input, integer A[0:NA], the coefficients of a polynomial.
#
#    Input, integer D, the number of times the polynomial
#    is to be differentiated.
#
#    Output, integer B[0:NA-D], the coefficients of the
#    differentiated polynomial.
#
  import numpy as np
  from i4_fall import i4_fall

  if ( na < d ):
    b = np.zeros ( 1 )
    return b

  nb = na - d
  b = np.zeros ( nb + 1 )

  for i in range ( 0, nb + 1 ):
    b[i] = a[i+d] * i4_fall ( i + d, d )

  return b

def i4poly_dif_test ( ):

#*****************************************************************************80
#
## I4POLY_DIF_TEST tests I4POLY_DIF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    27 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from i4poly_print import i4poly_print

  test_num = 2

  print ''
  print 'I4POLY_DIF_TEST'
  print '  I4POLY_DIF computes derivatives of an I4POLY.'
#
#  1: Differentiate X^3 + 2*X^2 - 5*X - 6 once.
#  2: Differentiate X^4 + 3*X^3 + 2*X^2 - 2  3 times.
#
  for test in range ( 0, 2 ):

    if ( test == 0 ):
      na = 3
      d = 1
      a = np.array ( [ -6, -5, 2, 1 ] )
    elif ( test == 1 ):
      na = 4
      d = 3
      a = np.array ( [ -2, 5, 2, 3, 1 ] )

    i4poly_print ( na, a, '  The polynomial A:' )

    print ''
    print '  Differentiate A %d times.' % ( d )

    b = i4poly_dif ( na, a, d )
 
    i4poly_print ( na - d, b, '  The derivative, B:' )
#
#  Terminate.
#
  print ''
  print 'I4POLY_DIF_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4poly_dif_test ( )
  timestamp ( )

