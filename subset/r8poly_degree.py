#! /usr/bin/env python
#
def r8poly_degree ( na, a ):

#*****************************************************************************80
#
## R8POLY_DEGREE returns the degree of a polynomial.
#
#  Discussion:
#
#    The degree of a polynomial is the index of the highest power
#    of X with a nonzero coefficient.
#
#    The degree of a constant polynomial is 0.  The degree of the
#    zero polynomial is debatable, but this routine returns the
#    degree as 0.
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
#    Input, integer NA, the dimension of A.
#
#    Input, real A[0:NA], the coefficients of the polynomial.
#
#    Output, integer DEGREE, the degree of A.
#
  degree = na

  while ( 0 < degree ):

    if ( a[degree] != 0.0 ):
      return degree

    degree = degree - 1;

  return degree

def r8poly_degree_test ( ):

#*****************************************************************************80
#
## R8POLY_DEGREE_TEST tests R8POLY_DEGREE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    26 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from r8poly_print import r8poly_print

  print ''
  print 'R8POLY_DEGREE_TEST'
  print '  R8POLY_DEGREE returns the degree of an R8POLY.'

  n = 10
  a = np.array ( [ 0.0, 1.1, 0.0, 3.3, 4.4, 0.0, 6.6, 7.7, 0.0, 0.0, 0.0 ] )

  r8poly_print ( n, a, '  The polynomial:' )

  degree = r8poly_degree ( n, a )

  print ''
  print '  The polynomial degree is %d' % ( degree )
#
#  Terminate.
#
  print ''
  print 'R8POLY_DEGREE_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8poly_degree_test ( )
  timestamp ( )

