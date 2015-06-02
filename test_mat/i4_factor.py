#!/usr/bin/env python

def i4_factor ( n ):

#*****************************************************************************80
#
## I4_FACTOR factors an integer into prime factors.
#
#  Formula:
#
#    N = NLEFT * Product ( 1 <= I <= NFACTOR ) FACTOR(I)^POWER(I).
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
#  Parameters:
#
#    Input, integer N, the integer to be factored.  N may be positive,
#    negative, or 0.
#
#    Output, integer NFACTOR, the number of prime factors of N discovered
#    by the routine.
#
#    Output, integer FACTOR(NFACTOR), the prime factors of N.
#
#    Output, integer POWER(NFACTOR).  POWER(I) is the power of
#    the FACTOR(I) in the representation of N.
#
#    Output, integer NLEFT, the factor of N that the routine could not
#    divide out.  If NLEFT is 1, then N has been completely factored.
#    Otherwise, NLEFT represents factors of N involving large primes.
#
  from prime import prime

  nfactor = 0
  factor = []
  power = []
  nleft = n

  if ( n == 0 ):
    return nfactor, factor, power, nleft

  if ( abs ( n ) == 1 ):
    nfactor = 1
    factor.append ( 1 )
    power.append ( 1 )
    return nfactor, factor, power, nleft
#
#  Find out how many primes we stored.
#
  maxprime = prime ( -1 )
#
#  Try dividing the remainder by each prime.
#
  for i in range ( 1, maxprime + 1 ):

    p = prime ( i )

    if ( ( ( abs ( nleft ) ) % p ) == 0 ):

      nfactor = nfactor + 1
      factor.append ( p )
      power.append ( 0 )

      while ( True ):

        power[nfactor-1] = power[nfactor-1] + 1
        nleft =  ( nleft // p )

        if ( ( ( abs ( nleft ) ) % p ) != 0 ):
          break

      if ( abs ( nleft ) == 1 ):
        break

  return nfactor, factor, power, nleft

def i4_factor_test ( ):

#*****************************************************************************80
#
## I4_FACTOR_TEST tests I4_FACTOR.
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
  n_test = [ 60, 664048, 8466763 ]

  print ''
  print 'I4_FACTOR_TEST'
  print '  I4_FACTOR tries to factor an I4.'

  for i in range ( 0, 3 ):
    n = n_test[i]
    nfactor, factor, power, nleft = i4_factor ( n )
    print ''
    print '  Factors of N = %d' % ( n )
    for j in range ( 0, nfactor ):
      print '    %d^%d' % ( factor[j], power[j] )
    if ( nleft != 1 ):
      print '  Unresolved factor NLEFT = %d' % ( nleft )

  print ''
  print 'I4_FACTOR_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_factor_test ( )
  timestamp ( )
