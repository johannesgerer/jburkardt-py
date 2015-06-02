#!/usr/bin/env python
#
def fem_to_xml ( prefix ):

#*****************************************************************************80
#
## FEM_TO_XML converts mesh data from FEM to DOLFIN XML format.
#
#  Location:
#
#    http://people.sc.fsu.edu/~jburkardt/py_src/fem_to_xml/fem_to_xml.py
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    13 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, string PREFIX, the common filename prefix.
#
  import numpy as np
  from i4mat_data_read import i4mat_data_read
  from i4mat_header_read import i4mat_header_read
  from r8mat_data_read import r8mat_data_read
  from r8mat_header_read import r8mat_header_read

  filename_elements = prefix + '_elements.txt'
  filename_nodes = prefix + '_nodes.txt'
  filename_xml = prefix + '.xml'

  node_num, dim_num = r8mat_header_read ( filename_nodes )
  node_x = r8mat_data_read ( filename_nodes, node_num, dim_num )

  element_num, element_order = i4mat_header_read ( filename_elements )
  element_node = i4mat_data_read ( filename_elements, element_num, element_order )

  if ( dim_num == 1 ):
    xml_mesh1d_write ( filename_xml, node_num, dim_num, element_num, \
      element_order, node_x, element_node )
  elif ( dim_num == 2 ):
    xml_mesh2d_write ( filename_xml, node_num, dim_num, element_num, \
      element_order, node_x, element_node )
  elif ( dim_num == 3 ):
    xml_mesh3d_write ( filename_xml, node_num, dim_num, element_num, \
      element_order, node_x, element_node )

  return

def mesh_base_zero ( node_num, element_order, element_num, element_node ):

#*****************************************************************************80
#
## MESH_BASE_ZERO ensures that the element definition is zero-based.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    18 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer NODE_NUM, the number of nodes.
#
#    Input, integer ELEMENT_ORDER, the order of the elements.
#
#    Input, integer ELEMENT_NUM, the number of elements.
#
#    Input/output, integer ELEMENT_NODE[ELEMENT_NUM,ELEMENT_ORDER], the element
#    definitions.
#
  i4_huge = 2147483647
  node_min = + i4_huge
  node_max = - i4_huge
  for j in range ( 0, element_order ):
    for i in range ( 0, element_num ):
      node_min = min ( node_min, element_node[i,j] )
      node_max = max ( node_max, element_node[i,j] )

  if ( node_min == 0 and node_max == node_num - 1 ):
    print '';
    print 'MESH_BASE_ZERO:';
    print '  The element indexing appears to be 0-based!';
    print '  No conversion is necessary.';
  elif ( node_min == 1 and node_max == node_num ):
    print ''
    print 'MESH_BASE_ZERO:'
    print '  The element indexing appears to be 1-based!'
    print '  This will be converted to 0-based.'
    for j in range ( 0, element_order ):
      for i in range ( 0, element_num ):
        element_node[i,j] = element_node[i,j] - 1
  else:
    print ''
    print 'MESH_BASE_ZERO - Warning!'
    print '  The element indexing is not of a recognized type.'
    print '  NODE_MIN = %d' % ( node_min )
    print '  NODE_MAX = %d' % ( node_max )
    print '  NODE_NUM = %d' % ( node_num )

  return element_node

def xml_mesh1d_write ( filename_xml, node_num, dim_num, element_num, \
  element_order, node_x, element_node ):

#*****************************************************************************80
#
## XML_MESH1D_WRITE writes 1D mesh data to a DOLFIN XML file.
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
#    Input, string FILENAME_XML, the name of the XML file.
#
#    Input, integer NODE_NUM, the number of nodes.
#
#    Input, integer DIM_NUM, the spatial dimension.
#
#    Input, integer ELEMENT_NUM, the number of elements.
#
#    Input, integer ELEMENT_ORDER, the order of the elements.
#
#    Input, real NODE_X(NODE_NUM,DIM_NUM), the node coordinates.
#
#    Input, integer ELEMENT_NODE(ELEMENT_NUM,ELEMENT_ORDER)
#

#
#  Enforce 0-based indexing.
#
  element_node = mesh_base_zero ( node_num, element_order, element_num, element_node );

  output = open ( filename_xml, 'w' )

  output.write ( '<?xml version="1.0" encoding="UTF-8"?>\n' )
  output.write ( '<dolfin xmlns:dolfin="http://www.fenics.org/dolfin/">\n' )
  output.write ( '  <mesh celltype="interval" dim="1">\n' );

  output.write ( '    <vertices size="' + repr ( node_num ) + '">\n' )
  for i in range ( 0, node_num ):
    output.write ( '      <vertex index="' + repr ( i ) + '"')
    output.write ( ' x="' + repr ( node_x[i,0] ) + '"/>\n' )

  output.write ( '    </vertices>\n' )

  output.write ( '    <cells size="' + repr ( element_num ) + '">\n' )
  for i in range ( 0, element_num ):
    output.write ( '      <interval index="' + repr ( i ) + '"' )
    for j in range ( 0, element_order ):
      output.write ( ' v' + repr ( j ) + '="' + repr ( element_node[i,j] ) + '"' )
    output.write ( '/>\n' );
  output.write ( '    </cells>\n' )
  output.write ( '  </mesh>\n' )
  output.write ( '</dolfin>\n' )

  output.close ( )

  return

def xml_mesh2d_write ( filename_xml, node_num, dim_num, element_num, \
      element_order, node_x, element_node ):

#*****************************************************************************80
#
## XML_MESH2D_WRITE writes 2D mesh data to a DOLFIN XML file.
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
#    Input, string FILENAME_XML, the name of the XML file.
#
#    Input, integer NODE_NUM, the number of nodes.
#
#    Input, integer DIM_NUM, the spatial dimension.
#
#    Input, integer ELEMENT_NUM, the number of elements.
#
#    Input, integer ELEMENT_ORDER, the order of the elements.
#
#    Input, real NODE_X(NODE_NUM,DIM_NUM), the node coordinates.
#
#    Input, integer ELEMENT_NODE(ELEMENT_NUM,ELEMENT_ORDER)
#

#
#  Enforce 0-based indexing.
#
  element_node = mesh_base_zero ( node_num, element_order, element_num, element_node );

  output = open ( filename_xml, 'w' )

  output.write ( '<?xml version="1.0" encoding="UTF-8"?>\n' )
  output.write ( '<dolfin xmlns:dolfin="http://www.fenics.org/dolfin/">\n' )
  output.write ( '  <mesh celltype="triangle" dim="2">\n' );

  output.write ( '    <vertices size="' + repr ( node_num ) + '">\n' )
  for i in range ( 0, node_num ):
    output.write ( '      <vertex index="' + repr ( i ) + '"')
    output.write ( ' x="' + repr ( node_x[i,0] ) + '"' )
    output.write ( ' y="' + repr ( node_x[i,1] ) + '"/>\n' )

  output.write ( '    </vertices>\n' )

  output.write ( '    <cells size="' + repr ( element_num ) + '">\n' )
  for i in range ( 0, element_num ):
    output.write ( '      <triangle index="' + repr ( i ) + '"' )
    for j in range ( 0, element_order ):
      output.write ( ' v' + repr ( j ) + '="' + repr ( element_node[i,j] ) + '"' )
    output.write ( '/>\n' );
  output.write ( '    </cells>\n' )
  output.write ( '  </mesh>\n' )
  output.write ( '</dolfin>\n' )

  output.close ( )

  return

def xml_mesh3d_write ( filename_xml, node_num, dim_num, element_num, \
      element_order, node_x, element_node ):

#*****************************************************************************80
#
## XML_MESH3D_WRITE writes 3D mesh data to a DOLFIN XML file.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    13 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, string FILENAME_XML, the name of the XML file.
#
#    Input, integer NODE_NUM, the number of nodes.
#
#    Input, integer DIM_NUM, the spatial dimension.
#
#    Input, integer ELEMENT_NUM, the number of elements.
#
#    Input, integer ELEMENT_ORDER, the order of the elements.
#
#    Input, real NODE_X(NODE_NUM,DIM_NUM), the node coordinates.
#
#    Input, integer ELEMENT_NODE(ELEMENT_NUM,ELEMENT_ORDER)
#

#
#  Enforce 0-based indexing.
#
  element_node = mesh_base_zero ( node_num, element_order, element_num, element_node );

  output = open ( filename_xml, 'w' )

  output.write ( '<?xml version="1.0" encoding="UTF-8"?>\n' )
  output.write ( '<dolfin xmlns:dolfin="http://www.fenics.org/dolfin/">\n' )
  output.write ( '  <mesh celltype="tetrahedron" dim="3">\n' );

  output.write ( '    <vertices size="' + repr ( node_num ) + '">\n' )
  for i in range ( 0, node_num ):
    output.write ( '      <vertex index="' + repr ( i ) + '"')
    output.write ( ' x="' + repr ( node_x[i,0] ) + '"' )
    output.write ( ' y="' + repr ( node_x[i,1] ) + '"' )
    output.write ( ' z="' + repr ( node_x[i,2] ) + '"/>\n' )

  output.write ( '    </vertices>\n' )

  output.write ( '    <cells size="' + repr ( element_num ) + '">\n' )
  for i in range ( 0, element_num ):
    output.write ( '      <tetrahedron index="' + repr ( i ) + '"' )
    for j in range ( 0, element_order ):
      output.write ( ' v' + repr ( j ) + '="' + repr ( element_node[i,j] ) + '"' )
    output.write ( '/>\n' );
  output.write ( '    </cells>\n' )
  output.write ( '  </mesh>\n' )
  output.write ( '</dolfin>\n' )

  output.close ( )

  return

def fem_to_xml_test ( ):

#*****************************************************************************80
#
## FEM_TO_XML_TEST tests a 1D, 2D and 3D mesh.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    13 October 2014
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'FEM_TO_XML_TEST:'
  print '  Read mesh data from FEM files.'
  print '  Write mesh data to equivalent XML file.'
  print ''

  prefix = 'cheby9'
  print '  Using common file prefix "%s"' % ( prefix )
  fem_to_xml ( prefix )

  prefix = 'rectangle'
  print '  Using common file prefix "%s"' % ( prefix )
  fem_to_xml ( prefix )

  prefix = 'tet_mesh'
  print '  Using common file prefix "%s"' % ( prefix )
  fem_to_xml ( prefix )

  print ''
  print 'FEM_TO_XML_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):

#*****************************************************************************80
#
## MAIN calls FEM_TO_XML_TEST.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    13 October 2014
#
#  Author:
#
#    John Burkardt
#
  from timestamp import timestamp
  timestamp ( )
  fem_to_xml_test ( )
  timestamp ( )

