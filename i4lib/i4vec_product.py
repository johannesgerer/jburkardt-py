#!/usr/bin/env python
#
def i4vec_product ( n, a ):

#*****************************************************************************80
#
## I4VEC_PRODUCT computes the product of the entries of an I4VEC.
#
#  Discussion:
#
#    An I4VEC is a vector of I4's.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of entries in the vector.
#
#    Input, integer A(N), the vector.
#
#    Output, integer VALUE, the product of the entries.
#
  value = 1
  for i in range ( 0, n ):
    value = value * a[i]

  return value

def i4vec_product_test ( ):

#*****************************************************************************80
#
## I4VEC_PRODUCT_TEST tests I4VEC_PRODUCT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 May 2015
#
#  Author:
#
#    John Burkardt
#
  from i4vec_print import i4vec_print
  from i4vec_uniform_ab import i4vec_uniform_ab

  print ''
  print 'I4VEC_PRODUCT_TEST'
  print '  I4VEC_PRODUCT computes the product of the entries in an I4VEC.'

  n = 10
  i4_lo = - 5
  i4_hi = + 5
  seed = 123456789

  a, seed = i4vec_uniform_ab ( n, i4_lo, i4_hi, seed )

  i4vec_print ( n, a, '  Input vector:' )

  value = i4vec_product ( n, a )
  print ''
  print '  Product of entries = %d' % ( value )
#
#  Terminate.
#
  print ''
  print 'I4VEC_PRODUCT_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4vec_product_test ( )
  timestamp ( )

