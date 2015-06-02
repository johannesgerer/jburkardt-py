#!/usr/bin/env python

def i4_is_prime ( n ) :

#*****************************************************************************80
#
## I4_IS_PRIME reports whether an I4 is prime.
#
#  Discussion:
#
#    A simple, unoptimized sieve of Erasthosthenes is used to
#    check whether N can be divided by any integer between 2
#    and SQRT(N).
#
#    Note that negative numbers, 0 and 1 are not considered prime.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 September 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the integer to be tested.
#
#    Output, boolean VALUE, is TRUE if N is prime, and FALSE
#    otherwise.
#
  from math import floor
  from math import sqrt

  if ( n <= 0 ):
    value = False
    return value

  if ( n == 1 ):
    value = False
    return value

  if ( n <= 3 ):
    value = True
    return value

  nhi = int ( sqrt ( n ) )

  for i in range ( 2, nhi + 1 ):
    if ( ( n % i ) == 0 ):
      value = False
      return value

  value = True

  return value

def i4_is_prime_test ( ) :

#*****************************************************************************80
#
## I4_IS_PRIME_TEST tests I4_IS_PRIME.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 September 2014
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'I4_IS_PRIME_TEST'
  print '  I4_IS_PRIME reports whether an I4 is prime.'
  print ' '
  print '         I  I4_IS_PRIME(I)'
  print ' '

  for i in range ( -2, 26 ):
    j = i4_is_prime ( i )
    print '  %8d  %r' % ( i, j )
#
#  Terminate.
#
  print ''
  print 'I4_IS_PRIME_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_is_prime_test ( )
  timestamp ( )
