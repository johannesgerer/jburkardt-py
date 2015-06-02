#! /usr/bin/env python
#
def ellipse_grid_display ( n, r, c, ng, cg, filename ):

#*****************************************************************************80
#
## ELLIPSE_GRID_DISPLAY displays grid points inside an ellipse.
#
#  Discussion:
#
#    The ellipse is specified as
#
#      ( ( X - C1 ) / R1 )^2 + ( ( Y - C2 ) / R2 )^2 = 1
#
#    The user supplies a number N.  There will be N+1 grid points along
#    the shorter axis.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of subintervals.
#
#    Input, real R(2), the half axis lengths.
#
#    Input, real C(2), the center of the ellipse.
#
#    Input, integer NG, the number of grid points inside the ellipse.
#
#    Input, real XY(2,NG), the grid points.
#
#    Input, string FILENAME, the name of the plotfile to be created.
#
  import matplotlib.pyplot as plt
  import numpy as np

#
#  Make points on the circumference and plot them.
#
  cx = np.zeros ( 51 )
  cy = np.zeros ( 51 )
  for i in range ( 0, 51 ):
    t = 2.0 * np.pi * float ( i ) / 50.0
    cx[i] = c[0] + r[0] * np.cos ( t )
    cy[i] = c[1] + r[1] * np.sin ( t )

  plt.plot ( cx, cy, linewidth = 2.0, color = 'r' )
#
#  Plot the gridpoints.
#
  plt.plot ( cg[0,0:ng], cg[1,0:ng], 'bs' )
#
#  Cleanup and annotate.
#
  plt.xlabel ( '<---X--->' )
  plt.ylabel ( '<---Y--->' )
  plt.title ( 'Grid points in ellipse' )
  plt.grid ( True )
  plt.axis ( 'equal' )
# plt.show ( )
#
#  Save plot to file.
#
  plt.savefig ( filename )

  plt.clf ( )

  print ''
  print '  Graphics data saved in file "%s"' % (filename )

  return

def ellipse_grid_display_test ( ):

#*****************************************************************************80
#
## ELLIPSE_GRID_DISPLAY_TEST tests ELLIPSE_GRID_DISPLAY.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 April 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ''
  print 'ELLIPSE_GRID_DISPLAY_TEST:'
  print '  ELLIPSE_GRID_DISPLAY can display a grid of points in an ellipse.'

  n = 3
  r = np.array ( [ 3.0, 2.0 ] )
  c = np.array ( [ 3.0, 0.0 ] )
  ng = 19
  cg = np.array ( [ \
    [  3.0,  2.0 ], \
    [  1.0,  1.0 ], \
    [  2.0,  1.0 ], \
    [  3.0,  1.0 ], \
    [  4.0,  1.0 ], \
    [  5.0,  1.0 ], \
    [  0.0,  0.0 ], \
    [  1.0,  0.0 ], \
    [  2.0,  0.0 ], \
    [  3.0,  0.0 ], \
    [  4.0,  0.0 ], \
    [  5.0,  0.0 ], \
    [  6.0,  0.0 ], \
    [  1.0, -1.0 ], \
    [  2.0, -1.0 ], \
    [  3.0, -1.0 ], \
    [  4.0, -1.0 ], \
    [  5.0, -1.0 ], \
    [  3.0, -2.0 ]  ] )

  cg = np.transpose ( cg )
  filename = 'ellipse_grid_display.png'

  ellipse_grid_display ( n, r, c, ng, cg, filename )
#
#  Terminate.
#
  print ''
  print 'ELLIPSE_GRID_DISPLAY_TEST:'
  print '  Normal end of execution.'

  return
  
if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  ellipse_grid_display_test ( )
  timestamp ( )
