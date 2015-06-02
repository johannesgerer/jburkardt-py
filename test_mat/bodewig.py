#! /usr/bin/env python
#
def bodewig ( ):

#*****************************************************************************80
#
## BODEWIG returns the BODEWIG matrix.
#
#  Example:
#
#    2   1   3   4
#    1  -3   1   5
#    3   1   6  -2
#    4   5  -2  -1
#
#  Properties:
#
#    A is symmetric: A' = A.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Joan Westlake,
#    Test Matrix A27,
#    A Handbook of Numerical Matrix Inversion and Solution of Linear Equations,
#    John Wiley, 1968.
#
#  Parameters:
#
#    Output, real A(4,4), the matrix.
#
  import numpy as np

  a = np.array ( [ \
    [ 2.0,  1.0,  3.0,  4.0 ], \
    [ 1.0, -3.0,  1.0,  5.0 ], \
    [ 3.0,  1.0,  6.0, -2.0 ], \
    [ 4.0,  5.0, -2.0, -1.0 ] ] )
 
  return a

def bodewig_condition ( ):

#*****************************************************************************80
#
## BODEWIG_CONDITION returns the L1 condition of the BODEWIG matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real VALUE, the L1 condition number.
#
  value = 10.436619718309862

  return value

def bodewig_condition_test ( ):

#*****************************************************************************80
#
## BODEWIG_CONDITION_TEST tests BODEWIG_CONDITION.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 December 2014
#
#  Author:
#
#    John Burkardt
#
  from bodewig import bodewig
  from r8mat_print import r8mat_print

  print ''
  print 'BODEWIG_CONDITION_TEST'
  print '  BODEWIG_CONDITION computes the condition of the BODEWIG matrix.'
  print ''

  seed = 123456789

  n = 4
  a = bodewig ( )
  r8mat_print ( n, n, a, '  BODEWIG matrix:' )

  value = bodewig_condition ( )
  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'BODEWIG_CONDITION_TEST'
  print '  Normal end of execution.'

  return

def bodewig_determinant ( ):

#*****************************************************************************80
#
## BODEWIG_DETERMINANT computes the determinant of the BODEWIG matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real DETERM, the determinant.
#
  determ = 568.0

  return determ

def bodewig_determinant_test ( ):

#*****************************************************************************80
#
## BODEWIG_DETERMINANT_TEST tests BODEWIG_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 December 2014
#
#  Author:
#
#    John Burkardt
#
  from bodewig import bodewig
  from r8mat_print import r8mat_print

  print ''
  print 'BODEWIG_DETERMINANT_TEST'
  print '  BODEWIG_DETERMINANT computes the BODEWIG determinant.'

  m = 4
  n = 4
  a = bodewig ( )
  r8mat_print ( n, n, a, '  BODEWIG matrix:' )

  value = bodewig_determinant ( )
  print '  Value =  %g' % ( value )

  print ''
  print 'BODEWIG_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def bodewig_eigen_right ( ):

#*****************************************************************************80
#
## BODEWIG_EIGEN_RIGHT returns the right eigenvectors of the BODEWIG matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real A(4,4), the matrix.
#
  import numpy as np
#
#  Note that the matrix entries are listed by row.
#
  a = np.array ( [ \
  [  0.263462395147524,   0.560144509774526,   \
     0.378702689441644,  -0.688047939843040 ], \
  [  0.659040718046439,   0.211632763260098,   \
     0.362419048574935,   0.624122855455373 ], \
  [ -0.199633529128396,   0.776708263894565,   \
    -0.537935161097828,   0.259800864702728 ], \
  [ -0.675573350827063,   0.195381612446620,   \
     0.660198809976478,   0.263750269148100 ] ] )

  return a

def bodewig_eigenvalues ( ):

#*****************************************************************************80
#
## BODEWIG_EIGENVALUES returns the eigenvalues of the BODEWIG matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real LAMBDA(4,1), the eigenvalues.
#
  import numpy as np

  lam = np.array ( [ \
    [ -8.028578352396531 ], \
    [  7.932904717870018 ], \
    [  5.668864372830019 ], \
    [ -1.573190738303506 ] ] )

  return lam

def bodewig_inverse ( ):

#*****************************************************************************80
#
## BODEWIG_INVERSE returns the inverse of the BODEWIG matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real A(4,4), the matrix.
#
  import numpy as np
#
#  Note that the matrix entries are listed by row.
#
  a  = np.array ( [ \
    [ -139.0,  165.0,  79.0,  111.0 ], \
    [  165.0, -155.0, -57.0,   -1.0 ], \
    [   79.0,  -57.0,  45.0,  -59.0 ], \
    [  111.0,   -1.0, -59.0,  -11.0 ] ] )

  for j in range ( 0, 4 ):
    for i in range ( 0, 4 ):
      a[i,j] = a[i,j] / 568.0

  return a

def bodewig_plu ( ):

#*****************************************************************************80
#
## BODEWIG_PLU returns the PLU factors of the BODEWIG matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real P(4,4), L(4,4), U(4,4), the factors.
#
  import numpy as np
#
#  Note that the matrix entries are listed by row.
#
  p = np.array ( [ \
    [ 0.0, 0.0, 0.0, 1.0 ], \
    [ 0.0, 1.0, 0.0, 0.0 ], \
    [ 0.0, 0.0, 1.0, 0.0 ], \
    [ 1.0, 0.0, 0.0, 0.0 ] ] )

  l = np.array ( [ \
    [ 1.00, 0.00,              0.00,              0.00 ], \
    [ 0.25, 1.00,              0.00,              0.00 ], \
    [ 0.75, 0.647058823529412, 1.00,              0.00 ], \
    [ 0.50, 0.352941176470588, 0.531531531531532, 1.00 ] ] )

  u = np.array ( [ \
    [ 4.00,  5.00, -2.00,              -1.00 ], \
    [ 0.00, -4.25,  1.50,               5.25 ], \
    [ 0.00,  0.00,  6.529411764705882, -4.647058823529412 ], \
    [ 0.00,  0.00,  0.00,               5.117117117117118 ] ] )

  return p, l, u

def bodewig_rhs ( ):

#*****************************************************************************80
#
## BODEWIG_RHS returns the BODEWIG right hand side.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real B(4,1), the right hand side vector.
#
  import numpy as np

  b = np.array ( [ [ 29.0 ], [ 18.0 ], [ 15.0 ], [ 4.0 ] ] )

  return b

def bodewig_solution ( ):

#*****************************************************************************80
#
## BODEWIG_SOLUTION returns the BODEWIG_SOLUTION
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real X(4,1), the solution.
#
  import numpy as np

  x = np.array ( [ [ 1.0], [ 2.0 ], [ 3.0 ], [ 4.0 ] ] )

  return x

def bodewig_test ( ):

#*****************************************************************************80
#
## BODEWIG_TEST tests BODEWIG.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 December 2014
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'BODEWIG_TEST'
  print '  BODEWIG computes the BODEWIG matrix.'

  n = 4
  a = bodewig ( )
  r8mat_print ( n, n, a, '  BODEWIG matrix:' )

  print ''
  print 'BODEWIG_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  bodewig_test ( )
  timestamp ( )
