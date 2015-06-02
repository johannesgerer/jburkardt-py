#!/usr/bin/env python

def mono_upto_enum ( m, n ):

#*****************************************************************************80
#
## MONO_UPTO_ENUM enumerates monomials in M dimensions of degree up to N.
#
#  Discussion:
#
#    For M = 2, we have the following values:
#
#    N  VALUE
#
#    0    1
#    1    3
#    2    6
#    3   10
#    4   15
#    5   21
#
#    In particular, VALUE(2,3) = 10 because we have the 10 monomials:
#
#      1, x, y, x^2, xy, y^2, x^3, x^2y, xy^2, y^3.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the spatial dimension.
#
#    Input, integer N, the maximum degree.
#
#    Output, integer VALUE, the number of monomials in
#    M variables, of total degree N or less.
#
  from i4_choose import i4_choose

  value = i4_choose ( n + m, n )

  return value

def mono_upto_enum_test ( ):

#*****************************************************************************80
#
## MONO_UPTO_ENUM_TEST tests MONO_UPTO_ENUM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 October 2014
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'MONO_UPTO_ENUM_TEST'
  print '  MONO_UPTO_ENUM can enumerate the number of monomials'
  print '  in M variables, of total degree between 0 and N.'

  print '';
  print '    N:',
  for n in range ( 0, 9 ):
    print '  %4d' % ( n ),
  print ''
  print '   M +---------------------------------------------------------------'
  for m in range ( 1, 9 ):
    print '  %2d |' % ( m ),
    for n in range ( 0, 9 ):
      v = mono_upto_enum ( m, n )
      print ' %5d' % ( v ),
    print ''

  print ''
  print 'MONO_UPTO_ENUM_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp

  timestamp ( )
  mono_upto_enum_test ( )
  timestamp ( )
