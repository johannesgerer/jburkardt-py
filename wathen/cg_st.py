#!/usr/bin/env python

def cg_st ( n, nz_num, row, col, a, b, x ):

#*****************************************************************************80
#
## CG_ST uses the conjugate gradient method for a sparse triplet storage matrix.
#
#  Discussion:
#
#    The linear system has the form A*x=b, where A is a positive-definite
#    symmetric matrix, stored as a full storage matrix.
#
#    The method is designed to reach the solution to the linear system
#      A * x = b
#    after N computational steps.  However, roundoff may introduce
#    unacceptably large errors for some problems.  In such a case,
#    calling the routine a second time, using the current solution estimate
#    as the new starting guess, should result in improved results.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Frank Beckman,
#    The Solution of Linear Equations by the Conjugate Gradient Method,
#    in Mathematical Methods for Digital Computers,
#    edited by John Ralston, Herbert Wilf,
#    Wiley, 1967,
#    ISBN: 0471706892,
#    LC: QA76.5.R3.
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, integer NZ_NUM, the number of nonzeros.
#
#    Input, integer ROW(NZ_NUM), COL(NZ_NUM), the row and column indices
#    of the nonzero entries.
#
#    Input, real A(NZ_NUM), the nonzero entries.
#
#    Input, real B(N), the right hand side vector.
#
#    Input/output, real X(N).
#    On input, an estimate for the solution, which may be 0.
#    On output, the approximate solution vector.  
#
  import numpy as np

  from mv_st import mv_st
#
#  Initialize
#    AP = A * x,
#    R  = b - A * x,
#    P  = b - A * x.
#
  ap = mv_st ( n, n, nz_num, row, col, a, x )

  r = b - ap
  p = b - ap
#
#  Do the N steps of the conjugate gradient method.
#
  for it in range ( 0, n ):
#
#  Compute the matrix*vector product AP = A*P.
#
    ap = mv_st ( n, n, nz_num, row, col, a, p )
#
#  Compute the dot products
#    PAP = P*AP,
#    PR  = P*R
#  Set
#    ALPHA = PR / PAP.
#
    pap = np.dot ( p, ap )
    pr =  np.dot ( p, r )

    if ( pap == 0.0 ):
      return x

    alpha = pr / pap
#
#  Set
#    X = X + ALPHA * P
#    R = R - ALPHA * AP.
#
    x = x + alpha * p
    r = r - alpha * ap
#
#  Compute the vector dot product
#    RAP = R*AP
#  Set
#    BETA = - RAP / PAP.
#
    rap = np.dot ( r, ap )

    beta = - rap / pap
#
#  Update the perturbation vector
#    P = R + BETA * P.
#
    p = r + beta * p

  return x

