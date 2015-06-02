#!/usr/bin/env python

def r8_mop ( i ):

#*****************************************************************************80
#
## R8_MOP returns the I-th power of -1 as an R8 value.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    01 June 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer I, the power of -1.
#
#    Output, real R8_MOP, the I-th power of -1.
#
  if ( ( i % 2 ) == 0 ):
    value = + 1.0
  else:
    value = - 1.0

  return value

def r8_mop_test ( ):

#*****************************************************************************80
#
## R8_MOP_TEST tests R8_MOP.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 December 2014
#
#  Author:
#
#    John Burkardt
#
  from i4_uniform_ab import i4_uniform_ab

  print ''
  print 'R8_MOP_TEST'
  print '  R8_MOP evaluates (-1.0)^I4 as an R8.'
  print ''
  print '    I4  R8_MOP(I4)'
  print ''

  i4_min = -100;
  i4_max = +100;
  seed = 123456789;

  for test in range ( 0, 10 ):
    i4, seed = i4_uniform_ab ( i4_min, i4_max, seed )
    r8 = r8_mop ( i4 )
    print '  %4d  %4.1f' % ( i4, r8 )
#
#  Terminate.
#
  print ''
  print 'R8_MOP_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_mop_test ( )
  timestamp ( )
