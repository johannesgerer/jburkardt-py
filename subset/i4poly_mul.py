#! /usr/bin/env python
#
def i4poly_mul ( na, a, nb, b ):

#*****************************************************************************80
#
## I4POLY_MUL computes the product of two integer polynomials A and B.
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
#    Input, integer NA, the dimension of A.
#
#    Input, integer A[0:NA], the coefficients of the first polynomial factor.
#
#    Input, integer NB, the dimension of B.
#
#    Input, integer B[0:NB], the coefficients of the second polynomial factor.
#
#    Output, integer C[0:NA+NB], the coefficients of A * B.
#
  import numpy as np

  nc = na + nb

  c = np.zeros ( nc + 1 )

  for i in range ( 0, na + 1 ):
    for j in range ( 0, nb + 1 ):
      c[i+j] = c[i+j] + a[i] * b[j]

  return c

def i4poly_mul_test ( ):

#*****************************************************************************80
#
## I4POLY_MUL_TEST tests I4POLY_MUL.
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

  ntest = 2

  print ''
  print 'I4POLY_MUL_TEST'
  print '  I4POLY_MUL multiplies two polynomials.'
#
#  1: Multiply (1+X) times (1-X).  Answer is 1-X^2.
#  2: Multiply (1+2*X+3*X^2) by (1-2*X). Answer is 1 + 0*X - X^2 - 6*X^3
#
  for test in range ( 0, ntest ):

    if ( test == 0 ):
      na = 1
      a = np.array ( [ 1, 1 ] )
      nb = 1
      b = np.array ( [ 1, -1 ] )
    elif ( test == 1 ):
      na = 2
      a = np.array ( [ 1, 2, 3 ] )
      nb = 1
      b = np.array ( [ 1, -2 ] )

    c = i4poly_mul ( na, a, nb, b )

    i4poly_print ( na, a, '  The factor A:' )
    i4poly_print ( nb, b, '  The factor B:' )
    i4poly_print ( na+nb, c, '  The product C = A*B:' )
#
#  Terminate.
#
  print ''
  print 'I4POLY_MUL_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4poly_mul_test ( )
  timestamp ( )

