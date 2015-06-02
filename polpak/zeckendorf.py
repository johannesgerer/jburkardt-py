#!/usr/bin/env python

def zeckendorf ( n ):

#*****************************************************************************80
#
## ZECKENDORF produces the Zeckendorf decomposition of a positive integer.
#
#  Discussion:
#
#    Zeckendorf proved that every positive integer can be represented
#    uniquely as the sum of non-consecutive Fibonacci numbers.
#
#    N = sum ( 1 <= I <= M ) F_LIST(I)
#
#  Example:
#
#     N    Decomposition
#
#    50    34 + 13 + 3
#    51    34 + 13 + 3 + 1
#    52    34 + 13 + 5
#    53    34 + 13 + 5 + 1
#    54    34 + 13 + 5 + 2
#    55    55
#    56    55 + 1
#    57    55 + 2
#    58    55 + 3
#    59    55 + 3 + 1
#    60    55 + 5
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the positive integer to be decomposed.
#
#    Output, integer M, the number of parts in the decomposition.
#
#    Output, integer I_LIST(M), the index of the Fibonacci numbers.
#
#    Output, integer F_LIST(M), the value of the Fibonacci numbers.
#
  import numpy as np
  from fibonacci_direct import fibonacci_direct
  from fibonacci_floor import fibonacci_floor

  m = 0
  i_list = []
#
#  Extract a sequence of Fibonacci numbers.
#
  while ( 0 < n ):
    [ f, i ] = fibonacci_floor ( n )
    i_list.append ( i )
    m = m + 1
    n = n - f
#
#  Replace any pair of consecutive indices ( I, I-1 ) by I+1.
#
  for i in range ( m - 1, 0, -1 ):

    if ( i_list[i-1] == i_list[i] + 1 ):
      i_list[i-1] = i_list[i-1] + 1
      for j in range ( i, m - 1 ):
        i_list[j] = i_list[j+1]
      m = m - 1
      i_list[m] = 0
#
#  Fill in the actual values of the Fibonacci numbers.
#
  f_list = np.zeros ( m )
  for i in range ( 0, m ):
    f_list[i] = fibonacci_direct ( i_list[i] )

  return m, i_list, f_list

def zeckendorf_test ( ):

#*****************************************************************************80
#
## ZECKENDORF_TEST tests ZECKENDORF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    28 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'ZECKENDORF_TEST'
  print '  ZECKENDORF computes the Zeckendorf decomposition of'
  print '  an integer N into nonconsecutive Fibonacci numbers.'
  print ''
  print '   N Sum M Parts'
  print ''

  for n in range ( 1, 101 ):

    m, i_list, f_list = zeckendorf ( n )

    print '  %3d' % ( n ),
    for j in range ( 0, m ):
      print'  %d' % ( f_list[j] ),
    print ''

  print ''
  print 'ZECKENDORF_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  zeckendorf_test ( )
  timestamp ( )
