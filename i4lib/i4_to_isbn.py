#!/usr/bin/env python

def i4_to_isbn ( i ) :

#*****************************************************************************80
#
## I4_TO_ISBN converts an I4 to an ISBN digit.
#
#  Discussion:
#
#    Only the integers 0 through 10 can be input.  The representation
#    of 10 is 'X'.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Book Industry Study Group,
#    The Evolution in Product Identification:
#    Sunrise 2005 and the ISBN-13,
#    http://www.bisg.org/docs/The_Evolution_in_Product_ID.pdf
#
#  Parameters:
#
#    Input, integer I, an integer between 0 and 10.
#
#    Output, character VALUE, the ISBN character code of the integer.
#    If I is illegal, then VALUE is set to '?'.
#
  if ( i == 0 ):
    value = '0'
  elif ( i == 1 ):
    value = '1'
  elif ( i == 2 ):
    value = '2'
  elif ( i == 3 ):
    value = '3'
  elif ( i == 4 ):
    value = '4'
  elif ( i == 5 ):
    value = '5'
  elif ( i == 6 ):
    value = '6'
  elif ( i == 7 ):
    value = '7'
  elif ( i == 8 ):
    value = '8'
  elif ( i == 9 ):
    value = '9'
  elif ( i == 10 ):
    value = 'X'
  else:
    value = '?'

  return value

def i4_to_isbn_test ( ):

#*****************************************************************************80
#
## I4_TO_ISBN_TEST tests I4_TO_ISBN. 
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 May 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'I4_TO_ISBN_TEST'
  print '  I4_TO_ISBN converts an I4 digit to an ISBN symbol.'
  print ''
  print '  I4   S'
  print ''

  for i4 in range ( 0, 11 ):

    s1 = i4_to_isbn ( i4 )
    print '  %2d   %c' % ( i4, s1 )
#
#  Terminate.
#
  print ''
  print 'I4_TO_ISBN_TEST'
  print '  Normal end of execution.'

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_to_isbn_test ( )
  timestamp ( )
