#!/usr/bin/env python

def asm_enum ( n ):

#*****************************************************************************80
#
## ASM_ENUM returns the number of alternating sign matrices of a given order.
#
#  Discussion:
#
#    N     ASM_NUM
#
#    0       1
#    1       1
#    2       2
#    3       7
#    4      42
#    5     429
#    6    7436
#    7  218348
#
#    A direct formula is
#
#      ASM_NUM ( N ) = product ( 0 <= I <= N-1 ) ( 3 * I + 1 )# / ( N + I )#
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 January 2001
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrices.
#
#    Output, integer VALUE, the number of alternating sign
#    matrices of order N.
#
  import numpy as np

  value = 0

  if ( n + 1 <= 0 ):
    return value
#
#  Row 1
#
  if ( n + 1 == 1 ):
    value = 1
    return value
#
#  Row 2
#
  if ( n + 1 == 2 ):
    value = 1
    return value

  a = np.zeros ( n + 1 )
  b = np.zeros ( n + 1 )
  c = np.zeros ( n + 1 )

  a[0] = 1
  a[1] = 1
  b[0] = 2
  c[0] = 2
#
#  Row 3 and on.
#
  for nn in range ( 3, n + 1 ):

    b[nn-2] = nn
    for i in range ( nn - 2, 1, -1 ):
      b[i-1] = b[i-1] + b[i-2]

    b[0] = 2

    c[nn-2] = 2
    for i in range ( nn - 2, 1, -1 ):
      c[i-1] = c[i-1] + c[i-2]

    c[0] = nn

    for i in range ( 1, nn - 1 ):
      a[0] = a[0] + a[i]

    for i in range ( 1, nn ):
      a[i] = a[i-1] * c[i-1] // b[i-1]
 
  value = 0
  for i in range ( 0, n ):
    value = value + a[i]

  return value

def asm_enum_test ( ):

#*****************************************************************************80
#
## ASM_ENUM_TEST tests ASM_ENUM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    23 October 2014
#
#  Author:
#
#    John Burkardt
#
  n_max = 7

  print ''
  print 'ASM_ENUM_TEST:'
  print '  ASM_ENUM returns the number of alternating sign'
  print '  matrices of a given order.'
  print ''

  for n in range ( 0, n_max + 1 ):
    value = asm_enum ( n )
    print '  %2d  %8d' % ( n, value )
#
#  Terminate.
#
  print ''
  print 'ASM_ENUM_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  asm_enum_test ( )
  timestamp ( )
