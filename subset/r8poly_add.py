#! /usr/bin/env python
#
def r8poly_add ( na, a, nb, b ):

#*****************************************************************************80
#
## R8POLY_ADD adds two R8POLY's.
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
#    28 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer NA, the degree of polynomial A.
#
#    Input, real A(1:NA+1), the coefficients of the first
#    polynomial factor.
#
#    Input, integer NB, the degree of polynomial B.
#
#    Input, real B(1:NB+1), the coefficients of the
#    second polynomial factor.
#
#    Output, real C(1:max(NA,NB)+1), the coefficients of A + B.
#
  import numpy as np

  nc = max ( na, nb )

  c = np.zeros ( nc + 1 )

  for i in range ( 0, na + 1 ):
    c[i] = c[i] + a[i]

  for i in range ( 0, nb + 1 ):
    c[i] = c[i] + b[i]

  return c

def r8poly_add_test ( ):

#*****************************************************************************80
#
## R8POLY_ADD_TEST tests R8POLY_ADD.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    28 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from r8poly_degree import r8poly_degree
  from r8poly_print import r8poly_print

  print ''
  print 'R8POLY_ADD_TEST'
  print '  R8POLY_ADD adds two R8POLY\'s.'

  na = 5
  a = np.array ( [ 0.0,  1.1, 2.2, 3.3, 4.4,  5.5 ] )
  nb = 5
  b = np.array ( [ 1.0, -2.1, 7.2, 8.3, 0.0, -5.5 ] )

  c = r8poly_add ( na, a, nb, b )

  r8poly_print ( na, a, '  Polynomial A:' )

  r8poly_print ( nb, b, '  Polynomial B:' )

  nc = max ( na, nb )

  nc2 = r8poly_degree ( nc, c );

  r8poly_print ( nc2, c, '  Polynomial C = A+B:' )
#
#  Terminate.
#
  print ''
  print 'R8POLY_ADD_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8poly_add_test ( )
  timestamp ( )

