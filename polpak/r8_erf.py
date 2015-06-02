#!/usr/bin/env python

def r8_erf ( x ):

#*****************************************************************************80
#
## R8_ERF evaluates the error function.
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
#    W J Cody,
#    Mathematics and Computer Science Division,
#    Argonne National Laboratory,
#    Argonne, Illinois, 60439.
#
#  Reference:
#
#    W J Cody,
#    "Rational Chebyshev approximations for the error function",
#    Mathematics of Computation, 
#    1969, pages 631-638.
#
#  Parameters:
#
#    Input, real X, the argument of the error function.
#
#    Output, real VALUE, the value of the error function.
#
  import numpy as np

  a = np.array ( ( \
    3.16112374387056560E+00, \
    1.13864154151050156E+02, \
    3.77485237685302021E+02, \
    3.20937758913846947E+03, \
    1.85777706184603153E-01 ))
  b = np.array ( ( \
    2.36012909523441209E+01, \
    2.44024637934444173E+02, \
    1.28261652607737228E+03, \
    2.84423683343917062E+03 ))
  c = np.array ( ( \
    5.64188496988670089E-01, \
    8.88314979438837594E+00, \
    6.61191906371416295E+01, \
    2.98635138197400131E+02, \
    8.81952221241769090E+02, \
    1.71204761263407058E+03, \
    2.05107837782607147E+03, \
    1.23033935479799725E+03, \
    2.15311535474403846E-08 ))
  d = np.array ( ( \
    1.57449261107098347E+01, \
    1.17693950891312499E+02, \
    5.37181101862009858E+02, \
    1.62138957456669019E+03, \
    3.29079923573345963E+03, \
    4.36261909014324716E+03, \
    3.43936767414372164E+03, \
    1.23033935480374942E+03 ))
  p = np.array ( ( \
    3.05326634961232344E-01, \
    3.60344899949804439E-01, \
    1.25781726111229246E-01, \
    1.60837851487422766E-02, \
    6.58749161529837803E-04, \
    1.63153871373020978E-02 ))
  q = np.array ( ( \
    2.56852019228982242E+00, \
    1.87295284992346047E+00, \
    5.27905102951428412E-01, \
    6.05183413124413191E-02, \
    2.33520497626869185E-03 ))
  sqrpi = 0.56418958354775628695E+00
  thresh = 0.46875E+00
  xbig = 26.543E+00
  xsmall = 1.11E-16

  xabs = abs ( x )
#
#  Evaluate ERF(X) for |X| <= 0.46875.
#
  if ( xabs <= thresh ):

    if ( xsmall < xabs ):
      xsq = xabs * xabs
    else:
      xsq = 0.0

    xnum = a[4] * xsq
    xden = xsq
    for i in range ( 0, 3 ):
      xnum = ( xnum + a[i] ) * xsq
      xden = ( xden + b[i] ) * xsq

    value = x * ( xnum + a[3] ) / ( xden + b[3] )
#
#  Evaluate ERFC(X) for 0.46875 <= |X| <= 4.0.
#
  elif ( xabs <= 4.0 ):

    xnum = c[8] * xabs
    xden = xabs
    for i in range ( 0, 7 ):
      xnum = ( xnum + c[i] ) * xabs
      xden = ( xden + d[i] ) * xabs

    value = ( xnum + c[7] ) / ( xden + d[7] )
    xsq = np.floor ( xabs * 16.0 ) / 16.0
    delt = ( xabs - xsq ) * ( xabs + xsq )
    value = np.exp ( - xsq * xsq ) * np.exp ( - delt ) * value

    value = ( 0.5 - value ) + 0.5

    if ( x < 0.0 ):
      value = -value
#
#  Evaluate ERFC(X) for 4.0 < |X|.
#
  else:

    if ( xbig <= xabs ):

      if ( 0.0 < x ):
        value = 1.0
      else:
        value = -1.0;

    else:

      xsq = 1.0 / ( xabs * xabs )

      xnum = p[5] * xsq
      xden = xsq
      for i in range ( 0, 4 ):
        xnum = ( xnum + p[i] ) * xsq
        xden = ( xden + q[i] ) * xsq

      value = xsq * ( xnum + p[4] ) / ( xden + q[4] )
      value = ( sqrpi -  value ) / xabs
      xsq = np.floor ( xabs * 16.0 ) / 16.0
      delt = ( xabs - xsq ) * ( xabs + xsq )
      value = np.exp ( - xsq * xsq ) * np.exp ( - delt ) * value

      value = ( 0.5 - value ) + 0.5

      if ( x < 0.0 ):
        value = -value;

  return value

def r8_erf_test ( ):

#*****************************************************************************80
#
## R8_ERF_TEST tests R8_ERF.
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
  from erf_values import erf_values
  from r8_erf import r8_erf

  print ''
  print 'R8_ERF_TEST:'
  print '  R8_ERF evaluates the error function.'
  print ''
  print '      X            ERF(X)    R8_ERF(X)'
  print ''

  n_data = 0

  while ( True ):

    n_data, x, fx1 = erf_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_erf ( x )

    print '  %12g  %24.16g  %24.16g' % ( x, fx1, fx2 )

  print ''
  print 'R8_ERF_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  r8_erf_test ( )
  timestamp ( )
