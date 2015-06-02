#!/usr/bin/env python

def bvec_print ( n, bvec, title ) :

#*****************************************************************************80
#
## BVEC_PRINT prints a binary integer vector, with an optional title.
#
#  Discussion:
#
#    A BVEC is an integer vector of binary digits, intended to
#    represent an integer.  BVEC(1) is the units digit, BVEC(N-1)
#    is the coefficient of 2^(N-2), and BVEC(N) contains sign
#    information.  It is 0 if the number is positive, and 1 if
#    the number is negative.
#
#    The vector is printed "backwards", that is, the first entry
#    printed is BVEC(N).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of components of the vector.
#
#    Input, integer BVEC(N), the vector to be printed.
#
#    Input, character ( len = * ) TITLE, a title to be printed first.
#    TITLE may be blank.
#
  if ( 0 < len ( title ) ):
    print ''
    print title

  for ihi in range ( n - 1, -1, -70 ):
    ilo = max ( ihi - 70, -1 )
    print '  ',
    for i in range ( ihi, -1, ilo ):
      print '%1d' % ( bvec[i] ),
    print ''

  return

def bvec_print_test ( ):

#*****************************************************************************80
#
## BVEC_PRINT_TEST tests BVEC_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    24 December 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 10
  bvec = np.array ( [ 1, 0, 0, 1, 0, 1, 1, 1, 0, 0 ] )

  print ''
  print 'BVEC_PRINT_TEST'
  print '  BVEC_PRINT prints a binary vector.'

  bvec_print ( n, bvec, '  BVEC:' )
 
  print ''
  print 'BVEC_PRINT_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  bvec_print_test ( )
  timestamp ( )
