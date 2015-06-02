#!/usr/bin/env python
#
def euler_number ( n ):

#*****************************************************************************80
#
## EULER_NUMBER computes the Euler numbers.
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
#    04 February 2015
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
#    Input, integer N, the index of the last Euler number to compute.
#
#    Output, integer E[0:N], the Euler numbers.
#
  import numpy as np
  from i4_choose import i4_choose

  e = np.zeros ( n + 1 )

  e[0] = 1

  if ( 0 < n ):

    e[1] = 0

    if ( 1 < n ):

      e[2] = -1

      for i in range ( 3, n + 1 ):

        e[i] = 0

        if ( ( i % 2 ) == 0 ):

          for j in range ( 2, i + 1, 2 ):
            e[i] = e[i] - i4_choose ( i, j ) * e[i-j]

  return e

def euler_number_test ( ):

#*****************************************************************************80
#
## EULER_NUMBER_TEST tests EULER_NUMBER.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 February 2015
#
#  Author:
#
#    John Burkardt
#
  from euler_number_values import euler_number_values

  print ''
  print 'EULER_NUMBER_TEST'
  print '  EULER_NUMBER computes Euler numbers;'
  print ''
  print '   I      Exact        Euler'
  print ''

  n_data = 0

  while ( True ):

    n_data, n, e1 = euler_number_values ( n_data )

    if ( n_data == 0 ):
      break

    e2 = euler_number ( n )

    print '  %2d  %14d  %14d' % ( n, e1, e2[n] )


  print ''
  print 'EULER_NUMBER_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  euler_number_test ( )
  timestamp ( )
