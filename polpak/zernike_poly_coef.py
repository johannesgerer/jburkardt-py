#!/usr/bin/env python
#
def zernike_poly_coef ( m, n ):

#*****************************************************************************80
#
## ## ZERNIKE_POLY_COEF: coefficients of a Zernike polynomial.
#
#  Discussion:
#
#    With our coefficients stored in COEFS(1:N+1), the
#    radial function R^M_N(RHO) is given by
#
#      R^M_N(RHO) = COEFS(1) 
#                 + COEFS(2) * RHO
#                 + COEFS(3) * RHO^2
#                 + ...
#                 + COEFS(N+1) * RHO^N
#
#    and the odd and even Zernike polynomials are
#
#      Z^M_N(RHO,PHI,odd)  = R^M_N(RHO) * sin(PHI)
#      Z^M_N(RHO,PHI,even) = R^M_N(RHO) * cos(PHI)
#
#    The first few "interesting" values of R are:
#
#    R^0_0 = 1
#
#    R^1_1 = RHO
#
#    R^0_2 = 2 * RHO^2 - 1
#    R^2_2 =     RHO^2
#
#    R^1_3 = 3 * RHO^3 - 2 * RHO
#    R^3_3 =     RHO^3
#
#    R^0_4 = 6 * RHO^4 - 6 * RHO^2 + 1
#    R^2_4 = 4 * RHO^4 - 3 * RHO^2
#    R^4_4 =     RHO^4
#
#    R^1_5 = 10 * RHO^5 - 12 * RHO^3 + 3 * RHO
#    R^3_5 =  5 * RHO^5 -  4 * RHO^3
#    R^5_5 =      RHO^5
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 October 2005
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Eric Weisstein,
#    Zernike Polynomials,
#    CRC Concise Encyclopedia of Mathematics,
#    CRC Press, 1998,
#    QA5.W45
#
#  Parameters:
#
#    Input, integer M, N, the parameters of the polynomial.
#    Normally, 0 <= M <= N and 0 <= N.
#  
#    Output, real C(1:N+1), the coefficients of the polynomial.
#
  import numpy as np
  from r8_choose import r8_choose

  c = np.zeros ( n + 1 )

  if ( n < 0 ):
    return c

  if ( m < 0 ):
    return c
      
  if ( n < m ):
    return c

  if ( ( ( m - n ) % 2 ) == 1 ):
    return c

  nm_plus = ( ( m + n ) // 2 )
  nm_minus = ( ( n - m ) // 2 )

  c[n] = r8_choose ( n, nm_plus )

  for l in range ( 0, nm_minus ):

    c[n-2*l-2] = - float ( ( nm_plus - l ) * ( nm_minus - l ) ) * c[n-2*l] \
      / float ( ( n - l ) * ( l + 1 ) )

  return c

def zernike_poly_coef_test ( ):

#*****************************************************************************80
#
## ZERNIKE_POLY_COEF_TEST tests ZERNIKE_POLY_COEF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 February 2015
#
#  Author:
#
#    John Burkardt
#
  from r8poly_print import r8poly_print

  n = 5

  print ''
  print 'ZERNIKE_POLY_COEF_TEST'
  print '  ZERNIKE_POLY_COEF determines the Zernike'
  print '  polynomial coefficients.'

  for m in range ( 0, n + 1 ):

    c = zernike_poly_coef ( m, n )
 
    r8poly_print ( n, c, '  Zernike polynomial:' )

  print ''
  print 'ZERNIKE_POLY_COEF_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  zernike_poly_coef_test ( )
  timestamp ( )
