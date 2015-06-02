#!/usr/bin/env python

def r8vec_concatenate ( n1, a1, n2, a2 ):

#*****************************************************************************80
#
## R8VEC_CONCATENATE concatenates two R8VEC's.
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
#    Input, real A1(N1), the first vector.
#
#    Input, integer N2, the number of entries in the second vector.
#
#    Input, real A2(N2), the second vector.
#
#    Output, real A3(N1+N2), the concatenation of A1 and A2.
#
  import numpy as np

  a3 = np.concatenate ( ( a1, a2 ), axis = 0 )

  return a3

def r8vec_concatenate_test ( ):

#*****************************************************************************80
#
## R8VEC_CONCATENATE_TEST tests R8VEC_CONCATENATE.
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
  from r8vec_print import r8vec_print
  import numpy as np

  n1 = 5;
  n2 = 3;
  n3 = n1 + n2;

  a1 = np.array ( [ 91.1, 31.2, 71.3, 51.4, 31.5 ] )
  a2 = np.array ( [ 42.6, 22.7, 12.8 ] )

  print ''
  print 'R8VEC_CONCATENATE_TEST'
  print '  R8VEC_CONCATENATE concatenates two I4VECs'

  r8vec_print ( n1, a1, '  Array 1:' );
  r8vec_print ( n2, a2, '  Array 2:' );
  a3 = r8vec_concatenate ( n1, a1, n2, a2 );
  r8vec_print ( n3, a3, '  Array 3 = Array 1 + Array 2:' );

  print ''
  print 'R8VEC_CONCATENATE_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp

  timestamp ( )
  r8vec_concatenate_test ( )
  timestamp ( )
