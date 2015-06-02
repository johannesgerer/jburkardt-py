#!/usr/bin/env python
#
def r1mach ( i ):

#*****************************************************************************80
#
## R1MACH returns single precision real machine constants.
#
#  Discussion:
#
#    Assume that single precision real numbers are stored with a mantissa
#    of T digits in base B, with an exponent whose value must lie
#    between EMIN and EMAX.  Then for values of I between 1 and 5,
#    R1MACH will return the following values:
#
#      R1MACH(1) = B^(EMIN-1), the smallest positive magnitude.
#      R1MACH(2) = B^EMAX*(1-B^(-T)), the largest magnitude.
#      R1MACH(3) = B^(-T), the smallest relative spacing.
#      R1MACH(4) = B^(1-T), the largest relative spacing.
#      R1MACH(5) = log10(B)
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
    print 'R1MACH - Fatal error!'
    print '  The input argument I is out of bounds.'
    print '  Legal values satisfy 1 <= I <= 5.'
    print '  I = %d' % ( i )
    sys.exit ( 'R1MACH - Fatal error!' )
  elif ( i == 1 ):
    value = 1.1754944E-38
  elif ( i == 2 ):
    value = 3.4028235E+38
  elif ( i == 3 ):
    value = 5.9604645E-08
  elif ( i == 4 ):
    value = 1.1920929E-07
  elif ( i == 5 ):
    value = 0.3010300
  elif ( 5 < i ):
    print ''
    print 'R1MACH - Fatal error!'
    print '  The input argument I is out of bounds.'
    print '  Legal values satisfy 1 <= I <= 5.'
    print '  I = %d' % ( i )
    sys.exit ( 'R1MACH - Fatal error!' )

  return value

def r1mach_test ( ):

#*****************************************************************************80
#
## R1MACH_TEST reports the constants returned by R1MACH.
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
  print 'R1MACH_TEST'
  print '  R1MACH reports the value of constants associated'
  print '  with real single precision computer arithmetic.'

  print ''
  print '  Assume that single precision numbers are stored '
  print '  with a mantissa of T digits in base B, with an '
  print '  exponent whose value must lie between EMIN and EMAX.'

  print ''
  print '  For input arguments of 1 <= I <= 5,'
  print '  R1MACH will return the following values:'

  print ''
  print '  R1MACH(1) = B^*(EMIN-1), the smallest positive magnitude.'
  print '  %26.16e' % ( r1mach ( 1 ) )

  print ''
  print '  R1MACH(2) = B^EMAX*(1-B^(-T)), the largest magnitude.'
  print '  %26.16e' % ( r1mach ( 2 ) )

  print ''
  print '  R1MACH(3) = B^(-T), the smallest relative spacing.'
  print '  %26.16e' % ( r1mach ( 3 ) )

  print ''
  print '  R1MACH(4) = B^(1-T), the largest relative spacing.'
  print '  %26.16e' % ( r1mach ( 4 ) )

  print ''
  print '  R1MACH(5) = log10(B).'
  print '  %26.16e' % ( r1mach ( 5 ) )

  print ''
  print 'R1MACH_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r1mach_test ( )
  timestamp ( )
