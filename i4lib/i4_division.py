#!/usr/bin/env python

def i4_division ( a, b ):

#*****************************************************************************80
#
## I4_DIVISION returns the result of integer division.
#
#  Discussion:
#
#    This routine computes C = A / B, where the result is rounded to the
#    integer value nearest 0.
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
#    Input, integer A, B, the number to be divided,
#    and the divisor.
#
#    Output, integer C, the rounded result of the division.
#
  from math import floor

  if ( a * b < 0.0 ):
    s = -1
  else:
    s = +1

  a = abs ( a )
  b = abs ( b )
  c = s * floor ( a / b )

  return c

def i4_division_test ( ):

#*****************************************************************************80
#
## I4_DIVISION_TEST tests I4_DIVISION.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 May 2015
#
#  Author:
#
#    John Burkardt
#
  from i4_uniform_ab import i4_uniform_ab
  from math import floor

  a_hi =  100
  a_lo = -100
  b_hi =  10
  b_lo = -10
  test_num = 20

  print ' '
  print 'I4_DIVISION_TEST'
  print '  I4_DIVISION performs integer division.'
  print ' '
  print '  C0 = real ( a ) / real ( b )'
  print '  C1 = I4_DIVISION ( A, B )'
  print '  C2 = nint ( real ( a ) / real ( b ) )'
  print '  C3 = int ( A / B )'
  print '  C4 = floor ( real ( a ) / real ( b ) )'
  print '  C5 = a // b'
  print ' '
  print '  C1 and C3 and C4 and C5 should be equal.'
  print '  (They are not, for some negative cases!)'
  print '  C2 may differ;'
  print ' '
  print '     A     B           C0         C1    C2      C3    C4      C5'
  print ' '

  seed = 123456789

  for test in range ( 1, test_num ):
    a, seed = i4_uniform_ab ( a_lo, a_hi, seed )
    b, seed = i4_uniform_ab ( b_lo, b_hi, seed )
    if ( b == 0 ):
      b = 7
    c0 = float ( a ) / float ( b )
    c1 = i4_division ( a, b )
    c2 = round ( float ( a ) / float ( b ) )
    c3 = int ( a / b )
    c4 = floor ( float ( a ) / float ( b ) )
    c5 = a // b
    print '  %4d  %4d    %14.6f  %4d  %4d    %4d  %4d    %4d' \
      % ( a, b, c0, c1, c2, c3, c4, c5 )
#
#  Terminate.
#
  print ' '
  print 'I4_DIVISION_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_division_test ( )
  timestamp ( )

