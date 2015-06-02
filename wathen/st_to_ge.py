#!/usr/bin/env python

def st_to_ge ( n_st, row, col, a_st ):

%*****************************************************************************80
%
%% ST_TO_GE converts a sparse tripet (ST) matrix to general (GE) storage.
%
%  Licensing:
%
%    This code is distributed under the GNU LGPL license.
%
%  Modified:
%
%    01 June 2014
%
%  Author:
%
%    John Burkardt
%
%  Parameters:
%
%    Input, integer N_ST, the number of sparse triplet values.
%
%    Input, integer ROW(N_ST), COL(N_ST), the row and column indices.
%
%    Input, real A_ST(N_ST), the nonzero matrix values.
%
%    Output, real A_GE(M,N), the corresponding full storage matrix.
%
  import numpy as np
%
%  Guess the number of rows and columns.
%
  m = max ( row ) + 1
  n = max ( col ) + 1
%
%  Set up the GE matrix.
%
  a_ge = np.zeros ( ( m, n ) )
%
%  Copy the data as a vector.
%
  for k in range ( 0, n_st ):
    a_ge[row[k],col[k]] = a_st[k]

  return a_ge

