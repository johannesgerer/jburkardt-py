#!/usr/bin/env python

def i4_max ( a, b ):

#*****************************************************************************80
#
## I4_MAX returns the maximum of two I4's.
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
#    Output, integer VALUE, the maximum of A and B.
#
  if ( a < b ):
    value = b
  else:
    value = a

  return value

def i4_max_test ( ):

#*****************************************************************************80
#
## I4_MAX_TEST tests I4_MAX.
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
  print 'I4_MAX_TEST'
  print '  I4_MAX computes the maximum of two I4\'s.'

  i4_lo = - 100
  i4_hi = + 100
  seed = 123456789

  print ''
  print '         A         B     C=I4_MAX(A,B)'
  print ''
  for i in range ( 0, 10 ):
    a, seed = i4_uniform_ab ( i4_lo, i4_hi, seed )
    b, seed = i4_uniform_ab ( i4_lo, i4_hi, seed )
    c = i4_max ( a, b )
    print '  %8d  %8d  %8d' % ( a, b, c )
#
#  Terminate.
#
  print ''
  print 'I4_MAX_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_max_test ( )
  timestamp ( )

