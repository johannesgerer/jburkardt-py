#! /usr/bin/env python
#
def fourier_cosine ( n ):

#*****************************************************************************80
#
## FOURIER_COSINE returns the discrete Fourier Cosine Transform matrix.
#
#  Example:
#
#    N = 5
#
#    0.447214      0.447214      0.447214      0.447214      0.447214
#    0.601501      0.371748      0.000000     -0.371748     -0.601501
#    0.511667     -0.195440     -0.632456     -0.195439      0.511667
#    0.371748     -0.601501      0.000000      0.601501     -0.371748
#    0.195439     -0.511667      0.632456     -0.511668      0.195439
#
#  Properties:
#
#    A * A' = I.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 October 2007
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

  for j in range ( 0, n ):
    a[0,j] = 1.0 / np.sqrt ( float ( n ) )

  for i in range ( 1, n ) :
    for j in range ( 0, n ):
      
      angle = float ( i ) * float ( 2 * j + 1 ) * np.pi / float ( 2 * n )
      a[i,j] = np.sqrt ( 2.0 ) * np.cos ( angle ) / np.sqrt ( float ( n ) )

  return a

def fourier_cosine_determinant ( n ):

#*****************************************************************************80
#
## FOURIER_COSINE_DETERMINANT returns the determinant of the FOURIER_COSINE matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Output, real DETERM, the determinant.
#
  if ( ( n % 2 ) == 1 ):
    value = + 1.0
  else:
    value = -1.0

  return value

def fourier_cosine_determinant_test ( ):

#*****************************************************************************80
#
## FOURIER_COSINE_DETERMINANT_TEST tests FOURIER_COSINE_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 February 2015
#
#  Author:
#
#    John Burkardt
#
  from fourier_cosine import fourier_cosine
  from r8mat_print import r8mat_print

  print ''
  print 'FOURIER_COSINE_DETERMINANT_TEST'
  print '  FOURIER_COSINE_DETERMINANT computes the determinant of the FOURIER_COSINE matrix.'
  print ''

  m = 5
  n = m

  a = fourier_cosine ( n )
  r8mat_print ( m, n, a, '  FOURIER_COSINE matrix:' )

  value = fourier_cosine_determinant ( n )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'FOURIER_COSINE_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def fourier_cosine_inverse ( n ):

#*****************************************************************************80
#
## FOURIER_COSINE_INVERSE returns the inverse of the FOURIER_COSINE matrix.
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

  a = fourier_cosine ( n )

  a = np.transpose ( a )

  return a

def fourier_cosine_test ( ):

#*****************************************************************************80
#
## FOURIER_COSINE_TEST tests FOURIER_COSINE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 February 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'FOURIER_COSINE_TEST'
  print '  FOURIER_COSINE computes the FOURIER_COSINE matrix.'

  m = 5
  n = m

  a = fourier_cosine ( n )
  r8mat_print ( m, n, a, '  FOURIER_COSINE matrix:' )

  print ''
  print 'FOURIER_COSINE_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  fourier_cosine_test ( )
  timestamp ( )
