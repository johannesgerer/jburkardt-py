#! /usr/bin/env python
#
def daub2 ( n ):

#*****************************************************************************80
#
## DAUB2 returns the DAUB2 matrix.
#
#  Discussion:
#
#    The DAUB2 matrix is the Daubechies wavelet transformation matrix
#    with 2 coefficients.
#
#    The DAUB2 matrix is also known as the Haar matrix.
#
#  Properties:
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#    N must be at least 2 and a multiple of 2.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np
  from math import sqrt
  from sys import exit

  if ( n < 2 or ( n % 2 ) != 0 ):
    print ''
    print 'DAUB2 - Fatal error!'
    print '  N must be at least 2 and a multiple of 2.'
    exit ( 'DAUB2 - Fatal error!' )

  a = np.zeros ( [ n, n ] )

  c0 = sqrt ( 2.0 ) / 2.0
  c1 = sqrt ( 2.0 ) / 2.0

  for i in range ( 0, n - 1, 2 ):
 
    a[i,i]     =   c0
    a[i,i+1]   =   c1

    a[i+1,i]   =   c1
    a[i+1,i+1] = - c0

  return a

def daub2_condition ( n ):

#*****************************************************************************80
#
## DAUB2_CONDITION returns the L1 condition of the DAUB2 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the dimension of the matrix.
#
#    Output, real VALUE, the condition.
#
  import numpy as np

  c0 = np.sqrt ( 2.0 ) / 2.0
  c1 = np.sqrt ( 2.0 ) / 2.0

  a_norm = np.abs ( c0 ) + np.abs ( c1 )
  b_norm = a_norm
  value = a_norm * b_norm

  return value

def daub2_condition_test ( ):

#*****************************************************************************80
#
## DAUB2_CONDITION_TEST tests DAUB2_CONDITION.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 January 2015
#
#  Author:
#
#    John Burkardt
#
  from daub2 import daub2
  from r8mat_print import r8mat_print

  print ''
  print 'DAUB2_CONDITION_TEST'
  print '  DAUB2_CONDITION computes the condition of the DAUB2 matrix.'

  m = 4
  n = m

  a = daub2 ( n )
  r8mat_print ( m, n, a, '  DAUB2 matrix:' )

  value = daub2_condition ( n )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'DAUB2_CONDITION_TEST'
  print '  Normal end of execution.'

  return

def daub2_determinant ( n ):

#*****************************************************************************80
#
## DAUB2_DETERMINANT returns the determinant of the DAUB2 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the dimension of the matrix.
#
#    Output, real DETERM, the determinant.
#
  determ = 1.0

  return determ

def daub2_determinant_test ( ):

#*****************************************************************************80
#
## DAUB2_DETERMINANT_TEST tests DAUB2_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 January 2015
#
#  Author:
#
#    John Burkardt
#
  from daub2 import daub2
  from r8mat_print import r8mat_print

  print ''
  print 'DAUB2_DETERMINANT_TEST'
  print '  DAUB2_DETERMINANT computes the determinant of the DAUB2 matrix.'

  m = 4
  n = m

  a = daub2 ( n )
  r8mat_print ( m, n, a, '  DAUB2 matrix:' )

  value = daub2_determinant ( n )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'DAUB2_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def daub2_inverse ( n ):

#*****************************************************************************80
#
## DAUB2_INVERSE returns the inverse of the DAUB2 matrix.
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
#    Input, integer N, the order of the matrix.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  a = daub2 ( n )
  a = np.transpose ( a )

  return a

def daub2_test ( ):

#*****************************************************************************80
#
## DAUB2_TEST tests DAUB2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 January 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'DAUB2_TEST'
  print '  DAUB2 computes the DAUB2 matrix.'

  m = 4
  n = m

  a = daub2 ( n )
  r8mat_print ( m, n, a, '  DAUB2 matrix:' )

  print ''
  print 'DAUB2_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  daub2_test ( )
  timestamp ( )
