#!/usr/bin/env python

def perm0_check ( n, p ):

#*****************************************************************************80
#
## PERM0_CHECK checks a permutation of (0,...,N-1).
#
#  Discussion:
#
#    The routine verifies that each of the integers from 0 to
#    to N-1 occurs among the N entries of the permutation.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    24 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of entries.
#
#    Input, integer P(N), the array to check.
#
#    Output, logical CHECK:
#    True if P is a legal permutation of (0,...,N-1).
#    False if P is not a legal permutation of (0,...,N-1).
#
  check = True

  for value in range ( 0, n ):

    check = False

    for location in range ( 0, n ):
      if ( p[location] == value ):
        check = True
        break

    if ( not check ):
      print ''
      print 'PERM0_CHECK - Warning!'
      print '  Permutation is missing the value %d.' % ( value )
      break

  return check

def perm0_check_test ( ):

#*****************************************************************************80
#
## PERM0_CHECK_TEST tests PERM0_CHECK.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from i4vec_transpose_print import i4vec_transpose_print

  n = 5
  p1 = np.array ( [ 5, 2, 3, 4, 1 ] )
  p2 = np.array ( [ 4, 1, 3, 0, 2 ] )
  p3 = np.array ( [ 0, 2, 1, 3, 2 ] )

  print ''
  print 'PERM0_CHECK_TEST'
  print '  PERM0_CHECK checks a permutation of 0,...,N-1.'

  i4vec_transpose_print ( n, p1, '  Permutation 1:' )
  check = perm0_check ( n, p1 )

  i4vec_transpose_print ( n, p2, '  Permutation 2:' )
  check = perm0_check ( n, p2 )

  i4vec_transpose_print ( n, p3, '  Permutation 3:' )
  check = perm0_check ( n, p3 )
#
#  Terminate.
#
  print ''
  print 'PERM0_CHECK_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  perm0_check_test ( )
  timestamp ( )

