#!/usr/bin/env python
#
def euler_number2 ( n ):

#*****************************************************************************80
#
## EULER_NUMBER2 computes the Euler numbers.
#
#  Discussion:
#
#    The Euler numbers can be evaluated in Mathematica by the call
#
#      EulerE[n]
#
#    These numbers rapidly get too big to store in an ordinary integer!
#
#    The terms of odd index are 0.
#
#    E(N) = -C(N,N-2) * E(N-2) - C(N,N-4) * E(N-4) - ... - C(N,0) * E(0).
#
#  First terms:
#
#    E0  = 1
#    E1  = 0
#    E2  = -1
#    E3  = 0
#    E4  = 5
#    E5  = 0
#    E6  = -61
#    E7  = 0
#    E8  = 1385
#    E9  = 0
#    E10 = -50521
#    E11 = 0
#    E12 = 2702765
#    E13 = 0
#    E14 = -199360981
#    E15 = 0
#    E16 = 19391512145
#    E17 = 0
#    E18 = -2404879675441
#    E19 = 0
#    E20 = 370371188237525
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Parameters:
#
#    Input, integer N, the index of the Euler number.
#
#    Output, real VALUE, the value of the Euler number.
#
  import numpy as np
  import r8_factorial as r8_factorial

  evec = np.array ( ( 1.0, -1.0, 5.0, -61.0, 1385.0, -50521.0, 2702765.0 ) )
  itmax = 1000
  r8_pi = 3.141592653589793

  value = 0.0

  if ( ( n % 2 ) == 0 ):

    if ( n <= 12 ):
      i = ( n // 2 )
      value = evec[i]
    else:

      sum1 = 0.0

      for i in range ( 0, itmax ):

        term = 1.0 / float ( ( 2 * i - 1 ) ** ( n + 1 ) )

        if ( ( i % 2 ) == 0 ):
          sum1 = sum1 + term
        else:
          sum1 = sum1 - term

        if ( abs ( term ) < 1.0E-10 ):
          break
        elif ( abs ( term ) < 1.0E-08 * abs ( sum1 ) ):
          break

      value = 2.0 ** ( n + 2 ) * sum1 * r8_factorial ( n ) / r8_pi ** ( n + 1 )

      if ( ( n % 4 ) != 0 ):
        value = -value

  return value

def euler_number2_test ( ):

#*****************************************************************************80
#
## EULER_NUMBER2_TEST tests EULER_NUMBER2.
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
  from euler_number_values import euler_number_values

  print ''
  print 'EULER_NUMBER2_TEST'
  print '  EULER_NUMBER2 computes Euler numbers;'
  print ''
  print '   I      Exact        Euler'
  print ''

  n_data = 0

  while ( True ):

    n_data, n, e1 = euler_number_values ( n_data )

    if ( n_data == 0 ):
      break

    e2 = euler_number2 ( n )

    print '  %2d  %14d  %14d' % ( n, e1, e2 )


  print ''
  print 'EULER_NUMBER2_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  euler_number2_test ( )
  timestamp ( )
