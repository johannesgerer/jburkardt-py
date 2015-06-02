#!/usr/bin/env python

def i4_gcdb ( i, j, k ) :

#*****************************************************************************80
#
## I4_GCDB finds the greatest common divisor of the form K^N of two numbers.
#
#  Discussion:
#
#    Note that if J is negative, I4_GCDB will also be negative.
#    This is because it is likely that the caller is forming
#    the fraction I/J, and so any minus sign should be
#    factored out of J.
#
#    If I and J are both zero, I4_GCDB is returned as 1.
#
#    If I is zero and J is not, I4_GCDB is returned as J,
#    and vice versa.
#
#    If I and J are nonzero, and have no common divisor of the
#    form K**N, I4_GCDB is returned as 1.
#
#    Otherwise, I4_GCDB is returned as the largest common divisor
#    of the form K**N shared by I and J.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer I, J, two numbers whose greatest common divisor K**N
#    is desired.
#
#    Input, integer K, the possible divisor of I and J.
#
#    Output, integer VALUE, the greatest common divisor of
#    the form K^N shared by I and J.
#
  value = 1
#
#  If both I and J are zero, I4_GCDB is 1.
#
  if ( i == 0 and j == 0 ):
    value = 1
    return value
#
#  If just one of I and J is zero, I4_GCDB is the other one.
#
  if ( i == 0 ):
    value = j
    return value
  elif ( j == 0 ):
    value = i
    return value
#
#  Divide out K as long as you can.
#
  if ( 0 < j ):
    value = 1
  else:
    value = -1

  while ( True ):

    if ( ( i % k ) != 0 or ( j % k ) != 0 ):
      break

    value = value * k
    i = i // k
    j = j // k

  return value

def i4_gcdb_test ( ):

#*****************************************************************************80
#
## I4_GCDB_TEST tests I4_GCDB.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  test_num = 4

  i_test = np.array ( [ 288, 288, 288, 288 ] )
  j_test = np.array ( [ 2880, 2880, 2880, 2880 ] )
  k_test = np.array ( [ 2, 3, 4, 5 ] )

  print ''
  print 'I4_GCDB_TEST'
  print '  I4_GCDB computes the greatest common factor'
  print '  of the form K^N.'
  print 
  print '       I       J       K    I4_GCDB'
  print ''
 
  for test in range ( 0, test_num ):
    i = i_test[test]
    j = j_test[test]
    k = k_test[test]
    l = i4_gcdb ( i, j, k )
    print '  %6d  %6d  %6d  %6d' % ( i, j, k, l )
#
#  Terminate.
#
  print ''
  print 'I4_GCDB_TEST'
  print '  Normal end of execution'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_gcdb_test ( )
  timestamp ( )
