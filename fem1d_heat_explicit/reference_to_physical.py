#!/usr/bin/env python

#*****************************************************************************80

def reference_to_physical ( element, element_node, node_x, reference_num, \
  reference_x ):

#*****************************************************************************80
#
## REFERENCE_TO_PHYSICAL maps points in the reference interval into an element.
#
#  Discussion:
#
#    The reference interval is [ -1.0, +1.0 ].
#
#    Element ELEMENT extends from node ELEMENT_NODE(1,ELEMENT) to ELEMENT_NODE(2,ELEMENT).
#
#    The coordinate of node NODE is NODE_X(NODE).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 November 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer ELEMENT, the index of the element.
#
#    Input, integer ELEMENT_NODE(ELEMENT_ORDER,ELEMENT_NUM);
#    ELEMENT_NODE(I,J) is the global index of local node I in element J.
#
#    Input, real NODE_X(NODE_NUM), the coordinates of nodes.
#
#    Input, integer REFERENCE_NUM, the number of points in the reference
#    interval to be transformed.
#
#    Input, real REFERENCE_X(REFERENCE_NUM), the coordinates of the
#    points in the reference interval.
#
#    Output, real PHYSICAL_X(REFERENCE_NUM), the coordinates of the
#    points in the element which correspond to the reference points.
#
  import numpy as np

  physical_x = np.zeros ( reference_num )

  for i in range ( 0, reference_num ):
    a = node_x[element_node[0,element] ]
    b = node_x[element_node[1,element] ]

    physical_x[i] = ( ( 1.0 - reference_x[i]             ) * a   \
                    + (       reference_x[i] - ( - 1.0 ) ) * b ) \
                    / ( 1.0                  - ( - 1.0 ) )

  return physical_x

def reference_to_physical_test ( ):

#*****************************************************************************80
#
## REFERENCE_TO_PHYSICAL_TEST tests REFERENCE_TO_PHYSICAL
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 November 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ''
  print 'REFERENCE_TO_PHYSICAL_TEST'
  print '  REFERENCE_TO_PHYSICAL maps points in [-1,+1] to points in'
  print '  a physical interval.'

  element_num = 4
  element_node = np.array ( [ [ 0, 1, 2, 3 ], [ 1, 2, 3, 4 ] ] )

  node_num = 5
  node_x = np.array ( [ 0.0, 2.0, 3.0, 6.0, 10.0 ] )

  reference_num = 5
  reference_x = np.array ( [ -1.0, -0.5, 0.0, 0.25, 1.0 ] )

  element = 3
  physical_x = reference_to_physical ( element, element_node, node_x, \
    reference_num, reference_x )

  print ''
  print '   I      Ref[i]    Phys[i]'
  print ''
  for i in range ( 0, reference_num ):
    print '  %2d  %8.4f  %8.4f' % ( i, reference_x[i], physical_x[i] )

  print ''
  print 'REFERENCE_TO_PHYSICAL_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp

  timestamp ( )
  reference_to_physical_test ( )
  timestamp ( )


