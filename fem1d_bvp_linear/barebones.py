#! /usr/bin/env python
#
def barebones ( n, a, c, f, x ):

#  Location:
#
#    http://people.sc.fsu.edu/~jburkardt/py_src/fem1d_bvp_linear/barebones.py
#
  import numpy as np
  import scipy.linalg as la

  quad_num = 2
  abscissa = np.array ( [ -0.577350269189625764509148780502, \
                          +0.577350269189625764509148780502 ] )
  weight = np.array ( [ 1.0, 1.0 ] )

  A = np.zeros ( [ n, n ] )
  b = np.zeros ( n )

  e_num = n - 1

  for e in range ( 0, e_num ):

    l = e
    xl = x[l]
    r = e + 1
    xr = x[r]

    for q in range ( 0, quad_num ):

      xq = ( ( 1.0 - abscissa[q] ) * xl   \
           + ( 1.0 + abscissa[q] ) * xr ) \
           / 2.0
      wq = weight[q] * ( xr - xl ) / 2.0

      vl = ( xr - xq ) / ( xr - xl )
      vlp =     - 1.0  / ( xr - xl )

      vr = ( xq - xl ) / ( xr - xl )
      vrp = +1.0       / ( xr - xl )

      axq = a ( xq )
      cxq = c ( xq )
      fxq = f ( xq )

      A[l,l] = A[l,l] + wq * ( vlp * axq * vlp + vl * cxq * vl )
      A[l,r] = A[l,r] + wq * ( vlp * axq * vrp + vl * cxq * vr )
      b[l]   = b[l]   + wq * ( vl * fxq )

      A[r,l] = A[r,l] + wq * ( vrp * axq * vlp + vr * cxq * vl )
      A[r,r] = A[r,r] + wq * ( vrp * axq * vrp + vr * cxq * vr )
      b[r]   = b[r]   + wq * ( vr * fxq )

  for j in range ( 0, n ):
    A[0,j] = 0.0
  A[0,0] = 1.0
  b[0] = 0.0

  for j in range ( 0, n ):
    A[n-1,j] = 0.0
  A[n-1,n-1] = 1.0
  b[n-1] = 0.0

  u = la.solve ( A, b )

  return u

def barebones_test ( ):

  import matplotlib.pyplot as plt
  import numpy as np
  from h1s_error_linear import h1s_error_linear
  from l1_error import l1_error
  from l2_error_linear import l2_error_linear

  n = 11

  print ''
  print 'BAREBONES_TEST'
  print '  Solve -( A(x) U\'(x) )\' + C(x) U(x) = F(x)'
  print '  for 0 < x < 1, with U(0) = U(1) = 0.'
  print '  A(X)  = 1.0'
  print '  C(X)  = 1.0'
  print '  F(X)  = X'
  print '  U(X)  = X - SINH(X) / SINH(1)'
  print ''
  print '  Number of nodes = %d' % ( n )

  x_lo = 0.0
  x_hi = 1.0
  x = np.linspace ( x_lo, x_hi, n )

  u = barebones ( n, a, c, f, x )

  g = np.zeros ( n )
  for i in range ( 0, n ):
    g[i] = exact ( x[i] )

  print ''
  print '     I    X         U         Uexact    Error'
  print ''

  for i in range ( 0, n ):
    print '  %4d  %8f  %8f  %8f  %8e' \
      % ( i, x[i], u[i], g[i], abs ( u[i] - g[i] ) )

  e1 = l1_error ( n, x, u, exact )
  e2 = l2_error_linear ( n, x, u, exact )
  h1s = h1s_error_linear ( n, x, u, exactp )

  print ''
  print '  l1 norm of error  = %g' % ( e1 )
  print '  L2 norm of error  = %g' % ( e2 )
  print '  Seminorm of error = %g' % ( h1s  )

  fig = plt.figure ( )
  plt.plot ( x, u, 'bo-' )
  plt.xlabel ( '<---X--->' )
  plt.ylabel ( '<---U(X)--->' )
  plt.title ( 'BAREBONES Solution' )
  plt.savefig ( 'barebones.png' )
  plt.show ( )

  print ''
  print 'BAREBONES'
  print '  Normal end of execution.'

  return

def a ( x ):
  value = 1.0
  return value

def c ( x ):
  value = 1.0
  return value

def exact ( x ):
  from math import sinh
  value = x - sinh ( x ) / sinh ( 1.0 )
  return value

def exactp ( x ):
  from math import cosh
  from math import sinh
  value = 1.0 - cosh ( x ) / sinh ( 1.0 )
  return value

def f ( x ):
  value = x
  return value

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  barebones_test ( )
  timestamp ( )
