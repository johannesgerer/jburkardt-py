#!/usr/bin/env python

def lpp_to_polynomial ( m, l, o_max ):

#*****************************************************************************80
#
## LPP_TO_POLYNOMIAL writes a Legendre Product Polynomial as a polynomial.
#
#  Discussion:
#
#    For example, if 
#      M = 3,
#      L = ( 1, 0, 2 ),
#    then
#      L(1,0,2)(X,Y,Z) 
#      = L(1)(X) * L(0)(Y) * L(2)(Z)
#      = X * 1 * ( 3Z^2-1)/2
#      = - 1/2 X + (3/2) X Z^2
#    so
#      O = 2 (2 nonzero terms)
#      C = -0.5
#           1.5
#      E = 4    <-- index in 3-space of exponent (1,0,0)
#          15   <-- index in 3-space of exponent (1,0,2)
#
#    The output value of O is no greater than
#      O_MAX = product ( 1 <= I <= M ) (L(I)+2)/2
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, int M, the spatial dimension.
#
#    Input, int L[M], the index of each Legendre product 
#    polynomial factor.  0 <= L(*).
#
#    Input, int O_MAX, an upper limit on the size of the 
#    output arrays.
#      O_MAX = product ( 1 <= I <= M ) (L(I)+2)/2.
#
#    Output, int O, the "order" of the polynomial product.
#
#    Output, double C[O], the coefficients of the polynomial product.
#
#    Output, int E[O], the indices of the exponents of the 
#    polynomial product.
#
  from lp_coefficients import lp_coefficients
  from mono_rank_grlex import mono_rank_grlex
  from mono_unrank_grlex import mono_unrank_grlex
  from polynomial_compress import polynomial_compress
  from polynomial_sort import polynomial_sort
  import numpy as np

  c1 = np.zeros ( o_max, dtype = np.float64 )
  c2 = np.zeros ( o_max, dtype = np.float64 )
  e1 = np.zeros ( o_max, dtype = np.int32 )
  e2 = np.zeros ( o_max, dtype = np.int32 )
  f2 = np.zeros ( o_max, dtype = np.int32 )
  pp = np.zeros ( m, dtype = np.int32 )

  o1 = 1
  c1[0] = 1.0
  e1[0] = 1
#
#  Implicate one factor at a time.
#
  for i in range ( 0, m ):

    o2, c2, f2 = lp_coefficients ( l[i] );
 
    o = 0;
    c = np.zeros ( o_max, dtype = np.float64 )
    e = np.zeros ( o_max, dtype = np.int32 )

    for j2 in range ( 0, o2 ):
      for j1 in range ( 0, o1 ):
        c[o] = c1[j1] * c2[j2]
        if ( 0 < i ):
          p = mono_unrank_grlex ( i, e1[j1] )
        for i2 in range ( 0, i ):
          pp[i2] = p[i2]
        pp[i] = f2[j2]
        e[o] = mono_rank_grlex ( i + 1, pp )
        o = o + 1

    c, e = polynomial_sort ( o, c, e )
    o, c, e = polynomial_compress ( o, c, e )

    o1 = o;
    for i1 in range ( 0, o ):
      c1[i1] = c[i1]
      e1[i1] = e[i1]

  return o1, c1, e1

def lpp_to_polynomial_test ( ):

#*****************************************************************************80
#
## LPP_TO_POLYNOMIAL_TEST tests LPP_TO_POLYNOMIAL.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 October 2014
#
#  Author:
#
#    John Burkardt
#
  from comp_unrank_grlex import comp_unrank_grlex
  from polynomial_print import polynomial_print
  import numpy as np

  m = 2

  print ''
  print 'LPP_TO_POLYNOMIAL_TEST:'
  print '  LPP_TO_POLYNOMIAL is given a Legendre product polynomial'
  print '  and determines its polynomial representation.'

  print ''
  print '  Using spatial dimension M = %d' % ( m )

  for rank in range ( 1, 12 ):
    l = comp_unrank_grlex ( m, rank )

    o_max = 1
    for i in range ( 0, m ):
      o_max = o_max * ( l[i] + 2 ) // 2

    c = np.zeros ( o_max, dtype = np.float64 )
    e = np.zeros ( o_max, dtype = np.int32 )

    o, c, e = lpp_to_polynomial ( m, l, o_max )

    label = '  LPP #' + repr ( rank ) + ' = L(' + repr ( l[0] ) \
      + ',X)*L(' + repr ( l[1] ) + ',Y) = '

    print ''
    polynomial_print ( m, o, c, e, label )

  print ''
  print 'LPP_TO_POLYNOMIAL_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp

  timestamp ( )
  lpp_to_polynomial_test ( )
  timestamp ( )
