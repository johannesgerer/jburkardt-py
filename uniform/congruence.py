#!/usr/bin/env python

def congruence ( a, b, c ):

#*****************************************************************************80
#
## CONGRUENCE solves a congruence of the form A * X = C ( mod B ).
#
#  Discussion:
#
#    A, B and C are given integers.  The equation is solvable if and only
#    if the greatest common divisor of A and B also divides C.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    05 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Eric Weisstein, editor,
#    CRC Concise Encylopedia of Mathematics,
#    CRC Press, 1998, page 446.
#
#  Parameters:
#
#    Input, integer A, B, C, the coefficients of the Diophantine equation.
#
#    Output, integer X, the solution of the Diophantine equation.
#    X will be between 0 and B-1.
#
#    Output, integer IERROR, error flag.
#    0, no error, X was computed.
#    1, A = B = 0, C is nonzero.
#    2, A = 0, B and C nonzero, but C is not a multiple of B.
#    3, A nonzero, B zero, C nonzero, but C is not a multiple of A.
#    4, A, B, C nonzero, but GCD of A and B does not divide C.
#    5, algorithm ran out of internal space.
#
  import numpy as np
  from i4_gcd import i4_gcd
  from i4_sign import i4_sign
  from math import floor
  from sys import exit

  a = floor ( a )
  b = floor ( b )
  c = floor ( c )

  nmax = 100
#
#  Defaults for output parameters.
#
  ierror = 0
  x = 0
  y = 0
#
#  Special cases.
#
  if ( a == 0 and b == 0 and c == 0 ):
    x = 0
    return x, ierror
  elif ( a == 0 and b == 0 and c != 0 ):
    ierror = 1
    x = 0
    return x, ierror
  elif ( a == 0 and b != 0 and c == 0 ):
    x = 0
    return x, ierror
  elif ( a == 0 and b != 0 and c != 0 ):
    x = 0
    if ( ( c % b ) != 0 ):
      ierror = 2
    return x, ierror
  elif ( a != 0 and b == 0 and c == 0 ):
    x = 0
    return x, ierror
  elif ( a != 0 and b == 0 and c != 0 ):
    x = floor ( c / a )
    if ( ( c % a ) != 0 ):
      ierror = 3
    return x, ierror
  elif ( a != 0 and b != 0 and c == 0 ):
#   g = i4_gcd ( a, b )
#   x = floor ( b / g )
    x = 0
    return x, ierror
#
#  Now handle the "general" case: A, B and C are nonzero.
#
#  Step 1: Compute the GCD of A and B, which must also divide C.
#
  g = i4_gcd ( a, b )

  if ( ( c % g ) != 0 ):
    ierror = 4
    return x, ierror

  a_copy = floor ( a / g )
  b_copy = floor ( b / g )
  c_copy = floor ( c / g )
#
#  Step 2: Split A and B into sign and magnitude.
#
  a_mag = abs ( a_copy )
  a_sign = i4_sign ( a_copy )
  b_mag = abs ( b_copy )
  b_sign = i4_sign ( b_copy )
#
#  Another special case, A_MAG = 1 or B_MAG = 1.
#
  if ( a_mag == 1 ):
    x = a_sign * c_copy
    return x, ierror
  elif ( b_mag == 1 ):
    x = 0
    return x, ierror
#
#  Step 3: Produce the Euclidean remainder sequence.
#
  q = np.zeros ( nmax )

  if ( b_mag <= a_mag ):
    swap = 0;
    q[0] = a_mag;
    q[1] = b_mag;
  else:
    swap = 1;
    q[0] = b_mag;
    q[1] = a_mag;

  n = 2

  while ( True ):

    q[n] = ( q[n-2] % q[n-1] )

    if ( q[n] == 1 ):
      break

    n = n + 1

    if ( nmax <= n ):
      ierror = 5
      print ''
      print 'CONGRUENCE - Fatal error!'
      print '  Exceeded number of iterations.'
      exit ( 'CONGRUENCE - Fatal error!' )
#
#  Step 4: Now go backwards to solve X * A_MAG + Y * B_MAG = 1.
#
  y = 0
  for k in range ( n, 0, -1 ):
    x = y
    y = ( 1 - x * q[k-1] ) / q[k]
#
#  Step 5: Undo the swapping.
#
  if ( swap ):
    z = x
    x = y
    y = z
#
#  Step 6: Now apply signs to X and Y so that X * A + Y * B = 1.
#
  x = x * a_sign
#
#  Step 7: Multiply by C, so that X * A + Y * B = C.
#
  x = x * c_copy
#
#  Step 8: Now force 0 <= X < B.
#
  x = ( x % b )
#
#  Step 9: Force positivity.
#
  if ( x < 0 ):
    x = x + b

  return x, ierror

def congruence_test ( ):

#*****************************************************************************80
#
## CONGRUENCE_TEST tests CONGRUENCE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 December 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from i4_modp import i4_modp

  test_num = 20

  a_test = np.array ( ( \
     1027,  1027,  1027,  1027, -1027, \
    -1027, -1027, -1027,     6,     0, \
        0,     0,     1,     1,     1, \
     1024,     0,     0,     5,     2 ) )
  b_test = np.array ( ( \
      712,   712,  -712,  -712,   712, \
      712,  -712,  -712,     8,     0, \
        1,     1,     0,     0,     1, \
   -15625,     0,     3,     0,     4 ) )
  c_test = np.array ( ( \
        7,    -7,     7,    -7,     7, \
       -7,     7,    -7,    50,     0, \
        0,     1,     0,     1,     0, \
    11529,     1,    11,    19,     7 ) )

  print ''
  print 'CONGRUENCE_TEST'
  print '  CONGRUENCE solves a congruence equation:'
  print '    A * X = C mod ( B )'
  print ''
  print '   I        A         B         C         X     Mod ( A*X-C,B)'
  print ''

  for test_i in range ( 0, test_num ):

    a = a_test[test_i]
    b = b_test[test_i]
    c = c_test[test_i]

    x, ierror = congruence ( a, b, c )

    if ( b != 0 ):
      result = i4_modp ( a * x - c, b )
    else:
      result = 0

    print '  %2d  %8d  %8d  %8d  %8d  %8d' % ( test_i, a, b, c, x, result )

  print ''
  print 'CONGRUENCE_TEST'
  print '  Normal end of execution.'

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  congruence_test ( )
  timestamp ( )

