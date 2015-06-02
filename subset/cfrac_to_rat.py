#! /usr/bin/env python
#
def cfrac_to_rat ( n, a ):

#*****************************************************************************80
#
## CFRAC_TO_RAT converts a monic continued fraction to an ordinary fraction.
#
#  Discussion:
#
#    The routine is given the monic or "simple" continued fraction with
#    integer coefficients:
#
#      A(1) + 1 / ( A(2) + 1 / ( A(3) ... + 1 / A(N) ) )
#
#    and returns the N successive approximants P(I)/Q(I)
#    to the value of the rational number represented by the continued
#    fraction, with the value exactly equal to the final ratio P(N)/Q(N).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Hart, Cheney, Lawson, Maehly, Mesztenyi, Rice, Thacher, Witzgall,
#    Computer Approximations,
#    Wiley, 1968.
#
#  Parameters:
#
#    Input, integer N, the number of continued fraction coefficients.
#
#    Input, integer A(N), the continued fraction coefficients.
#
#    Output, integer P(N), Q(N), the N successive approximations
#    to the value of the continued fraction.
#
  import numpy as np

  p = np.zeros ( n )
  q = np.zeros ( n )

  for i in range ( 0, n ):

    if ( i == 0 ):
      p[i] = a[i] * 1 + 0
      q[i] = a[i] * 0 + 1
    elif ( i == 1 ):
      p[i] = a[i] * p[i-1] + 1
      q[i] = a[i] * q[i-1] + 0
    else:
      p[i] = a[i] * p[i-1] + p[i-2]
      q[i] = a[i] * q[i-1] + q[i-2]

  return p, q

def cfrac_to_rat_test ( ):

#*****************************************************************************80
#
#% CFRAC_TO_RAT_TEST tests CFRAC_TO_RAT.
#
#  Discussion:
#
#    Compute the continued fraction form of 4096/15625.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 May 2015
#
#  Author:
#
#    John Burkardt
#
  from rat_to_cfrac import rat_to_cfrac
  from i4vec_print import i4vec_print

  m = 10

  print ''
  print 'CFRAC_TO_RAT_TEST'
  print '  CFRAC_TO_RAT continued fraction => fraction.'
  print ''

  top = 4096
  bot = 15625

  print '  Regular fraction is %6d / %6d' % ( top, bot )
 
  n, a = rat_to_cfrac ( top, bot )
 
  i4vec_print ( n, a, '  Continued fraction coefficients:' )

  p, q = cfrac_to_rat ( n, a )
 
  print ''
  print '  The continued fraction convergents.'
  print '  The last row contains the value of the continued'
  print '  fraction, written as a common fraction.'
  print ''
  print '  I, P(I), Q(I), P(I)/Q(I)'
  print ''

  for i in range ( 0, n ):
    print '  %3d  %6d  %6d  %14f' % ( i, p[i], q[i], p[i] / q[i] )
#
#  Terminate.
#
  print ''
  print 'CFRAC_TO_RAT_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  cfrac_to_rat_test ( )
  timestamp ( )
