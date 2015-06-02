#!/usr/bin/env python

def i4_mod_inv ( b, n ):

#*****************************************************************************80
#
## I4_MOD_INV calculates the inverse of B mod N.
#
#  Discussion:
#
#    This function uses the extended Euclidean algorithm.
#
#    Unless the algorithm fails, the output value Y will satisfy
#
#      ( B * Y ) mod N = 1
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 May 2013
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Wade Trappe, Lawrence Washington,
#    Introduction to Cryptography with Coding Theory,
#    Prentice Hall, 2005,
#    ISBN13: 978-0131862395,
#    LC: QA268.T73.
#
#  Parameters:
#
#    Input, integer B, the value whose inverse is desired.
#    B must not be 0, or a multiple of N.  However, B can be negative.
#
#    Input, integer N, the value with respect to which the inverse is desired.
#    N must be 2 or greater.
#
#    Output, integer Y, the inverse of B mod N.  However, if the inverse
#    does not exist, Y is returned as the empty value [].
#
  from numpy import floor

  n0 = n
  b0 = abs ( b )
  t0 = 0
  t = 1

  q = ( n0 // b0 )
  r = n0 - q * b0

  while ( 0 < r ):

    temp = t0 - q * t

    if ( 0 <= temp ):
      temp =           temp   % n
    else:
      temp = n - ( ( - temp ) % n )

    n0 = b0
    b0 = r
    t0 = t
    t = temp

    q = ( n0 // b0 )
    r = n0 - q * b0

  if ( b0 != 1 ):
    y = 0
  else:
    y = ( t % n )
    if ( b < 0 ):
      y = - y

  return y

def i4_mod_inv_test ( ):

#*****************************************************************************80
#
## I4_MOD_INV_TEST tests I4_MOD_INV.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 May 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'I4_MOD_INV_TEST'
  print '  I4_MOD_INV finds the inverse of B mod N,'
  print '  that is, Y such that ( B * Y ) mod N = 1.'
  print ' '
  print '       B       N       Y     B*YmodN'
  print ' '

  n = 17
  for b in range ( 1, 17 ):
    y = i4_mod_inv ( b, n )
    t = ( ( b * y ) % n )
    print '  %6d  %6d  %6d  %6d' % ( b, n, y, t )

#
#  Terminate.
#
  print ''
  print 'I4_MOD_INV_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_mod_inv_test ( )
  timestamp ( )
