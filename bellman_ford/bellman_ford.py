#!/usr/bin/env python
#
def bellman_ford ( v_num, e_num, source, e, e_weight ):

#*****************************************************************************80
#
#  Purpose:
#
#    BELLMAN_FORD finds shortest paths from a given vertex of a weighted directed graph.
#
#  Discussion:
#
#    The Bellman-Ford algorithm is used.
#
#    Each edge of the graph has a weight, which may be negative.  However,
#    it should not be the case that there is any negative loop, that is,
#    a circuit whose total weight is negative.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 November 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer V_NUM, the number of vertices.
#
#    Input, integer E_NUM, the number of edges.
#
#    Input, integer SOURCE, the vertex from which distances will 
#    be calculated.
#
#    Input, integer E(2,E_NUM), the edges, given as pairs of 
#    vertex indices.
#
#    Input, real E_WEIGHT(E_NUM), the weight of each edge.
#
#    Output, real V_WEIGHT(V_NUM), the weight of each node, 
#    that is, its minimum distance from SOURCE.
#
#    Output, integer PREDECESSOR(V_NUM), a list of predecessors, 
#    which can be used to recover the shortest path from any node back to SOURCE.
#
  import numpy as np
  from sys import exit

  r8_big = 1.0E+30
#
#  Step 1: initialize the graph.
#
  v_weight = np.zeros ( v_num, dtype = np.float64 )
  for i in range ( 0, v_num ):
    v_weight[i] = r8_big
  v_weight[source] = 0.0

  predecessor = np.zeros ( v_num, dtype = np.int32 )
  for i in range ( 0, v_num ):
    predecessor[i] = -1
#
#  Step 2: Relax edges repeatedly.
#
  for i in range ( 1, v_num ):
    for j in range ( 0, e_num ):
      u = e[1][j]
      v = e[0][j]
      t = v_weight[u] + e_weight[j];
      if ( t < v_weight[v] ):
        v_weight[v] = t
        predecessor[v] = u
#
#  Step 3: check for negative-weight cycles
#
  for j in range ( 0, e_num ):
    u = e[1][j]
    v = e[0][j]
    if ( v_weight[u] + e_weight[j] < v_weight[v] ):
      print ''
      print 'BELLMAN_FORD - Fatal error!'
      print '  Graph contains a cycle with negative weight.'
      exit ( 'BELLMAN_FORD - Fatal error!' )

  return v_weight, predecessor

def bellman_ford_test ( ):

#*****************************************************************************80
#
## BELLMAN_FORD_TEST tests BELLMAN_FORD.
#
#  Discussion:
#
#    The correct distances are { 0, -6, -2, 3, 0, 0 }.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 November 2014
#
#  Author:
#
#    John Burkardt
#
  from i4mat_transpose_print import i4mat_transpose_print
  from i4vec_print import i4vec_print
  from r8vec_print import r8vec_print
  import numpy as np

  e_num = 10
  v_num = 6

  e = np.array ( ( \
    ( 1, 4, 1, 2, 4, 2, 5, 3, 5, 3 ), \
    ( 0, 1, 2, 4, 0, 5, 0, 2, 3, 0 ) ) )
  e_weight = np.array ( ( \
    -3.0,  6.0, -4.0, -1.0,  4.0, -2.0,  2.0, 8.0, -3.0,  3.0 ) )
 
  source = 0

  print ''
  print 'BELLMAN_FORD_TEST'
  print '  Bellman-Ford shortest path algorithm.'

  print ''
  print '  Number of vertices = %d' % ( v_num )
  print '  Number of edges = %d' % ( e_num )
  print '  The reference vertex is %d' % ( source )

  i4mat_transpose_print ( 2, e_num, e, '  The edge array:' )
  r8vec_print ( e_num, e_weight, '  The edge weights:' )

  [ v_weight, predecessor ] = bellman_ford ( v_num, e_num, source, e, e_weight )

  r8vec_print ( v_num, v_weight, '  The shortest distances:' )

  i4vec_print ( v_num, predecessor, \
    '  The vertex predecessor parents for the shortest paths:' )

  print ''
  print 'BELLMAN_FORD_TEST_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  bellman_ford_test ( )
  timestamp ( )

