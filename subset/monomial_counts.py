#! /usr/bin/env python
#
def monomial_counts ( degree_max, dim ):

#*****************************************************************************80
#
## MONOMIAL_COUNTS counts the number of monomials up to a given degree.
#
#  Discussion:
#
#    In 3D, there are 10 monomials of degree 3 or less:
#
#    Degree  Count  List
#    ------  -----  ----
#         0      1  1
#         1      3  x y z
#         2      6  xx xy xz yy yz zz
#         3     10  xxx xxy xxz xyy xyz xzz yyy yyz yzz zzz
#
#    Total      20
#
#    The formula is
#
#      COUNTS(DEGREE,DIM) = (DIM-1+DEGREE)% / (DIM-1)% / DEGREE%
#
#      TOTAL              = (DIM  +DEGREE)% / (DIM)%   / DEGREE%
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer DEGREE_MAX, the maximum degree.
#
#    Input, integer DIM, the spatial dimension.
#
#    Output, integer COUNTS(1:DEGREE_MAX+1), the number of
#    monomials of each degree.
#
  import numpy as np

  counts = np.zeros ( degree_max + 1 )

  degree = 0
  counts[degree] = 1

  for degree in range ( 1, degree_max + 1 ):
    counts[degree] = ( counts[degree-1] * ( dim - 1 + degree ) ) / degree

  return counts

def monomial_counts_test ( ):

#*****************************************************************************80
#
## MONOMIAL_COUNTS_TEST tests MONOMIAL_COUNTS.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 May 2015
#
#  Author:
#
#    John Burkardt
#
  from i4vec_sum import i4vec_sum

  degree_max = 9

  print ''
  print 'MONOMIAL_COUNTS_TEST'
  print '  MONOMIAL_COUNTS counts the number of monomials of'
  print '  degrees 0 through DEGREE_MAX in a space of dimension DIM.'

  for dim in range ( 1, 7 ):

    counts = monomial_counts ( degree_max, dim )

    s = i4vec_sum ( degree_max + 1, counts )

    print ''
    print '  DIM = %d' % ( dim )
    print ''
    for degree in range ( 0, degree_max + 1 ):
      print '  %8d  %8d' % ( degree + 1, counts[degree] )
    print ''
    print '     Total  %8d' % ( s )
#
#  Terminate.
#
  print ''
  print 'MONOMIAL_COUNTS_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  monomial_counts_test ( )
  timestamp ( )

