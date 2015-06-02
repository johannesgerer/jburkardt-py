#!/usr/bin/env python

def i4_sqrt_cf ( n, max_term ):

#*****************************************************************************80
#
## I4_SQRT_CF finds the continued fraction representation of a square root of an integer.
#
#  Discussion:
#
#    The continued fraction representation of the square root of an integer
#    has the form
#
#      [ B0, (B1, B2, B3, ..., BM), ... ]
#
#    where
#
#      B0 = int ( sqrt ( real ( N ) ) )
#      BM = 2 * B0
#      the sequence ( B1, B2, B3, ..., BM ) repeats in the representation.
#      the value M is termed the period of the representation.
#
#  Example:
#
#     N  Period  Continued Fraction
#
#     2       1  [ 1, 2, 2, 2, ... ]
#     3       2  [ 1, 1, 2, 1, 2, 1, 2... ]
#     4       0  [ 2 ]
#     5       1  [ 2, 4, 4, 4, ... ]
#     6       2  [ 2, 2, 4, 2, 4, 2, 4, ... ]
#     7       4  [ 2, 1, 1, 1, 4, 1, 1, 4, 1, 1, 4... ]
#     8       2  [ 2, 1, 4, 1, 4, 1, 4, 1, 4, ... ]
#     9       0  [ 3 ]
#    10       1  [ 3, 6, 6, 6, ... ]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 May 2015
#
#  Author:
#
#   John Burkardt
#
#  Reference:
#
#    Mark Herkommer,
#    Number Theory, A Programmer's Guide,
#    McGraw Hill, 1999, pages 294-307.
#
#  Parameters:
#
#    Input, integer N, the number whose continued fraction square root
#    is desired.
#
#    Input, integer MAX_TERM, the maximum number of terms that may
#    be computed.
#
#    Output, integer B(1:N_TERM), the continued fraction coefficients.
#
#    Output, integer N_TERM, the number of terms computed  The routine should 
#    stop if it detects that the period has been reached.
#
  import numpy as np
  from i4_sqrt import i4_sqrt

  c = np.zeros ( max_term + 1 )

  n_term = 0

  s, r = i4_sqrt ( n )

  c[0] = s

  if ( 0 < r ):

    p = 0
    q = 1

    while ( True ):

      p = c[n_term+1-1] * q - p
      q = ( ( n - p * p ) // q )

      if ( max_term <= n_term ):
        break

      n_term = n_term + 1
      c[n_term+1-1] = ( ( p + s ) // q )

      if ( q == 1 ):
        break

  b = np.zeros ( n_term+1 )
  for i in range ( 0, n_term + 1 ):
    b[i] = c[i]

  return b, n_term

def i4_sqrt_cf_test ( ):

#*****************************************************************************80
#
## I4_SQRT_CF_TEST tests I4_SQRT_CF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 May 2015
#
#  Author:
#
#    John Burkardt
#
  max_term = 100

  print ''
  print 'I4_SQRT_CF_TEST'
  print '  I4_SQRT_CF computes the continued fraction form'
  print '  of the square root of an integer.'
  print ''
  print '   N  Period  Whole  Repeating Part'
  print ''

  for n in range ( 1, 21 ):

    b, n_term = i4_sqrt_cf ( n, max_term )

    print '  %3d  %6d  %5d' % ( n, n_term, b[0] ),
    for i in range ( 1, n_term + 1 ):

      print '  %3d' % ( b[i] ),
      
      if ( ( ( i + 1 ) % 10 ) == 0 ):
        print ''
        print '               ',

    print ''
#
#  Terminate.
#
  print ''
  print 'I4_SQRT_CF_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_sqrt_cf_test ( )
  timestamp ( )

