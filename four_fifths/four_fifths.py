#! /usr/bin/env python
#
def four_fifths ( n ):

#*****************************************************************************80
#
## FOUR_FIFTHS searches for a solution to the four fifths problem.
#
#  Discussion:
#
#    Euler conjectured that a fifth power cannot be represented as
#    the sum of less than 5 fifth powers.
#
#    The correct equation is:
#
#      27^5 + 84^5 + 110^5 + 133^5 = 144^5 = 61917364224
#
#    Note that this script does NOT work on the SC system, presumably
#    because our Python is out of date, or we don't have the itertools
#    package.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    19 December 2014
#
#  Author:
#
#    Brian Hayes
#
#  Reference:
#
#    Brian Hayes,
#    Four Fifths = A Fifth
#    http://bit-player.org/
#    Posted on 03 December 2014.
#
#  Parameters:
#
#    Input, integer N, the upper limit for the range of integers to search.
#
  import itertools as it

  """Return smallest positive integers ((a,b,c,d),e) such that
     a^5 + b^5 + c^5 + d^5 = e^5; if no such tuple exists
     with e < n, return the string 'Failed'."""

  fifths = [ x**5 for x in range(n) ]

  combos = it.combinations_with_replacement ( range(1,n), 4 )

  while True:
    try:
      cc = combos.next()
      cc_sum = sum ( [fifths[i] for i in cc] )
      if cc_sum in fifths:
        return ( cc, fifths.index(cc_sum) )
    except StopIteration:
      return ( 'Failed' )

def four_fifths_test ( ):

#*****************************************************************************80
#
## FOUR_FIFTHS_TEST tests FOUR_FIFTHS.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    20 December 2014
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'FOUR_FIFTHS_TEST'
  print '  FOUR_FIFTHS seeks a solution of the four fifths problem:'
  print '  find integers a, b, c, d and e such that'
  print '    a^5 + b^5 + c^5 + d^5 = e^5.'

  n = 150
  cc, index = four_fifths ( n )
  
  print ''
  print '  Result:'
  print '  %d^5  + %d^5  + %d^5  + %d^5  = %d^5' % ( cc[0], cc[1], cc[2], cc[3], index )

  print ''
  print 'FOUR_FIFTHS_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  four_fifths_test ( )
  timestamp ( )
