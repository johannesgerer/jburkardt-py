#! /usr/bin/env python
#
def xy_to_rs_map ( t ):

#*****************************************************************************80
#
## XY_TO_RS_MAP returns the linear map from physical to reference triangle.
#
#  Location:
#
#    http://people.sc.fsu.edu/~jburkardt/py_src/triangle_integrals/xy_to_rs_map.py
#
#  Discussion:
#
#    Given the vertices T of an arbitrary triangle in the (X,Y) coordinate
#    system, this function returns the coefficients of the linear map
#    that sends the vertices of T to (0,0), (1,0) and (0,1) respectively
#    in the reference triangle with coordinates (R,S):
#
#      R = A + B * X + C * Y;
#      S = D + E * X + F * Y.
#
#  Reference Element T3:
#
#    |
#    1  3
#    |  |\
#    |  | \
#    S  |  \
#    |  |   \
#    |  |    \
#    0  1-----2
#    |
#    +--0--R--1-->
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real T[3,2], the X and Y coordinates
#    of the vertices.  The vertices are assumed to be the images of
#    (0,0), (1,0) and (0,1) respectively.
#
#    Output, real A, B, C, D, E, F, the mapping coefficients.
#
  g =   ( ( t[2,1] - t[0,1] ) * ( t[1,0] - t[0,0] )   \
        - ( t[2,0] - t[0,0] ) * ( t[1,1] - t[0,1] ) )

  a = ( - ( t[2,1] - t[0,1] ) * t[0,0]   \
        + ( t[2,0] - t[0,0] ) * t[0,1] ) / g

  b =     ( t[2,1] - t[0,1] ) / g

  c =   - ( t[2,0] - t[0,0] ) / g

  d = (   ( t[1,1] - t[0,1] ) * t[0,0] \
        - ( t[1,0] - t[0,0] ) * t[0,1] ) / g

  e =   - ( t[1,1] - t[0,1] ) / g

  f =     ( t[1,0] - t[0,0] ) / g

  return a, b, c, d, e, f


def xy_to_rs_map_test ( ):

#*****************************************************************************80
#
## XY_TO_RS_MAP_TEST tests XY_TO_RS_MAP.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 April 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from r8mat_print import r8mat_print

  print ''
  print 'XY_TO_RS_MAP_TEST:'
  print '  XY_TO_RS_MAP determines the coefficients of the linear map'
  print '  from a general triangle in XY coordinates to the reference'
  print '  triangle in RS coordinates:'
  print '    R = a + b * X + c * Y'
  print '    S = d + e * X + f * Y'

  t = np.array ( [ \
    [ 2.0, 0.0 ], \
    [ 3.0, 4.0 ], \
    [ 0.0, 3.0 ] ] )

  r8mat_print ( 3, 2, t, '  XY triangle vertices:' )

  a, b, c, d, e, f = xy_to_rs_map ( t )

  print ''
  print '  Mapping coefficients are:'
  print ''
  print '    R = %g + %g * X + %g * Y' % ( a, b, c )
  print '    S = %g + %g * X + %g * Y' % ( d, e, f )

  print ''
  print '  Apply map to XY triangle vertices.'
  print '  Recover RS vertices (0,0), (1,0) and (0,1).'
  print ''
  for i in range ( 0, 3 ):
    r = a + b * t[i,0] + c * t[i,1]
    s = d + e * t[i,0] + f * t[i,1]
    print '  V(%d) = (%g,%g)' % ( i, r, s )
#
#  Terminate.
#
  print ''
  print 'XY_TO_RS_MAP_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  xy_to_rs_map_test ( )
  timestamp ( )
