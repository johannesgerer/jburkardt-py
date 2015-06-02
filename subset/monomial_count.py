#! /usr/bin/env python
#
def monomial_count ( degree_max, dim ):

#*****************************************************************************80
#
## MONOMIAL_COUNT counts the number of monomials up to a given degree.
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
#      COUNTS(DEGREE,DIM) = (DIM-1+DEGREE)! / (DIM-1)! / DEGREE!
#
#      TOTAL              = (DIM  +DEGREE)! / (DIM)!   / DEGREE!
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
#    Output, integer TOTAL, the total number of monomials
#    of degrees 0 through DEGREE_MAX.
#
  total = 1

  if ( degree_max < dim ):

    top = dim + 1
    for bot in range ( 1, degree_max + 1 ):
      total = ( total * top ) // bot
      top = top + 1

  else:

    top = degree_max + 1
    for bot in range ( 1, dim + 1 ):
      total = ( total * top ) // bot
      top = top + 1

  return total

def monomial_count_test ( ):

#*****************************************************************************80
#
## MONOMIAL_COUNT_TEST tests MONOMIAL_COUNT.
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
  degree_max = 9

  print ''
  print 'MONOMIAL_COUNT_TEST'
  print '  MONOMIAL_COUNT counts the number of monomials of'
  print '  degrees 0 through DEGREE_MAX in a space of dimension DIM.'
  print ''
  print '  Using DEGREE_MAX = %d' % ( degree_max )
  print ''
  print '  Dim  Count'
  print ''

  for dim in range ( 1, 7 ):

    total = monomial_count ( degree_max, dim )
    print '  %2d  %8d' % ( dim, total )
#
#  Terminate.
#
  print ''
  print 'MONOMIAL_COUNT_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  monomial_count_test ( )
  timestamp ( )

