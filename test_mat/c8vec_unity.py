#!/usr/bin/env python

def c8vec_unity ( n ):

#*****************************************************************************80
#
## C8VEC_UNITY returns the N roots of unity.
#
#  Discussion:
#
#    X(1:N) = exp ( 2 * PI * (0:N-1) / N )
#
#    X(1:N)^N = ( (1,0), (1,0), ..., (1,0) ).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of elements.
#
#    Output, complex A(N), the array.
#
  import numpy as np

  a = np.zeros ( n, 'complex' )

  for i in range ( 0, n ):
    t = 2.0 * np.pi * float ( i ) / float ( n )
    a[i] = np.cos ( t ) + 1j * np.sin ( t )

  return a

def c8vec_unity_test ( ):

#*****************************************************************************80
#
## C8VEC_UNITY_TEST tests C8VEC_UNITY.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    12 February 2015
#
#  Author:
#
#    John Burkardt
#
  from c8vec_print import c8vec_print

  print ''
  print 'C8VEC_UNITY_TEST'
  print '  C8VEC_UNITY returns the N roots of unity.'

  n = 12

  x = c8vec_unity ( n )

  c8vec_print ( n, x, '  The N roots of unity:' )

  print ''
  print 'C8VEC_UNITY_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  c8vec_unity_test ( )
  timestamp ( )

