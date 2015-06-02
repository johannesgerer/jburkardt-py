#! /usr/bin/env python
#
def i4vec_index ( n, a, aval ):

#*****************************************************************************80
#
## I4VEC_INDEX returns the location of the first occurrence of a given value.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of entries in the vector.
#
#    Input, integer A(N), the vector to be searched.
#
#    Input, integer AVAL, the value to be indexed.
#
#    Output, integer VALUE, the first location in A which has the
#    value AVAL, or -1 if no such index exists.
#
  value = -1

  for i in range ( 0, n ):
    if ( a[i] == aval ):
      value = i
      break

  return value

def i4vec_index_test ( ):

#*****************************************************************************80
#
## I4VEC_INDEX_TEST tests I4VEC_INDEX;
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 May 2015
#
#  Author:
#
#    John Burkardt
#
  from i4vec_print import i4vec_print
  from i4vec_uniform_ab import i4vec_uniform_ab

  n = 10

  print ''
  print 'I4VEC_INDEX_TEST'
  print '  For an integer vector:'
  print '  I4VEC_INDEX:              first index of given value;'

  seed = 123456789
  i4_lo = -n
  i4_hi = n

  a, seed = i4vec_uniform_ab ( n, i4_lo, i4_hi, seed );

  i4vec_print ( n, a, '  Input vector:' )

  i = ( n // 2 )
  aval = a[i]

  print ''
  j = i4vec_index ( n, a, aval )
  print '  Index of first occurrence of %d is %d' % ( aval, j )

  aval = aval + 1
  j = i4vec_index ( n, a, aval )
  print '  Index of first occurrence of %d is %d' % ( aval, j )
#
#  Terminate.
#
  print ''
  print 'I4VEC_INDEX_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4vec_index_test ( )
  timestamp ( )

