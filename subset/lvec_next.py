#!/usr/bin/env python

def lvec_next ( n, lvec ):

#*****************************************************************************80
#
## LVEC_NEXT generates the next logical vector.
#
#  Discussion:
#
#    In the following discussion, we will let '0' stand for FALSE and
#    '1' for TRUE.
#
#    The vectors have the order
#
#      (0,0,...,0),
#      (0,0,...,1),
#      ...
#      (1,1,...,1)
#
#    and the "next" vector after (1,1,...,1) is (0,0,...,0).  That is,
#    we allow wrap around.
#
#  Example:
#
#    N = 3
#
#    Input      Output
#    -----      ------
#    0 0 0  =>  0 0 1
#    0 0 1  =>  0 1 0
#    0 1 0  =>  0 1 1
#    0 1 1  =>  1 0 0
#    1 0 0  =>  1 0 1
#    1 0 1  =>  1 1 0
#    1 1 0  =>  1 1 1
#    1 1 1  =>  0 0 0
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the dimension of the vectors.
#
#    Input, logical LVEC(N), the vector whose successor is desired.
#
#    Output, logical LVEC(N), the successor to the input vector.
#
  for i in range ( n - 1, -1, -1 ):

    if ( not lvec[i] ):
      lvec[i] = True
      break

    lvec[i] = False

  return lvec

def lvec_next_test ( ):

#*****************************************************************************80
#
## LVEC_NEXT_TEST tests LVEC_NEXT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ''
  print 'LVEC_NEXT_TEST'
  print '  LVEC_NEXT generates logical vectors of dimension N one at a time.'

  for n in range ( 2, 4 ):

    print ''
    print '  Vector size N = %d' % ( n )
    print ''

    k = 0

    lvec = np.zeros ( n, dtype = np.bool )

    for i in range ( 0, n ):
      lvec[i] = False

    while ( True ):

      print '  %2d:  ' % ( k ),
      for i in range ( 0, n ):
        print '  %s' % ( lvec[i] ),
      print ''

      lvec = lvec_next ( n, lvec )

      if ( not any ( lvec ) ):
        break

      k = k + 1
#
#  Terminate.
#
  print ''
  print 'LVEC_NEXT_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  lvec_next_test ( )
  timestamp ( )
