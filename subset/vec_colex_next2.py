#!/usr/bin/env python

def vec_colex_next2 ( dim_num, base, a, more ):

#*****************************************************************************80
#
## VEC_COLEX_NEXT2 generates vectors in colex order.
#
#  Discussion:
#
#    The vectors are produced in colexical order, starting with
#    (0,0,...,0),
#    (1,0,...,0),
#    ...
#    (BASE(1)-1,BASE(2)-1,...,BASE(DIM_NUM)-1).
#
#  Example:
#
#    DIM_NUM = 2, 
#    BASE = [ 3, 3]
#
#    0   0
#    1   0
#    2   0
#    0   1
#    1   1
#    2   1
#    0   2
#    1   2
#    2   2
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Dennis Stanton, Dennis White,
#    Constructive Combinatorics,
#    Springer, 1986,
#    ISBN: 0387963472,
#    LC: QA164.S79.
#
#  Parameters:
#
#    Input, integer DIM_NUM, the spatial dimension.
#
#    Input, integer BASE(DIM_NUM), the base to be used in each dimension.
#
#    Input, integer A(DIM_NUM), except on the first call, this should
#    be the output value of A on the last call.
#
#    Input, logical MORE, should be FALSE on the first call, and
#    thereafter should be the output value of MORE from the previous call.  
#
#    Output, integer A(DIM_NUM), the next vector.
#
#    Output, logical MORE, is TRUE if another vector was computed.
#    If MORE is FALSE on return, then ignore the output value A, and
#    stop calling the routine.
#
  if ( not more ):

    for i in range ( 0, dim_num ):
      a[i] = 0

    more = True

  else:

    more = False

    for i in range ( 0, dim_num ):

      a[i] = a[i] + 1

      if ( a[i] < base[i] ):
        more = True
        break

      a[i] = 0

  return a, more

def vec_colex_next2_test ( ):

#*****************************************************************************80
#
## VEC_COLEX_NEXT2_TEST tests VEC_COLEX_NEXT2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from i4vec_transpose_print import i4vec_transpose_print

  print ''
  print 'VEC_COLEX_NEXT2_TEST'
  print '  VEC_COLEX_NEXT2 generates all DIM_NUM-vectors'
  print '  in colex order in a given base BASE.'
  
  dim_num = 3
  base = np.array ( [ 2, 1, 3 ] )
  a = np.zeros ( dim_num )
  more = False

  print ''
  print '  The spatial dimension DIM_NUM = %d' % ( dim_num )
  i4vec_transpose_print ( dim_num, base, '  The base vector:' )
  print ''

  while ( True ):

    a, more = vec_colex_next2 ( dim_num, base, a, more )

    if ( not more ):
      break

    i4vec_transpose_print ( dim_num, a, '' )
#
#  Terminate.
#
  print ''
  print 'VEC_COLEX_NEXT2_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  vec_colex_next2_test ( )
  timestamp ( )
