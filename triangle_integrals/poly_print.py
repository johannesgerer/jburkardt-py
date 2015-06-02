#! /usr/bin/env python
#
def poly_print ( d, p, title ):

#*****************************************************************************80
#
## POLY_PRINT prints an XY polynomial.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer D, the degree of the polynomial.
#
#    Output, real P(M), the coefficients of all monomials of degree 0 through D.
#    P must contain ((D+1)*(D+2))/2 entries.
#
#    Input, string TITLE, a title string.
#
  from i4_to_pascal import i4_to_pascal

  m = ( ( d + 1 ) * ( d + 2 ) ) / 2

  allzero = True

  for i in range ( 0, m ):
    if ( p[i] != 0.0 ):
      allzero = False
  
  if ( allzero ):

    print '%s = 0.0' % ( title )

  else:

    print '%s = ' % ( title )

    for k in range ( 1, m + 1 ):

      i, j = i4_to_pascal ( k )
      di = i + j
      km1 = k - 1

      if ( p[km1] != 0.0 ):

        if ( p[km1] < 0.0 ):
          print '  -%g' % ( abs ( p[km1] ) ),
        else:
          print '  +%g' % ( p[km1] ),

        if ( di != 0 ):
          print '',
#
#  "PASS" does nothing, but Python requires a statement here.
#
#  Python idiotically insists on putting a space between successive prints,
#  and I don't feel like calling sys.stdout.write ( string ) in order to
#  suppress something I shouldn't have to deal with in the first place,
#  so pretend you like it.
#
        if ( i == 0 ):
          pass
        elif ( i == 1 ):
          print 'x',
        else:
          print 'x^%d' % ( i ),

        if ( j == 0 ):
          pass
        elif ( j == 1 ):
          print 'y',
        else:
          print 'y^%d' % ( j ),

        print ''

  return

def poly_print_test ( ):

#*****************************************************************************80
#
## POLY_PRINT_TEST tests POLY_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 April 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ''
  print 'POLY_PRINT_TEST:'
  print '  POLY_PRINT can print a D-degree polynomial in X and Y.'
#
#  P = 12.34
#
  d = 0
  p = np.array ( [ 12.34 ] )
  print ''
  poly_print ( d, p, '  p1(x,y)' )
#
#  P = 1.0 + 2.0 * x + 3.0 * Y
#
  d = 1
  p = np.array ( [ 1.0, 2.0, 3.0 ] )
  print ''
  poly_print ( d, p, '  p2(x,y)' )
#
#  P = XY
#
  d = 2
  p = np.array ( [ 0.0, 0.0, 0.0, 0.0, 1.0, 0.0 ] )
  print ''
  poly_print ( d, p, '  p3(x,y) = xy' )
#
#  P = 1 - 2.1 * x + 3.2 * y - 4.3 * x^2 + 5.4 * xy - 6.5 * y^2
#    + 7.6 * x^3 - 8.7 * x^2y + 9.8 * xy^2 - 10.9 * y^3.
#
  d = 3
  p = np.array ( [ 1.0, -2.1, +3.2, -4.3, +5.4, -6.5, +7.6, -8.7, +9.8, -10.9 ] )
  print ''
  poly_print ( d, p, '  p4(x,y)' )
#
#  Terminate.
#
  print ''
  print 'POLY_PRINT_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  poly_print_test ( )
  timestamp ( )
