#! /usr/bin/env python
#
def moulton_set ( n ):

#*****************************************************************************80
#
## MOULTON_SET sets weights for Adams-Moulton quadrature.
#
#  Discussion:
#
#    Adams-Moulton quadrature formulas are normally used in solving
#    ordinary differential equations, and are not suitable for general
#    quadrature computations.  However, an Adams-Moulton formula is
#    equivalent to approximating the integral of F(Y(X)) between X(M)
#    and X(M+1), using an implicit formula that relies on known values
#    of F(Y(X)) at X(M-N+1) through X(M), plus the unknown value at X(M+1).
#
#    Suppose the unknown function is denoted by Y(X), with derivative F(Y(X)),
#    and that approximate values of the function are known at a series of
#    X values, which we write as X(1), X(2), ..., X(M).  We write the value
#    Y(X(1)) as Y(1) and so on.
#
#    Then the solution of the ODE Y' = F(X,Y) at the next point X(M+1) is
#    computed by:
#
#      Y(M+1) = Y(M) + Integral ( X(M) < X < X(M+1) ) F(Y(X)) dX
#             = Y(M) + H * Sum ( 1 <= I <= N ) W(I) * F(Y(M+2-I)) approximately.
#
#    Note that this formula is implicit, since the unknown value Y(M+1)
#    appears on the right hand side.  Hence, in ODE applications, this
#    equation must be solved via a nonlinear equation solver.  For
#    quadrature problems, where the function to be integrated is known
#    beforehand, this is not a problem, and the calculation is explicit.
#
#    In the documentation that follows, we replace F(Y(X)) by F(X).
#
#
#    The Adams-Moulton formulas require equally spaced data.
#
#    Here is how the formula is applied in the case with non-unit spacing:
#
#      Integral ( A <= X <= A+H ) F(X) dX =
#      H * Sum ( 1 <= I <= N ) W(I) * F ( A - (I-2)*H ),
#      approximately.
#
#    The integral:
#
#      Integral ( 0 <= X <= 1 ) F(X) dX
#
#    The quadrature rule:
#
#      Sum ( 1 <= I <= N ) W(I) * F ( 2 - I )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    National Bureau of Standards, 1964,
#    page 915 ("Lagrangian Integration Coefficients").
#
#    Jean Lapidus and John Seinfeld,
#    Numerical Solution of Ordinary Differential Equations,
#    Academic Press, 1971.
#
#    Daniel Zwillinger, editor,
#    Standard Mathematical Tables and Formulae,
#    30th Edition,
#    CRC Press, 1996.
#
#  Parameters:
#
#    Input, integer N, the order.
#    N must be between 1 and 10, 12, 14, 16, 18 or 20.
#
#    Output, real X(N), the abscissas.
#
#    Output, real W(N), the weights.
#    W(1) is the weight at X = 1, W(2) the weight at X = 0, and so on.
#    The weights are rational.  The weights are not symmetric, and
#    some weights may be negative.  They should sum to 1.
#
  import numpy as np
  from sys import exit

  x = np.zeros ( n )
  w = np.zeros ( n )

  if ( n == 1 ):

    d = 1.0

    w = np.array ( [ \
       1.0 \
    ] )

  elif ( n == 2 ):

    d = 2.0

    w = np.array ( [ \
      1.0, \
      1.0 \
    ] )

  elif ( n == 3 ):

    d = 12.0

    w = np.array ( [ \
        5.0, \
        8.0, \
      - 1.0 \
    ] )

  elif ( n == 4 ):

    d = 24.0

    w = np.array ( [ \
        9.0, \
       19.0, \
      - 5.0, \
        1.0 \
    ] )

  elif ( n == 5 ):

    d = 720.0

    w = np.array ( [ \
        251.0, \
        646.0, \
      - 264.0, \
        106.0, \
       - 19.0 \
    ] )

  elif ( n == 6 ):

    d = 1440.0

    w = np.array ( [ \
        475.0, \
       1427.0, \
      - 798.0, \
        482.0, \
      - 173.0, \
         27.0 \
    ] )

  elif ( n == 7 ):

    d = 60480.0

    w = np.array ( [ \
        19087.0, \
        65112.0, \
      - 46461.0, \
        37504.0, \
      - 20211.0, \
         6312.0, \
        - 863.0 \
    ] )

  elif ( n == 8 ):

    d = 120960.0

    w = np.array ( [ \
        36799.0, \
       139849.0, \
     - 121797.0, \
       123133.0, \
      - 88547.0, \
        41499.0, \
      - 11351.0, \
         1375.0 \
    ] )

  elif ( n == 9 ):
  
    d = 3628800.0

    w = np.array ( [ \
       1070017.0, \
       4467094.0, \
     - 4604594.0, \
       5595358.0, \
     - 5033120.0, \
       3146338.0, \
     - 1291214.0, \
        312874.0, \
       - 33953.0 \
    ] )
  
  elif ( n == 10 ):
  
    d = 7257600.0

    w = np.array ( [ \
        2082753.0, \
        9449717.0, \
     - 11271304.0, \
       16002320.0, \
     - 17283646.0, \
       13510082.0, \
      - 7394032.0, \
        2687864.0, \
       - 583435.0, \
          57281.0 \
    ] )
  
  elif ( n == 12 ):
  
    d = 958003200.0

    w = np.array ( [ \
        262747265.0, \
       1374799219.0, \
      -2092490673.0, \
       3828828885.0, \
      -5519460582.0, \
       6043521486.0, \
      -4963166514.0, \
       3007739418.0, \
      -1305971115.0, \
        384709327.0, \
        -68928781.0, \
          5675265.0 \
    ] )
  
  elif ( n == 14 ):
  
    d = 5230697472000.0

    w = np.array ( [ \
        1382741929621.0, \
        8153167962181.0, \
      -15141235084110.0, \
       33928990133618.0, \
      -61188680131285.0, \
       86180228689563.0, \
      -94393338653892.0, \
       80101021029180.0, \
      -52177910882661.0, \
       25620259777835.0, \
       -9181635605134.0, \
        2268078814386.0, \
        -345457086395.0, \
          24466579093.0 \
    ] )
  
  elif ( n == 16 ):
  
    d = 62768369664000.0

    w = np.array ( [ \
         16088129229375.0, \
        105145058757073.0, \
       -230992163723849.0, \
        612744541065337.0, \
      -1326978663058069.0, \
       2285168598349733.0, \
      -3129453071993581.0, \
       3414941728852893.0, \
      -2966365730265699.0, \
       2039345879546643.0, \
      -1096355235402331.0, \
        451403108933483.0, \
       -137515713789319.0, \
         29219384284087.0, \
         -3867689367599.0, \
           240208245823.0 \
    ] )
  
  elif ( n == 18 ):
  
    d = 64023737057280000.0

    w = np.array ( [ \
          15980174332775873.0, \
         114329243705491117.0, \
        -290470969929371220.0, \
         890337710266029860.0, \
       -2250854333681641520.0, \
        4582441343348851896.0, \
       -7532171919277411636.0, \
       10047287575124288740.0, \
      -10910555637627652470.0, \
        9644799218032932490.0, \
       -6913858539337636636.0, \
        3985516155854664396.0, \
       -1821304040326216520.0, \
         645008976643217360.0, \
        -170761422500096220.0, \
          31816981024600492.0, \
          -3722582669836627.0, \
            205804074290625.0 \
    ] )
  
  elif ( n == 20 ):
  
    d = 102181884343418880000.0

    w = np.array ( [ \
           24919383499187492303.0, \
          193280569173472261637.0, \
         -558160720115629395555.0, \
         1941395668950986461335.0, \
        -5612131802364455926260.0, \
        13187185898439270330756.0, \
       -25293146116627869170796.0, \
        39878419226784442421820.0, \
       -51970649453670274135470.0, \
        56154678684618739939910.0, \
       -50320851025594566473146.0, \
        37297227252822858381906.0, \
       -22726350407538133839300.0, \
        11268210124987992327060.0, \
        -4474886658024166985340.0, \
         1389665263296211699212.0, \
         -325187970422032795497.0, \
           53935307402575440285.0, \
           -5652892248087175675.0, \
             281550972898020815.0 \
      ] )

  else:

    print ''
    print 'MOULTON_SET - Fatal error!'
    print '  Illegal value of N = %d' % ( n )
    print '  Legal values are 1 through 10,'
    print '  or 12, 14, 16, 18 or 20.'
    exit ( 'MOULTON_SET - Fatal error!' )

  for i in range ( 0, n ):
    w[i] = w[i] / d

  for i in range ( 0, n ):
    x[i] = float ( 1 - i )

  return x, w

def moulton_set_test ( ):

#*****************************************************************************80
#
## MOULTON_SET_TEST tests MOULTON_SET.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    18 April 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'MOULTON_SET_TEST'
  print '  MOULTON_SET sets the abscissas and weights'
  print '  for an Adams-Moulton quadrature rule.'
  print ''
  print '    Order  W             X'
  print ''

  for n in range ( 1, 11 ):

    x, w = moulton_set ( n )

    print ''
    print '  %8d' % ( n )

    for i in range ( 0, n ):
      print '            %12g  %12g' % ( w[i], x[i] )
#
#  Terminate.
#
  print ''
  print 'MOULTON_SET_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  moulton_set_test ( )
  timestamp ( )
