#!/usr/bin/env python
#
def r8_hyper_2f1 ( a, b, c, x ):

#*****************************************************************************80
#
## R8_HYPER_2F1 evaluates the hypergeometric function F(A,B,C,X).
#
#  Discussion:
#
#    A minor bug was corrected.  The HW variable, used in several places as
#    the "old" value of a quantity being iteratively improved, was not
#    being initialized.  JVB, 11 February 2008.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    28 February 2015
#
#  Author:
#
#    Original FORTRAN77 version by Shanjie Zhang, Jianming Jin.
#    Python version by John Burkardt.
#
#    The F77 original version of this routine is copyrighted by
#    Shanjie Zhang and Jianming Jin.  However, they give permission to
#    incorporate this routine into a user program provided that the copyright
#    is acknowledged.
#
#  Reference:
#
#    Shanjie Zhang, Jianming Jin,
#    Computation of Special Functions,
#    Wiley, 1996,
#    ISBN: 0-471-11963-6,
#    LC: QA351.C45
#
#  Parameters:
#
#    Input, real A, B, C, X, the arguments of the function.
#    C must not be equal to a nonpositive integer.
#    X < 1.
#
#    Output, real VALUE, the value of the function.
#
  import numpy as np
  from r8_gamma import r8_gamma
  from r8_psi import r8_psi

  el = 0.5772156649015329

  l0 = ( c == int ( c ) ) and ( c < 0.0 )
  l1 = ( 1.0 - x < 1.0E-15 ) and ( c - a - b <= 0.0 )
  l2 = ( a == int ( a ) ) and ( a < 0.0 )
  l3 = ( b == int ( b ) ) and ( b < 0.0 )
  l4 = ( c - a == int ( c - a ) ) and ( c - a <= 0.0 )
  l5 = ( c - b == int ( c - b ) ) and ( c - b <= 0.0 )

  if ( l0 ):
    print ''
    print 'R8_HYPER_2F1 - Fatal error!'
    print '  The hypergeometric series is divergent.'
    print '  C is integral and negative.'
    print '  C = %f' % ( c )

  if ( l1 ):
    print ''
    print 'R8_HYPER_2F1 - Fatal error!'
    print '  The hypergeometric series is divergent.'
    print '  1 = X < 0, C - A - B <= 0.'
    print '  A = %f' % ( a )
    print '  B = %f' % ( b )
    print '  C = %f' % ( c )
    print '  X = %f' % ( x )

  if ( 0.95 < x ):
    eps = 1.0E-08
  else:
    eps = 1.0E-15

  if ( x == 0.0 or a == 0.0 or b == 0.0 ):

    value = 1.0
    return value

  elif ( 1.0 - x == eps and 0.0 < c - a - b ):

    gc = r8_gamma ( c )
    gcab = r8_gamma ( c - a - b )
    gca = r8_gamma ( c - a )
    gcb = r8_gamma ( c - b )
    value = gc * gcab / ( gca * gcb )
    return value

  elif ( 1.0 + x <= eps and abs ( c - a + b - 1.0 ) <= eps ):

    g0 = np.sqrt ( np.pi ) * 2.0 ** ( - a )
    g1 = r8_gamma ( c )
    g2 = r8_gamma ( 1.0 + a / 2.0 - b )
    g3 = r8_gamma ( 0.5 + 0.5 * a )
    value = g0 * g1 / ( g2 * g3 )
    return value

  elif ( l2 or l3 ):

    if ( l2 ):
      nm = int ( abs ( a ) )

    if ( l3 ):
      nm = int ( abs ( b ) )

    value = 1.0
    r = 1.0

    for k in range ( 1, nm + 1 ):
      r = r * ( a + float ( k ) - 1.0 ) * ( b + float ( k ) - 1.0 ) \
        / ( float ( k ) * ( c + float ( k ) - 1.0 ) ) * x
      value = value + r

    return value

  elif ( l4 or l5 ):

    if ( l4 ):
      nm = int ( abs ( c - a ) )
 
    if ( l5 ):
      nm = int ( abs ( c - b ) )

    value = 1.0
    r  = 1.0
    for k in range ( 1, nm + 1 ):
      r = r * ( c - a + float ( k ) - 1.0 ) * ( c - b + float ( k ) - 1.0 ) \
        / ( float ( k ) * ( c + float ( k ) - 1.0 ) ) * x
      value = value + r
    value = ( 1.0 - x ) ** ( c - a - b ) * hf
    return value

  aa = a
  bb = b
  x1 = x

  if ( x < 0.0 ):
    x = x / ( x - 1.0 )
    if ( a < c and b < a and 0.0 < b ):
      a = bb
      b = aa
    b = c - b

  if ( 0.75 <= x ):

    gm = 0.0

    if ( abs ( c - a - b - int ( c - a - b ) ) < 1.0E-15 ):

      m = int ( c - a - b )
      ga = r8_gamma ( a )
      gb = r8_gamma ( b )
      gc = r8_gamma ( c )
      gam = r8_gamma ( a + float ( m ) )
      gbm = r8_gamma ( b + float ( m ) )

      pa = r8_psi ( a )
      pb = r8_psi ( b )

      if ( m != 0 ):
        gm = 1.0

      for j in range ( 1, abs ( m ) ):
        gm = gm * float ( j )

      rm = 1.0
      for j in range ( 1, abs ( m ) + 1 ):
        rm = rm * float ( j )
 
      f0 = 1.0
      r0 = 1.0
      r1 = 1.0
      sp0 = 0.0
      sp = 0.0

      if ( 0 <= m ):

        c0 = gm * gc / ( gam * gbm )
        c1 = - gc * ( x - 1.0 ) ** m / ( ga * gb * rm )

        for k in range ( 1, m ):
          r0 = r0 * ( a + float ( k ) - 1.0 ) * ( b + float ( k ) - 1.0 ) \
            / float ( k * ( k - m ) ) * ( 1.0 - x )
          f0 = f0 + r0
 
        for k in range ( 1, m + 1 ):
          sp0 = sp0 + 1.0 / ( a + float ( k ) - 1.0 ) \
            + 1.0 / ( b + float ( k ) - 1.0 ) - 1.0 / float ( k )

        f1 = pa + pb + sp0 + 2.0 * el + np.log ( 1.0 - x )
        hw = f1

        for k in range ( 1, 251 ):

          sp = sp + ( 1.0 - a ) / ( float ( k ) * ( a + float ( k ) - 1.0 ) ) \
            + ( 1.0 - b ) / ( float ( k ) * ( b + float ( k ) - 1.0 ) )

          sm = 0.0
          for j in range ( 1, m + 1 ):
            sm = sm + ( 1.0 - a ) \
              / ( float ( j + k ) * ( a + float ( j + k ) - 1.0 ) ) \
              + 1.0 / ( b + float ( j + k ) - 1.0 )

          rp = pa + pb + 2.0 * el + sp + sm + np.log ( 1.0 - x )

          r1 = r1 * ( a + m + float ( k ) - 1.0 ) * ( b + m + float ( k ) - 1.0 ) \
            / ( float ( k ) * float ( m + k ) ) * ( 1.0 - x )

          f1 = f1 + r1 * rp

          if ( abs ( f1 - hw ) < abs ( f1 ) * eps ):
            break
 
          hw = f1

        value = f0 * c0 + f1 * c1

      elif ( m < 0 ):

        m = - m
        c0 = gm * gc / ( ga * gb * ( 1.0 - x ) ** m )
        c1 = - ( - 1 ) ** m * gc / ( gam * gbm * rm )

        for k in range ( 1, m ):
          r0 = r0 * ( a - float ( m ) + float ( k ) - 1.0 ) \
            * ( b - float ( m ) + float ( k ) - 1.0 ) \
            / ( float ( k ) * float ( k - m ) ) * ( 1.0 - x )
          f0 = f0 + r0

        for k in range ( 1, m + 1 ):
          sp0 = sp0 + 1.0 / float ( k )

        f1 = pa + pb - sp0 + 2.0 * el + np.log ( 1.0 - x )
        hw = f1

        for k in range ( 1, 251 ):

          sp = sp + ( 1.0 - a ) \
            / ( float ( k ) * ( a + float ( k ) - 1.0 ) ) \
            + ( 1.0 - b ) / ( float ( k ) * ( b + float ( k ) - 1.0 ) )

          sm = 0.0
          for j in range ( 1, m + 1 ):
            sm = sm + 1.0 / float ( j + k )

          rp = pa + pb + 2.0 * el + sp - sm + np.log ( 1.0 - x )

          r1 = r1 * ( a + float ( k ) - 1.0 ) * ( b + float ( k ) - 1.0 ) \
            / float ( k * ( m + k ) ) * ( 1.0 - x )

          f1 = f1 + r1 * rp

          if ( abs ( f1 - hw ) < abs ( f1 ) * eps ):
            break

          hw = f1

        value = f0 * c0 + f1 * c1

    else:

      ga = r8_gamma ( a )
      gb = r8_gamma ( b )
      gc = r8_gamma ( c )
      gca = r8_gamma ( c - a )
      gcb = r8_gamma ( c - b )
      gcab = r8_gamma ( c - a - b )
      gabc = r8_gamma ( a + b - c )
      c0 = gc * gcab / ( gca * gcb )
      c1 = gc * gabc / ( ga * gb ) * ( 1.0 - x ) ** ( c - a - b )
      value = 0.0
      hw = value
      r0 = c0
      r1 = c1

      for k in range ( 1, 251 ):

        r0 = r0 * ( a + float ( k ) - 1.0 ) * ( b + float ( k ) - 1.0 ) \
          / ( float ( k ) * ( a + b - c + float ( k ) ) ) * ( 1.0 - x )

        r1 = r1 * ( c - a + float ( k ) - 1.0 ) \
          * ( c - b + float ( k ) - 1.0 ) \
          / ( float ( k ) * ( c - a - b + float ( k ) ) ) * ( 1.0 - x )

        value = value + r0 + r1

        if ( abs ( value - hw ) < abs ( value ) * eps ):
          break

        hw = value

      value = value + c0 + c1

  else:

    a0 = 1.0

    if ( a < c and c < 2.0 * a and b < c and c < 2.0 * b ):

      a0 = ( 1.0 - x ) ** ( c - a - b )
      a = c - a
      b = c - b

    value = 1.0
    hw = value
    r = 1.0

    for k in range ( 1, 251 ):

      r = r * ( a + float ( k ) - 1.0 ) * ( b + float ( k ) - 1.0 ) \
        / ( k * ( c + float ( k ) - 1.0 ) ) * x

      value = value + r

      if ( abs ( value - hw ) <= abs ( value ) * eps ):
        break

      hw = value

    value = a0 * value

  if ( x1 < 0.0 ):
    x = x1
    c0 = 1.0 / ( 1.0 - x ) ** aa
    value = c0 * value

  if ( 120 < k ):
    print ''
    print 'R8_HYPER_2F1 - Warning!'
    print '  A large number of iterations were needed.'
    print '  The accuracy of the results should be checked.'

  return value

def r8_hyper_2f1_test ( ):

#*****************************************************************************80
#
## R8_HYPER_2F1_TEST tests R8_HYPER_2F1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from hyper_2f1_values import hyper_2f1_values

  print ''
  print 'R8_HYPER_2F1_TEST'
  print '  R8_HYPER_2F1 evaluates the hypergeometric 2F1 function.'
  print ''
  print '      A       B       C       X      ',
  print ' 2F1                       2F1                     DIFF'
  print '                                     '
  print '(tabulated)               (computed)'
  print ''

  n_data = 0

  while ( True ):

    [ n_data, a, b, c, x, fx1 ] = hyper_2f1_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_hyper_2f1 ( a, b, c, x )
 
    diff = abs ( fx1 - fx2 )
    print '  %6g  %6g  %6g  %6g  %24g  %24g  %10g' \
      % ( a, b, c, x, fx1, fx2, diff )

  print ''
  print 'R8_HYPER_2F1_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_hyper_2f1_test ( )
  timestamp ( )
