#!/usr/bin/env python
#
def i4_rise_values ( n_data ):

#*****************************************************************************80
#
## I4_RISE_VALUES returns values of the integer rising factorial function.
#
#  Discussion:
#
#    The integer rising factorial function is sometimes symbolized by (m)_n.
#
#    The definition is
#
#      (m)_n = (m-1+n)! / (m-1)!
#            = ( m ) * ( m + 1 ) * ( m + 2 ) ... * ( m - 1 + n )
#            = Gamma ( m + n ) / Gamma ( m )
#
#    We assume 0 <= N <= M.
#
#    In Mathematica, the function can be evaluated by:
#
#      Pochhammer[m,n]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Parameters:
#
#    Input/output, integer N_DATA.  The user sets N_DATA to 0 before the
#    first call.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, integer M, N, the arguments of the function.
#
#    Output, integer FMN, the value of the function.
#
  import numpy as np

  n_max = 15

  fmn_vec = np.array ( [ 
     1, 5, 30, 210, 1680, \
     15120, 151200, 1, 10, 4000, \
     110, 6840, 840, 970200, 5040 ] )
  m_vec = np.array ( [ 
    5, 5, 5, 5, 5, \
    5, 5, 50, 10, 4000, \
    10, 18, 4, 98, 1 ] )
  n_vec = np.array ( [ 
     0, 1, 2, 3, 4, \
    5, 6, 0, 1, 1, \
    2, 3, 4, 3, 7 ] )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    m = 0
    n = 0
    fmn = 0
  else:
    m = m_vec[n_data]
    n = n_vec[n_data]
    fmn = fmn_vec[n_data]
    n_data = n_data + 1

  return n_data, m, n, fmn

def i4_rise_values_test ( ):

#*****************************************************************************80
#
## I4_RISE_VALUES_TEST tests I4_RISE_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 December 2014
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'I4_RISE_VALUES_TEST:'
  print '  I4_RISE_VALUES returns values of the integer rising factorial.'
  print ''
  print '          M         N          I4_RISE(M,N)'
  print ''

  n_data = 0

  while ( True ):

    n_data, m, n, fmn = i4_rise_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %8d  %8d  %8d' % ( m, n, fmn )

  print ''
  print 'I4_RISE_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_rise_values_test ( )
  timestamp ( )

