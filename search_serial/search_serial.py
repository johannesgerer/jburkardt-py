#!/usr/bin/env python
#

#*****************************************************************************80

def search_serial ( a, b, c ):

#*****************************************************************************80
#
## SEARCH_SERIAL searches for a solution to an integer equation.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 October 2012
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer A, the lower limit of the search.
#
#    Input, integer B, the upper limit of the search.
#
#    Input, integer C, the desired value.
#
#    Output, integer J, is:
#    -1, if no solution could be found.
#    otherwise, F(J) = C and A <= J <= B.
#
  from time import time, ctime

  print ctime ( time ( ) )
  print ""
  print "SEARCH_SERIAL:"
  print "  PYTHON version"
  print "  Search the integers from A to B"
  print "  for a value J such that F(J) = C."
  print ""
  print "  A        = ", a
  print "  B        = ", b
  print "  C        = ", c

  wtime = time ( )

  j = search ( a, b, c )

  wtime = time ( ) - wtime
 
  print ""
  if j == -1:
    print "  No solution was found."
  else:
    print "  Found J = ", j
    print "  Verify F(J) = ", f ( j )
  
  print "  Time     = ", wtime
#
#  Terminate.
#
  print ""
  print "SEARCH_SERIAL:"
  print "  Normal end of execution."
  print ""
  print ( ctime ( time ( ) ) )

  return j

#*****************************************************************************80

def search ( a, b, c ):

#*****************************************************************************80
#
## SEARCH searches integers in [A,B] for a J so that F(J) = C.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 October 2012
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer A, B, the search range.
#
#    Input, integer C, the desired function value.
#
#    Output, integer J, the computed solution, or -1
#    if no solution was found.
#
  for i in range ( a, b + 1 ):

    if ( f ( i ) == c ):
      return i

  return ( - 1 )

#*****************************************************************************80

def f ( i ):

#*****************************************************************************80
#
## F is the function we are analyzing.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 October 2012
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer I, the argument.
#
#    Input, integer VALUE, the value.
#
  from math import floor

  i4_huge = 2147483647;

  value = i;

  for j in range ( 0, 5 ):

    k = floor ( value / 127773 )

    value = 16807 * ( value - k * 127773 ) - k * 2836

    if ( value <= 0 ):
      value = value + i4_huge

  return value

#*****************************************************************************80

search_serial ( 1,               10000, 45 )
search_serial ( 1,              100000, 45 )
search_serial ( 1,             1000000, 45 )
search_serial ( 1674924000, 1674924999, 45 )
