#! /usr/bin/env python
#
def cpv ( f, a, b, n ):

#*****************************************************************************80
#
## CPV estimates the Cauchy Principal Value of an integral.
#
#  Location:
#
#    http://people.sc.fsu.edu/~jburkardt/f_src/cauchy_principal_value/cpv.f90
#
#  Discussion:
#
#    This function can be used to estimate the Cauchy Principal Value of
#    a singular integral of the form 
#      Integral f(t)/(t-x) dt 
#    over an interval which includes the singularity point t=x.
#
#    Isolate the singularity at x in a symmetric interval of finite size delta:
#
#        CPV ( Integral ( a         <= t <= b         ) p(t) / ( t - x ) dt )
#      =       Integral ( a         <= t <= x - delta ) p(t) / ( t - x ) dt
#      + CPV ( Integral ( x - delta <= t <= x + delta ) p(t) / ( t - x ) dt )
#      +       Integral ( x + delta <= t <= b         ) p(t) / ( t - x ) dt.
#
#    We assume the first and third integrals can be handled in the usual way.
#    The second integral can be rewritten as
#      Integral ( -1 <= s <= +1 ) ( p(s*delta+x) - p(x) ) / s ds
#    and approximated by
#      Sum ( 1 <= i <= N ) w(i) * ( p(xi*delta+x) - p(x) ) / xi(i)
#    = Sum ( 1 <= i <= N ) w(i) * ( p(xi*delta+x) ) / xi(i)
#    if we assume that N is even, so that coefficients of p(x) sum to zero.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Julian Noble,
#    Gauss-Legendre Principal Value Integration,
#    Computing in Science and Engineering,
#    Volume 2, Number 1, January-February 2000, pages 92-95.
#
#  Parameters:
#
#    Input, real F ( X ), the function that evaluates the
#    integrand.
#
#    Input, real A, B, the endpoints of the symmetric interval, 
#    which contains a singularity of the form 1/(X-(A+B)/2).
#
#    Input, integer N, the number of Gauss points to use.
#    N must be even.
#
#    Output, real VALUE, the estimate for the Cauchy Principal Value.
#
  from legendre_set import legendre_set
  from sys import exit
#
#  N must be even.
#
  if ( ( n % 2 ) != 0 ):
    print ''
    print 'CPV - Fatal error!'
    print '  N must be even.'
    exit ( 'CPV - Fatal error.' )
#
#  Get the Gauss-Legendre rule.
#
  [ x, w ] = legendre_set ( n );
#
#  Estimate the integral.
#
  value = 0.0;
  for i in range ( 0, n ):
    x2 = ( ( 1.0 - x[i] ) * a   \
         + ( 1.0 + x[i] ) * b ) \
         /   2.0
    value = value + w[i] * ( f ( x2 ) ) / x[i]

  return value

def cpv_test01 ( ):

#*****************************************************************************80
#
## CPV_TEST01 seeks the CPV of Integral ( -1 <= t <= 1 ) exp(t) / t dt
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 April 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'CPV_TEST01:'
  print '  CPV of Integral ( -1 <= t <= 1 ) exp(t) / t dt'

  print ''
  print '   N           Estimate             Error'
  print ''

  exact = 2.11450175075
  a = -1.0
  b = +1.0
  for n in range ( 2, 10, 2 ):
    value = cpv ( f01, a, b, n )
    print '  %2d  %24.16g  %14.6g' % ( n, value, abs ( value - exact ) )

  return

def f01 ( t ):

#*****************************************************************************80
#
## F01 evaluates the integrand of Integral ( -1 <= t <= 1 ) exp(t) / t dt
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real T, the argument.
#
#    Output, real VALUE, the value of the integrand.
#
  import numpy as np

  value = np.exp ( t )

  return value

def cpv_test02 ( ):

#*****************************************************************************80
#
## CPV_TEST02 is another test.
#
#  Discussion:
#
#    We seek
#      CPV ( Integral ( 1-delta <= t <= 1+delta ) 1/(1-t)^3 dt )
#    which we must rewrite as
#      CPV ( Integral ( 1-delta <= t <= 1+delta ) 1/(1+t+t^2) 1/(1-t) dt )
#    so that our "integrand" is 1/(1+t+t^2).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 April 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ''
  print 'CPV_TEST02:'
  print '  Compute CPV ( Integral ( 1-delta <= t <= 1+delta ) 1/(1-t)^3 dt )'
  print '  Try this for delta = 1, 1/2, 1/4.'
  print ''
  print '   N          Estimate                  Exact                  Error'

  delta = 1.0

  for k in range ( 0, 3 ):
    print ''
    r1 = (   delta + 1.5 ) ** 2 + 0.75
    r2 = ( - delta + 1.5 ) ** 2 + 0.75
    r3 = np.arctan ( np.sqrt ( 0.75 ) / (   delta + 1.5 ) )
    r4 = np.arctan ( np.sqrt ( 0.75 ) / ( - delta + 1.5 ) )
    exact = - np.log ( r1 / r2 ) / 6.0 + ( r3 - r4 ) / np.sqrt ( 3.0 )
    for n in range ( 2, 10, 2 ):
      a = 1.0 - delta
      b = 1.0 + delta
      value = cpv ( f02, a, b, n )
      print '  %2d  %24.16g  %24.16g %14.6g' \
        % ( n, value, exact, abs ( value - exact ) )

    delta = delta / 2.0

  return

def f02 ( t ):

#*****************************************************************************80
#
## F02: integrand of Integral ( 1-delta <= t <= 1+delta ) 1/(1-t^3) dt
#
#  Discussion:
#
#    1/(1-t^3) = 1/(1+t+t^2) * 1/(1-t)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
  value = 1.0 / ( 1.0 + t + t * t )

  return value

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  cpv_test01 ( )
  cpv_test02 ( )
  timestamp ( )
