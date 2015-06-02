#! /usr/bin/env python
#
def leslie ( b, di, da ):

#*****************************************************************************80
#
## LESLIE returns the LESLIE matrix, for population dynamics.
#
#  Formula:
#
#    5/6 * ( 1.0 - DI )    0      B         0
#    1/6 * ( 1.0 - DI )  13/14    0         0
#        0                1/14  39/40       0
#        0                 0     1/40  9/10 * ( 1 - DA )
#
#  Discussion:
#
#    A human population is assumed to be grouped into the categories:
#
#      X(1) = between  0 and  5+
#      X(2) = between  6 and 19+
#      X(3) = between 20 and 59+
#      X(4) = between 60 and 69+
#
#    Humans older than 69 are ignored.  Deaths occur in the 60 to 69
#    year bracket at a relative rate of DA per year, and in the 0 to 5
#    year bracket at a relative rate of DI per year.  Deaths do not occurr
#    in the other two brackets.
#
#    Births occur at a rate of B relative to the population in the
#    20 to 59 year bracket.
#
#    Thus, given the population vector X in a given year, the population
#    in the next year will be A * X.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Ke Chen, Peter Giblin, Alan Irving,
#    Mathematical Explorations with MATLAB,
#    Cambridge University Press, 1999,
#    ISBN: 0-521-63920-4.
#
#  Parameters:
#
#    Input, real B, DI, DA, the birth rate, infant mortality rate,
#    and aged mortality rate.  These should be positive values.
#    The mortality rates must be between 0.0 and 1.0.  Reasonable
#    values might be B = 0.025, DI = 0.010, and DA = 0.100
#
#    Output, real A(4,4), the matrix.
#
  import numpy as np

  if ( b < 0.0 ):
    print ''
    print 'LESLIE - Fatal error!'
    print '  0 <= B is required.'
 
  if ( da < 0.0 or 1.0 < da ):
    print ''
    print 'LESLIE - Fatal error!'
    print '  0 <= DA <= 1.0 is required.'

  if ( di < 0.0 or 1.0 < di ):
    print ''
    print 'LESLIE - Fatal error!'
    print '  0 <= DI <= 1.0 is required.'

  a = np.zeros ( ( 4, 4, ) )

  a[0,0] = 5.0 * ( 1.0 - di ) / 6.0
  a[0,1] = 0.0
  a[0,2] = b
  a[0,3] = 0.0

  a[1,0] = ( 1.0 - di ) / 6.0
  a[1,1] = 13.0 / 14.0
  a[1,2] = 0.0
  a[1,3] = 0.0

  a[2,0] = 0.0
  a[2,1] = 1.0 / 14.0
  a[2,2] = 39.0 / 40.0
  a[2,3] = 0.0

  a[3,0] = 0.0
  a[3,1] = 0.0
  a[3,2] = 1.0 / 40.0
  a[3,3] = 9.0 * ( 1.0 - da ) / 10.0

  return a

def leslie_determinant ( b, di, da ):

#*****************************************************************************80
#
## LESLIE_DETERMINANT computes the determinant of the LESLIE matrix.
#
#  Discussion:
#
#    DETERM = a(4,4) * ( 
#        a(1,1) * a(2,2) * a(3,3)
#      + a(1,3) * a(2,1) * a(3,2) )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Output, real VALUE, the determinant.
#
#    Input, real B, DI, DA, the birth rate, infant mortality rate,
#    and aged mortality rate.  These should be positive values.
#    The mortality rates must be between 0.0 and 1.0.  Reasonable
#    values might be B = 0.025, DI = 0.010, and DA = 0.100
#
#    Output, real VALUE, the determinant.
#
  value = 9.0 * ( 1.0 - da ) / 10.0 * \
  ( \
      5.0 * ( 1.0 - di ) / 6.0 \
    * 13.0 / 14.0 \
    * 39.0 / 40.0 \
  +   b \
    * ( 1.0 - di ) / 6.0 \
    * 1.0 / 14.0 \
   )

  return value

def leslie_determinant_test ( ):

#*****************************************************************************80
#
## LESLIE_DETERMINANT_TEST tests LESLIE_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 February 2015
#
#  Author:
#
#    John Burkardt
#
  from leslie import leslie
  from r8mat_print import r8mat_print

  print ''
  print 'LESLIE_DETERMINANT_TEST'
  print '  LESLIE_DETERMINANT computes the LESLIE determinant.'

  m = 4
  n = m
 
  b =  0.025
  di = 0.010
  da = 0.100
  a = leslie ( b, di, da )

  r8mat_print ( m, n, a, '  LESLIE matrix:' )

  value = leslie_determinant ( b, di, da )

  print '  Value =  %g' % ( value )

  print ''
  print 'LESLIE_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def leslie_test ( ):

#*****************************************************************************80
#
## LESLIE_TEST tests LESLIE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 February 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'LESLIE_TEST'
  print '  LESLIE computes the LESLIE matrix.'

  m = 4
  n = m

  b =  0.025
  di = 0.010
  da = 0.100

  a = leslie ( b, di, da )
 
  r8mat_print ( m, n, a, '  LESLIE matrix:' )

  print ''
  print 'LESLIE_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  leslie_test ( )
  timestamp ( )
