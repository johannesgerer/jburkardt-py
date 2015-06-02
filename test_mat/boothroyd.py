#! /usr/bin/env python
#
def boothroyd ( n ):

#*****************************************************************************80
#
## BOOTHROYD returns the BOOTHROYD matrix.
#
#  Formula:
#
#    A(I,J) = C(N+I-1,I-1) * C(N-1,N-J) * N / ( I + J - 1 )
#
#  Example:
#
#    N = 5
#
#     5    10    10     5     1
#    15    40    45    24     5
#    35   105   126    70    15
#    70   224   280   160    35
#   126   420   540   315    70
#
#  Properties:
#
#    A is not symmetric.
#
#    A is positive definite.
#
#    det ( A ) = 1.
#
#    The inverse matrix has the same entries, but with alternating sign.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 September 2007
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
  from r8_choose import r8_choose

  a = np.zeros ( [ n, n ] )

  for j in range ( 0, n ):
    for i in range ( 0, n ):

      a[i,j] = r8_choose ( n + i, i ) * r8_choose ( n - 1, n - j - 1 ) * n \
        / ( i + j + 1 );

  return a

def boothroyd_condition ( n ):

#*****************************************************************************80
#
## BOOTHROYD_CONDITION computes the L1 condition of the BOOTHROYD matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Output, real VALUE, the L1 condition.
#
  from r8_choose import r8_choose

  a_norm = 0.0

  for j in range ( 0, n ):
    s = 0.0
    for i in range ( 0, n ):
      s = s + r8_choose ( n + i, i ) * r8_choose ( n - 1, n - j - 1 ) * n \
        / ( i + j + 1 );
    a_norm = max ( a_norm, s )

  b_norm = a_norm

  value = a_norm * b_norm
 
  return value

def boothroyd_determinant ( n ):

#*****************************************************************************80
#
## BOOTHROYD_DETERMINANT computes the determinant of the BOOTHROYD matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 December 2014
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
  value = 1.0
 
  return value

def boothroyd_determinant_test ( ):

#*****************************************************************************80
#
## BOOTHROYD_DETERMINANT_TEST tests BOOTHROYD_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 December 2014
#
#  Author:
#
#    John Burkardt
#
  from boothroyd import boothroyd
  from r8mat_print import r8mat_print

  print ''
  print 'BOOTHROYD_DETERMINANT_TEST'
  print '  BOOTHROYD_DETERMINANT computes the BOOTHROYD determinant.'

  m = 4
  n = 4
  a = boothroyd ( n )

  r8mat_print ( m, n, a, '  BOOTHROYD matrix:' )

  value = boothroyd_determinant ( n )

  print '  Value =  %g' % ( value )

  print ''
  print 'BOOTHROYD_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def boothroyd_inverse ( n ):

#*****************************************************************************80
#
## BOOTHROYD_INVERSE returns the inverse of the BOOTHROYD matrix.
#
#  Example:
#
#    N = 5
#
#      5   -10    10    -5     1
#    -15    40   -45    24    -5
#     35  -105   126   -70    15
#    -70   224  -280   160   -35
#    126  -420   540  -315    70
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 March 2015
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
  from r8_choose import r8_choose
  from r8_mop import r8_mop

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      a[i,j] = r8_mop ( i + j ) * r8_choose ( n + i, i ) \
        * r8_choose ( n-1, n-j-1 ) * float ( n  ) / float ( i + j + 1 )

  return a

def boothroyd_test ( ):

#*****************************************************************************80
#
## BOOTHROYD_TEST tests BOOTHROYD.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 December 2014
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'BOOTHROYD_TEST'
  print '  BOOTHROYD computes the BOOTHROYD matrix.'

  m = 5
  n = m
  a = boothroyd ( n )
  r8mat_print ( m, n, a, '  BOOTHROYD matrix:' )

  print ''
  print 'BOOTHROYD_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  boothroyd_test ( )
  timestamp ( )
