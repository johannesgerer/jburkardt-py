#!/usr/bin/env python

def bvec_mul ( n, bvec1, bvec2 ):

#*****************************************************************************80
#
## BVEC_MUL computes the product of two binary vectors.
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
#    05 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the length of the vectors.
#
#    Input, integer BVEC1(N), BVEC2(N), the vectors to be multiplied.
#
#    Output, integer BVEC3(N), the product of the two input vectors.
#
  import numpy as np
  from bvec_complement2 import bvec_complement2

  base = 2
#
#  Copy the input.
#
  bveca = np.zeros ( n, dtype = np.int32 )
  bvecb = np.zeros ( n, dtype = np.int32 )
  for i in range ( 0, n ):
    bveca[i] = bvec1[i]
    bvecb[i] = bvec2[i]
#
#  Record the sign of the product.
#  Make the factors positive.
#
  product_sign = 1

  if ( bveca[n-1] != 0 ):
    product_sign = - product_sign
    bveca = bvec_complement2 ( n, bveca )

  if ( bvecb[n-1] != 0 ):
    product_sign = - product_sign
    bvecb = bvec_complement2 ( n, bvecb )

  bvecc = np.zeros ( n, dtype = np.int32 )
#
#  Multiply.
#
  for i in range ( 0, n - 1 ):
    for j in range ( i, n - 1 ):
      bvecc[j] = bvecc[j] + bveca[i] * bvecb[j-i]
#
#  Take care of carries.
#
  for i in range ( 0, n - 1 ):

    carry = ( bvecc[i] // base )
    bvecc[i] = bvecc[i] - carry * base
#
#  Unlike the case of BVEC_ADD, we do NOT allow carries into
#  the N-th position when multiplying.
#
    if ( i < n - 2 ):
      bvecc[i+1] = bvecc[i+1] + carry
#
#  Take care of the sign of the product.
#
  if ( product_sign < 0 ):
    bvecc = bvec_complement2 ( n, bvecc )

  return bvecc

def bvec_mul_test ( ):

#*****************************************************************************80
#
## BVEC_MUL_TEST tests BVEC_MUL.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    05 January 2015
#
#  Author:
#
#    John Burkardt
#
  from bvec_to_i4 import bvec_to_i4
  from i4_to_bvec import i4_to_bvec
  from i4_uniform_ab import i4_uniform_ab

  n = 15
  seed = 123456789
  test_num = 10

  print ''
  print 'BVEC_MUL_TEST'
  print '  BVEC_MUL multiplies binary vectors representing integers;'
  print ''
  print '        I        J        I * J   BVEC_MUL'
  print ''

  for test in range ( 0, test_num ):
    
    i, seed = i4_uniform_ab ( -100, 100, seed )
    j, seed = i4_uniform_ab ( -100, 100, seed )

    print '  %8d  %8d' % ( i, j ),

    k = i * j

    print '  %8d' % ( k ),

    bvec1 = i4_to_bvec ( i, n )
    bvec2 = i4_to_bvec ( j, n )
    bvec3 = bvec_mul ( n, bvec1, bvec2 )
    l = bvec_to_i4 ( n, bvec3 )

    print '  %8d' % ( l )

  print ''
  print 'BVEC_MUL_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  bvec_mul_test ( )
  timestamp ( )
