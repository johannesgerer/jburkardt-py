#! /usr/bin/env python
#
def dvec_add ( n, dvec1, dvec2 ):

#*****************************************************************************80
#
## DVEC_ADD adds two (signed) decimal vectors.
#
#  Discussion:
#
#    A DVEC is an integer vector of decimal digits, intended to
#    represent an integer.  DVEC(1) is the units digit, DVEC(N-1)
#    is the coefficient of 10**(N-2), and DVEC(N) contains sign
#    information.  It is 0 if the number is positive, and 1 if
#    the number is negative.
#
#  Example:
#
#    N = 4
#
#      DVEC1     +   DVEC2     =   DVEC3
#
#    ( 0 0 1 7 ) + ( 0 1 0 4 ) = ( 0 0 1 2 1 )
#
#          17    +       104   =         121
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the length of the vectors.
#
#    Input, integer DVEC1(N), DVEC2(N), the vectors to be added.
#
#    Output, integer DVEC3(N), the sum of the two input vectors.
#
  import numpy as np

  base = 10
  overflow = 0

  dvec3 = np.zeros ( n, dtype = np.int32 )

  for i in range ( 0, n ):
    dvec3[i] = dvec1[i] + dvec2[i]

  for i in range ( 0, n ):
    while ( base <= dvec3[i] ):
      dvec3[i] = dvec3[i] - base
      if ( i < n - 1 ):
        dvec3[i+1] = dvec3[i+1] + 1
      else:
        overflow = 1

  return dvec3

def dvec_add_test ( ):

#*****************************************************************************80
#
## DVEC_ADD_TEST tests DVEC_ADD.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 May 2015
#
#  Author:
#
#    John Burkardt
#
  from dvec_to_i4 import dvec_to_i4
  from i4_to_dvec import i4_to_dvec
  from i4_uniform_ab import i4_uniform_ab

  n = 10
  seed = 123456789
  test_num = 10

  print ''
  print 'DVEC_ADD_TEST'
  print '  DVEC_ADD adds decimal vectors representing integers'
  print ''
  print '        I        J        K = I + J'
  print ''

  for test in range ( 0, test_num ):
    
    i, seed = i4_uniform_ab ( -100, 100, seed )
    j, seed = i4_uniform_ab ( -100, 100, seed )

    print ''

    print '  %8d  %8d' % ( i, j )

    k = i + j

    print '  Directly:           %8d' % ( k )

    dvec1 = i4_to_dvec ( i, n )
    dvec2 = i4_to_dvec ( j, n )

    dvec3 = dvec_add ( n, dvec1, dvec2 )
    k = dvec_to_i4 ( n, dvec3 )

    print '  DVEC_ADD  %8d' % ( k )
#
#  Terminate.
#
  print ''
  print 'DVEC_ADD_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  dvec_add_test ( )
  timestamp ( )
