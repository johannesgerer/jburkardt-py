#! /usr/bin/env python
#
def conex4 ( ):

#*****************************************************************************80
#
## CONEX4 returns the CONEX4 matrix.
#
#  Discussion:
#
#    7  10   8   7
#    6   8  10   9
#    5   7   9  10
#    5   7   6   5
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 January 2015
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

  a = np.array ( [
    [ 7.0, 10.0,  8.0,  7.0 ], \
    [ 6.0,  8.0, 10.0,  9.0 ], \
    [ 5.0,  7.0,  9.0, 10.0 ], \
    [ 5.0,  7.0,  6.0,  5.0 ] \
  ] )

  return a

def conex4_condition ( ):

#*****************************************************************************80
#
## CONEX4_CONDITION returns the L1 condition of the CONEX4 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Output, real COND, the L1 condition number.
#
  a_norm = 33.0
  b_norm = 136.0
  cond = a_norm * b_norm

  return cond

def conex4_condition_test ( ):

#*****************************************************************************80
#
## CONEX4_CONDITION_TEST tests CONEX4_CONDITION.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 January 2015
#
#  Author:
#
#    John Burkardt
#
  from conex4 import conex4
  from r8mat_print import r8mat_print

  print ''
  print 'CONEX4_CONDITION_TEST'
  print '  CONEX4_CONDITION computes the condition of the CONEX4 matrix.'
  print ''

  n = 4
  a = conex4 ( )
  r8mat_print ( n, n, a, '  CONEX4 matrix:' )

  value = conex4_condition ( )

  print ''
  print '  Value =  #g' # ( value )

  print ''
  print 'CONEX4_CONDITION_TEST'
  print '  Normal end of execution.'

  return

def conex4_determinant ( ):

#*****************************************************************************80
#
## CONEX4_DETERMINANT returns the determinant of the CONEX4 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real DETERM, the determinant.
#
  determ = -1.0

  return determ

def conex4_determinant_test ( ):

#*****************************************************************************80
#
## CONEX4_DETERMINANT_TEST tests CONEX4_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 January 2015
#
#  Author:
#
#    John Burkardt
#
  from conex4 import conex4
  from r8mat_print import r8mat_print

  print ''
  print 'CONEX4_DETERMINANT_TEST'
  print '  CONEX4_DETERMINANT computes the determinant of the CONEX4 matrix.'
  print ''

  m = 4
  n = m

  a = conex4 ( )
  r8mat_print ( m, n, a, '  CONEX4 matrix:' )

  value = conex4_determinant ( )

  print ''
  print '  Value =  #g' # ( value )

  print ''
  print 'CONEX4_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def conex4_inverse ( ):

#*****************************************************************************80
#
## CONEX4_INVERSE returns the inverse of the CONEX4 matrix.
#
#  Discussion:
#
#   -41  -17   10   68
#    25   10   -6  -41
#    10    5   -3  -17
#    -6   -3    2   10
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
   [ -41.0,  -17.0,   10.0,   68.0 ], \
   [  25.0,   10.0,   -6.0,  -41.0 ], \
   [  10.0,    5.0,   -3.0,  -17.0 ], \
   [  -6.0,   -3.0,    2.0,   10.0 ] ] )

  return a

def conex4_test ( ):

#*****************************************************************************80
#
## CONEX4_TEST tests CONEX4.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 January 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'CONEX4_TEST'
  print '  CONEX4 computes the CONEX4 matrix.'

  m = 4
  n = m

  a = conex4 ( )
  r8mat_print ( m, n, a, '  CONEX4 matrix:' )

  print ''
  print 'CONEX4_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  conex4_test ( )
  timestamp ( )
