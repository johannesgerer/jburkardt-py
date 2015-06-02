#!/usr/bin/env python

def perm_check0 ( n, p ):

#*****************************************************************************80
#
## PERM_CHECK0 checks a 0-based permutation.
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
#    25 October 2014
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
  from sys import exit

  for value in range ( 0, n ):

    ierror = 1

    for location in range ( 0, n ):
      if ( p[location] == value ):
        ierror = 0
        break

    if ( ierror != 0 ):
      print ''
      print 'PERM_CHECK0 - Fatal error!'
      print '  Permutation is missing the value %d.' % ( value )
      exit ( 'PERM_CHECK0 - Fatal error!' )

  return

