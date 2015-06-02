#! /usr/bin/env python
#
def equiv_print2 ( n, s, title ):

#*****************************************************************************80
#
## EQUIV_PRINT2 prints a partition of a set.
#
#  Discussion:
#
#    The partition is printed using the parenthesis format.
#
#    For example, here are the partitions of a set of 4 elements:
#
#      (1,2,3,4)
#      (1,2,3)(4)
#      (1,2,4)(3)
#      (1,2)(3,4)
#      (1,2)(3)(4)
#      (1,3,4)(2)
#      (1,3)(2,4)
#      (1,3)(2)(4)
#      (1,4)(2,3)
#      (1)(2,3,4)
#      (1)(2,3)(4)
#      (1,4)(2)(3)
#      (1)(2,4)(3)
#      (1)(2)(3,4)
#      (1)(2)(3)(4)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of elements in the set.
#
#    Input, integer S(N), defines the partition.  
#    Element I belongs to subset S(I).
#
#    Input, string TITLE, a title to be printed first.
#
  import numpy as np

  if ( 0 < len ( title ) ):
    print ''
    print title

  print ''
  s_min = np.min ( s )
  s_max = np.max ( s )

  for j in range ( s_min, s_max + 1 ):

    print '(',
    size = 0
    for i in range ( 0, n ):
      if ( s[i] == j ):
        if ( 0 < size ):
          print ',',
        print '%d' % ( i ),
        size = size + 1
    print ')'

  return

def equiv_print2_test ( ):

#*****************************************************************************80
#
## EQUIV_PRINT2_TEST tests EQUIV_PRINT2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 May 2015
#
#  Author:
#
#    John Burkardt
#
  from equiv_random import equiv_random

  n = 4

  print ''
  print 'EQUIV_PRINT2_TEST'
  print '  EQUIV_PRINT2 prints a set partition.'
 
  seed = 123456789

  for i in range ( 0, 5 ):
 
    npart, a, seed = equiv_random ( n, seed )

    equiv_print2 ( n, a, '  The partition:' )
#
#  Terminate.
#
  print ''
  print 'EQUIV_PRINT2_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  equiv_print2_test ( )
  timestamp ( )

