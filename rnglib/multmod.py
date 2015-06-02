#!/usr/bin/env python

def multmod ( a, s, m ):

#*****************************************************************************80
#
## MULTMOD carries out modular multiplication.
#
#  Discussion:
#
#    This procedure returns
#
#      ( A * S ) mod M
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 May 2013
#
#  Author:
#
#    Original Pascal version by Pierre L'Ecuyer, Serge Cote.
#    MATLAB version by John Burkardt.
#
#  Reference:
#
#    Pierre LEcuyer, Serge Cote,
#    Implementing a Random Number Package with Splitting Facilities,
#    ACM Transactions on Mathematical Software,
#    Volume 17, Number 1, March 1991, pages 98-111.
#
#  Parameters:
#
#    Input, integer A, S, M, the arguments.
#
#    Output, integer VALUE, the value of the product of A and S,
#    modulo M.
#
  from i4_division import i4_division
  from sys import exit

  h = 32768

  if ( a <= 0 ):
    print ''
    print 'MULTMOD - Fatal error!'
    print '  A <= 0.'
    exit ( 'MULTMOD - Fatal error!' )

  if ( m <= a ):
    print ''
    print 'MULTMOD - Fatal error!'
    print '  M <= A.'
    exit ( 'MULTMOD - Fatal error!' )

  if ( s <= 0 ):
    print ''
    print 'MULTMOD - Fatal error!'
    print '  S <= 0.'
    exit ( 'MULTMOD - Fatal error!' )

  if ( m <= s ):
    print ''
    print 'MULTMOD - Fatal error!'
    print '  M <= S.'
    exit ( 'MULTMOD - Fatal error!' )

  if ( a < h ):

    a0 = a
    p = 0

  else:

    a1 = i4_division ( a, h )
    a0 = a - h * a1
    qh = i4_division ( m, h )
    rh = m - h * qh

    if ( h <= a1 ):

      a1 = a1 - h
      k = i4_division ( s, qh )
      p = h * ( s - k * qh ) - k * rh

      while ( p < 0 ):
        p = p + m

    else:

      p = 0

    if ( a1 != 0 ):

      q = i4_division ( m, a1 )
      k = i4_division ( s, q )
      p = p - k * ( m - a1 * q )

      if ( 0 < p ):
        p = p - m

      p = p + a1 * ( s - k * q )

      while ( p < 0 ):
        p = p + m

    k = i4_division ( p, qh )
    p = h * ( p - k * qh ) - k * rh

    while ( p < 0 ):
      p = p + m

  if ( a0 != 0 ):

    q = i4_division ( m, a0 )
    k = i4_division ( s, q )
    p = p - k * ( m - a0 * q )

    if ( 0 < p ):
      p = p - m

    p = p + a0 * ( s - k * q )

    while ( p < 0 ):
      p = p + m

  return p

