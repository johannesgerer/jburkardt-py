#!/usr/bin/env python

def r8_power_fast ( r, p ):

#*****************************************************************************80
#
## R8_POWER_FAST computes the P-th power of R.
#
#  Discussion:
#
#    Obviously, R**P can be computed using P-1 multiplications.
#
#    However, R**P can also be computed using at most 2*LOG2(P) multiplications.
#    To do the calculation this way, let N = LOG2(P).
#    Compute A, A**2, A**4, ..., A**N by N-1 successive squarings.
#    Start the value of R**P at A, and each time that there is a 1 in
#    the binary expansion of P, multiply by the current result of the squarings.
#
#    This algorithm is not optimal.  For small exponents, and for special
#    cases, the result can be computed even more quickly.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    25 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real R, the base.
#
#    Input, integer P, the power, which may be negative.
#
#    Output, real RP, the value of R**P.
#
#    Output, integer MULTS, the number of multiplications and divisions.
#
  from i4_sign import i4_sign
  from math import floor
  from sys import exit

  mults = 0
#
#  Force P to be an integer.
#
  p = floor ( p )
#
#  Special bases.
#
  if ( r == 1.0 ):
    rp = 1.0
    return rp, mults

  if ( r == -1.0 ):

    if ( ( p % 2 ) == 1 ):
      rp = -1.0
    else:
      rp = 1.0

    return rp, mults

  if ( r == 0.0 ):

    if ( p <= 0 ):
      print ''
      print 'R8_POWER_FAST - Fatal error!'
      print '  Base is zero, and exponent is negative.'
      exit ( 'R8_POWER_FAST - Fatal error!' );

    rp = 0.0
    return rp, mults
#
#  Special powers.
#
  if ( p == -1 ):
    rp = 1.0 / r
    mults = mults + 1
    return rp, mults
  elif ( p == 0 ):
    rp = 1.0
    return rp, mults
  elif ( p == 1 ):
    rp = r
    return rp, mults
#
#  Some work to do.
#
  p_mag = abs ( p )
  p_sign = i4_sign ( p )

  rp = 1.0
  r2 = r

  while ( 0 < p_mag ):

    if ( ( p_mag % 2 ) == 1 ):
      rp = rp * r2
      mults = mults + 1

    p_mag = floor ( p_mag / 2 )
    r2 = r2 * r2
    mults = mults + 1

  if ( p_sign == -1 ):
    rp = 1.0 / rp
    mults = mults + 1

  return rp, mults

def r8_power_fast_test ( ):

#*****************************************************************************80
#
## R8_POWER_FAST_TEST tests R8_POWER_FAST.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 July 2014
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'R8_POWER_FAST_TEST'
  print '  R8_POWER_FAST computes R^P, economizing on'
  print '  multiplications.'
  print ''
  print '      R          P       R^P        Mults'
  print ''

  for i in range ( -10, 41 ):

    r = 2.0
    p = i
    rp, mults = r8_power_fast ( r, p )
    print '  %12f  %5d  %12f  %5d' % ( r, p, rp, mults )
#
#  Terminate.
#
  print ''
  print 'R8_POWER_FAST_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_power_fast_test ( )
  timestamp ( )
