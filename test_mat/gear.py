#! /usr/bin/env python
#
def gear ( ii, jj, n ):

#*****************************************************************************80
#
## GEAR returns the Gear matrix.
#
#  Formula:
#
#    if ( I = 1 and J = abs ( II ) )
#      A(I,J) = SIGN(II)
#    elseif ( I = N and J = N + 1 - abs ( JJ ) )
#      A(I,J) = SIGN(JJ)
#    elseif ( I = J+1 or I = J-1 )
#      A(I,J) = 1
#    else
#      A(I,J) = 0
#
#    Common values for II and JJ are II = N, JJ=-N.
#
#  Example:
#
#    II = 5, JJ = - 5, N = 5
#
#    0 1 0 0 1
#    1 0 1 0 0
#    0 1 0 1 0
#    0 0 1 0 1
#   -1 0 0 1 0
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is integral: int ( A ) = A.
#
#    A is border-banded.
#
#    All eigenvalues are of the form 2*COS(ALPHA), and the eigenvectors
#    are of the form
#
#      ( sin(W+ALPHA), sin(W+2*ALPHA), ..., sin(W+N*ALPHA) ).
#
#    The values of ALPHA and W are given in the reference.  A can have
#    double and triple eigenvalues.
#
#    If II = N and JJ=-N, A is singular.
#
#    A is defective.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Charles Gear,
#    A simple set of test matrices for eigenvalue programs,
#    Mathematics of Computation,
#    Volume 23, 1969, pages 119-125.
#
#  Parameters:
#
#    Input, integer II, JJ, define the two special entries.
#
#    Input, integer N, the order of A.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np
  from i4_sign import i4_sign

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( i == 0 and j + 1 == abs ( ii ) ):
        a[i,j] = i4_sign ( ii )
      elif ( i == n - 1 and j == n - abs ( jj ) ):
        a[i,j] = i4_sign ( jj )
      elif ( j == i - 1 or j == i + 1 ):
        a[i,j] = 1.0

  return a

def gear_determinant ( ii, jj, n ):

#*****************************************************************************80
#
## GEAR_DETERMINANT computes the determinant of the GEAR matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer II, JJ, define the two special entries.
#
#    Input, integer N, the order of the matrix.
#
#    Output, real VALUE, the determinant.
#
  import numpy as np

  lam = gear_eigenvalues ( ii, jj, n )

  value = np.prod ( lam )
 
  return value

def gear_determinant_test ( ):

#*****************************************************************************80
#
## GEAR_DETERMINANT_TEST tests GEAR_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 February 2015
#
#  Author:
#
#    John Burkardt
#
  from i4_uniform_ab import i4_uniform_ab
  from r8mat_print import r8mat_print

  print ''
  print 'GEAR_DETERMINANT_TEST'
  print '  GEAR_DETERMINANT computes the GEAR determinant.'

  m = 4
  n = 4
  i4_lo = -n
  i4_hi = +n
  seed = 123456789
  ii, seed = i4_uniform_ab ( i4_lo, i4_hi, seed )
  jj, seed = i4_uniform_ab ( i4_lo, i4_hi, seed )
  a = gear ( ii, jj, n )

  r8mat_print ( m, n, a, '  GEAR matrix:' )

  value = gear_determinant ( ii, jj, n )

  print '  Value =  %g' % ( value )

  print ''
  print 'GEAR_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def gear_eigenvalues ( ii, jj, n ):

#*****************************************************************************80
#
## GEAR_EIGENVALUES returns the eigenvalues of the GEAR matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer II, JJ, define the two special entries.
#
#    Input, integer N, the order of the matrix.
#
#    Output, real LAM(N), the eigenvalues.
#
  import numpy as np
  from i4_is_even import i4_is_even
  from i4_is_odd import i4_is_odd
  from i4_sign import i4_sign

  lam = np.zeros ( n )

  r8_pi = 3.141592653589793
#
#  Separate the sign and value.
#
  alpha = np.zeros ( n )

  j = abs ( ii )
  js = i4_sign ( ii )

  k = abs ( jj )
  ks = i4_sign ( jj )

  if ( 0 < js and 0 < ks ):

    w = 0

    phi = n - ( ( j + k ) // 2 )
    for p in range ( 1, phi + 1 ):
      alpha[w] = 2 * p * r8_pi / float ( 2 * n + 2 - j - k )
      w = w + 1
 
    phi = ( ( j - 1 ) // 2 )
    for p in range ( 1, phi + 1 ):
      alpha[w] = 2 * p * r8_pi / float ( j )
      w = w + 1
 
    phi = ( ( k - 1 ) // 2 )
    for p in range ( 1, phi + 1 ):
      alpha[w] = 2 * p * r8_pi / float ( k )
      w = w + 1

    alpha[w] = 0.0
    w = w + 1

    if ( i4_is_even ( j ) & i4_is_even ( k ) ):
      alpha[w] = r8_pi
      w = w + 1

  elif ( 0 < js and ks < 0 ):

    w = 0

    phi = n + 1 - ( ( j + k + 1 ) // 2 )
    for p in range ( 1, phi + 1 ):
      alpha[w] = ( 2 * p - 1 ) * r8_pi / float ( 2 * n + 2 - j - k )
      w = w + 1

    phi = ( ( j - 1 ) // 2 )
    for p in range ( 1, phi + 1 ):
      alpha[w] = 2 * p * r8_pi / float ( j )
      w = w + 1

    phi = ( k // 2 )
    for p in range ( 1, phi + 1 ):
      alpha[w] = ( 2 * p - 1 ) * r8_pi / float ( k )
      w = w + 1

    if ( i4_is_even ( j ) and i4_is_odd ( k ) ):
      alpha[w] = r8_pi
      w = w + 1

  elif ( js < 0 and 0 < ks ):

    w = 0

    phi = n + 1 - ( ( j + k + 1 ) // 2 )
    for p in range ( 1, phi + 1 ):
      alpha[w] = ( 2 * p - 1 ) * r8_pi / float ( 2 * n + 2 - j - k )
      w = w + 1

    phi = ( j // 2 )
    for p in range ( 1, phi + 1 ):
      alpha[w] = ( 2 * p - 1 ) * r8_pi / float ( j )
      w = w + 1

    phi = ( ( k - 1 ) // 2 )
    for p in range ( 1, phi + 1 ):
      alpha[w] = 2 * p * r8_pi / float ( k )
      w = w + 1

    if ( i4_is_odd ( j ) and i4_is_even ( k ) ):
      alpha[w] = r8_pi
      w = w + 1

  elif ( js < 0 and ks < 0 ):

    w = 0

    phi = n - ( ( j + k ) // 2 )
    for p in range ( 1, phi + 1 ):
      alpha[w] = 2 * p * r8_pi / float ( 2 * n + 2 - j - k )
      w = w + 1

    phi = ( j // 2 )
    for p in range ( 1, phi + 1 ):
      alpha[w] = ( 2 * p - 1 ) * r8_pi / float ( j )
      w = w + 1

    phi = ( k // 2 )
    for p in range ( 1, phi + 1 ):
      alpha[w] = ( 2 * p - 1 ) * r8_pi / float ( k )
      w = w + 1

    if ( i4_is_odd ( j ) and i4_is_odd ( k ) ):
      alpha[w] = r8_pi
      w = w + 1

  for w in range ( 0, n ):
    lam[w] = 2.0 * np.cos ( alpha[w] )
 
  return lam

def gear_eigenvalues_test ( ):

#*****************************************************************************80
#
## GEAR_EIGENVALUES_TEST tests GEAR_EIGENVALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 February 2015
#
#  Author:
#
#    John Burkardt
#
  from gear import gear
  from i4_uniform_ab import i4_uniform_ab
  from r8mat_print import r8mat_print
  from r8vec_print import r8vec_print

  print ''
  print 'GEAR_EIGENVALUES_TEST'
  print '  GEAR_EIGENVALUES computes the GEAR eigenvalues.'

  m = 5
  n = 5
  i4_lo = -n
  i4_hi = +n
  seed = 123456789
  ii, seed = i4_uniform_ab ( i4_lo, i4_hi, seed )
  jj, seed = i4_uniform_ab ( i4_lo, i4_hi, seed )
  a = gear ( ii, jj, n )

  r8mat_print ( m, n, a, '  GEAR matrix:' )

  lam = gear_eigenvalues ( ii, jj, n )

  r8vec_print ( n, lam, '  GEAR eigenvalues:' )

  print ''
  print 'GEAR_EIGENVALUES_TEST'
  print '  Normal end of execution.'

  return

def gear_test ( ):

#*****************************************************************************80
#
## GEAR_TEST tests GEAR.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 February 2015
#
#  Author:
#
#    John Burkardt
#
  from i4_uniform_ab import i4_uniform_ab
  from r8mat_print import r8mat_print

  print ''
  print 'GEAR_TEST'
  print '  GEAR computes the GEAR matrix.'

  m = 4
  n = 4
  i4_lo = -n
  i4_hi = +n
  seed = 123456789
  ii, seed = i4_uniform_ab ( i4_lo, i4_hi, seed )
  jj, seed = i4_uniform_ab ( i4_lo, i4_hi, seed )
  a = gear ( ii, jj, n )

  r8mat_print ( m, n, a, '  GEAR matrix:' )

  print ''
  print 'GEAR_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  gear_test ( )
  timestamp ( )
