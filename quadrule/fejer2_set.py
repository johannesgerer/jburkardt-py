#! /usr/bin/env python
#
def fejer2_set ( n ):

#*****************************************************************************80
#
## FEJER2_SET sets abscissas and weights for Fejer type 2 quadrature.
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
       -0.5000000000000000, \
        0.5000000000000000 \
    ] )

    w = np.array ( [ \
      1.0000000000000000, \
      1.0000000000000000 \
    ] )

  elif ( n == 3 ):

    x = np.array ( [ \
      -0.7071067811865476, \
       0.0000000000000000, \
       0.7071067811865476 \
    ] )

    w = np.array ( [ \
      0.6666666666666666, \
      0.6666666666666666, \
      0.6666666666666666 \
    ] )

  elif ( n == 4 ):

    x = np.array ( [ \
      -0.8090169943749475, \
      -0.3090169943749475, \
       0.3090169943749475, \
       0.8090169943749475 \
    ] )

    w = np.array ( [ \
     0.4254644007500070, \
     0.5745355992499930, \
     0.5745355992499930, \
     0.4254644007500070 \
    ] )

  elif ( n == 5 ):

    x = np.array ( [ \
      -0.8660254037844387, \
      -0.5000000000000000, \
       0.0000000000000000, \
       0.5000000000000000, \
       0.8660254037844387 \
    ] )

    w = np.array ( [ \
     0.3111111111111111, \
     0.4000000000000000, \
     0.5777777777777777, \
     0.4000000000000000, \
     0.3111111111111111 \
    ] )

  elif ( n == 6 ):

    x = np.array ( [ \
      -0.9009688679024191, \
      -0.6234898018587336, \
      -0.2225209339563144, \
       0.2225209339563144, \
       0.6234898018587336, \
       0.9009688679024191 \
    ] )

    w = np.array ( [ \
     0.2269152467244296, \
     0.3267938603769863, \
     0.4462908928985841, \
     0.4462908928985841, \
     0.3267938603769863, \
     0.2269152467244296 \
    ] )

  elif ( n == 7 ):

    x = np.array ( [ \
      -0.9238795325112867, \
      -0.7071067811865476, \
      -0.3826834323650898, \
       0.0000000000000000, \
       0.3826834323650898, \
       0.7071067811865476, \
       0.9238795325112867 \
    ] )

    w = np.array ( [ \
     0.1779646809620499, \
     0.2476190476190476, \
     0.3934638904665215, \
     0.3619047619047619, \
     0.3934638904665215, \
     0.2476190476190476, \
     0.1779646809620499 \
    ] )

  elif ( n == 8 ):

    x = np.array ( [ \
      -0.9396926207859084, \
      -0.7660444431189780, \
      -0.5000000000000000, \
      -0.1736481776669304, \
       0.1736481776669304, \
       0.5000000000000000, \
       0.7660444431189780, \
       0.9396926207859084 \
    ] )

    w = np.array ( [ \
     0.1397697435050225, \
     0.2063696457302284, \
     0.3142857142857143, \
     0.3395748964790348, \
     0.3395748964790348, \
     0.3142857142857143, \
     0.2063696457302284, \
     0.1397697435050225 \
    ] )

  elif ( n == 9 ):

    x = np.array ( [ \
      -0.9510565162951535, \
      -0.8090169943749475, \
      -0.5877852522924731, \
      -0.3090169943749475, \
       0.0000000000000000, \
       0.3090169943749475, \
       0.5877852522924731, \
       0.8090169943749475, \
       0.9510565162951535 \
    ] )

    w = np.array ( [ \
     0.1147810750857217, \
     0.1654331942222276, \
     0.2737903534857068, \
     0.2790112502222170, \
     0.3339682539682539, \
     0.2790112502222170, \
     0.2737903534857068, \
     0.1654331942222276, \
     0.1147810750857217 \
    ] )

  elif ( n == 10 ):

    x = np.array ( [ \
      -0.9594929736144974, \
      -0.8412535328311812, \
      -0.6548607339452851, \
      -0.4154150130018864, \
      -0.1423148382732851, \
       0.1423148382732851, \
       0.4154150130018864, \
       0.6548607339452851, \
       0.8412535328311812, \
       0.9594929736144974 \
    ] )

    w = np.array ( [ \
     0.09441954173982806, \
     0.1411354380109716, \
     0.2263866903636005, \
     0.2530509772156453, \
     0.2850073526699544, \
     0.2850073526699544, \
     0.2530509772156453, \
     0.2263866903636005, \
     0.1411354380109716, \
     0.09441954173982806 \
    ] )

  else:

    print ''
    print 'FEJER2_SET - Fatal error!'
    print '  Illegal value of N = %d' % ( n )
    print '  Legal values are 1 through 10.'
    exit ( 'FEJER2_SET - Fatal error!' )

  return x, w

def fejer2_set_test ( ):

#*****************************************************************************80
#
## FEJER2_SET_TEST tests FEJER2_SET.
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
  print 'FEJER2_SET_TEST'
  print '  FEJER2_SET sets the abscissas and weights'
  print '  of a Fejer type 2 quadrature rule.'
  print ''
  print '    Order  W             X'
  print ''

  for n in range ( 1, 11 ):

    x, w = fejer2_set ( n )

    print ''
    print '  %8d' % ( n )

    for i in range ( 0, n ):
      print '            %12g  %12g' % ( w[i], x[i] )
#
#  Terminate.
#
  print ''
  print 'FEJER2_SET_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  fejer2_set_test ( )
  timestamp ( )
