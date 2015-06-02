#!/usr/bin/env python

def i4_wrap ( ival, ilo, ihi ):

#*****************************************************************************80
#
## I4_WRAP forces an integer to lie between given limits by wrapping.
#
#  Example:
#
#    ILO = 4, IHI = 8
#
#    I   Value
#
#    -2     8
#    -1     4
#     0     5
#     1     6
#     2     7
#     3     8
#     4     4
#     5     5
#     6     6
#     7     7
#     8     8
#     9     4
#    10     5
#    11     6
#    12     7
#    13     8
#    14     4
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
#    Input, integer IVAL, an integer value.
#
#    Input, integer ILO, IHI, the desired bounds for the integer value.
#
#    Output, integer VALUE, a "wrapped" version of IVAL.
#
  from i4_modp import i4_modp

  jlo = min ( ilo, ihi )
  jhi = max ( ilo, ihi )

  wide = jhi - jlo + 1

  if ( wide == 1 ):
    value = jlo
  else:
    value = jlo + i4_modp ( ival - jlo, wide )

  return value

def i4_wrap_test ( ):

#*****************************************************************************80
#
## I4_WRAP_TEST tests I4_WRAP.
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
  ilo = 4
  ihi = 8

  print ''
  print 'I4_WRAP_TEST'
  print '  I4_WRAP forces an integer to lie within given limits.'
  print ''
  print '  ILO = %d' % ( ilo )
  print '  IHI = %d' % ( ihi )
  print ''
  print '     I  I4_WRAP(I)'
  print ''

  for i in range ( -10, 21 ):
    j = i4_wrap ( i, ilo, ihi )
    print '  %6d  %6d' % ( i, j )
#
#  Terminate.
#
  print ''
  print 'I4_WRAP_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_wrap_test ( )
  timestamp ( )
