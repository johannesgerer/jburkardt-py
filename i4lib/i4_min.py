#!/usr/bin/env python

def i4_min ( a, b ):

#*****************************************************************************80
#
## I4_MIN returns the minimum of two I4's.
#
#  Discussion:
#
#    An I4 is an integer.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer A, B, values to compare.
#
#    Output, real VALUE, the minimum of A and B.
#
  if ( a < b ):
    value = a
  else:
    value = b

  return value

def i4_min_test ( ):

#*****************************************************************************80
#
## I4_MIN_TEST tests I4_MIN.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 March 2015
#
#  Author:
#
#    John Burkardt
#
  from i4_uniform_ab import i4_uniform_ab

  print ''
  print 'I4_MIN_TEST'
  print '  I4_MIN computes the minimum of two I4\'s.'

  i4_lo = - 100
  i4_hi = + 100
  seed = 123456789

  print ''
  print '         A         B     C=I4_MIN(A,B)'
  print ''
  for i in range ( 0, 10 ):
    a, seed = i4_uniform_ab ( i4_lo, i4_hi, seed )
    b, seed = i4_uniform_ab ( i4_lo, i4_hi, seed )
    c = i4_min ( a, b )
    print '  %8d  %8d  %8d' % ( a, b, c )
#
#  Terminate.
#
  print ''
  print 'I4_MIN_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_min_test ( )
  timestamp ( )

