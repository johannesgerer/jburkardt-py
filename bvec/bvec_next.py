#!/usr/bin/env python

def bvec_next ( n, bvec ):

#*****************************************************************************80
#
## BVEC_NEXT generates the next binary vector.
#
#  Discussion:
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
#    03 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the dimension of the vectors.
#
#    Input, integer BVEC(N), the vector whose successor is desired.
#
#    Output, integer BVEC(N), the successor to the input vector.
#
  for i in range ( n - 1, -1, -1 ):

    if ( bvec[i] == 0 ):
      bvec[i] = 1
      return bvec

    bvec[i] = 0

  return bvec

def bvec_next_test ( ):

#*****************************************************************************80
#
## BVEC_NEXT_TEST tests BVEC_NEXT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    03 January 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from bvec_print import bvec_print

  n = 4

  print ''
  print 'BVEC_NEXT_TEST'
  print '  BVEC_NEXT computes the "next" BVEC.'
  print ''

  b = np.zeros ( n, dtype = np.int32 )

  for i in range ( 0, 17 ):
    bvec_print ( n, b, '' )
    b = bvec_next ( n, b )

  print ''
  print 'BVEC_NEXT_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  bvec_next_test ( )
  timestamp ( )
