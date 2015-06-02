#!/usr/bin/env python

def c8mat_identity ( n ):

#*****************************************************************************80
#
## C8MAT_IDENTITY returns the identity matrix.
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
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Output, complex C(N,N), the identity matrix.
#
  import numpy

  c = numpy.zeros ( ( n, n ), 'complex' )

  for i in range ( 0, n ): 
    c[i][i] = complex ( 1.0, 0.0 )

  return c

def c8mat_identity_test ( ):

#*****************************************************************************80
#
## C8MAT_IDENTITY_TEST tests C8MAT_IDENTITY.
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
  from c8mat_print import c8mat_print

  import numpy as np

  m = 4
  n = 4

  print ''
  print 'C8MAT_IDENTITY_TEST'
  print '  C8MAT_IDENTITY returns the complex identity matrix.'

  c = c8mat_identity ( n )

  c8mat_print ( m, n, c, '  Identity matrix:' )

  print ''
  print 'C8MAT_IDENTITY_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  c8mat_identity_test ( )
  timestamp ( )
