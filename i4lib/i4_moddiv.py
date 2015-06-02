#!/usr/bin/env python

def i4_moddiv ( n, d ):

#*****************************************************************************80
#
## I4_MODDIV breaks a number into a multiple of a divisor and remainder.
#
#  Discussion:
#
#    N = M * D + R
#
#    0 <= || R || < || D ||
#
#    R has the sign of N.
#
#  Example:
#
#    N         D       M      R
#
#   107       50      2      7
#   107      -50     -2      7
#  -107       50     -2     -7
#  -107      -50      2     -7
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number to be decomposed.
#
#    Input, integer D, the divisor.  D may not be zero.
#
#    Output, integer M, the number of times N
#    is evenly divided by D.
#
#    Output, integer R, a remainder.
#
  from math import floor
  from sys import exit

  if ( d == 0 ):
    print ''
    print 'I4_MODDIV - Fatal error!'
    print '  Input divisor D = 0'
    exit ( 'I4_MODDIV - Fatal error!' )

  m = floor ( n / d )
  r = n - d * m

  return m, r

def i4_moddiv_test ( ):

#*****************************************************************************80
#
## I4_MODDIV_TEST tests I4_MODDIV.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 September 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  test_num = 4

  n_vec = np.array ( ( 107, 107, -107, -107 ) )
  d_vec = np.array ( ( 50, -50, 50, -50 ) )

  print ''
  print 'I4_MODDIV_TEST'
  print '  I4_MODDIV factors a number'
  print '  into a multiple M and a remainder R.'
  print ''
  print '    Number   Divisor  Multiple Remainder'
  print ''

  for test in range ( 0, test_num ):
    n = n_vec[test]
    d = d_vec[test]
    m, r = i4_moddiv ( n, d )
    print '  %8d  %8d  %8d  %8d' % ( n, d, m, r )

  print ''
  print '  Repeat using Python % Operator:'
  print ''

  for test in range ( 0, test_num ):
    n = n_vec[test]
    d = d_vec[test]
    m = n // d
    r = n % d
    print '  %8d  %8d  %8d  %8d' % ( n, d, m, r )
#
#  Terminate.
#
  print ''
  print 'I4_MODDIV_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_moddiv_test ( )
  timestamp ( )
