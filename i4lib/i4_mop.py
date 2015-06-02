#!/usr/bin/env python
#
def i4_mop ( i ):

#*****************************************************************************80
#
## I4_MOP returns the I-th power of -1 as an I4.
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
#    Input, integer I, the power of -1.
#
#    Output, integer I4_MOP, the I-th power of -1.
#
  if ( ( i % 2 ) == 0 ):
    value = + 1
  else:
    value = - 1

  return value

def i4_mop_test ( ):

#*****************************************************************************80
#
## I4_MOP_TEST tests I4_MOP.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 May 2015
#
#  Author:
#
#    John Burkardt
#
  from i4_uniform_ab import i4_uniform_ab

  print ''
  print 'I4_MOP_TEST'
  print '  I4_MOP computes a minus-one-power (-1)^I.'
  print ' '
  print '        I4  I4_MOP(I4)'
  print ' '

  i4_lo = -1000000
  i4_hi = +1000000
  seed = 123456789
  
  for i in range ( 0, 10 ):
    i4, seed = i4_uniform_ab ( i4_lo, i4_hi, seed )
    print '  %8d  %10d' % ( i4, i4_mop ( i4 ) )
#
#  Terminate.
#
  print ''
  print 'I4_MOP_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_mop_test ( )
  timestamp ( )

