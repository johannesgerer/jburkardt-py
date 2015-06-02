#!/usr/bin/env python
#
def r8poly_degree ( m, a ):

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
#    05 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the nominal degree of A.
#
#    Input, real A(M+1), the coefficients of the polynomials.
#
#    Output, integer VALUE, the degree of A.
#
  value = m

  while ( 0 < value ):
    if ( a[value] != 0.0 ):
      break
    value = value - 1

  return value

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
#    05 January 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from r8poly_print import r8poly_print

  c1 = np.array ( [ 1.0, 2.0, 3.0, 4.0 ] )
  c2 = np.array ( [ 1.0, 2.0, 3.0, 0.0 ] )
  c3 = np.array ( [ 1.0, 2.0, 0.0, 4.0 ] )
  c4 = np.array ( [ 1.0, 0.0, 0.0, 0.0 ] )
  c5 = np.array ( [ 0.0, 0.0, 0.0, 0.0 ] )

  print ''
  print 'R8POLY_DEGREE_TEST'
  print '  R8POLY_DEGREE determines the degree of an R8POLY.'

  m = 3

  r8poly_print ( m, c1, '  The R8POLY:' )
  d = r8poly_degree ( m, c1 )
  print '  Dimensioned degree = %d,  Actual degree = %d' % ( m, d )

  r8poly_print ( m, c2, '  The R8POLY:' )
  d = r8poly_degree ( m, c2 )
  print '  Dimensioned degree = %d,  Actual degree = %d' % ( m, d )

  r8poly_print ( m, c3, '  The R8POLY:' )
  d = r8poly_degree ( m, c3 )
  print '  Dimensioned degree = %d,  Actual degree = %d' % ( m, d )

  r8poly_print ( m, c4, '  The R8POLY:' )
  d = r8poly_degree ( m, c4 )
  print '  Dimensioned degree = %d,  Actual degree = %d' % ( m, d )

  r8poly_print ( m, c5, '  The R8POLY:' )
  d = r8poly_degree ( m, c5 )
  print '  Dimensioned degree = %d,  Actual degree = %d' % ( m, d )

  print ''
  print 'R8POLY_DEGREE_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8poly_degree_test ( )
  timestamp ( )


