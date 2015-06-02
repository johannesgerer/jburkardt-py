#! /usr/bin/env python
#
def i4poly_print ( n, a, title ):

#*****************************************************************************80
#
## I4POLY_PRINT prints out a polynomial.
#
#  Discussion:
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
#    26 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the dimension of A.
#
#    Input, integer A(1:N+1), the polynomial coefficients.
#    A(1) is the constant term and
#    A(N+1) is the coefficient of X**N.
#
#    Input, character TITLE(*), an optional title.
#
  from i4poly_degree import i4poly_degree

  if ( 0 < len ( title ) ):
    print ''
    print title

  print ''

  n2 = i4poly_degree ( n, a )

  if ( a[n2] < 0 ):
    plus_minus = '-'
  else:
    plus_minus = ' '

  mag = abs ( a[n2] )

  if ( 2 <= n2 ):
    print ' p(x) = %c%d * x^%d' % ( plus_minus, mag, n2 )
  elif ( n2 == 1 ):
    print ' p(x) = %c%d * x' % ( plus_minus, mag )
  elif ( n2 == 0 ):
    print ' p(x) = %c%d' % ( plus_minus, mag )

  for i in range ( n2 - 1, -1, -1 ):

    if ( a[i] < 0.0 ):
      plus_minus = '-'
    else:
      plus_minus = '+'

    mag = abs ( a[i] )

    if ( mag != 0 ):

      if ( 2 <= i ):
        print '        %c%d * x^%d' % ( plus_minus, mag, i )
      elif ( i == 1 ):
        print '        %c%d * x' % ( plus_minus, mag )
      elif ( i == 0 ):
        print '        %c%d' % ( plus_minus, mag )

  return

def i4poly_print_test ( ):

#*****************************************************************************80
#
## I4POLY_PRINT_TEST tests I4POLY_PRINT.
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

  print ''
  print 'I4POLY_PRINT_TEST'
  print '  I4POLY_PRINT prints an I4POLY.'

  n = 4
  a = np.array ( [ -2, 5, 2, 3, 1 ] )

  i4poly_print ( n, a, '  The polynomial:' )
#
#  Terminate.
#
  print ''
  print 'I4POLY_PRINT_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4poly_print_test ( )
  timestamp ( )

