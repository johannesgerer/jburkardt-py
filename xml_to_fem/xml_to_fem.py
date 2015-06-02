#!/usr/bin/env python
#
def xml_to_fem ( filename ):

#*****************************************************************************80
#
## XML_TO_FEM reads mesh information from a DOLFIN or FENICS mesh XML file.
#
#  Location:
#
#    http://people.sc.fsu.edu/~jburkardt/py_src/xml_to_fem/xml_to_fem.py
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    12 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, string FILENAME, the name of the XML file.
#
  import numpy as np
  import xml.etree.ElementTree as ET

  tree = ET.parse ( filename )

  root = tree.getroot ( )

  for alice in root:

    if alice.tag == 'mesh':

      celltype = alice.get ( 'celltype' )
      dim = int ( alice.get ( 'dim' ) )

      for bob in alice:

        if ( bob.tag == 'vertices' ):

          node_num = int ( bob.get ( 'size' ) )

          node_x = np.zeros ( ( node_num, dim ) )

          for carol in bob:

            for dave in carol.attrib:
              if ( dave == 'index' ):
                index = int ( carol.get ( 'index' ) )

            for dave in carol.attrib:
              if ( dave == 'x' ):
                x = float ( carol.get ( 'x' ) )
                node_x[index,0] = x
              elif ( dave == 'y' ):
                y = float ( carol.get ( 'y' ) )
                node_x[index,1] = y
              elif ( dave == 'z' ):
                z = float ( carol.get ( 'z' ) )
                node_x[index,2] = z

        elif ( bob.tag == 'cells' ):

          elem_num = int ( bob.get ( 'size' ) )

          if ( celltype == 'interval' ):
            elem_order = 2
          elif ( celltype == 'triangle' ):
            elem_order = 3
          elif ( celltype == 'tetrahedron' ):
            elem_order = 4

          elem_node = np.zeros ( ( elem_num, elem_order ) )

          for carol in bob:

            for dave in carol.attrib:
              if ( dave == 'index' ):
                index = int ( carol.get ( 'index' ) )

            for dave in carol.attrib:
              if ( dave == 'v0' ):
                v0 = int ( carol.get ( 'v0' ) )
                elem_node[index,0] = v0
              elif ( dave == 'v1' ):
                v1 = int ( carol.get ( 'v1' ) )
                elem_node[index,1] = v1
              elif ( dave == 'v2' ):
                v2 = int ( carol.get ( 'v2' ) )
                elem_node[index,2] = v2
              elif ( dave == 'v3' ):
                v3 = int ( carol.get ( 'v3' ) )
                elem_node[index,3] = v3

  return node_x, elem_node

def xml_to_fem_test ( prefix ):

#*****************************************************************************80
#
## XML_TO_FEM_TEST tests XML_TO_FEM on a user file, printing the output.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    10 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, string PREFIX, the common filename prefix.
#
  filename_xml = prefix + '.xml'

  print ''
  print '  Read the XML file "%s"' % ( filename_xml )

  node_x, elem_node = xml_to_fem ( filename_xml )

  node_x_shape = node_x.shape
  node_num = node_x_shape[0]
  dim_num = node_x_shape[1]
  print '  Spatial dimension = %d' % ( dim_num )
  print '  Number of nodes = %d' % ( node_num )

  elem_node_shape = elem_node.shape
  elem_num = elem_node_shape[0]
  elem_order = elem_node_shape[1]
  print '  Element order = %d' % ( elem_order )
  print '  Number of elements = %d' % ( elem_num )

  print ''
  print '  NODE_X array of node coordinates:'
  print ''
  for i in range ( 0, node_num ):
    for j in range ( 0, dim_num ):
      print '  %g' % ( node_x[i][j] ),
    print ''

  print ''
  print '  ELEM_NODE array of node indices:'
  print ''
  for i in range ( 0, elem_num ):
    for j in range ( 0, elem_order ):
      print '  %d' % ( elem_node[i][j] ),
    print ''

  filename_elements = prefix + '_elements.txt'
  i4mat_write ( filename_elements, elem_num, elem_order, elem_node )

  filename_nodes = prefix + '_nodes.txt'
  r8mat_write ( filename_nodes, node_num, dim_num, node_x )

  return

def i4mat_write ( filename, m, n, a ):

#*****************************************************************************80
#
## I4MAT_WRITE writes an I4MAT to a file.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, string FILENAME, the name of the output file.
#
#    Input, integer M, the number of rows in A.
#
#    Input, integer N, the number of columns in A.
#
#    Input, integer A(M,N), the matrix.
#
  output = open ( filename, 'w' )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      s = '  %d' % ( a[i,j] )
      output.write ( s )
    output.write ( '\n' )

  output.close ( )

def r8mat_write ( filename, m, n, a ):

#*****************************************************************************80
#
## R8MAT_WRITE writes an R8MAT to a file.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, string FILENAME, the name of the output file.
#
#    Input, integer M, the number of rows in A.
#
#    Input, integer N, the number of columns in A.
#
#    Input, real A(M,N), the matrix.
#
  output = open ( filename, 'w' )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      s = '  %g' % ( a[i,j] )
      output.write ( s )
    output.write ( '\n' )

  output.close ( )

  return

if ( __name__ == '__main__' ):

#*****************************************************************************80
#
## MAIN runs the test case.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 December 2014
#
#  Author:
#
#    John Burkardt
#
  from timestamp import timestamp

  timestamp ( )
  print ''
  print 'XML_TO_FEM_TEST.'
  print '  Python version'
  print '  Read a DOLFIN/FENICS XML mesh file.'
  print '  Extract the coordinate and element information.'

  xml_to_fem_test ( 'cheby9' )
  xml_to_fem_test ( 'rectangle' )
  xml_to_fem_test ( 'tet_mesh' )

  print ''
  print 'XML_TO_FEM_TEST.'
  print '  Normal end of execution'
  print ''
  timestamp ( )
