#! /usr/bin/env python
#
def index_box_next_2d ( n1, n2, i, j, more ):

#*****************************************************************************80
#
## INDEX_BOX_NEXT_2D produces index vectors on the surface of a box in 2D.
#
#  Discussion:
#
#    The index vectors are exactly those which are between (1,1) and
#    (N1,N2) with the property that at least one of I and J
#    is an "extreme" value.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N1, N2, the "dimensions" of the box, that is, the
#    maximum values allowed for I and J.  The minimum values are
#    assumed to be 1.
#
#    Input, integer I, J, the previous index set.  The values of I and J
#    are not needed on the first call, with MORE set to FALSE.
#
#    Input, logical MORE, is FALSE on the first call, and TRUE therafter.
#
#    Output, integer I, J, the next index set.
#
#    Output, logical MORE, is TRUE if the routine can be called again
#    for more index sets.
#
  if ( not more ):
    more = True
    i = 1
    j = 1
    return i, j, more

  if ( i == n1 and j == n2 ):
    more = False
    return i, j, more
#
#  Increment J.
#
  j = j + 1
#
#  Check J.
#
  if ( n2 < j ):
    j = 1
    i = i + 1
  elif ( j < n2 and ( i == 1 or i == n1 ) ):
    pass
  else:
    j = n2

  return i, j, more

def index_box_next_2d_test ( ):

#*****************************************************************************80
#
#% INDEX_BOX_NEXT_2D_TEST tests INDEX_BOX_NEXT_2D.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n1 = 5
  n2 = 3

  print ''
  print 'INDEX_BOX_NEXT_2D_TEST'
  print '  INDEX_BOX_NEXT_2D produces IJ indices that'
  print '  lie on the surface of a box in 2D.'
  print ''
  print '  The box has logical dimensions:'
  print '  %3d by %3d' % ( n1, n2 )
  print ''
  print '    #    I    J'
  print ''

  i = 0
  j = 0
  more = False
  n = 0

  while ( True ):

    i, j, more = index_box_next_2d ( n1, n2, i, j, more )

    if ( not more ):
      break

    n = n + 1
    print '  %3d  %3d  %3d' % ( n, i, j )
#
#  Terminate.
#
  print ''
  print 'INDEX_BOX_NEXT_2D_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  index_box_next_2d_test ( )
  timestamp ( )

