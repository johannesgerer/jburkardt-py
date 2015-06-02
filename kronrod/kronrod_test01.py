#!/usr/bin/env python

def kronrod_test01 ( ):

#*****************************************************************************80
#
## KRONROD_TEST01 tests the code for the odd case N = 3.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 April 2013
#
#  Author:
#
#    John Burkardt
#
  import numpy
  from kronrod import kronrod

  n = 3

  wg = numpy.array ( [ \
    0.555555555555555555556, \
    0.888888888888888888889, \
    0.555555555555555555556 ] )

  wk = numpy.array ( [ \
    0.104656226026467265194, \
    0.268488089868333440729, \
    0.401397414775962222905, \
    0.450916538658474142345, \
    0.401397414775962222905, \
    0.268488089868333440729, \
    0.104656226026467265194 ] )

  xg = numpy.array ( [ \
   -0.77459666924148337704, \
    0.0, \
    0.77459666924148337704 ] )

  xk = numpy.array ( [ \
   -0.96049126870802028342, \
   -0.77459666924148337704, \
   -0.43424374934680255800, \
    0.0, \
    0.43424374934680255800, \
    0.77459666924148337704, \
    0.96049126870802028342 ] )

  print ''
  print 'KRONROD_TEST01'
  print '  Request KRONROD to compute the Gauss rule'
  print '  of order 3, and the Kronrod extension of'
  print '  order 3+4=7.'
  print ''
  print '  Compare to exact data.'

  tol = 0.000001

  [ x, w1, w2 ] = kronrod ( n, tol )

  print ''
  print '  KRONROD returns 3 vectors of length %d' % ( n + 1 ) 
  print ''
  print '     I      X               WK              WG'
  print ''
  for i in range ( 1, n + 2 ):
    print '  %4d  %14f  %14f  %14f' % ( i, x[i-1], w1[i-1], w2[i-1] )

  print ''
  print '               Gauss Abscissas'
  print '            Exact           Computed'
  print ''
  for i in range ( 1, n + 1 ):
    if ( 2 * i <= n + 1 ):
      i2 = 2 * i
      s = -1.0
    else:
      i2 = 2 * ( n + 1 ) - 2 * i
      s = +1.0
    print '  %4d  %14f  %14f' % ( i, xg[i-1], s * x[i2-1] )
  print ''
  print '               Gauss Weights'
  print '            Exact           Computed'
  print ''
  for i in range ( 1, n + 1 ):
    if ( 2 * i <= n + 1 ):
      i2 = 2 * i
    else:
      i2 = 2 * ( n + 1 ) - 2 * i
    print '  %4d  %14f  %14f' % ( i, wg[i-1], w2[i2-1] )

  print ''
  print '             Gauss Kronrod Abscissas'
  print '            Exact           Computed'
  print ''
  for i in range ( 1, 2 * n + 2 ):
    if ( i <= n + 1 ):
      i2 = i
      s = -1.0
    else:
      i2 = 2 * ( n + 1 ) - i
      s = +1.0
    print '  %4d  %14f  %14f' % ( i, xk[i-1], s * x[i2-1] )
  print ''
  print '             Gauss Kronrod Weights'
  print '            Exact           Computed'
  print ''
  for i in range ( 1, 2 * n + 2 ):
    if ( i <= n + 1 ):
      i2 = i
    else:
      i2 = 2 * ( n + 1 ) - i
    print '  %4d  %14f  %14f' % ( i, wk[i-1], w1[i2-1] )

  return

