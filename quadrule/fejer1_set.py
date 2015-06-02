#! /usr/bin/env python
#
def fejer1_set ( n ):

#*****************************************************************************80
#
## FEJER1_SET sets abscissas and weights for Fejer type 1 quadrature.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Philip Davis, Philip Rabinowitz,
#    Methods of Numerical Integration,
#    Second Edition,
#    Dover, 2007,
#    ISBN: 0486453391,
#    LC: QA299.3.D28.
#
#    Walter Gautschi,
#    Numerical Quadrature in the Presence of a Singularity,
#    SIAM Journal on Numerical Analysis,
#    Volume 4, Number 3, 1967, pages 357-362.
#
#    Joerg Waldvogel,
#    Fast Construction of the Fejer and Clenshaw-Curtis Quadrature Rules,
#    BIT Numerical Mathematics,
#    Volume 43, Number 1, 2003, pages 1-18.
#
#  Parameters:
#
#    Input, integer N, the order.
#    N should be between 1 and 10.
#
#    Output, real X(N), the abscissas.
#
#    Output, real W(N), the weights.
#
  import numpy as np
  from sys import exit

  if ( n == 1 ):

    x = np.array ( [ \
      0.000000000000000 \
    ] )

    w = np.array ( [ \
      2.000000000000000 \
    ] )

  elif ( n == 2 ):

    x = np.array ( [ \
       -0.7071067811865475, \
        0.7071067811865475 \
    ] )

    w = np.array ( [ \
      1.000000000000000, \
      1.000000000000000 \
    ] )

  elif ( n == 3 ):

    x = np.array ( [ \
      -0.8660254037844387, \
       0.0000000000000000, \
       0.8660254037844387 \
    ] )

    w = np.array ( [ \
      0.4444444444444444, \
      1.111111111111111, \
      0.4444444444444444 \
    ] )

  elif ( n == 4 ):

    x = np.array ( [ \
      -0.9238795325112867, \
      -0.3826834323650897, \
       0.3826834323650898, \
       0.9238795325112867 \
    ] )

    w = np.array ( [ \
     0.2642977396044841, \
     0.7357022603955158, \
     0.7357022603955158, \
     0.2642977396044841 \
    ] )

  elif ( n == 5 ):

    x = np.array ( [ \
      -0.9510565162951535, \
      -0.5877852522924730, \
       0.0000000000000000, \
       0.5877852522924731, \
       0.9510565162951535 \
    ] )

    w = np.array ( [ \
      0.1677812284666835, \
      0.5255521048666498, \
      0.6133333333333333, \
      0.5255521048666498, \
      0.1677812284666835 \
    ] )

  elif ( n == 6 ):

    x = np.array ( [ \
       -0.9659258262890682, \
       -0.7071067811865475, \
       -0.2588190451025206, \
        0.2588190451025207, \
        0.7071067811865476, \
        0.9659258262890683 \
    ] )

    w = np.array ( [ \
      0.1186610213812358, \
      0.3777777777777778, \
      0.5035612008409863, \
      0.5035612008409863, \
      0.3777777777777778, \
      0.1186610213812358 \
    ] )

  elif ( n == 7 ):

    x = np.array ( [ \
       -0.9749279121818237, \
       -0.7818314824680295, \
       -0.4338837391175581, \
        0.0000000000000000, \
        0.4338837391175582, \
        0.7818314824680298, \
        0.9749279121818236 \
    ] )

    w = np.array ( [ \
     0.08671618072672234, \
     0.2878313947886919, \
     0.3982415401308441, \
     0.4544217687074830, \
     0.3982415401308441, \
     0.2878313947886919, \
     0.08671618072672234 \
    ] )

  elif ( n == 8 ):

    x = np.array ( [ \
      -0.9807852804032304, \
      -0.8314696123025453, \
      -0.5555702330196020, \
      -0.1950903220161282, \
       0.1950903220161283, \
       0.5555702330196023, \
       0.8314696123025452, \
       0.9807852804032304 \
    ] )

    w = np.array ( [ \
     0.06698294569858981, \
     0.2229879330145788, \
     0.3241525190645244, \
     0.3858766022223071, \
     0.3858766022223071, \
     0.3241525190645244, \
     0.2229879330145788, \
     0.06698294569858981 \
    ] )

  elif ( n == 9 ):

    x = np.array ( [ \
      -0.9848077530122080, \
      -0.8660254037844385, \
      -0.6427876096865394, \
      -0.3420201433256685, \
       0.0000000000000000, \
       0.3420201433256688, \
       0.6427876096865394, \
       0.8660254037844387, \
       0.9848077530122080 \
    ] )

    w = np.array ( [ \
     0.05273664990990676, \
     0.1791887125220458, \
     0.2640372225410044, \
     0.3308451751681364, \
     0.3463844797178130, \
     0.3308451751681364, \
     0.2640372225410044, \
     0.1791887125220458, \
     0.05273664990990676 \
    ] )

  elif ( n == 10 ):

    x = np.array ( [ \
      -0.9876883405951377, \
      -0.8910065241883678, \
      -0.7071067811865475, \
      -0.4539904997395467, \
      -0.1564344650402306, \
       0.1564344650402309, \
       0.4539904997395468, \
       0.7071067811865476, \
       0.8910065241883679, \
       0.9876883405951378 \
    ] )

    w = np.array ( [ \
     0.04293911957413078, \
     0.1458749193773909, \
     0.2203174603174603, \
     0.2808792186638755, \
     0.3099892820671425, \
     0.3099892820671425, \
     0.2808792186638755, \
     0.2203174603174603, \
     0.1458749193773909, \
     0.04293911957413078 \
    ] )

  else:

    print ''
    print 'FEJER1_SET - Fatal error!'
    print '  Illegal value of N = %d' % ( n )
    print '  Legal values are 1 through 10.'
    exit ( 'FEJER1_SET - Fatal error!' )

  return x, w

def fejer1_set_test ( ):

#*****************************************************************************80
#
## FEJER1_SET_TEST tests FEJER1_SET.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    15 April 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'FEJER1_SET_TEST'
  print '  FEJER1_SET sets the abscissas and weights'
  print '  of a Fejer type 1 quadrature rule.'
  print ''
  print '    Order  W             X'
  print ''

  for n in range ( 1, 11 ):

    x, w = fejer1_set ( n )

    print ''
    print '  %8d' % ( n )

    for i in range ( 0, n ):
      print '            %12g  %12g' % ( w[i], x[i] )
#
#  Terminate.
#
  print ''
  print 'FEJER1_SET_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  fejer1_set_test ( )
  timestamp ( )
