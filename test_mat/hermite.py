#! /usr/bin/env python
#
def hermite ( n ):

#*****************************************************************************80
#
## HERMITE returns the HERMITE matrix.
#
#  Example:
#
#    N = 11
#
#        1     .      .      .       .     .      .     .      .   .    .
#        .     2      .      .       .     .      .     .      .   .    .
#       -2     .      4      .       .     .      .     .      .   .    .
#        .   -12      .      8       .     .      .     .      .   .    .
#       12     .    -48      .      16     .      .     .      .   .    .
#        .   120      .   -160       .    32      .     .      .   .    .
#     -120     .    720      .    -480     .     64     .      .   .    .
#        . -1680      .   3360       . -1344      .   128      .   .    .
#     1680     . -13440      .   13440     .  -3584     .    256   .    .
#        . 30240      . -80640       . 48384      . -9216      . 512    .
#   -30240     . 302400      . -403200     . 161280     . -23040   . 1024
#
#  Properties:
#
#    A is generally not symmetric: A' ~= A.
#
#    A is lower triangular.
#
#    det ( A ) = 2^((N*(N-1))/2)
#
#    LAMBDA(I) = 2^(I-1).
#
#    A is integral: int ( A ) = A.
#
#    A is reducible.
#
#    Successive diagonals are zero, positive, zero, negative.
#
#    A is generally not normal: A' * A ~= A * A'.
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of A.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np
  
  a = np.zeros ( ( n, n ) )

  a[0,0] = 1.0

  if ( 1 < n ):

    a[1,1] = 2.0

    for i in range ( 2, n ):
      for j in range ( 0, n ):
        if ( j == 0 ):
          a[i,j] =                  - 2.0 * ( i - 1 ) * a[i-2,j]
        else:
          a[i,j] = 2.0 * a[i-1,j-1] - 2.0 * ( i - 1 ) * a[i-2,j]

  return a

def hermite_determinant ( n ):

#*****************************************************************************80
#
## HERMITE_DETERMINANT computes the determinant of the HERMITE matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Output, real VALUE, the determinant.
#
  power = ( n * ( n - 1 ) ) // 2
  value = 2 ** power

  return value

def hermite_determinant_test ( ):

#*****************************************************************************80
#
## HERMITE_DETERMINANT_TEST tests HERMITE_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 February 2015
#
#  Author:
#
#    John Burkardt
#
  from hermite import hermite
  from r8mat_print import r8mat_print

  print ''
  print 'HERMITE_DETERMINANT_TEST'
  print '  HERMITE_DETERMINANT computes the HERMITE determinant.'

  m = 5
  n = m
 
  a = hermite ( m, n )

  r8mat_print ( m, n, a, '  HERMITE matrix:' )

  value = hermite_determinant ( n )

  print '  Value =  %g' % ( value )

  print ''
  print 'HERMITE_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def hermite_inverse ( n ):

#*****************************************************************************80
#
## HERMITE_INVERSE returns the inverse of the HERMITE matrix.
#
#  Example:
#
#    N = 11
#
#        1     .     .     .     .    .    .  .  . . .
#        .     1     .     .     .    .    .  .  . . .  /    2
#        2     .     1     .     .    .    .  .  . . .  /    4
#        .     6     .     1     .    .    .  .  . . .  /    8
#       12     .    12     .     1    .    .  .  . . .  /   16
#        .    60     .    20     .    1    .  .  . . .  /   32
#      120     .   180     .    30    .    1  .  . . .  /   64
#        .   840     .   420     .   42    .  1  . . .  /  128
#     1680     .  3360     .   840    .   56  .  1 . .  /  256
#        . 15120     . 10080     . 1512    . 72  . 1 .  /  512
#    30240     . 75600     . 25200    . 2520  . 90 . 1  / 1024
#
#  Properties:
#
#    A is generally not symmetric: A' ~= A.
#
#    A is nonnegative.
#
#    A is lower triangular.
#
#    det ( A ) = 1 / 2^((N*(N-1))/2)
#
#    LAMBDA(I) = 1 / 2^(I-1)
#
#    A is reducible.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of A.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  a[0,0] = 1.0

  if ( 1 < n ):

    a[1,1] = 0.5

    if ( 2 < n ):

      for i in range ( 2, n ):
        for j in range ( 0, n ):
          if ( j == 0 ):
            a[i,j] = ( float ( i - 1 ) * a[i-2,j]              ) / 2.0
          else:
            a[i,j] = ( float ( i - 1 ) * a[i-2,j] + a[i-1,j-1] ) / 2.0

  return a

def hermite_test ( ):

#*****************************************************************************80
#
## HERMITE_TEST tests HERMITE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 February 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'HERMITE_TEST'
  print '  HERMITE computes the HERMITE matrix.'

  m = 5
  n = m

  a = hermite ( n )
 
  r8mat_print ( m, n, a, '  HERMITE matrix:' )

  print ''
  print 'HERMITE_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  hermite_test ( )
  timestamp ( )
