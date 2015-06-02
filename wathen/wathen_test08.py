#!/usr/bin/env python

def wathen_test08 ( ):

#*****************************************************************************80
#
## WATHEN_TEST08 assemble, factor and solve using WATHEN_ST + CG_ST.
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

  from cg_st import cg_st
  from mv_st import mv_st
  from numpy.linalg import norm
  from r8vec_uniform_01 import r8vec_uniform_01
  from wathen_order import wathen_order
  from wathen_st import wathen_st
  from wathen_st_size import wathen_st_size

  print ''
  print 'WATHEN_TEST08'
  print '  Assemble, factor and solve a Wathen system'
  print '  defined by WATHEN_ST and CG_ST.'
  print ''

  nx = 1
  ny = 1
  print '  Elements in X direction NX = %d' % ( nx )
  print '  Elements in Y direction NY = %d' % ( ny )
  print '  Number of elements = %d' % ( nx * ny )
#
#  Compute the number of unknowns.
#
  n = wathen_order ( nx, ny )
  print '  Number of nodes N = %d' % ( n )
#
#  Compute the matrix size.
#
  nz_num = wathen_st_size ( nx, ny )
  print '  Number of nonzeros = %d\n' % ( nz_num )
#
#  Set up a random solution X1.
#
  seed = 123456789
  x1, seed = r8vec_uniform_01 ( n, seed )
#
#  Compute the matrix.
#
  seed = 123456789
  row, col, a, seed = wathen_st ( nx, ny, nz_num, seed )
#
#  Compute the corresponding right hand side B.
#
  b = mv_st ( n, n, nz_num, row, col, a, x1 )
#
#  Solve the linear system.
#
  x2 = np.ones ( n )
  x2 = cg_st ( n, nz_num, row, col, a, b, x2 )
#
#  Compute the solution error norm.
#
  e = norm ( x1 - x2 )
  print '  Maximum solution error is %g' % ( e )

  return

if ( __name__ == '__main__' ):
  wathen_test08 ( )
