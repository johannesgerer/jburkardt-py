#!/usr/bin/env python

def i4vec_decrement ( n, v ):

#*****************************************************************************80
#
## I4VEC_DECREMENT decrements an I4VEC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the size of the I4VEC.
#
#    Input/output, integer V[N], the vector to be decremented.
#
  for i in range ( 0, n ):
    v[i] = v[i] - 1

  return v

def i4vec_decrement_test ( ):

#*****************************************************************************80
#
## I4VEC_DECREMENT_TEST tests I4VEC_DECREMENT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 January 2015
#
#  Author:
#
#    John Burkardt
#
  from i4vec_print import i4vec_print
  from i4vec_uniform_ab import i4vec_uniform_ab

  n = 4

  print ''
  print 'I4VEC_DECREMENT_TEST'
  print '  I4VEC_DECREMENT decrements an I4VEC.'

  v_lo = -5
  v_hi = 10
  seed = 123456789
  v, seed = i4vec_uniform_ab ( n, v_lo, v_hi, seed )
  i4vec_print ( n, v, '  The I4VEC:' )
  v = i4vec_decrement ( n, v )
  i4vec_print ( n, v, '  The I4VEC after decrementing:' )
#
#  Terminate.
#
  print ''
  print 'I4VEC_DECREMENT_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4vec_decrement_test ( )
  timestamp ( )
