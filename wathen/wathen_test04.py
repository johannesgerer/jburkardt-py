#!/usr/bin/env python

def wathen_test04 ( ):

#*****************************************************************************80
#
## WATHEN_TEST04 times WATHEN_CSC assembly and solution.
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
  import scipy.sparse.linalg as ssl
  import time

  from numpy.linalg import norm
  from r8vec_uniform_01 import r8vec_uniform_01
  from wathen_csc import wathen_csc
  from wathen_order import wathen_order
 
  print ''
  print 'WATHEN_TEST04'
  print '  For various problem sizes,'
  print '  time the assembly and factorization of a Wathen system'
  print '  using the WATHEN_CSC function.'
  print ''
  print '    NX  Elements   Nodes    Assembly      ',
  print 'Factor      Error'
  print ''

  nx = 1
  ny = 1

  for test in range ( 0, 7 ):
#
#  Compute the number of unknowns.
#
    n = wathen_order ( nx, ny )
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
    a, seed = wathen_csc ( nx, ny, seed )
    t1 = ( time.clock ( ) - t0 )
#
#  Compute the corresponding right hand side B.
#
    b = a.dot ( x1 )
#
#  Solve the system.
#
    t0 = time.clock ( )
    x2 = ssl.spsolve ( a, b )
    t2 = ( time.clock ( ) - t0 )
#
#  Compute the norm of the solution error.
#
    e = norm ( x1 - x2 )
#
#  Report.
#
    print '  %4d      %4d  %6d  %10.2e  %10.2e  %10.2e' % \
      ( nx, nx * ny, n, t1, t2, e )
#
#  Ready for next iteration.
#
    nx = nx * 2
    ny = ny * 2

  return

if ( __name__ == '__main__' ):
  wathen_test04 ( )

