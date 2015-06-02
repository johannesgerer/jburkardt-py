#!/usr/bin/env python

def bvec_add ( n, bvec1, bvec2 ):

#*****************************************************************************80
#
## BVEC_ADD adds two binary vectors.
#
#  Discussion:
#
#    A BVEC is an integer vector of binary digits, intended to
#    represent an integer.  BVEC(1) is the units digit, BVEC(N-1)
#    is the coefficient of 2^(N-2), and BVEC(N) contains sign
#    information.  It is 0 if the number is positive, and 1 if
#    the number is negative.
#
#  Example:
#
#    N = 4
#
#    BVEC1    dec  BVEC2    dec  BVEC3    dec
#    -------  ---  -------  ---  -------  ---
#    1 0 0 0   1   1 1 0 0   3   0 0 1 0   4
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the length of the vectors.
#
#    Input, integer BVEC1(N), BVEC2(N), the vectors to be added.
#
#    Output, integer BVEC3(N), the sum of the two input vectors.
#
#    Output, logical OVERFLOW, is true if the sum overflows.
#
  import numpy as np
  from bvec_print import bvec_print

  base = 2
  overflow = False

  bvec3 = np.zeros ( n, dtype = np.int32 )

  for i in range ( 0, n ):
    bvec3[i] = bvec1[i] + bvec2[i]

  for i in range ( 0, n ):
    
    while ( base <= bvec3[i] ):
      bvec3[i] = bvec3[i] - base
      if ( i < n - 1 ):
        bvec3[i+1] = bvec3[i+1] + 1
      else:
        overflow = True

  return bvec3, overflow

def bvec_add_test ( ):

#*****************************************************************************80
#
## BVEC_ADD_TEST tests BVEC_ADD.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    24 December 2014
#
#  Author:
#
#    John Burkardt
#
  from bvec_to_i4 import bvec_to_i4
  from i4_to_bvec import i4_to_bvec
  from i4_uniform_ab import i4_uniform_ab

  n = 10
  seed = 123456789
  test_num = 10

  print ''
  print 'BVEC_ADD_TEST'
  print '  BVEC_ADD adds binary vectors representing integers;'
  print ''
  print '        I        J        K = I + J   Kb = Ib + Jb'
  print ''

  for test in range ( 0, test_num ):
    
    i, seed = i4_uniform_ab ( -100, 100, seed )
    j, seed = i4_uniform_ab ( -100, 100, seed )

    print '  %8d  %8d' % ( i, j ),

    k = i + j

    print '  %8d' % ( k ),

    bvec1 = i4_to_bvec ( i, n )

    bvec2 = i4_to_bvec ( j, n )

    bvec3, overflow = bvec_add ( n, bvec1, bvec2 )

    k = bvec_to_i4 ( n, bvec3 )

    print '  %8d' % ( k )

  print ''
  print 'BVEC_ADD_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  bvec_add_test ( )
  timestamp ( )
