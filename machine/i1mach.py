#!/usr/bin/env python
#
def i1mach ( i ):

#*****************************************************************************80
#
## I1MACH returns integer machine constants.
#
#  Discussion:
#
#    Input/output unit numbers.
#
#      I1MACH(1) = the standard input unit.
#      I1MACH(2) = the standard output unit.
#      I1MACH(3) = the standard punch unit.
#      I1MACH(4) = the standard error message unit.
#
#    Words.
#
#      I1MACH(5) = the number of bits per integer storage unit.
#      I1MACH(6) = the number of characters per integer storage unit.
#
#    Integers.
#
#    Assume integers are represented in the S digit base A form:
#
#      Sign * (X(S-1)*A^(S-1) + ... + X(1)*A + X(0))
#
#    where 0 <= X(1:S-1) < A.
#
#      I1MACH(7) = A, the base.
#      I1MACH(8) = S, the number of base A digits.
#      I1MACH(9) = A^S-1, the largest integer.
#
#    Floating point numbers
#
#    Assume floating point numbers are represented in the T digit
#    base B form:
#
#      Sign * (B^E) * ((X(1)/B) + ... + (X(T)/B^T) )
#
#    where 0 <= X(I) < B for I=1 to T, 0 < X(1) and EMIN <= E <= EMAX.
#
#      I1MACH(10) = B, the base.
#
#    Single precision
#
#      I1MACH(11) = T, the number of base B digits.
#      I1MACH(12) = EMIN, the smallest exponent E.
#      I1MACH(13) = EMAX, the largest exponent E.
#
#    Double precision
#
#      I1MACH(14) = T, the number of base B digits.
#      I1MACH(15) = EMIN, the smallest exponent E.
#      I1MACH(16) = EMAX, the largest exponent E.
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
#    1 <= I <= 16.
#
#    Output, integer VALUE, the value of the chosen parameter.
#
  if ( i < 1 ):
    print ''
    print 'I1MACH - Fatal error!'
    print '  The input argument I is out of bounds.'
    print '  Legal values satisfy 1 <= I <= 16.'
    print '  I =   %d' % ( i )
    sys.exit ( 'I1MACH - Fatal error!' )
  elif ( i == 1 ):
    value = 5
  elif ( i == 2 ):
    value = 6
  elif ( i == 3 ):
    value = 7
  elif ( i == 4 ):
    value = 6
  elif ( i == 5 ):
    value = 32
  elif ( i == 6 ):
    value = 4
  elif ( i == 7 ):
    value = 2
  elif ( i == 8 ):
    value = 31
  elif ( i == 9 ):
    value = 2147483647
  elif ( i == 10 ):
    value = 2
  elif ( i == 11 ):
    value = 24
  elif ( i == 12 ):
    value = -125
  elif ( i == 13 ):
    value = 128
  elif ( i == 14 ):
    value = 53
  elif ( i == 15 ):
    value = -1021
  elif ( i == 16 ):
    value = 1024
  elif ( 16 < i ):
    print ''
    print 'I1MACH - Fatal error!'
    print '  The input argument I is out of bounds.'
    print '  Legal values satisfy 1 <= I <= 16.'
    print '  I =   %d' % ( i )
    sys.exit ( 'I1MACH - Fatal error!' )

  return value

def i1mach_test ( ):

#*****************************************************************************80
#
## I1MACH_TEST reports the constants returned by I1MACH.
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
  print 'I1MACH_TEST'
  print '  I1MACH reports the value of constants associated'
  print '  with integer computer arithmetic.'

  print ''
  print '  Numbers associated with input/output units:'

  print ''
  print '  I1MACH(1) = the standard input unit.'
  print '  %d' % ( i1mach ( 1 ) )

  print ''
  print '  I1MACH(2) = the standard output unit.'
  print '  %d' % ( i1mach ( 2 ) )

  print ''
  print '  I1MACH(3) = the standard punch unit.'
  print '  %d' % ( i1mach ( 3 ) )

  print ''
  print '  I1MACH(4) = the standard error message unit.'
  print '  %d' % ( i1mach ( 4 ) )

  print ''
  print '  Numbers associated with words:'

  print ''
  print '  I1MACH(5) = the number of bits per integer.'
  print '  %d' % ( i1mach ( 5 ) )

  print ''
  print '  I1MACH(6) = the number of characters per integer.'
  print '  %d' % ( i1mach ( 6 ) )

  print ''
  print '  Numbers associated with integer values:'

  print ''
  print '  Assume integers are represented in the S digit'
  print '  base A form:'
  print ''
  print '    Sign * (X(S-1)*A^(S-1) + ... + X(1)*A + X(0))'
  print ''
  print '  where the digits X satisfy 0 <= X(1:S-1) < A.'

  print ''
  print '  I1MACH(7) = A, the base.'
  print '  %d' % ( i1mach ( 7 ) )

  print ''
  print '  I1MACH(8) = S, the number of base A digits.'
  print '  %d' % ( i1mach ( 8 ) )

  print ''
  print '  I1MACH(9) = A^S-1, the largest integer.'
  print '  %d' % ( i1mach ( 9 ) )

  print ''
  print '  Numbers associated with floating point values:'
  print ''
  print '  Assume floating point numbers are represented '
  print '  in the T digit base B form:'
  print ''
  print '    Sign * (B^E) * ((X(1)/B) + ... + (X(T)/B^T) )'
  print ''
  print '  where'
  print ''
  print '    0 <= X(1:T) < B,'
  print '    0 < X(1) (unless the value being represented is 0),'
  print '    EMIN <= E <= EMAX.'

  print ''
  print '  I1MACH(10) = B, the base.'
  print '  %d' % ( i1mach ( 10 ) )

  print ''
  print '  Numbers associated with single precision values:'
  print ''
  print '  I1MACH(11) = T, the number of base B digits.'
  print '  %d' % ( i1mach ( 11 ) )

  print ''
  print '  I1MACH(12) = EMIN, the smallest exponent E.'
  print '  %d' % ( i1mach ( 12 ) )

  print ''
  print '  I1MACH(13) = EMAX, the largest exponent E.'
  print '  %d' % ( i1mach ( 13 ) )

  print ''
  print '  Numbers associated with double precision values:'
  print ''
  print '  I1MACH(14) = T, the number of base B digits.'
  print '  %d' % ( i1mach ( 14 ) )

  print ''
  print '  I1MACH(15) = EMIN, the smallest exponent E.'
  print '  %d' % ( i1mach ( 15 ) )

  print ''
  print '  I1MACH(16) = EMAX, the largest exponent E.'
  print '  %d' % ( i1mach ( 16 ) )

  print ''
  print 'I1MACH_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i1mach_test ( )
  timestamp ( )
