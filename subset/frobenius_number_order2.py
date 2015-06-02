#!/usr/bin/env python

def frobenius_number_order2 ( c1, c2 ):

#*****************************************************************************80
#
## FROBENIUS_NUMBER_ORDER2 returns the Frobenius number for order 2.
#
#  Discussion:
#
#    The Frobenius number of order N is the solution of the Frobenius
#    coin sum problem for N coin denominations.
#
#    The Frobenius coin sum problem assumes the existence of
#    N coin denominations, and asks for the largest value that cannot
#    be formed by any combination of coins of these denominations.
#
#    The coin denominations are assumed to be distinct positive integers.
#
#    For general N, this problem is fairly difficult to handle.
#
#    For N = 2, it is known that:
#
#    * if C1 and C2 are not relatively prime, then
#      there are infinitely large values that cannot be formed.
#
#    * otherwise, the largest value that cannot be formed is
#      C1 * C2 - C1 - C2, and that exactly half the values between
#      1 and C1 * C2 - C1 - C2 + 1 cannot be represented.
#
#    As a simple example, if C1 = 2 and C2 = 7, then the largest
#    unrepresentable value is 5, and there are (5+1)/2 = 3
#    unrepresentable values, namely 1, 3, and 5.
#
#    For a general N, and a set of coin denominations C1, C2, ..., CN,
#    the Frobenius number F(N, C(1:N) ) is defined as the largest value
#    B for which the equation
#
#      C1*X1 + C2*X2 + ... + CN*XN = B
#
#    has no nonnegative integer solution X(1:N).
#
#    In the Mathematica Package "NumberTheory", the Frobenius number
#    can be determined by
#
#    <<NumberTheory`Frobenius`
#    FrobeniusF[ {C1,...,CN} ]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    James Sylvester,
#    Question 7382,
#    Mathematical Questions with their Solutions,
#    Educational Times,
#    Volume 41, page 21, 1884.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Cambridge University Press, 1999,
#    ISBN: 0-521-64314-7,
#    LC: QA76.95.W65.
#
#  Parameters:
#
#    Input, integer C1, C2, the coin denominations. C1 and C2
#    should be positive and relatively prime.
#
#    Output, integer FROBENIUS_NUMBER_ORDER2, the Frobenius number of (C1,C2).
#
  from i4_gcd import i4_gcd
  from i4_huge import i4_huge

  if ( c1 <= 0 ):
    value = i4_huge ( )
  elif ( c2 <= 0 ):
    value = i4_huge ( )
  elif ( i4_gcd ( c1, c2 ) != 1 ):
    value = i4_huge ( )
  else:
    value = c1 * c2 - c1 - c2

  return value

def frobenius_number_order2_test ( ):

#*****************************************************************************80
#
## FROBENIUS_NUMBER_ORDER2_TEST tests FROBENIUS_NUMBER_ORDER2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    08 May 2015
#
#  Author:
#
#    John Burkardt
#
  from frobenius_number_order2_values import frobenius_number_order2_values

  print ''
  print 'FROBENIUS_NUMBER_ORDER2_TEST';
  print '  FROBENIUS_NUMBER_ORDER2 computes Frobenius numbers of order 2.'
  print ''
  print '        C1        C1   exact F  computed F'
  print ''

  n_data = 0

  while ( True ):

    n_data, c1, c2, f1 = frobenius_number_order2_values ( n_data )

    if ( n_data == 0 ):
      break

    f2 = frobenius_number_order2 ( c1, c2 )

    print '  %8d  %8d  %8d  %8d' % ( c1, c2, f1, f2 )
#
#  Terminate.
#
  print ''
  print 'FROBENIUS_NUMBER_ORDER2_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  frobenius_number_order2_test ( )
  timestamp ( )
