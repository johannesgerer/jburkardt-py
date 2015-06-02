#!/usr/bin/env python

def wathen_test06 ( ):

#*****************************************************************************80
#
## WATHEN_TEST06 assembles, factor and solves using WATHEN_GE + CG_GE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  from cg_ge import cg_ge
  from numpy.linalg import norm
  from r8vec_uniform_01 import r8vec_uniform_01
  from wathen_ge import wathen_ge
  from wathen_order import wathen_order

  print ''
  print 'WATHEN_TEST06'
  print '  Assemble, factor and solve a Wathen system'
  print '  defined by WATHEN_GE and CG_GE.'
  print ''

  nx = 2
  ny = 2
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
  x2 = np.ones ( n )
  x2 = cg_ge ( n, a, b, x2 )
#
#  Compute the maximum solution error.
#
  e = norm ( x1 - x2 )

  print '  Maximum solution error is %g' % ( e )

  return

if ( __name__ == '__main__' ):
  wathen_test06 ( )


