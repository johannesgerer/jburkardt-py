#!/usr/bin/env python

def bvec_next_grlex ( n, bvec ):

#*****************************************************************************80
#
## BVEC_NEXT generates the next binary vector in GRLEX order.
#
#  Discussion:
#
#    N = 3
#
#    Input      Output
#    -----      ------
#    0 0 0  =>  0 0 1
#    0 0 1  =>  0 1 0
#    0 1 0  =>  1 0 0
#    1 0 0  =>  0 1 1
#    0 1 1  =>  1 0 1
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
#    13 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, int N, the dimension of the vectors.
#
#    Input/output, int BVEC[N], on output, the successor to the
#    input vector.  
#

#
#  Initialize locations of 0 and 1.
#
  if ( bvec[0] == 0 ):
    z = 0
    o = -1
  else:
    z = -1
    o = 0
#
#  Moving from right to left, search for a "1", preceded by a "0".
#
  for i in range ( n - 1, 0, -1 ):
    if ( bvec[i] == 1 ):
      o = i
      if ( bvec[i-1] == 0 ):
        z = i - 1
        break
#
#  BVEC = 0
#
  if ( o == -1 ):
    bvec[n-1] = 1
#
#  01 never occurs.  So for sure, B(1) = 1.
#
  elif ( z == -1 ):

    s = 0
    for i in range ( 0, n ):
      s = s + bvec[i]

    if ( s == n ):

      for i in range ( 0, n ):
        bvec[i] = 0

    else:

      for i in range ( 0, n - s - 1 ):
        bvec[i] = 0

      for i in range ( n - s - 1, n ):
        bvec[i] = 1
      type ( n - s - 1 )
#
#  Found the rightmost "01" string.
#  Replace it by "10".
#  Shift following 1's to the right.
#
  else:

    bvec[z] = 1
    bvec[o] = 0

    s = 0
    for i in range ( o + 1, n ):
      s = s + bvec[i]

    for i in range ( o + 1, n - s ):
      bvec[i] = 0
    
    for i in range ( n - s, n ):
      bvec[i] = 1

  return bvec

def bvec_next_grlex_test ( ):

#*****************************************************************************80
#
## BVEC_NEXT_GRLEX_TEST tests BVEC_NEXT_GRLEX.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    13 March 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 4

  print ''
  print 'BVEC_NEXT_GRLEX_TEST'
  print '  BVEC_NEXT_GRLEX computes binary vectors in GRLEX order.'
  print ''

  b = np.zeros ( n, dtype = np.int32 )

  for i in range ( 0, 17 ):
    print '  %2d:  ' % ( i ),
    for j in range ( 0, n ):
      print '%1d' % ( b[j] ),
    print ''
    b = bvec_next_grlex ( n, b )

  print ''
  print 'BVEC_NEXT_GRLEX_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  bvec_next_grlex_test ( )
  timestamp ( )
