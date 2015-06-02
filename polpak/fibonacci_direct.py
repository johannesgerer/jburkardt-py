#!/usr/bin/env python
#
def fibonacci_direct ( n ):

#*****************************************************************************80
#
## FIBONACCI_DIRECT computes the N-th Fibonacci number directly.
#
#  Formula:
#
#      F(N) = ( PHIP^N - PHIM^N ) / sqrt(5)
#
#    where 
#
#      PHIP = ( 1 + sqrt(5) ) / 2, 
#      PHIM = ( 1 - sqrt(5) ) / 2.
#
#  Example:
#
#     N   F
#    --  --
#     0   0
#     1   1
#     2   1
#     3   2
#     4   3
#     5   5
#     6   8
#     7  13
#     8  21
#     9  34
#    10  55
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the index of the Fibonacci number to compute.
#    N should be nonnegative.
#
#    Output, integer VALUE, the value of the N-th Fibonacci number.
#
  r8_sqrt5 = 2.236067977499790

  r8_phim = -0.618033988749895
  r8_phip =  1.618033988749895

  value = round ( ( r8_phip ** n - r8_phim ** n ) / r8_sqrt5 )

  return value

def fibonacci_direct_test ( ):

#*****************************************************************************80
#
## FIBONACCI_DIRECT_TEST tests FIBONACCI_DIRECT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'FIBONACCI_DIRECT_TEST'
  print '  FIBONACCI_DIRECT computes a Fibonacci number directly;'
  print ''
  print '   I      F(I)'
  print ''

  for i in range ( 0, 21 ):
    value = fibonacci_direct ( i )
    print '  %2d  %14d' % ( i, value )

  print ''
  print 'FIBONACCI_DIRECT_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  fibonacci_direct_test ( )
  timestamp ( )
