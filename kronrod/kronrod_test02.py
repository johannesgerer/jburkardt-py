#!/usr/bin/env python

def kronrod_test02 ( ):

#*****************************************************************************80
#
## KRONROD_TEST02 tests the code for the even case N = 4.
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

  n = 4

  print ''
  print 'KRONROD_TEST02'
  print '  Request KRONROD to compute the Gauss rule'
  print '  of order 4, and the Kronrod extension of'
  print '  order 4+5=9.'

  tol = 0.000001

  [ x, w1, w2 ] = kronrod ( n, tol )

  print ''
  print '  KRONROD returns 3 vectors of length %d' % ( n + 1 )
  print ''
  print '     I      X               WK              WG'
  print ''
  for i in range ( 1, n + 2 ):
    print '  %4d  %14f  %14f  %14f' % ( i, x[i-1], w1[i-1], w2[i-1] )

  return

