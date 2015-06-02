#!/usr/bin/env python

def i4vec_copy ( n1, a1 ):

#*****************************************************************************80
#
## I4VEC_COPY copies an I4VEC.
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
#    Input, integer A1(N1), the vector.
#
#    Output, integer A2(N1), a copy of A2.
#
  import numpy as np

  a2 = np.zeros ( n1, dtype = np.int32 )
  for i in range ( 0, n1 ):
    a2[i] = a1[i]

  return a2

def i4vec_copy_test ( ):

#*****************************************************************************80
#
## I4VEC_COPY_TEST tests I4VEC_COPY.
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
  from i4vec_print import i4vec_print
  import numpy as np

  n1 = 5;

  a1 = np.array ( [ 91, 31, 71, 51, 31 ], dtype = np.int32 )
 
  print ''
  print 'I4VEC_COPY_TEST'
  print '  I4VEC_COPY copies an I4VEC.'

  i4vec_print ( n1, a1, '  Array 1:' );
  a2 = i4vec_copy ( n1, a1 );
  i4vec_print ( n1, a2, '  Array 2:' );
#
#  Terminate.
#
  print ''
  print 'I4VEC_COPY_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp

  timestamp ( )
  i4vec_copy_test ( )
  timestamp ( )
