#!/usr/bin/env python
#
def r8vec_house_column ( n, a_vec, k ):

#*****************************************************************************80
#
## R8VEC_HOUSE_COLUMN defines a Householder premultiplier that "packs" a column.
#
#  Discussion:
#
#    The routine returns a vector V that defines a Householder
#    premultiplier matrix H(V) that zeros out the subdiagonal entries of
#    column K of the matrix A.
#
#       H(V) = I - 2 * v * v'
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix A.
#
#    Input, real A_VEC(N), a row or column of the matrix A.
#
#    Input, integer K, the "special" entry in A_VEC.
#    The Householder matrix will zero out the entries after this.
#
#    Output, real V(N), a vector of unit L2 norm which defines an
#    orthogonal Householder premultiplier matrix H with the property
#    that the K-th column of H*A is zero below the diagonal.
#
  import numpy as np

  v = np.zeros ( n )

  if ( k < 0 or n - 1 <= k ):
    return v

  s = 0.0
  for i in range ( k, n ):
    s = s + a_vec[i] ** 2
  s = np.sqrt ( s )

  if ( s == 0.0 ):
    return v

  if ( a_vec[k] < 0.0 ):
    v[k] = a_vec[k] - abs ( s )
  else:
    v[k] = a_vec[k] + abs ( s )

  for i in range ( k + 1, n ):
    v[i] = a_vec[i]

  s = 0.0
  for i in range ( k, n ):
    s = s + v[i] ** 2
  s = np.sqrt ( s )

  for i in range ( k, n ):
    v[i] = v[i] / s

  return v

def r8vec_house_column_test ( ):

#*****************************************************************************80
#
## R8VEC_HOUSE_COLUMN_TEST tests R8VEC_HOUSE_COLUMN.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from r8mat_house_form import r8mat_house_form
  from r8mat_mm import r8mat_mm
  from r8mat_print import r8mat_print
  from r8mat_uniform_ab import r8mat_uniform_ab

  print ''
  print 'R8VEC_HOUSE_COLUMN_TEST'
  print '  R8VEC_HOUSE_COLUMN returns the compact form of'
  print '  a Householder matrix that "packs" a column'
  print '  of a matrix.'
#
#  Get a random matrix.
#
  n = 4
  r8_lo = 0.0
  r8_hi = 5.0
  seed = 123456789;

  a, seed = r8mat_uniform_ab ( n, n, r8_lo, r8_hi, seed )

  r8mat_print ( n, n, a, '  Matrix A:' )

  a_col = np.zeros ( n )

  for k in range ( 0, n - 1 ):

    print ''
    print '  Working on column K = %d' % ( k )

    for i in range ( 0, n ):
      a_col[i] = a[i,k]

    v = r8vec_house_column ( n, a_col, k )

    h = r8mat_house_form ( n, v )

    r8mat_print ( n, n, h, '  Householder matrix H:' )

    ha = r8mat_mm ( n, n, n, h, a )

    r8mat_print ( n, n, ha, '  Product H*A:' )
#
#  If we set A := HA, then we can successively convert A to upper
#  triangular form.
#
    a = ha

  print ''
  print 'R8VEC_HOUSE_COLUMN_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  r8vec_house_column_test ( )
  timestamp ( )
