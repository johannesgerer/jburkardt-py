#! /usr/bin/env python
#
#*****************************************************************************80

def assemble_fem ( x_num, x, element_num, element_node, quad_num, t, k_fun, \
  rhs_fun ):

#*****************************************************************************80
#
## ASSEMBLE_FEM assembles the finite element stiffness matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 November 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer X_NUM, the number of nodes.
#
#    Input, real X(X_NUM), the coordinates of nodes.
#
#    Input, integer ELEMENT_NUM, the number of elements.
#
#    Input, integer ELEMENT_NODE(2,ELEMENT_NUM);
#    ELEMENT_NODE(I,J) is the global index of local node I in element J.
#
#    Input, integer QUAD_NUM, the number of quadrature points used in assembly.
#
#    Input, real T, the current time.
#
#    Input, real K_FUN(), a function to evaluate the heat conductivity.
#
#    Input, real RHS_FUN(), a function to evaluate the right hand side.
#
#    Output, sparse real A(X_NUM,X_NUM), the finite element stiffness matrix.
#
#    Output, real B(X_NUM), the right hand side.
#
#  Local parameters:
#
#    Local, real BI, DBIDX, the value of some basis function
#    and its first derivative at a quadrature point.
#
#    Local, real BJ, DBJDX, the value of another basis
#    function and its first derivative at a quadrature point.
#
  from basis_function import basis_function
  from quadrature_set import quadrature_set
  from reference_to_physical import reference_to_physical
  import numpy as np
#
#  Initialize the arrays.
#
  b = np.zeros ( x_num )
  a = np.zeros ( ( x_num, x_num ) )
#
#  Get the quadrature weights and nodes.
#
  reference_w, reference_q = quadrature_set ( quad_num )
#
#  Consider each ELEMENT.
#
  for element in range ( 0, element_num ):

    element_x = np.zeros ( 2 )
    element_x[0] = x[element_node[0,element]]
    element_x[1] = x[element_node[1,element]]

    element_q = reference_to_physical ( element, element_node, x, quad_num, \
      reference_q )

    element_area = element_x[1] - element_x[0]

    element_w = np.zeros ( quad_num )
    for quad in range ( 0, quad_num ):
      element_w[quad] = ( element_area / 2.0 ) * reference_w[quad]
#
#  Consider the QUAD-th quadrature point in the element.
#
    k_value = k_fun ( quad_num, element_q, t )
    rhs_value = rhs_fun ( quad_num, element_q, t )

    for quad in range ( 0, quad_num ):
#
#  Consider the TEST-th test function.
#
#  We generate an integral for every node associated with an unknown.
#
      for i in range ( 0, 2 ):

        test = element_node[i,element]

        bi, dbidx = basis_function ( test, element, x, element_q[quad] )

        b[test] = b[test] + element_w[quad] * rhs_value[quad] * bi
#
#  Consider the BASIS-th basis function, which is used to form the
#  value of the solution function.
#
        for j in range ( 0, 2 ):

          basis = element_node[j,element]

          bj, dbjdx = basis_function ( basis, element, x, element_q[quad] )

          a[test,basis] = a[test,basis] + element_w[quad] * ( \
            + k_value[quad] * dbidx * dbjdx )

  return a, b

