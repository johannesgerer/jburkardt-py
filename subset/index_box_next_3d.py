#! /usr/bin/env python
#
def index_box_next_3d ( n1, n2, n3, i, j, k, more ):

#*****************************************************************************80
#
## INDEX_BOX_NEXT_3D produces index vectors on the surface of a box in 3D.
#
#  Discussion:
#
#    The index vectors are exactly those which are between (1,1,1) and
#    (N1,N2,N3) with the property that at least one of I, J, and K
#    is an "extreme" value.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N1, N2, N3, the "dimensions" of the box, that is, the
#    maximum values allowed for I, J and K.  The minimum values are
#    assumed to be 1.
#
#    Input, integer I, J, K, the previous index set.  However, on
#    first call, with MORE = FALSE, the input values of I, J and K are not needed.
#
#    Input, logical MORE, is set to FALSE on the first call, and should be
#    TRUE thereafter.
#
#    Output, integer I, J, K, the next index set.
#
#    Output, logical MORE, is TRUE if there are more index sets available.
#
  if ( not more ):
    more = True
    i = 1
    j = 1
    k = 1
    return i, j, k, more

  if ( i == n1 and j == n2 and k == n3 ):
    more = False
    return i, j, k, more
#
#  Increment K.
#
  k = k + 1
#
#  Check K.
#
  if ( n3 < k ):
    k = 1
    j = j + 1
  elif ( k < n3 and ( i == 1 or i == n1 or j == 1 or j == n2 ) ):
    return i, j, k, more
  else:
    k = n3
    return i, j, k, more
#
#  Check J.
#
  if ( n2 < j ):
    j = 1
    i = i + 1
  elif ( j < n2 and ( i == 1 or i == n1 or k == 1 or k == n3 ) ):
    return i, j, k, more
  else:
    j = n2
    return i, j, k, more

  return i, j, k, more

def index_box_next_3d_test ( ):

#*****************************************************************************80
#
## INDEX_BOX_NEXT_3D_TEST tests INDEX_BOX_NEXT_3D.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 May 2015
#
#  Author:
#
#    John Burkardt
#
  n1 = 5
  n2 = 3
  n3 = 4
  i = 0
  j = 0
  k = 0
  more = False

  print ''
  print 'INDEX_BOX_NEXT_3D_TEST'
  print '  INDEX_BOX_NEXT_3D produces IJK indices that'
  print '  lie on the surface of a box.'
  print ''
  print '  The box has logical dimensions:'
  print '  %3d  %3d  %3d' % ( n1, n2, n3 )
  print ''
  print '   #    I   J   K'
  print ''

  n = 0

  while ( True ):

    i, j, k, more = index_box_next_3d ( n1, n2, n3, i, j, k, more )

    if ( not more ):
      break

    n = n + 1
    print '  %3d  %3d  %3d  %3d' % ( n, i, j, k )
#
#  Terminate.
#
  print ''
  print 'INDEX_BOX_NEXT_3D_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  index_box_next_3d_test ( )
  timestamp ( )

