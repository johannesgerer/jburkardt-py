#! /usr/bin/env python
#
def triangle_area ( t ):

#*****************************************************************************80
#
## TRIANGLE_AREA returns the area of a triangle.
#
#  Location:
#
#    http://people.sc.fsu.edu/~jburkardt/py_src/triangle_integrals/triangle_area.py
#
#  Discussion:
#
#    If the vertices are given in counter clockwise order, the area
#    will be positive.
#
#  Licensing:
#
#    This code is distributed under the GNU GPL license.
#
#  Modified:
#
#    23 April 2015
#
#  Author:
#
#    John Burkardt.
#
#  Parameters:
#
#    Input, real T[3,2], the vertices of the triangle.
#
#    Output, real AREA, the area of the triangle.
#
  area = 0.5 * \
    ( \
        ( t[1,0] - t[0,0] ) * ( t[2,1] - t[0,1] ) \
      - ( t[2,0] - t[0,0] ) * ( t[1,1] - t[0,1] ) \
    )

  return area

def triangle_area_test ( ):

#*****************************************************************************80
#
## TRIANGLE_AREA_TEST tests TRIANGLE_AREA_MAP.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 April 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ''
  print 'TRIANGLE_AREA_TEST:'
  print '  TRIANGLE_AREA determines the (signed) area of a triangle.'

  print ''
  print '  Triangle vertices are:'
  print '    (X1,Y1) = (0,0)'
  print '    (X2,Y2) = 2*(cos(angle),sin(angle))'
  print '    (X3,Y3) = (0,1)'
  print '  where angle will sweep from 0 to 360 degrees.'

  t = np.array ( [ \
    [ 0.0, 0.0 ], \
    [ 2.0, 0.0 ], \
    [ 0.0, 1.0 ] ] )

  r = 2.0

  print ''
  print '   I      Angle         X2          Y2           Area'
  print '        (degrees)'
  print ''
  for i in range ( 0, 25 ):
    angled = float ( i ) * 180.0 / 12.0
    angler = float ( i ) * np.pi / 12.0
    t[1,0] = r * np.cos ( angler );
    t[1,1] = r * np.sin ( angler );
    area = triangle_area ( t )
    print '  %2d  %10.4f  %10.4f  %10.4f  %14.6g' \
      % ( i, angled, t[1,0], t[1,1], area )
#
#  Terminate.
#
  print ''
  print 'TRIANGLE_AREA_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  triangle_area_test ( )
  timestamp ( )
