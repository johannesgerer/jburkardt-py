#!/usr/bin/env python

def poly_coef_count ( dim, degree ):

#*****************************************************************************80
#
## POLY_COEF_COUNT: polynomial coefficient count given dimension and degree.
#
#  Discussion:
#
#    To count all monomials of degree 5 or less in dimension 3,
#    we can count all monomials of degree 5 in dimension 4.
#
#    To count all monomials of degree 5 in dimension 4, we imagine
#    that each of the variables X, Y, Z and W is a "box" and that
#    we need to drop 5 pebbles into these boxes.  Every distinct
#    way of doing this represents a degree 5 monomial in dimension 4.
#    Ignoring W gives us monomials up to degree five in dimension 3.
#
#    To count them, we draw 3 lines as separators to indicate the
#    4 boxes, and then imagine all disctinct sequences involving
#    the three lines and the 5 pebbles.  Indicate the lines by 1's
#    and the pebbles by 0's and we're asking for the number of
#    permutations of 3 1's and 5 0's, which is 8! / (3! 5!)
#
#    In other words, 56 = 8! / (3! 5!) is:
#    * the number of monomials of degree exactly 5 in dimension 4,
#    * the number of monomials of degree 5 or less in dimension 3,
#    * the number of polynomial coefficients of a polynomial of
#      degree 5 in (X,Y,Z).
#
#    In general, the formula for the number of monomials of degree DEG
#    or less in dimension DIM is
#
#      (DEG+DIM)! / (DEG! * DIM!)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer DIM, the dimension of the polynomial.
#    0 <= DIM.
#
#    Input, integer DEGREE, the degree of the polynomnial
#    0 <= DEGREE
#
#    Output, integer VALUE, the number of coefficients
#    in the general polynomial of dimension DIM and degree DEGREE.
#
  from i4_choose import i4_choose

  if ( dim < 0 ):
    value = -1
  elif ( degree < 0 ):
    count = -1
  else:
    value = i4_choose ( degree + dim, degree )

  return value

def poly_coef_count_test ( ):

#*****************************************************************************80
#
## POLY_COEF_COUNT_TEST tests POLY_COEF_COUNT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'POLY_COEF_COUNT_TEST'
  print '  POLY_COEF_COUNT counts the number of coefficients'
  print '  in a polynomial of degree DEGREE and dimension DIM'
  print ''
  print ' Dimension    Degree     Count'
  print ''
 
  for dim in range ( 1, 11, 3 ):
    print ''
    for degree in range ( 0, 6 ):
      value = poly_coef_count ( dim, degree )
      print '  %8d  %8d  %8d' % ( dim, degree, value )

  print ''
  print 'POLY_COEF_COUNT_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  poly_coef_count_test ( )
  timestamp ( )
