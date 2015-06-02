#! /usr/bin/env python
#
def pord_check ( n, a ):

#*****************************************************************************80
#
## PORD_CHECK checks a matrix representing a partial ordering.
#
#  Discussion:
#
#    The array A is supposed to represent a partial ordering of
#    the elements of a set of N objects.
#
#    For distinct indices I and J, the value of A(I,J) is:
#
#      1, if I << J
#      0, otherwise ( I and J may be unrelated, or perhaps J << I).
#
#    Diagonal elements of A are ignored.
#
#    This routine checks that the values of A do represent
#    a partial ordering.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    30 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of elements in the set.
#
#    Input, integer A(N,N), the partial ordering.
#    1 if I is less than J in the partial ordering, 
#    0 otherwise.
#
#    Output, integer IERROR, error flag.
#    0, no errors detected.  A is a partial ordering.
#    1, N <= 0.
#    2, 0 < A(I,J) and 0 < A(J,I) for some I and J.
#
  ierror = 0

  if ( n <= 0 ):
    ierror = 1
    return ierror

  for i in range ( 0, n ): 
    for j in range ( i + 1, n ):

      if ( 0 < a[i,j] ):
        if ( 0 < a[j,i] ):
          ierror = 2
          return ierror

  return ierror

def pord_check_test ( ):

#*****************************************************************************80
#
## PORD_CHECK_TEST tests PORD_CHECK.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from i4mat_print import i4mat_print

  n = 10

  a = np.array ( [ \
    [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0 ], \
    [ 0, 1, 0, 1, 0, 1, 0, 1, 0, 0 ], \
    [ 1, 0, 1, 1, 0, 0, 0, 0, 0, 0 ], \
    [ 0, 0, 0, 1, 0, 0, 0, 0, 0, 0 ], \
    [ 1, 1, 1, 1, 1, 1, 1, 1, 0, 1 ], \
    [ 0, 0, 0, 1, 0, 1, 0, 1, 0, 0 ], \
    [ 1, 0, 1, 1, 0, 1, 1, 1, 0, 1 ], \
    [ 0, 0, 0, 1, 0, 0, 0, 1, 0, 0 ], \
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ], \
    [ 1, 0, 1, 1, 0, 0, 0, 1, 0, 1 ] ] )

  print ''
  print 'PORD_CHECK_TEST'
  print '  PORD_CHECK checks a partial ordering.'

  i4mat_print ( n, n, a, '  The partial ordering matrix:' )
 
  ierror = pord_check ( n, a )
 
  print ''
  print '  CHECK FLAG = %d' % ( ierror )
  print '  0 means no error.'
  print '  1 means illegal value of N.'
  print '  2 means some A(I,J) and A(J,I) are both nonzero.'
#
#  Terminate.
#
  print ''
  print 'PORD_CHECK_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  pord_check_test ( )
  timestamp ( )

