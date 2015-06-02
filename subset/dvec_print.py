#! /usr/bin/env python
#
def dvec_print ( n, dvec, title ):

#*****************************************************************************80
#
## DVEC_PRINT prints a DVEC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the dimension of the vector.
#
#    Input, real DVEC(N), the vector to be printed.
#
#    Input, character ( len = * ) TITLE, a title to be printed first.
#    TITLE may be blank.
#
  import sys

  if ( 0 < len ( title ) ):
    print ''
    print title
    print ''

  if ( dvec[n-1] == 9 ):
    sys.stdout.write ( '-' )
  else:
    sys.stdout.write ( '+' )
 
  for i in range ( n - 2, -1, -1 ):
    sys.stdout.write ( str ( dvec[i] ) )
  print ''

  return

def dvec_print_test ( ):

#*****************************************************************************80
#
## DVEC_PRINT_TEST tests DVEC_PRINT;
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    27 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  dvec = np.array ( [ \
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, \
    3, 4, 1, 7, 7, 5, 5, 0, 0, 9 ] )

  print ''
  print 'DVEC_PRINT_TEST'
  print '  DVEC_PRINT prints a (signed) decimal vector;'

  n = 20
  dvec_print ( n, dvec, '  The DVEC:' )
#
#  Terminate.
#
  print ''
  print 'DVEC_PRINT_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  dvec_print_test ( )
  timestamp ( )

