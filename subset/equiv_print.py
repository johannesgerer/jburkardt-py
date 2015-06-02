#! /usr/bin/env python
#
def equiv_print ( n, iarray, title ):

#*****************************************************************************80
#
## EQUIV_PRINT prints a partition of a set.
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
#    Input, integer N, number of elements in set to be partitioned.
#
#    Input, integer IARRAY(N), defines the partition or set of equivalence
#    classes.  Element I belongs to subset IARRAY(I).
#
#    Input, character ( len = * ) TITLE, a title to be printed first.
#    TITLE may be blank.
#
  import numpy as np

  if ( 0 < len ( title ) ):
    print ''
    print title

  print ''
  print '   Set  Size'

  s_min = np.min ( iarray )
  s_max = np.max ( iarray )

  karray = np.zeros ( n )

  for s in range ( s_min, s_max + 1 ):

    k = 0

    for j in range ( 0, n ):

      if ( iarray[j] == s ):
        karray[k] = j;
        k = k + 1

    if ( 0 < k ):
      print '  %4d  %4d :: ' % ( s, k ),
      for j in range ( 0, k ):
        print '%4d' % ( karray[j] ),
      print ''

  return

def equiv_print_test ( ):

#*****************************************************************************80
#
## EQUIV_PRINT_TEST tests EQUIV_PRINT.
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
  print 'EQUIV_PRINT_TEST'
  print '  EQUIV_PRINT prints a set partition.'
 
  seed = 123456789

  for i in range ( 0, 5 ):
 
    npart, a, seed = equiv_random ( n, seed )

    equiv_print ( n, a, '  The partition:' )
#
#  Terminate.
#
  print ''
  print 'EQUIV_PRINT_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  equiv_print_test ( )
  timestamp ( )

