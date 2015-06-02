#! /usr/bin/env python
#
def harman ( ):

#*****************************************************************************80
#
## HARMAN returns the Harman matrix.
#
#  Formula:
#
#   1.00  0.85  0.81  0.86  0.47  0.40  0.30  0.38
#   0.85  1.00  0.88  0.83  0.38  0.33  0.28  0.41
#   0.81  0.88  1.00  0.80  0.38  0.32  0.24  0.34
#   0.86  0.83  0.80  1.00  0.44  0.33  0.33  0.36
#   0.47  0.38  0.38  0.44  1.00  0.76  0.73  0.63
#   0.40  0.33  0.32  0.33  0.76  1.00  0.58  0.58
#   0.30  0.28  0.24  0.33  0.73  0.58  1.00  0.54
#   0.38  0.41  0.34  0.36  0.63  0.58  0.54  1.00
#
#  Properties:
#
#    A is symmetric.
#
#    A is a correlation matrix for 8 physical variables measured
#    for 305 girls.
#
#    The rows and columns of the matrix correspond to the variables
#    1) height
#    2) arm span
#    3) length of forearm
#    4) length of lower leg
#    5) weight
#    6) bitrochanteric diameter
#    7) chest girth
#    8) chest width
#
#    The largest two eigenvalues are 
#
#      LAMBDA(1) = 4.67 
#
#    with eigenvector
#
#      V(1) = 0.40, 0.39, 0.38, 0.39, 0.35, 0.31, 0.29, 0.31
#
#    and 
#
#      LAMBDA(2)= 1.77
#
#    with eigevector
#
#      V(2) = 0.28 0.33 0.34 0.30 -0.39, -0.40 -0.44 -0.31
#
#    The best rank 2 approximation to the matrix, in the least squares
#    sense, is
#
#      [ V(1) V(2) ] * Diag ( LAMBDA(1), LAMBDA(2) ) * [ V(1) V(2) ]'
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    HH Harman,
#    Modern Factor Analysis,
#    The University of Chicago Press, 1960.
#
#    Lawrence Huber, Jacqueline Meulman, Willem Heiser,
#    Two Purposes for Matrix Factorization: A Historical Appraisal,
#    SIAM Review, Volume 41 : number 1, pages 68-82.
#
#  Parameters:
#
#    Output, real A(8,8), the matrix.
#
  import numpy as np

  a = np.array ( [ \
    [ 1.00, 0.85, 0.81, 0.86, 0.47, 0.40, 0.30, 0.38 ], \
    [ 0.85, 1.00, 0.88, 0.83, 0.38, 0.33, 0.28, 0.41 ], \
    [ 0.81, 0.88, 1.00, 0.80, 0.38, 0.32, 0.24, 0.34 ], \
    [ 0.86, 0.83, 0.80, 1.00, 0.44, 0.33, 0.33, 0.36 ], \
    [ 0.47, 0.38, 0.38, 0.44, 1.00, 0.76, 0.73, 0.63 ], \
    [ 0.40, 0.33, 0.32, 0.33, 0.76, 1.00, 0.58, 0.58 ], \
    [ 0.30, 0.28, 0.24, 0.33, 0.73, 0.58, 1.00, 0.54 ], \
    [ 0.38, 0.41, 0.34, 0.36, 0.63, 0.58, 0.54, 1.00 ] ])

  return a

def harman_condition ( ):

#*****************************************************************************80
#
## HARMAN_CONDITION returns the L1 condition of the HARMAN matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real VALUE, the L1 condition number.
#
  a_norm = 5.07;
  b_norm = 15.200976381839961;
  value = a_norm * b_norm;

  return value

def harman_condition_test ( ):

#*****************************************************************************80
#
## HARMAN_CONDITION_TEST tests HARMAN_CONDITION.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 February 2015
#
#  Author:
#
#    John Burkardt
#
  from harman import harman
  from r8mat_print import r8mat_print

  print ''
  print 'HARMAN_CONDITION_TEST'
  print '  HARMAN_CONDITION computes the condition of the HARMAN matrix.'
  print ''

  seed = 123456789

  n = 8
  a = harman ( )
  r8mat_print ( n, n, a, '  HARMAN matrix:' )

  value = harman_condition ( )
  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'HARMAN_CONDITION_TEST'
  print '  Normal end of execution.'

  return

def harman_determinant ( ):

#*****************************************************************************80
#
## HARMAN_DETERMINANT computes the determinant of the HARMAN matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real VALUE, the determinant.
#
  value = 9.547789295599994E-04

  return value

def harman_determinant_test ( ):

#*****************************************************************************80
#
## HARMAN_DETERMINANT_TEST tests HARMAN_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 February 2015
#
#  Author:
#
#    John Burkardt
#
  from harman import harman
  from r8mat_print import r8mat_print

  print ''
  print 'HARMAN_DETERMINANT_TEST'
  print '  HARMAN_DETERMINANT computes the HARMAN determinant.'

  seed = 123456789

  m = 8
  n = 8
  a = harman ( )
  r8mat_print ( n, n, a, '  HARMAN matrix:' )

  value = harman_determinant ( )
  print '  Value =  %g' % ( value )

  print ''
  print 'HARMAN_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def harman_inverse ( ):

#*****************************************************************************80
#
## HARMAN_INVERSE returns the inverse of the HARMAN matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real A(8,8), the matrix.
#
  import numpy as np
#
#  Note that the matrix entries are listed by row.
#
  a = np.array ( [ \
  [  5.505750442924552,  -2.024827472733320, \
    -0.525564377998213,  -2.414725599885703, \
    -0.742871704140835,  -0.432339085897328, \
     0.506363394364808,   0.231316810459756 ], \
  [ -2.024827472733320,   6.632253606390529, \
    -3.266421707396942,  -1.157009948040102, \
     0.941928425100928,   0.010152122779319, \
    -0.318255180872113,  -0.850127918526706 ], \
  [ -0.525564377998213,  -3.266421707396943, \
     4.945029645612116,  -0.799896971199349, \
    -0.384019974978888,  -0.082141525217929, \
     0.342191583208235,   0.250391407726364 ], \
  [ -2.414725599885702,  -1.157009948040101, \
    -0.799896971199349,   4.769523661962869, \
    -0.343306754780455,   0.462478615948815, \
    -0.415704081428472,   0.119432120786903 ], \
  [ -0.742871704140835,   0.941928425100928, \
    -0.384019974978887,  -0.343306754780455, \
     3.941357428629264,  -1.549806320843210, \
    -1.467270532044103,  -0.641583610147637 ], \
  [ -0.432339085897328,   0.010152122779319, \
    -0.082141525217929,   0.462478615948815, \
    -1.549806320843210,   2.524233450449795, \
    -0.122867685019045,  -0.399766570085388 ], \
  [  0.506363394364808,  -0.318255180872113, \
     0.342191583208235,  -0.415704081428472, \
    -1.467270532044103,  -0.122867685019045, \
     2.276170982094793,  -0.262113772509967 ], \
  [  0.231316810459756,  -0.850127918526706, \
     0.250391407726364,   0.119432120786903, \
    -0.641583610147637,  -0.399766570085388, \
    -0.262113772509967,   1.910127138708912 ] ] )

  return a

def harman_test ( ):

#*****************************************************************************80
#
## HARMAN_TEST tests HARMAN.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 February 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'HARMAN_TEST'
  print '  HARMAN computes the HARMAN matrix.'

  n = 8
  a = harman ( )
  r8mat_print ( n, n, a, '  HARMAN matrix:' )

  print ''
  print 'HARMAN_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  harman_test ( )
  timestamp ( )
