#!/usr/bin/env python

def i4vec_concatenate ( n1, a1, n2, a2 ):

#*****************************************************************************80
#
## I4VEC_CONCATENATE concatenates two I4VEC's.
#
#  Discussion:
#
#    An I4VEC is a vector of I4 values.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N1, the number of entries in the first vector.
#
#    Input, integer A1(N1), the first vector.
#
#    Input, integer N2, the number of entries in the second vector.
#
#    Input, integer A2(N2), the second vector.
#
#    Output, integer A3(N1+N2), the concatenation of A1 and A2.
#
  import numpy as np

  a3 = np.concatenate ( ( a1, a2 ), axis = 0 )

  return a3

def i4vec_concatenate_test ( ):

#*****************************************************************************80
#
## I4VEC_CONCATENATE_TEST tests I4VEC_CONCATENATE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 October 2014
#
#  Author:
#
#    John Burkardt
#
  from i4vec_print import i4vec_print
  import numpy as np

  n1 = 5;
  n2 = 3;
  n3 = n1 + n2;

  a1 = np.array ( [ 91, 31, 71, 51, 31 ] )
  a2 = np.array ( [ 42, 22, 12 ] )

  print ''
  print 'I4VEC_CONCATENATE_TEST'
  print '  I4VEC_CONCATENATE concatenates two I4VECs'

  i4vec_print ( n1, a1, '  Array 1:' );
  i4vec_print ( n2, a2, '  Array 2:' );
  a3 = i4vec_concatenate ( n1, a1, n2, a2 );
  i4vec_print ( n3, a3, '  Array 3 = Array 1 + Array 2:' );
#
#  Terminate.
#
  print ''
  print 'I4VEC_CONCATENATE_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp

  timestamp ( )
  i4vec_concatenate_test ( )
  timestamp ( )
