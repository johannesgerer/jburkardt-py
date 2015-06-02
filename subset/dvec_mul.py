#! /usr/bin/env python
#
def dvec_mul ( n, dvec1, dvec2 ):

#*****************************************************************************80
#
## DVEC_MUL computes the product of two decimal vectors.
#
#  Discussion:
#
#    A DVEC is an integer vector of decimal digits, intended to
#    represent an integer.  DVEC(1) is the units digit, DVEC(N-1)
#    is the coefficient of 10^(N-2), and DVEC(N) contains sign
#    information.  It is 0 if the number is positive, and 1 if
#    the number is negative.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the length of the vectors.
#
#    Input, integer DVEC1(N), DVEC2(N), the vectors to be multiplied.
#
#    Output, integer DVEC3(N), the product of the two input vectors.
#
  import numpy as np
  from dvec_complementx import dvec_complementx

  base = 10
#
#  Record the sign of the product.
#  Make the factors positive.
#
  product_sign = 1

  if ( dvec1[n-1] != 0 ):
    product_sign = - product_sign
    dvec1 = dvec_complementx ( n, dvec1 )

  if ( dvec2[n-1] != 0 ):
    product_sign = - product_sign
    dvec2 = dvec_complementx ( n, dvec2 )

  dvec3 = np.zeros ( n )
#
#  Multiply.
#
  for i in range ( 0, n - 1 ):
    for j in range ( 0, n - 1 - i ):
      dvec3[i+j] = dvec3[i+j] + dvec1[i] * dvec2[j]
#
#  Take care of carries.
#
  for i in range ( 0, n - 1 ):

    carry = ( dvec3[i] // base )
    dvec3[i] = dvec3[i] - carry * base
#
#  Unlike the case of DVEC_ADD, we do NOT allow carries into
#  the N-th position when multiplying.
#
    if ( i < n - 2 ):
      dvec3[i+1] = dvec3[i+1] + carry
#
#  Take care of the sign of the product.
#
  if ( product_sign < 0 ):
    dvec3 = dvec_complementx ( n, dvec3 )

  return dvec3

def dvec_mul_test ( ):

#*****************************************************************************80
#
## DVEC_MUL_TEST tests DVEC_MUL;
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 May 2015
#
#  Author:
#
#    John Burkardt
#
  from dvec_to_i4 import dvec_to_i4
  from i4_to_dvec import i4_to_dvec
  from i4_uniform_ab import i4_uniform_ab

  n = 10
  seed = 123456789
  test_num = 10
  test2_num = 2

  print ''
  print 'DVEC_MUL_TEST'
  print '  DVEC_MUL multiplies decimal vectors'
  print '  representing integers;'

  for test2 in range ( 0, test2_num ):

    if ( test2 == 0 ):

      n2 = n

    elif ( test2 == 1 ):

      n2 = 6

      print ''
      print '  NOW REPEAT THE TEST...'
      print ''
      print '  but use too few digits to represent big products.'
      print '  This corresponds to an "overflow".'
      print '  The result here should get the final decimal'
      print '  digits correctly, though.'

    print ''
    print '        I        J        K = I * J'

    for test in range ( 0, test_num ):
    
      i, seed = i4_uniform_ab ( -1000, 1000, seed )
      j, seed = i4_uniform_ab ( -1000, 1000, seed )

      print ''

      print '  %8d  %8d' % ( i, j )

      k = i * j

      print '  Directly:           %8d' % ( k )

      dvec1 = i4_to_dvec ( i, n2 )
      dvec2 = i4_to_dvec ( j, n2 )
      dvec3 = dvec_mul ( n2, dvec1, dvec2 )
      k = dvec_to_i4 ( n2, dvec3 )

      print '  DVEC_MUL            %8d\n' % ( k )
#
#  Terminate.
#
  print ''
  print 'DVEC_MUL_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  dvec_mul_test ( )
  timestamp ( )

