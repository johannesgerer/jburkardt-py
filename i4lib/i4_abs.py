#!/usr/bin/env python

def i4_abs ( a ):

#*****************************************************************************80
#
## I4_ABS returns the absolute value of an I4.
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
#    10 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer A, the value.
#
#    Output, integer VALUE, the absolute value.
#
  if ( a < 0 ):
    value = -a
  else:
    value = a

  return value

def i4_abs_test ( ):

#*****************************************************************************80
#
## I4_ABS_TEST tests I4_ABS.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 March 2015
#
#  Author:
#
#    John Burkardt
#
  from i4_uniform_ab import i4_uniform_ab

  print ''
  print 'I4_ABS_TEST'
  print '  I4_ABS computes the absolute value of an I4.'

  i4_lo = - 100
  i4_hi = + 100
  seed = 123456789

  print ''
  print '         A         B=I4_ABS(A)'
  print ''
  for i in range ( 0, 10 ):
    a, seed = i4_uniform_ab ( i4_lo, i4_hi, seed )
    b = i4_abs ( a )
    print '  %8d  %8d' % ( a, b )
#
#  Terminate.
#
  print ''
  print 'I4_ABS_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_abs_test ( )
  timestamp ( )

