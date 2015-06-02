#!/usr/bin/env python

def r8mat_house_form ( n, v ):

#*****************************************************************************80
#
## R8MAT_HOUSE_FORM constructs a Householder matrix from its compact form.
#
#  Discussion:
#
#    H(v) = I - 2 * v * v' / ( v' * v )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, real V(N,1), the vector defining the Householder matrix.
#
#    Output, real H(N,N), the Householder matrix.
#
  import numpy as np

  v_dot_v = 0.0
  for i in range ( 0, n ):
    v_dot_v = v_dot_v + v[i] * v[i]

  c = - 2.0 / v_dot_v

  h = np.zeros ( ( n, n ) )

  for j in range ( 0, n ):
    h[j,j] = 1.0
    for i in range ( 0, n ):
      h[i,j] = h[i,j] + c * v[i] * v[j]
            
  return h

def r8mat_house_form_test ( ):

#*****************************************************************************80
#
## R8MAT_HOUSE_FORM_TEST tests R8MAT_HOUSE_FORM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  from r8mat_print import r8mat_print
  from r8vec_print import r8vec_print

  n = 5

  v = np.array ( ( 0.0, 0.0, 1.0, 2.0, 3.0 ) )

  print ''
  print 'R8MAT_HOUSE_FORM_TEST'
  print '  R8MAT_HOUSE_FORM forms a Householder'
  print '  matrix from its compact form.'

  r8vec_print ( n, v, '  Compact vector form V:' )

  h = r8mat_house_form ( n, v )
 
  r8mat_print ( n, n, h, '  Householder matrix H:' )

  print ''
  print 'R8MAT_HOUSE_FORM_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8mat_house_form_test ( )
  timestamp ( )
