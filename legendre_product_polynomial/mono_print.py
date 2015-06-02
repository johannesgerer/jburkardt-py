#!/usr/bin/env python

def mono_print ( m, f, title ):

#*****************************************************************************80
#
## MONO_PRINT prints a monomial.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the spatial dimension.
#
#    Input, integer F[M], the exponents.
#
#    Input, string TITLE, a title.
#
  import sys

  sys.stdout.write ( title )
  
  sys.stdout.write ( '  x^' )
  if ( 1 < m or f[0] < 0 ):
    sys.stdout.write ( '(' )
  for i in range ( 0, m ):
    sys.stdout.write ( repr ( f[i] ) )
    if ( i < m - 1 ):
      sys.stdout.write ( ',' )
    elif ( 1 < m or f[0] < 0 ):
      sys.stdout.write ( ')' )
  sys.stdout.write ( '\n' )

  return

def mono_print_test ( ):

#*****************************************************************************80
#
## MONO_PRINT_TEST tests MONO_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ''
  print 'MONO_PRINT_TEST'
  print '  MONO_PRINT can print out a monomial.'
  print ''

  m = 1
  f = np.array ( [ 5 ], dtype = np.int32 )
  mono_print ( m, f, '  Monomial [5]:' )

  m = 1
  f = np.array ( [ -5 ], dtype = np.int32 )
  mono_print ( m, f, '  Monomial [-5]:' )

  m = 4
  f = np.array ( [ 2, 1, 0, 3 ], dtype = np.int32 )
  mono_print ( m, f, '  Monomial [2,1,0,3]:' )

  m = 3
  f = np.array ( [ 17, -3, 199 ], dtype = np.int32 )
  mono_print ( m, f, '  Monomial [17,-3,199]:' )

  print ''
  print 'MONO_PRINT_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp

  timestamp ( )
  mono_print_test ( )
  timestamp ( )
