#!/usr/bin/env python
#
def spherical_harmonic ( l, m, theta, phi ):

#*****************************************************************************80
#
## SPHERICAL_HARMONIC evaluates spherical harmonic functions.
#
#  Discussion:
#
#    The spherical harmonic function Y(L,M,THETA,PHI)(X) is the
#    angular part of the solution to Laplace's equation in spherical
#    coordinates.
#
#    Y(L,M,THETA,PHI)(X) is related to the associated Legendre
#    function as follows:
#
#      Y(L,M,THETA,PHI)(X) = FACTOR * P(L,M)(cos(THETA)) * exp ( i * M * PHI )
#
#    Here, FACTOR is a normalization factor:
#
#      FACTOR = sqrt ( ( 2 * L + 1 ) * ( L - M )! / ( 4 * PI * ( L + M )! ) )
#
#    In Mathematica, a spherical harmonic function can be evaluated by
#
#      SphericalHarmonicY [ l, m, theta, phi ]
#
#    Note that notational tradition in physics requires that THETA
#    and PHI represent the reverse of what they would normally mean
#    in mathematical notation; that is, THETA goes up and down, and
#    PHI goes around.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#    Eric Weisstein,
#    CRC Concise Encyclopedia of Mathematics,
#    CRC Press, 1999.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Parameters:
#
#    Input, integer L, the first index of the spherical harmonic function.
#    Normally, 0 <= L.
#
#    Input, integer M, the second index of the spherical harmonic function.
#    Normally, -L <= M <= L.
#
#    Input, real THETA, the polar angle, for which
#    0 <= THETA <= PI.
#
#    Input, real PHI, the longitudinal angle, for which
#    0 <= PHI <= 2*PI.
#
#    Output, real C(1:L+1), S(1:L+1), the real and imaginary
#    parts of the functions Y(L,0:L,THETA,PHI).
#
  import numpy as np
  from legendre_associated_normalized import legendre_associated_normalized

  m_abs = abs ( m )

  plm = legendre_associated_normalized ( l, m_abs, np.cos ( theta ) )

  c = np.zeros ( l + 1 )
  s = np.zeros ( l + 1 )

  for i in range ( 0, l + 1 ):
    c[i] = plm[i] * np.cos ( float ( m ) * phi )
    s[i] = plm[i] * np.sin ( float ( m ) * phi )

  if ( m < 0 ):
    for i in range ( 0, l + 1 ):
      c[i] = - c[i]
      s[i] = - s[i]

  return c, s

def spherical_harmonic_test ( ):

#*****************************************************************************80
#
## SPHERICAL_HARMONIC_TEST tests SPHERICAL_HARMONIC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 February 2015
#
#  Author:
#
#    John Burkardt
#
  from spherical_harmonic_values import spherical_harmonic_values

  print ''
  print 'SPHERICAL_HARMONIC_TEST'
  print '  SPHERICAL_HARMONIC evaluats the spherical harmonic function;'
  print ''
  print '      L       M    THETA   PHI   YR   YI'
  print ''

  n_data = 0

  while ( True ):

    n_data, l, m, theta, phi, yr, yi = spherical_harmonic_values ( n_data )

    if ( n_data == 0 ):
      break

    c, s = spherical_harmonic ( l, m, theta, phi )

    print '  %6d  %6d  %6f  %6f  %12f  %12f' % ( l, m, theta, phi, yr, yi )
    print '                                      %12f  %12f' % ( c[l], s[l] )

  print ''
  print 'SPHERICAL_HARMONIC_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  spherical_harmonic_test ( )
  timestamp ( )
