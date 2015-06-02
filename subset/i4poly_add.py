#! /usr/bin/env python
#
def i4poly_add ( na, a, nb, b ):

#*****************************************************************************80
#
## I4POLY_ADD adds two I4POLY's.
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
#    Input, integer A[0:NA], the coefficients of the first
#    polynomial factor.
#
#    Input, integer NB, the degree of polynomial B.
#
#    Input, integer B[0:NB], the coefficients of the
#    second polynomial factor.
#
#    Output, integer C[0:max(NA,NB)], the coefficients of A + B.
#
  import numpy as np

  nc = max ( na, nb ) + 1

  c = np.zeros ( nc )

  for i in range ( 0, na + 1 ):
    c[i] = c[i] + a[i]

  for i in range ( 0, nb + 1 ):
    c[i] = c[i] + b[i]

  return c

def i4poly_add_test ( ):

#*****************************************************************************80
#
## I4POLY_ADD_TEST tests I4POLY_ADD.
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
  from i4poly_degree import i4poly_degree
  from i4poly_print import i4poly_print

  print ''
  print 'I4POLY_ADD_TEST'
  print '  I4POLY_ADD adds two I4POLY\'s.'

  na = 5
  a = np.array ( [ 0, 1, 2, 3, 4, 5 ] )
  nb = 5
  b = np.array ( [ 1, -2, 7, 8, 0, -5 ] )

  c = i4poly_add ( na, a, nb, b )

  i4poly_print ( na, a, '  Polynomial A:' )

  i4poly_print ( nb, b, '  Polynomial B:' )

  nc = max ( na, nb )

  nc2 = i4poly_degree ( nc, c )

  i4poly_print ( nc2, c, '  Polynomial C = A+B:' )
#
#  Terminate.
#
  print ''
  print 'I4POLY_ADD_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4poly_add_test ( )
  timestamp ( )

