#!/usr/bin/env python
#
def r8vec_copy ( n1, a1 ):

#*****************************************************************************80
#
## R8VEC_COPY copies an R8VEC.
#
#  Discussion:
#
#    An R8VEC is a vector of R8 values.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N1, the number of entries in the vector.
#
#    Input, real A1(N1), the vector.
#
#    Output, real A2(N1), a copy of A2.
#
  import numpy as np

  a2 = np.zeros ( n1, dtype = np.float64 )
  for i in range ( 0, n1 ):
    a2[i] = a1[i]

  return a2

def r8vec_copy_test ( ):

#*****************************************************************************80
#
## R8VEC_COPY_TEST tests R8VEC_COPY.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 October 2014
#
#  Author:
#
#    John Burkardt
#
  from r8vec_print import r8vec_print
  import numpy as np

  n1 = 5;

  a1 = np.array ( [ 91.1, 31.2, 71.3, 51.4, 31.5 ] )
 
  print ''
  print 'R8VEC_COPY_TEST'
  print '  R8VEC_COPY copies an R8VEC.'

  r8vec_print ( n1, a1, '  Array 1:' );
  a2 = r8vec_copy ( n1, a1 );
  r8vec_print ( n1, a2, '  Array 2:' );
#
#  Terminate.
#
  print ''
  print 'R8VEC_COPY_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp

  timestamp ( )
  r8vec_copy_test ( )
  timestamp ( )
