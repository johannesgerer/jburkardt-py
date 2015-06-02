#! /usr/bin/env python
#
def rs_to_xy_map ( t ):

#*****************************************************************************80
#
## RS_TO_XY_MAP returns the linear map from reference to physical triangle.
#
#  Location:
#
#    http://people.sc.fsu.edu/~jburkardt/py_src/triangle_poly_integral/rs_to_xy_map.py
#
#  Discussion:
#
#    This function returns the coefficients of the linear map that sends
#    the vertices of the reference triangle, (0,0), (1,0) and (0,1), to
#    the vertices of a physical triangle T, of the form:
#
#      X = A + B * R + C * S;
#      Y = D + E * R + F * S.
#
#  Reference Element:
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
#    Input, real T[3,2], the coordinates of the vertices.  The vertices are 
#    assumed to be the images of (0,0), (1,0) and (0,1) respectively.
#
#    Output, real A, B, C, D, E, F, the mapping coefficients.
#
  a = t[0,0]
  b = t[1,0] - t[0,0]
  c = t[2,0] - t[0,0]

  d = t[0,1]
  e = t[1,1] - t[0,1]
  f = t[2,1] - t[0,1]

  return a, b, c, d, e, f

def rs_to_xy_map_test ( ):

#*****************************************************************************80
#
## RS_TO_XY_MAP_TEST tests RS_TO_XY_MAP.
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
  print 'RS_TO_XY_MAP_TEST:'
  print '  RS_TO_XY_MAP determines the coefficients of the linear map'
  print '  from a the reference in RS coordinates to the physical'
  print '  triangle in XY coordinates:'
  print '    X = a + b * R + c * S'
  print '    Y = d + e * R + f * S'

  tr = np.array ( [ \
    [ 0.0, 0.0 ], \
    [ 1.0, 0.0 ], \
    [ 0.0, 1.0 ] ] )

  t = np.array ( [ \
    [ 2.0, 0.0 ], \
    [ 3.0, 4.0 ], \
    [ 0.0, 3.0 ] ] )

  r8mat_print ( 3, 2, t, '  XY triangle vertices:' )

  a, b, c, d, e, f = rs_to_xy_map ( t )

  print ''
  print '  Mapping coefficients are:'
  print ''
  print '    X = %g + %g * R + %g * S' % ( a, b, c )
  print '    Y = %g + %g * R + %g * S' % ( d, e, f )

  print ''
  print '  Apply map to RS triangle vertices.'
  print '  Recover XY vertices (2,0), (3,4) and (0,3).'
  print ''
  for i in range ( 0, 3 ):
    x = a + b * tr[i,0] + c * tr[i,1]
    y = d + e * tr[i,0] + f * tr[i,1]
    print '  V(%d) = ( %g, %g )' % ( i, x, y )
#
#  Terminate.
#
  print ''
  print 'RS_TO_XY_MAP_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  rs_to_xy_map_test ( )
  timestamp ( )
