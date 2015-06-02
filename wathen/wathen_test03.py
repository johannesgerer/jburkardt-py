#!/usr/bin/env python

def wathen_test03 ( ):

#*****************************************************************************80
#
## WATHEN_TEST03 times WATHEN_GE assembly and solution.
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
  import time

  from numpy.linalg import norm
  from r8vec_uniform_01 import r8vec_uniform_01
  from wathen_ge import wathen_ge
  from wathen_order import wathen_order
 
  print ''
  print 'WATHEN_TEST03'
  print '  For various problem sizes,'
  print '  time the assembly and factorization of a Wathen system'
  print '  using the WATHEN_GE function.'
  print ''
  print '    NX  Elements   Nodes   Storage    Assembly      ',
  print 'Factor      Error'
  print ''

  nx = 1
  ny = 1

  for test in range ( 0, 6 ):
#
#  Compute the number of unknowns.
#
    n = wathen_order ( nx, ny )
    storage_ge = n * n
#
#  Set up a random solution X1.
#
    seed = 123456789
    x1, seed = r8vec_uniform_01 ( n, seed )
#
#  Compute the matrix.
#
    seed = 123456789
    t0 = time.clock ( )
    a, seed = wathen_ge ( nx, ny, n, seed )
    t1 = ( time.clock ( ) - t0 )
#
#  Compute the corresponding right hand side B.
#
    b = np.dot ( a, x1 )
#
#  Solve the system.
#
    t0 = time.clock ( )
    x2 = la.solve ( a, b )
    t2 = ( time.clock ( ) - t0 )
#
#  Compute the norm of the solution error.
#
    e = norm ( x1 - x2 )
#
#  Report.
#
    print '  %4d      %4d  %6d  %8d  %10.2e  %10.2e  %10.2e' % \
      ( nx, nx * ny, n, storage_ge, t1, t2, e )
#
#  Ready for next iteration.
#
    nx = nx * 2
    ny = ny * 2

  return

if ( __name__ == '__main__' ):
  wathen_test03 ( )

