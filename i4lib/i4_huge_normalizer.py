#!/usr/bin/env python

def i4_huge_normalizer ( ) :

#*****************************************************************************80
#
## I4_HUGE_NORMALIZER returns the "normalizer" for I4_HUGE.
#
#  Discussion:
#
#    The value returned is 1 / ( I4_HUGE + 1 ).
#
#    For any I4, it should be the case that
#
#     -1 < I4 * I4_HUGE_NORMALIZER < 1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real I4_HUGE_NORMALIZER, the "normalizer"
#    for I4_HUGE.
#
  value = 4.656612873077392578125E-10

  return value

def i4_huge_normalizer_test ( ):

#*****************************************************************************80
#
## I4_HUGE_NORMALIZER_TEST tests I4_HUGE_NORMALIZER.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 September 2014
#
#  Author:
#
#    John Burkardt
#
  from i4_huge import i4_huge

  i4 = i4_huge ( )
  r8 = i4_huge_normalizer ( )

  print ''
  print 'I4_HUGE_NORMALIZER_TEST'
  print '  I4_HUGE_NORMALIZER returns 1/(I4_HUGE+1).'
  print ''
  print '  I4_HUGE() = %d' % ( i4 )
  print '  I4_HUGE_NORMALIZER() = %g' % ( r8 )

  product = i4 * r8

  print ''
  print '  I4_HUGE * I4_HUGE_NORMALIZER = %g' % ( product )
#
#  Terminate.
#
  print ''
  print 'I4_HUGE_NORMALIZER_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_huge_normalizer_test ( )
  timestamp ( )
