#! /usr/bin/env python
#
def i4poly_degree ( na, a ):

#*****************************************************************************80
#
## I4POLY_DEGREE returns the degree of a polynomial.
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
#    26 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer NA, the dimension of A.
#
#    Input, integer A[0:NA], the coefficients of the polynomial.
#
#    Output, integer DEGREE, the degree of A.
#
  degree = na

  while ( 0 < degree ):

    if ( a[degree] != 0 ):
      return degree

    degree = degree - 1;

  return degree

def i4poly_degree_test ( ):

#*****************************************************************************80
#
## I4POLY_DEGREE_TEST tests I4POLY_DEGREE.
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
  from i4poly_print import i4poly_print

  print ''
  print 'I4POLY_DEGREE_TEST'
  print '  I4POLY_DEGREE returns the degree of an I4POLY.'

  n = 10
  a = np.array ( [ 0, 1, 0, 3, 4, 0, 6, 7, 0, 0, 0 ] )

  i4poly_print ( n, a, '  The polynomial:' )

  degree = i4poly_degree ( n, a )

  print ''
  print '  The polynomial degree is %d' % ( degree )
#
#  Terminate.
#
  print ''
  print 'I4POLY_DEGREE_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4poly_degree_test ( )
  timestamp ( )
