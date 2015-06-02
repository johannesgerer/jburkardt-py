#!/usr/bin/env python

def r8_to_r8_discrete ( r, rmin, rmax, nr ):

#*****************************************************************************80
#
## R8_TO_R8_DISCRETE maps R to RD in [RMIN, RMAX] with NR possible values.
#
#  Discussion:
#
#    if ( R < RMIN ) then
#      RD = RMIN
#    else if ( RMAX < R ) then
#      RD = RMAX
#    else
#      T = nint ( ( NR - 1 ) * ( R - RMIN ) / ( RMAX - RMIN ) )
#      RD = RMIN + T * ( RMAX - RMIN ) / real ( NR - 1 )
#
#    In the special case where NR = 1, when
#
#      RD = 0.5 * ( RMAX + RMIN )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    05 June 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real R, the number to be converted.
#
#    Input, real RMAX, RMIN, the maximum and minimum
#    values for RD.
#
#    Input, integer NR, the number of allowed values for XD.
#    NR should be at least 1.
#
#    Output, real RD, the corresponding discrete value.
#
  from sys import exit
#
#  Check for errors.
#
  if ( nr < 1 ):
    print
    print 'R8_TO_R8_DISCRETE - Fatal error!'
    print '  NR = %d' % ( nr )
    print '  but NR must be at least 1.'
    exit ( 'R8_TO_R8_DISCRETE - Fatal error!' )

  if ( nr == 1 ):
    rd = 0.5 * ( rmin + rmax )
    return rd

  if ( rmax == rmin ):
    rd = rmax
    return rd

  f = round ( nr * ( rmax - r ) / ( rmax - rmin ) )
  f = max ( f, 0 )
  f = min ( f, nr )

  rd = ( (      f ) * rmin   \
       + ( nr - f ) * rmax ) \
       / ( nr     )


  return rd

def r8_to_r8_discrete_test ( ):

#*****************************************************************************80
#
## R8_TO_R8_DISCRETE_TEST tests R8_TO_R8_DISCRETE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 July 2014
#
#  Author:
#
#    John Burkardt
#
  from r8_uniform_ab import r8_uniform_ab

  ndx = 19
  rhi = 10.0
  rlo = 1.0
  test_num = 15

  print ''
  print 'R8_TO_R8_DISCRETE'
  print '  R8_TO_R8_DISCRETE maps numbers to a discrete set'
  print '  of equally spaced numbers in an interval.'
  print ''
  print '  Number of discrete values = %d' % ( ndx )
  print '  Real interval: [%f, %f]' % ( rlo, rhi )
  print ''
  print '       R        RD'
  print ''

  seed = 123456789

  rlo2 = rlo - 2.0
  rhi2 = rhi + 2.0

  for test in range ( 0, test_num ):
    r, seed = r8_uniform_ab ( rlo2, rhi2, seed )
    rd = r8_to_r8_discrete ( r, rlo, rhi, ndx )
    print '  %14f  %14f' % ( r, rd )
#
#  Terminate.
#
  print ''
  print 'R8_TO_R8_DISCRETE'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_to_r8_discrete_test ( )
  timestamp ( )
