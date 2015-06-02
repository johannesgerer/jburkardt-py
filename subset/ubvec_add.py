#! /usr/bin/env python
#
def ubvec_add ( n, bvec1, bvec2 ):

#*****************************************************************************80
#
## UBVEC_ADD adds two unsigned binary vectors.
#
#  Discussion:
#
#    A UBVEC is an integer vector of binary digits, intended to
#    represent a nonnegative integer.  BVEC(1) is the units digit, BVEC(N)
#    is the coefficient of 2^(N-1).
#
#  Example:
#
#    N = 4
#
#      BVEC1       +   BVEC2       =   BVEC3
#
#    ( 1 0 0 0 )   + ( 1 1 0 0 )   = ( 0 0 1 0 )
#
#      1           +   3           =   4
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 May 2015
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
  import numpy as np

  base = 2
  overflow = 0

  bvec3 = np.zeros ( n, dtype = np.int32 )

  for i in range ( 0, n ):
    bvec3[i] = bvec1[i] + bvec2[i]

  for i in range ( 0, n ):
    while ( base <= bvec3[i] ):
      bvec3[i] = bvec3[i] - base
      if ( i < n - 1 ):
        bvec3[i+1] = bvec3[i+1] + 1
      else:
        overflow = 1

  return bvec3

def ubvec_add_test ( ):

#*****************************************************************************80
#
## UBVEC_ADD_TEST tests UBVEC_ADD;
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 May 2015
#
#  Author:
#
#    John Burkardt
#
  from i4_uniform_ab import i4_uniform_ab
  from ui4_to_ubvec import ui4_to_ubvec
  from ubvec_to_ui4 import ubvec_to_ui4

  n = 10
  seed = 123456789
  test_num = 10

  print ''
  print 'UBVEC_ADD_TEST'
  print '  UBVEC_ADD adds unsigned binary vectors representing'
  print '  unsigned integers;'
  print ''
  print '        I        J        K = I + J'
  print ''

  for test in range ( 0, test_num ):
    
    i, seed = i4_uniform_ab ( 0, 100, seed )
    j, seed = i4_uniform_ab ( 0, 100, seed )

    print ''

    print '  %8d  %8d' % ( i, j )

    k = i + j

    print '  Directly:           %8d' % ( k )

    bvec1 = ui4_to_ubvec ( i, n )
    bvec2 = ui4_to_ubvec ( j, n )

    bvec3 = ubvec_add ( n, bvec1, bvec2 )
    k = ubvec_to_ui4 ( n, bvec3 )

    print '  BVEC_ADD            %8d' % ( k )
#
#  Terminate.
#
  print ''
  print 'UBVEC_ADD_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  ubvec_add_test ( )
  timestamp ( )

