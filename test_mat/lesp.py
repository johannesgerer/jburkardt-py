#! /usr/bin/env python
#
def lesp ( m, n ):

#*****************************************************************************80
#
## LESP returns the LESP matrix.
#
#  Formula:
#
#    if ( I - J == 1 )
#      A(I,J) = 1 / I
#    else if ( I - J == 0 )
#      A(I,J) = - ( 2*I+3 )
#    else if ( I - J == 1 )
#      A(I,J) = J
#    else
#      A(I,J) = 0.0
#
#  Example:
#
#    M = 5, N = 5
#
#     -5    2    .    .     .
#     1/2  -7    3    .     .
#      .   1/3  -9    4     .
#      .    .   1/4 -11     5
#      .    .    .   1/5  -13
#
#
#  Properties:
#
#    The matrix is tridiagonal.
#
#    Because A is tridiagonal, it has property A (bipartite).
#
#    A is generally not symmetric: A' /= A.
#
#    The eigenvalues are real, and smoothly distributed in [-2*N-3.5, -4.5].
#
#    The eigenvalues are sensitive.
#
#    The matrix is similar to the symmetric tridiagonal matrix with
#    the same diagonal entries and with off-diagonal entries 1,
#    via a similarity transformation using the diagonal matrix
#    D = diagonal ( 1!, 2!, ..., N! ).
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Wim Lenferink, MN Spijker,
#    On the use of stability regions in the numerical analysis of initial
#    value problems,
#    Mathematics of Computation,
#    Volume 57, 1991, pages 221-237.
#
#    Lloyd Trefethen,
#    Pseudospectra of matrices,
#    in Numerical Analysis 1991,
#    Proceedings of the 14th Dundee Conference,
#    D F Griffiths and G A Watson, editors,
#    Pitman Research Notes in Mathematics, volume 260,
#    Longman Scientific and Technical, Essex, UK, 1992, pages 234-266.
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns of A.
#
#    Output, real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( m, n ) )

  for i in range ( 0, m ):
    for j in range ( 0, n ):

      if ( i - j == 1 ):
        a[i,j] = 1.0 / float ( i + 1 )
      elif ( i - j == 0 ):
        a[i,j] = - float ( 2 * i + 5 )
      elif ( i - j == -1 ):
        a[i,j] = float ( j + 1 )

  return a

def lesp_determinant ( n ):

#*****************************************************************************80
#
## LESP_DETERMINANT returns the determinant of the LESP matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 February 2015
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
  determ_nm1 = - float ( 2 * n + 3 )
  value = determ_nm1

  if ( 1 < n ):
 
    determ_nm2 = determ_nm1
    determ_nm1 = float ( ( 2 * n + 1 ) * ( 2 * n + 3 ) - 1 )
    value = determ_nm1

    if ( 2 < n ):
 
      for i in range ( n - 2, 0, -1 ):

        determ = - float ( 2 * i + 3 ) * determ_nm1 - determ_nm2
  
        determ_nm2 = determ_nm1
        determ_nm1 = determ

      value = determ

  return value

def lesp_determinant_test ( ):

#*****************************************************************************80
#
## LESP_DETERMINANT_TEST tests LESP_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 February 2015
#
#  Author:
#
#    John Burkardt
#
  from lesp import lesp
  from r8mat_print import r8mat_print
 
  print ''
  print 'LESP_DETERMINANT_TEST'
  print '  LESP_DETERMINANT computes the determinant of the LESP matrix.'
  print ''

  m = 5
  n = m

  a = lesp ( m, n )
  r8mat_print ( m, n, a, '  LESP matrix:' )

  value = lesp_determinant ( n )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'LESP_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def lesp_inverse ( n ):

#*****************************************************************************80
#
## LESP_INVERSE returns the inverse of the LESP matrix.
#
#  Discussion:
#
#    This computation is an application of the TRIV_INVERSE function.
#
#  Example:
#
#    N = 5
#   -0.2060   -0.0598   -0.0201   -0.0074   -0.0028
#   -0.0150   -0.1495   -0.0504   -0.0184   -0.0071
#   -0.0006   -0.0056   -0.1141   -0.0418   -0.0161
#   -0.0000   -0.0001   -0.0026   -0.0925   -0.0356
#   -0.0000   -0.0000   -0.0000   -0.0014   -0.0775
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    CM daFonseca, J Petronilho,
#    Explicit Inverses of Some Tridiagonal Matrices,
#    Linear Algebra and Its Applications,
#    Volume 325, 2001, pages 7-21.
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Output, real A(N,N), the inverse of the matrix.
#
  import numpy as np
  from triv import triv_inverse

  x = np.zeros ( n - 1 )
  for i in range ( 0, n - 1 ):
    x[i] = 1.0 / float ( i + 2 )
 
  y = np.zeros ( n )
  for i in range ( 0, n ):
    y[i] = float ( - 2 * i - 5 )

  z = np.zeros ( n - 1 )
  for i in range ( 0, n - 1 ):
    z[i] = float ( i + 2 )

  a = triv_inverse ( n, x, y, z )

  return a

def lesp_test ( ):

#*****************************************************************************80
#
## LESP_TEST tests LESP.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 January 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'LESP_TEST'
  print '  LESP computes the LESP matrix.'

  m = 5
  n = m

  a = lesp ( m, n )
  r8mat_print ( m, n, a, '  LESP matrix:' )

  print ''
  print 'LESP_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  lesp_test ( )
  timestamp ( )
