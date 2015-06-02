#!/usr/bin/env python

def i4vec_add ( n, a, b ):

#*****************************************************************************80
#
## I4VEC_ADD computes C = A + B for I4VEC's.
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
#    29 September 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of elements of the vector.
#
#    Input, integer A(N), the first vector.
#
#    Input, integer B(N), the second vector.
#
#    Output, integer C(N), the sum of the vectors.
#
  import numpy

  c = numpy.zeros ( n );

  for i in range ( 0, n ):
    c[i] = a[i] + b[i]

  return c

def i4vec_add_test ( ):

#*****************************************************************************80
#
## I4VEC_ADD_TEST tests I4VEC_ADD.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 September 2014
#
#  Author:
#
#    John Burkardt
#
  from i4vec_uniform_ab import i4vec_uniform_ab

  print ''
  print 'I4VEC_ADD_TEST'
  print '  I4VEC_ADD adds two I4VECs.'

  n = 10
  seed = 123456789

  lo = - n
  hi = n

  a, seed = i4vec_uniform_ab ( n, lo, hi, seed )
  b, seed = i4vec_uniform_ab ( n, lo, hi, seed )
  c = i4vec_add ( n, a, b )

  print ''
  print '     I     A     B     C'
  print ''
  for i in range ( 0, n ):
    print '%6d%6d%6d%6d' % ( i, a[i], b[i], c[i] )
#
#  Terminate.
#
  print ''
  print 'I4VEC_ADD_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4vec_add_test ( )
  timestamp ( )
