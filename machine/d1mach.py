#!/usr/bin/env python
#
def d1mach ( i ):

#*****************************************************************************80
#
## D1MACH returns double precision real machine constants.
#
#  Discussion:
#
#    Assume that double precision real numbers are stored with a mantissa
#    of T digits in base B, with an exponent whose value must lie
#    between EMIN and EMAX.  Then for values of I between 1 and 5,
#    D1MACH will return the following values:
#
#      D1MACH(1) = B^(EMIN-1), the smallest positive magnitude.
#      D1MACH(2) = B^EMAX*(1-B^(-T)), the largest magnitude.
#      D1MACH(3) = B^(-T), the smallest relative spacing.
#      D1MACH(4) = B^(1-T), the largest relative spacing.
#      D1MACH(5) = log10(B)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 April 2015
#
#  Author:
#
#    Original FORTRAN77 version by Phyllis Fox, Andrew Hall, Norman Schryer
#    Python version by John Burkardt.
#
#  Reference:
#
#    Phyllis Fox, Andrew Hall, Norman Schryer,
#    Algorithm 528,
#    Framework for a Portable Library,
#    ACM Transactions on Mathematical Software,
#    Volume 4, Number 2, June 1978, page 176-188.
#
#  Parameters:
#
#    Input, integer I, chooses the parameter to be returned.
#    1 <= I <= 5.
#
#    Output, real VALUE, the value of the chosen parameter.
#
  if ( i < 1 ):
    print ''
    print 'D1MACH - Fatal error!'
    print '  The input argument I is out of bounds.'
    print '  Legal values satisfy 1 <= I <= 5.'
    print '  I = %d' % ( i )
    sys.exit ( 'D1MACH - Fatal error!' )
  elif ( i == 1 ):
    value = 1.112536929253601E-308
  elif ( i == 2 ):
    value = 4.494232837155789E+307
  elif ( i == 3 ):
    value = 1.110223024625157E-016
  elif ( i == 4 ):
    value = 2.220446049250313E-016
  elif ( i == 5 ):
    value = 0.301029995663981
  elif ( 5 < i ):
    print ''
    print 'D1MACH - Fatal error!'
    print '  The input argument I is out of bounds.'
    print '  Legal values satisfy 1 <= I <= 5.'
    print '  I = %d' % ( i )
    sys.exit ( 'D1MACH - Fatal error!' )

  return value

def d1mach_test ( ):

#*****************************************************************************80
#
## D1MACH_TEST reports the constants returned by D1MACH.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 April 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'D1MACH_TEST'
  print '  D1MACH reports the value of constants associated'
  print '  with real double precision computer arithmetic.'

  print ''
  print '  Assume that double precision numbers are stored '
  print '  with a mantissa of T digits in base B, with an'
  print '  exponent whose value must lie between EMIN and EMAX.'

  print ''
  print '  For input arguments of 1 <= I <= 5,'
  print '  D1MACH will return the following values:'

  print ''
  print '  D1MACH(1) = B^*(EMIN-1), the smallest positive magnitude.'
  print '  %26.16e' % ( d1mach ( 1 ) )

  print ''
  print '  D1MACH(2) = B^EMAX*(1-B^(-T)), the largest magnitude.'
  print '  %26.16e' % ( d1mach ( 2 ) )

  print ''
  print '  D1MACH(3) = B^(-T), the smallest relative spacing.'
  print '  %26.16e' % ( d1mach ( 3 ) )

  print ''
  print '  D1MACH(4) = B^(1-T), the largest relative spacing.'
  print '  %26.16e' % ( d1mach ( 4 ) )

  print ''
  print '  D1MACH(5) = log10(B).'
  print '  %26.16e' % ( d1mach ( 5 ) )

  print ''
  print 'D1MACH_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  d1mach_test ( )
  timestamp ( )
