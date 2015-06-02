#!/usr/bin/env python

def bvec_complement2 ( n, bvec1 ) :

#*****************************************************************************80
#
## BVEC_COMPLEMENT2 computes the two's complement of a binary vector.
#
#  Discussion:
#
#    A BVEC is an integer vector of binary digits, intended to
#    represent an integer.  BVEC(1) is the units digit, BVEC(N-1)
#    is the coefficient of 2^(N-2), and BVEC(N) contains sign
#    information.  It is 0 if the number is positive, and 1 if
#    the number is negative.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 November 2006
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the length of the vectors.
#
#    Input, integer BVEC1(N), the vector to be complemented.
#
#    Output, integer BVEC2(N), the two's complemented vector.
#
  from bvec_add import bvec_add
  from bvec_print import bvec_print
  import numpy as np

  base = 2

  bvec3 = np.zeros ( n, dtype = np.int32 )
  for i in range ( 0, n ):
    bvec3[i] = ( base - 1 ) - bvec1[i]

  bvec4 = np.zeros ( n, dtype = np.int32 )
  bvec4[0] = 1

  bvec2, overflow = bvec_add ( n, bvec3, bvec4 )

  return bvec2

def bvec_complement2_test ( ):

#*****************************************************************************80
#
## BVEC_COMPLEMENT2_TEST tests BVEC_COMPLEMENT2.
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
  from bvec_print import bvec_print
  from bvec_to_i4 import bvec_to_i4
  from i4_to_bvec import i4_to_bvec
  from i4_uniform_ab import i4_uniform_ab

  n = 10

  seed = 123456789
  test_num = 5

  print ''
  print 'BVEC_COMPLEMENT2_TEST'
  print '  BVEC_COMPLEMENT2 returns the twos complement'
  print '  of a (signed) binary vector;'

  for test in range ( 0, test_num ):

    print ''

    i, seed = i4_uniform_ab ( -100, 100, seed );
    bvec1 = i4_to_bvec ( i, n )
    bvec_print ( n, bvec1, '' )

    bvec2 = bvec_complement2 ( n, bvec1 )
    bvec_print ( n, bvec2, '' )

    j = bvec_to_i4 ( n, bvec2 )
 
  print ''
  print 'BVEC_COMPLEMENT2_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  bvec_complement2_test ( )
  timestamp ( )
