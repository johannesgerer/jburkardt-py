#! /usr/bin/env python
#
def hamming ( m, n ):

#*****************************************************************************80
#
## HAMMING computes the HAMMING matrix.
#
#  Example:
#
#    M = 3, N = 7
#
#    1 1 1 0 1 0 0
#    1 1 0 1 0 1 0
#    1 0 1 1 0 0 1
#
#    7 6 5 3 4 2 1 <-- binary interpretation of columns
#
#  Discussion:
#
#    For a given order M, the Hamming matrix is a rectangular array
#    of M rows and (2^M)-1 columns.  The entries of the matrix are
#    0 and 1.  The columns of A should be interpreted as the binary
#    representations of the integers between 1 and (2^M)-1.
#
#    We can also think of the columns as representing nonempty subsets
#    of an M set.  With this perspective, the columns of the matrix
#    are listed by order of size of subset.  For a given size, the columns
#    are ordered lexicographically.
#
#    The Hamming matrix can be viewed as an embodiment of the Hamming
#    code.  The nonsingleton columns correspond to data bits, and the
#    singleton columns correspond to check bits.  Each row of the
#    matrix represents a condition that the data bits and check bits
#    must satisfy.
#
#  Properties:
#
#    A has full row rank.
#
#    The last M columns of A contain the M by M identity matrix.
#
#    A is integral: int ( A ) = A.
#
#    A is a zero-one matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the number of rows in the matrix.
#
#    Input, integer N, the number of columns in the matrix.
#    N must be equal to 2^M-1.
#
#    Output, real A(M,N), the matrix.
#
  import numpy as np
  from bvec_next_grlex import bvec_next_grlex
  from sys import exit

  if ( n != ( 2 ** m - 1 ) ):
    print ''
    print 'HAMMING - Fatal error!'
    print '  M = %d' % ( m )
    print '  N = %d' % ( n )
    print '  but N = 2^M-1 is required.'
    exit ( 'HAMMING - Fatal error!' )

  a = np.zeros ( ( m, n ) )

  b = np.zeros ( m, dtype = np.int32 )

  for j in range ( n - 1, -1, -1 ):
    b = bvec_next_grlex ( m, b )
    for i in range ( 0, m ):
      a[i,j] = float ( b[i] )

  return a

def hamming_null_right ( m, n ):

#*****************************************************************************80
#
## HAMMING_NULL_RIGHT returns a right null vector for the HAMMING matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the order of the matrix.
#
#    Output, real X(N), a right null vector.
#
  import numpy as np
  from sys import exit

  if ( n != ( ( 2 ** m ) - 1 ) ):
    print ''
    print 'HAMMING_NULL_RIGHT - Fatal error!'
    print '  M = %d' % ( m )
    print '  N = %d' % ( n )
    print '  but N = 2^M-1 is required.'
    exit ( 'HAMMING_NULL_RIGHT - Fatal error!' )

  if ( m < 2 ):
    print ''
    print 'HAMMING_NULL_RIGHT - Fatal error!'
    print '  M must be at least 2.'
    exit ( 'HAMMING_NULL_RIGHT - Fatal error!' )

  x = np.zeros ( n )

  x[0] =  1.0
  for j in range ( n - m, n ):
    x[j] = -1.0

  return x

def hamming_test ( ):

#*****************************************************************************80
#
## HAMMING_TEST tests HAMMING.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 March 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'HAMMING_TEST'
  print '  HAMMING computes the HAMMING matrix.'

  m = 3
  n = ( 2 ** 3 ) - 1
  a = hamming ( m, n )
  r8mat_print ( m, n, a, '  HAMMING matrix:' )
#
#  Terminate.
#
  print ''
  print 'HAMMING_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  hamming_test ( )
  timestamp ( )
