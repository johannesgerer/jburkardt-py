#! /usr/bin/env python
#
def r8poly_print ( n, a, title ):

#*****************************************************************************80
#
## R8POLY_PRINT prints out a polynomial.
#
#  Discussion:
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
#    28 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the dimension of A.
#
#    Input, real A[0:N], the polynomial coefficients.
#    A(1) is the constant term and
#    A(N+1) is the coefficient of X^N.
#
#    Input, character TITLE(*), an optional title.
#
  from r8poly_degree import r8poly_degree

  if ( 0 < len ( title ) ):
    print ''
    print title

  print ''

  n = r8poly_degree ( n, a )

  if ( a[n] < 0.0 ):
    plus_minus = '-'
  else:
    plus_minus = ' '

  mag = abs ( a[n] )

  if ( 2 <= n ):
    print '  p(x) = %c%14f * x^%d' % ( plus_minus, mag, n )
  elif ( n == 1 ):
    print '  p(x) = %c%14f * x' % ( plus_minus, mag )
  elif ( n == 0 ):
    print '  p(x) = %c%14f' % ( plus_minus, mag )

  for i in range ( n - 1, -1, -1 ):

    if ( a[i] < 0.0 ):
      plus_minus = '-'
    else:
      plus_minus = '+'

    mag = abs ( a[i] )

    if ( mag != 0.0 ):

      if ( 2 <= i ):
        print '         %c%14f * x^%d' % ( plus_minus, mag, i )
      elif ( i == 1 ):
        print '         %c%14f * x' % ( plus_minus, mag )
      elif ( i == 0 ):
        print '         %c%14f' % ( plus_minus, mag )

  return

def r8poly_print_test ( ):

#*****************************************************************************80
#
## R8POLY_PRINT_TEST tests R8POLY_PRINT.
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

  print ''
  print 'R8POLY_PRINT_TEST'
  print '  R8POLY_PRINT prints an R8POLY.'

  n = 4
  a = np.array ( [ -2.0, 5.1, 2.2, 3.3, 1.4 ] )

  r8poly_print ( n, a, '  The polynomial:' )
#
#  Terminate.
#
  print ''
  print 'R8POLY_PRINT_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8poly_print_test ( )
  timestamp ( )

