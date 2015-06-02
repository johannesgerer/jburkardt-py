#!/usr/bin/env python
#
def bernoulli_number2 ( n ):

#*****************************************************************************80
#
## BERNOULLI_NUMBER2 evaluates the Bernoulli numbers.
#
#  Discussion:
#
#    The Bernoulli numbers are rational.
#
#    If we define the sum of the M-th powers of the first N integers as:
#
#      SIGMA(M,N) = sum ( 0 <= I <= N ) I**M
#
#    and let C(I,J) be the combinatorial coefficient:
#
#      C(I,J) = I! / ( ( I - J )! * J! )
#
#    then the Bernoulli numbers B(J) satisfy:
#
#      SIGMA(M,N) = 1/(M+1) * sum ( 0 <= J <= M ) C(M+1,J) B(J) * (N+1)**(M+1-J)
#
#    Note that the Bernoulli numbers grow rapidly.  Bernoulli number
#    62 is probably the last that can be computed on the VAX without
#    overflow.
#
#  First values:
#
#   B0  1                   =         1.00000000000
#   B1 -1/2                 =        -0.50000000000
#   B2  1/6                 =         1.66666666666
#   B3  0                   =         0
#   B4 -1/30                =        -0.03333333333
#   B5  0                   =         0
#   B6  1/42                =         0.02380952380
#   B7  0                   =         0
#   B8 -1/30                =        -0.03333333333
#   B9  0                   =         0
#  B10  5/66                =         0.07575757575
#  B11  0                   =         0
#  B12 -691/2730            =        -0.25311355311
#  B13  0                   =         0
#  B14  7/6                 =         1.16666666666
#  B15  0                   =         0
#  B16 -3617/510            =        -7.09215686274
#  B17  0                   =         0
#  B18  43867/798           =        54.97117794486
#  B19  0                   =         0
#  B20 -174611/330          =      -529.12424242424
#  B21  0                   =         0
#  B22  854,513/138         =      6192.123
#  B23  0                   =         0
#  B24 -236364091/2730      =    -86580.257
#  B25  0                   =         0
#  B26  8553103/6           =   1425517.16666
#  B27  0                   =         0
#  B28 -23749461029/870     = -27298231.0678
#  B29  0                   =         0
#  B30  8615841276005/14322 = 601580873.901
#
#  Recursion:
#
#    With C(N+1,K) denoting the standard binomial coefficient,
#
#    B(0) = 1.0
#    B(N) = - ( sum ( 0 <= K < N ) C(N+1,K) * B(K) ) / C(N+1,N)
#
#  Special Values:
#
#    Except for B(1), all Bernoulli numbers of odd index are 0.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the highest order Bernoulli number to compute.
#
#    Output, real B(1:N+1), the requested Bernoulli numbers B(0) through
#    B(N).
#
  from math import exp
  from math import log
  import numpy as np

  r8_pi = 3.141592653589793
  kmax = 400
  tol = 1.0E-06

  b = np.zeros ( n + 1 )

  b[0] = 1.0

  if ( n < 1 ):
    return b

  b[1] = -0.5

  if ( n < 2 ):
    return b

  altpi = log ( 2.0 * r8_pi )
#
#  Initial estimates for B(I), I = 2 to N
#
  b[2] = log ( 2.0 );
  for i in range ( 3, n + 1 ):
    if ( ( i % 2 ) == 1 ):
      b[i] = 0.0
    else:
      b[i] = log ( i * ( i - 1 ) ) + b[i-2]

  b[2] = 1.0 / 6.0

  if ( n <= 3 ):
    return b

  b[4] = - 1.0 / 30.0

  sgn = -1.0
 
  for i in range ( 6, n + 1, 2 ):
 
    sgn = -sgn
    t = 2.0 * sgn * exp ( b[i] - i * altpi )
 
    sum2 = 1.0

    for k in range ( 2, kmax + 1 ):

      term = 1.0 / ( k ** i )
      sum2 = sum2 + term

      if ( term <= tol * sum2 ):
        break
 
    b[i] = t * sum2
 
  return b

def bernoulli_number2_test ( ):

#*****************************************************************************80
#
## BERNOULLI_NUMBER2_TEST tests BERNOULLI_NUMBER2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 December 2014
#
#  Author:
#
#    John Burkardt
#
  from bernoulli_number_values import bernoulli_number_values

  print ''
  print 'BERNOULLI_NUMBER2_TEST'
  print '  BERNOULLI_NUMBER2 computes Bernoulli numbers;'
  print ''
  print '   I      Exact        Bernoulli'
  print ''

  n_data = 0

  while ( True ):

    n_data, n, c0 = bernoulli_number_values ( n_data )

    if ( n_data == 0 ):
      break

    c1 = bernoulli_number2 ( n )

    print '  %2d  %14e  %14e' % ( n, c0, c1[n] )

 
  print ''
  print 'BERNOULLI_NUMBER2_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  bernoulli_number2_test ( )
  timestamp ( )
