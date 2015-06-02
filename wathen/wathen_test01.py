#!/usr/bin/env python

def wathen_test01 ( ):

#*****************************************************************************80
#
## WATHEN_TEST01 assembles, factor and solve using WATHEN_GE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 September 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import scipy.linalg as la

  from numpy.linalg import norm
  from r8vec_uniform_01 import r8vec_uniform_01
  from wathen_ge import wathen_ge
  from wathen_order import wathen_order

  print ''
  print 'WATHEN_TEST01'
  print '  Assemble, factor and solve a Wathen system'
  print '  defined by WATHEN_GE.'
  print ''

  nx = 4
  ny = 4
  print '  Elements in X direction NX = %d' % ( nx )
  print '  Elements in Y direction NY = %d' % ( ny )
  print '  Number of elements = %d' % ( nx * ny )
#
#  Compute the number of unknowns.
#
  n = wathen_order ( nx, ny )
  print '  Number of nodes N = %d' % ( n )
#
#  Set up a random solution X1.
#
  seed = 123456789
  x1, seed = r8vec_uniform_01 ( n, seed )
#
#  Compute the matrix.
#
  seed = 123456789
  a, seed = wathen_ge ( nx, ny, n, seed )
#
#  Compute the corresponding right hand side B.
#
  b = np.dot ( a, x1 )
#
#  Solve the linear system.
#
  x2 = la.solve ( a, b )
#
#  Compute the norm of the solution error.
#
  e = norm ( x1 - x2 )
  print '  Norm of solution error is %g' % ( e )

  return

if ( __name__ == '__main__' ):
  wathen_test01 ( )
