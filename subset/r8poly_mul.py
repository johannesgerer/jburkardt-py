#! /usr/bin/env python
#
def r8poly_mul ( na, a, nb, b ):

#*****************************************************************************80
#
## R8POLY_MUL computes the product of two real polynomials A and B.
#
#  Discussion:
#
#    The polynomials are in power sum form.
#
#    The power sum form is:
#
#      p(x) = a(0) + a(1) * x + ... + a(n-1) * x^(n-1) + a(n) * x^(n)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    29 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer NA, the dimension of A.
#
#    Input, real A[0:NA], the coefficients of the first polynomial factor.
#
#    Input, integer NB, the dimension of B.
#
#    Input, real B[0:NB], the coefficients of the second polynomial factor.
#
#    Output, real C[0:NC], the coefficients of A * B.
#
  import numpy as np

  nc = na + nb
  c = np.zeros ( nc + 1 )

  for i in range ( 0, na + 1 ):
    for j in range ( 0, nb + 1 ):
      c[i+j] = c[i+j] + a[i] * b[j]

  return c

def r8poly_mul_test ( ):

#*****************************************************************************80
#
## R8POLY_MUL_TEST tests R8POLY_MUL.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from r8poly_print import r8poly_print

  ntest = 2

  print ''
  print 'R8POLY_MUL_TEST'
  print '  R8POLY_MUL multiplies two polynomials.'
#
#  1: Multiply (1+X) times (1-X).  Answer is 1-X^2.
#  2: Multiply (1+2*X+3*X^2) by (1-2*X). Answer is 1 + 0*X - X^2 - 6*X^3
#
  for itest in range ( 0, ntest ):

    if ( itest == 0 ):
      na = 1
      a = np.array ( [ 1.0, 1.0 ] )
      nb = 1
      b = np.array ( [ 1.0, -1.0 ] )
    elif ( itest == 1 ):
      na = 2
      a = np.array ( [ 1.0, 2.0, 3.0 ] )
      nb = 1
      b = np.array ( [ 1.0, -2.0 ] )

    c = r8poly_mul ( na, a, nb, b )

    r8poly_print ( na, a, '  The factor A:' )

    r8poly_print ( nb, b, '  The factor B:' )

    r8poly_print ( na+nb, c, '  The product C = A*B:' )
#
#  Terminate.
#
  print ''
  print 'R8POLY_MUL_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8poly_mul_test ( )
  timestamp ( )

