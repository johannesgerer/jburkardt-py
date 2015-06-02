#!/usr/bin/env python

def i4_characteristic ( q ) :

#*****************************************************************************80
#
## I4_CHARACTERISTIC gives the characteristic for an I4.
#
#  Discussion:
#
#    For any positive integer Q, the characteristic is:
#
#    Q, if Q is a prime;
#    P, if Q = P^N for some prime P and some integer N;
#    0, otherwise, that is, if Q is negative, 0, 1, or the product
#       of more than one distinct prime.
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
#    John Burkardt.
#
#  Reference:
#
#    Paul Bratley, Bennett Fox, Harald Niederreiter,
#    Algorithm 738:
#    Programs to Generate Niederreiter's Low-Discrepancy Sequences,
#    ACM Transactions on Mathematical Software,
#    Volume 20, Number 4, pages 494-495, 1994.
#
#  Parameters:
#
#    Input, integer Q, the value to be tested.
#
#    Output, integer VALUE, the characteristic of Q.
#
  from math import floor
  from math import sqrt

  if ( q <= 1 ):
    value = 0
    return value
#
#  If Q is not prime, then there is at least one prime factor
#  of Q no greater than SQRT(Q)+1.
#
#  A faster code would only consider prime values of I,
#  but that entails storing a table of primes and limiting the
#  size of Q.  Simplicity and flexibility for now!
#
  i_max = int ( sqrt ( q ) ) + 1

  for i in range ( 2, i_max + 1 ):

    if ( ( q % i ) == 0 ):

      while ( ( q % i ) == 0 ):
        q = q / i

      if ( q == 1 ):
        value = i
      else:
        value = 0

      return value
#
#  If no factor was found, then Q is prime.
#
  value = q

  return value

def i4_characteristic_test ( ):

#*****************************************************************************80
#
## I4_CHARACTERISTIC_TEST tests I4_CHARACTERISTIC.
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
  from i4_uniform_ab import i4_uniform_ab

  seed = 123456789
  test_num = 10

  print ''
  print 'I4_CHARACTERISTIC_TEST'
  print '  I4_CHARACTERISTIC computes the characteristic'
  print '  of an integer Q, which is  '
  print '    Q if Q is prime;'
  print '    P, if Q = P^N for some prime P;'
  print '    0, if Q is negative, 0, 1, or the product of '
  print '      more than 1 distinct prime.'
  print ' '
  print '   I  I4_CHARACTERISTIC'
  print ' '
 
  for i in range ( 1, 51 ):
    j = i4_characteristic ( i )
    print '  %2d             %4d' % ( i, j )
#
#  Terminate.
#
  print ''
  print 'I4_CHARACTERISTIC_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_characteristic_test ( )
  timestamp ( )
