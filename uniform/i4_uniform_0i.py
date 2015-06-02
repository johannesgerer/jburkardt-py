#!/usr/bin/env python

def i4_uniform_0i ( seed ):

#*****************************************************************************80
#
## I4_UNIFORM_0I returns a pseudorandom I4.
#
#  Discussion:
#
#    SEED = SEED * (7^5) mod (2^31 - 1)
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
#    Paul Bratley, Bennett Fox, Linus Schrage,
#    A Guide to Simulation,
#    Second Edition,
#    Springer, 1987,
#    ISBN: 0387964673,
#    LC: QA76.9.C65.B73.
#
#    Bennett Fox,
#    Algorithm 647:
#    Implementation and Relative Efficiency of Quasirandom
#    Sequence Generators,
#    ACM Transactions on Mathematical Software,
#    Volume 12, Number 4, December 1986, pages 362-376.
#
#    Pierre L'Ecuyer,
#    Random Number Generation,
#    in Handbook of Simulation,
#    edited by Jerry Banks,
#    Wiley, 1998,
#    ISBN: 0471134031,
#    LC: T57.62.H37.
#
#    Peter Lewis, Allen Goodman, James Miller,
#    A Pseudo-Random Number Generator for the System/360,
#    IBM Systems Journal,
#    Volume 8, Number 2, 1969, pages 136-143.
#
#  Parameters:
#
#    Input, integer SEED, the integer "seed" used to generate
#    the output value.  SEED should not be 0.
#
#    Output, integer SEED, a uniform random value between
#    1 and 2^31-1.
#
#  Local parameters:
#
#    IA = 7^5
#    IB = 2^15
#    IB16 = 2^16
#    IP = 2^31-1
#
  ia = 16807
  ib15 = 32768
  ib16 = 65536
  ip = 2147483647
#
#  Don't let SEED be 0.
#
  if ( seed == 0 ):
    seed = ip
#
#  Get the 15 high order bits of SEED.
#
  ixhi = ( seed // ib16 )
#
#  Get the 16 low bits of SEED and form the low product.
#
  loxa = ( seed - ixhi * ib16 ) * ia
#
#  Get the 15 high order bits of the low product.
#
  leftlo = ( loxa // ib16 )
#
#  Form the 31 highest bits of the full product.
#
  iprhi = ixhi * ia + leftlo
#
#  Get overflow past the 31st bit of full product.
#
  k = ( iprhi // ib15 )
#
#  Assemble all the parts and presubtract IP.  The parentheses are
#  essential.
#
  seed = ( ( ( loxa - leftlo * ib16 ) - ip ) \
          + ( iprhi - k * ib15 ) * ib16 ) + k
#
#  Add IP back in if necessary.
#
  if ( seed < 0 ):
    seed = seed + ip

  return seed

def i4_uniform_0i_test ( ):

#*****************************************************************************80
#
## I4_UNIFORM_0I_TEST tests I4_UNIFORM_0I.
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
  seed = 123456789

  print ''
  print 'I4_UNIFORM_OI_TEST'
  print '  I4_UNIFORM_0I computes pseudorandom integers'
  print '  in the interval [1,(2^31)-1].'

  print ''
  print '  The initial seed is %d' % ( seed )
  print ''

  for i in range ( 1, 11 ):
    seed = i4_uniform_0i ( seed )
    print '  %6d  %d' % ( i, seed )

  print ''
  print 'I4_UNIFORM_0I_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_uniform_0i_test ( )
  timestamp ( )

