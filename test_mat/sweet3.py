#! /usr/bin/env python
#
def sweet3 ( ):

#*****************************************************************************80
#
## SWEET3 returns the SWEET3 matrix.
#
#  Example:
#
#      8    4    1    6    2    3
#      4    8    4    1    6    2
#    -34    4    8    4    1    6
#      5  -34    4    8    4    1
#      3    5  -34    4    8    4
#      1    3    5  -34    4    8
#
#  Properties:
#
#    A is Toeplitz: constant along diagonals.
#
#    A is generally not symmetric: A' /= A.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Per Hansen, Tony Chan,
#    FORTRAN Subroutines for General Toeplitz Systems,
#    ACM Transactions on Mathematical Software,
#    Volume 18, Number 3, September 1992, pages 256-273.
#
#    Douglas Sweet,
#    The use of pivoting to improve the numerical performance of
#    Toeplitz solvers,
#    In "Advanced Algorithms and Architectures for Signal Processing",
#    Edited by J M Speiser,
#    Proceedings SPIE 696, 1986, pages 8-18.
#
#  Parameters:
#
#    Output, real A(6,6), the matrix.
#
  import numpy as np

  n = 6

  v = np.array ( [ 1.0, 3.0, 5.0, -34.0, 4.0, 8.0, 4.0, \
    1.0, 6.0, 2.0, 3.0 ] )

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      a[i,j] = v[j-i+5];

  return a

def sweet3_condition ( ):

#*****************************************************************************80
#
## SWEET3_CONDITION returns the L1 condition of the SWEET3 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real VALUE, the condition.
#
  a_norm = 58.0
  b_norm = 0.427215561206108
  value = a_norm * b_norm

  return value

def sweet3_condition_test ( ):

#*****************************************************************************80
#
## SWEET3_CONDITION_TEST tests SWEET3_CONDITION.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 February 2015
#
#  Author:
#
#    John Burkardt
#
  from sweet3 import sweet3
  from r8mat_print import r8mat_print

  print ''
  print 'SWEET3_CONDITION_TEST'
  print '  SWEET3_CONDITION computes the condition of the SWEET3 matrix.'
  print ''

  n = 6
  a = sweet3 ( )
  r8mat_print ( n, n, a, '  SWEET3 matrix:' )

  value = sweet3_condition ( )
  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'SWEET3_CONDITION_TEST'
  print '  Normal end of execution.'

  return

def sweet3_determinant ( ):

#*****************************************************************************80
#
## SWEET3_DETERMINANT returns the determinant of the SWEET3 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real VALUE, the determinant.
#
  value = - 5.4056067E+07

  return value

def sweet3_determinant_test ( ):

#*****************************************************************************80
#
## SWEET3_DETERMINANT_TEST tests SWEET3_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 February 2015
#
#  Author:
#
#    John Burkardt
#
  from sweet3 import sweet3
  from r8mat_print import r8mat_print

  print ''
  print 'SWEET3_DETERMINANT_TEST'
  print '  SWEET3_DETERMINANT computes the determinant of the SWEET3 matrix.'
  print ''

  n = 6
  a = sweet3 ( )
  r8mat_print ( n, n, a, '  SWEET3 matrix:' )

  value = sweet3_determinant ( )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'SWEET3_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def sweet3_inverse ( ):

#*****************************************************************************80
#
## SWEET3_INVERSE returns the inverse of the SWEET3 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real A(6,6), the matrix.
#
  import numpy as np

  a = np.array ( [ \
  [  0.041073816931594,  -0.007888550234334,  -0.020859268211281, \
     0.000304369165444,  -0.003979664299291,   0.004165693371662 ], \
  [  0.008091247186000,   0.017910145035154,   0.000156985153951, \
    -0.024742218112169,  -0.001114102511380,  -0.003979664299291 ], \
  [  0.006256245020564,   0.027534337635034,   0.003121055773444, \
     0.003970174152700,  -0.024742218112169,   0.000304369165444 ], \
  [  0.038877153234252,  -0.002789344626201,   0.008678729808441, \
     0.003121055773444,   0.000156985153951,  -0.020859268211281 ], \
  [ -0.119845197024785,   0.170102571465290,  -0.002789344626201, \
     0.027534337635034,   0.017910145035154,  -0.007888550234334 ], \
  [  0.213071901808913,  -0.119845197024785,   0.038877153234252, \
     0.006256245020564,   0.008091247186000,   0.041073816931594 ] ] )

  return a

def sweet3_test ( ):

#*****************************************************************************80
#
## SWEET3_TEST tests SWEET3.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 February 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'SWEET3_TEST'
  print '  SWEET3 computes the SWEET3 matrix.'

  n = 6
  a = sweet3 ( )
  r8mat_print ( n, n, a, '  SWEET3 matrix:' )

  print ''
  print 'SWEET3_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  sweet3_test ( )
  timestamp ( )
