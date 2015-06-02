#! /usr/bin/env python
#
def bashforth_set ( n ):

#*****************************************************************************80
#
## BASHFORTH_SET sets abscissas and weights for Adams-Bashforth quadrature.
#
#  Discussion:
#
#    Adams-Bashforth quadrature formulas are normally used in solving
#    ordinary differential equations, and are not really suitable for
#    general quadrature computations.  However, an Adams-Bashforth formula
#    is equivalent to approximating the integral of F(Y(X)) between X(M)
#    and X(M+1), using an explicit formula that relies only on known values
#    of F(Y(X)) at X(M-N+1) through X(M).  For this reason, the formulas
#    have been included here.
#
#    Suppose the unknown function is denoted by Y(X), with derivative
#    F(Y(X)), and that approximate values of the function are known at a
#    series of X values, which we write as X(1), X(2), ..., X(M).  We write
#    the value Y(X(1)) as Y(1) and so on.
#
#    Then the solution of the ODE Y'=F(X,Y) at the next point X(M+1) is
#    computed by:
#
#      Y(M+1) = Y(M) + Integral ( X(M) < X < X(M+1) ) F(Y(X)) dX
#             = Y(M) + H * Sum ( 1 <= I <= N ) W(I) * F(Y(M+1-I)) approximately.
#
#    In the documentation that follows, we replace F(Y(X)) by F(X).
#
#    The integral:
#
#      Integral ( 0 <= X <= 1 ) F(X) dX.
#
#    The quadrature rule:
#
#      Sum ( 1 <= I <= N ) W(I) * F ( 1 - I ),
#
#    The Adams-Bashforth formulas require equally spaced data.
#
#    Here is how the formula is applied in the case with non-unit spacing:
#
#      Integral ( A <= X <= A+H ) F(X) dX =
#      H * Sum ( 1 <= I <= N ) W(I) * F ( A - (I-1)*H ),
#      approximately.
#
#    The reference lists the second coefficient of the order 8 Adams-Bashforth
#    formula as
#      w(2) =  -1162169.0 / 120960.0
#    but this should be
#      w(2) =  -1152169.0 / 120960.0
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz, Irene Stegun,
#    Handbook of Mathematical Functions,
#    National Bureau of Standards, 1964.
#
#    Jean Lapidus, John Seinfeld,
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
#    N should be between 1 and 10, or 12, 14, 16, 18 or 20.
#
#    Output, real X(N), the abscissas.
#
#    Output, real W(N), the weights.
#    W(1) is the weight at X = 0, W(2) the weight at X = -1,
#    and so on.  The weights are rational, and should sum to 1.  Some
#    weights may be negative.
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
       3.0, \
     - 1.0 \
    ] )

  elif ( n == 3 ):

    d = 12.0

    w = np.array ( [ \
       23.0, \
     - 16.0, \
        5.0 \
    ] )

  elif ( n == 4 ):

    d = 24.0

    w = np.array ( [ \
       55.0, \
     - 59.0, \
       37.0, \
      - 9.0 \
    ] )

  elif ( n == 5 ):

    d = 720.0

    w = np.array ( [ \
       1901.0, \
     - 2774.0, \
       2616.0, \
     - 1274.0, \
        251.0 \
    ] )

  elif ( n == 6 ):

    d = 1440.0

    w = np.array ( [ \
       4277.0, \
     - 7923.0, \
       9982.0, \
     - 7298.0, \
       2877.0, \
      - 475.0 \
    ] )

  elif ( n == 7 ):

    d = 60480.0

    w = np.array ( [ \
        198721.0, \
      - 447288.0, \
        705549.0, \
      - 688256.0, \
        407139.0, \
      - 134472.0, \
         19087.0 \
    ] )

  elif ( n == 8 ):

    d = 120960.0

    w = np.array ( [ \
         434241.0, \
      - 1152169.0, \
        2183877.0, \
      - 2664477.0, \
        2102243.0, \
      - 1041723.0, \
         295767.0, \
        - 36799.0 \
    ] )

  elif ( n == 9 ):
  
    d = 3628800.0

    w = np.array ( [ \
       14097247.0, \
      -43125206.0, \
       95476786.0, \
     -139855262.0, \
      137968480.0, \
      -91172642.0, \
       38833486.0, \
       -9664106.0, \
        1070017.0 \
    ] )
  
  elif ( n == 10 ):
  
    d = 7257600.0

    w = np.array ( [ \
       30277247.0, \
     -104995189.0, \
      265932680.0, \
     -454661776.0, \
      538363838.0, \
     -444772162.0, \
      252618224.0, \
      -94307320.0, \
       20884811.0, \
       -2082753.0 \
    ] )
  
  elif ( n == 12 ):
  
    d = 958003200.0

    w = np.array ( [ \
        4527766399.0, \
      -19433810163.0, \
       61633227185.0, \
     -135579356757.0, \
      214139355366.0, \
     -247741639374.0, \
      211103573298.0, \
     -131365867290.0, \
       58189107627.0, \
      -17410248271.0, \
        3158642445.0, \
        -262747265.0 \
    ] )
  
  elif ( n == 14 ):
  
    d = 5230697472000.0

    w = np.array ( [ \
        27511554976875.0, \
      -140970750679621.0, \
       537247052515662.0, \
     -1445313351681906.0, \
      2854429571790805.0, \
     -4246767353305755.0, \
      4825671323488452.0, \
     -4204551925534524.0, \
      2793869602879077.0, \
     -1393306307155755.0, \
       505586141196430.0, \
      -126174972681906.0, \
        19382853593787.0, \
        -1382741929621.0 \
    ] )
  
  elif ( n == 16 ):
  
    d = 62768369664000.0

    w = np.array ( [ \
         362555126427073.0, \
       -2161567671248849.0, \
        9622096909515337.0, \
      -30607373860520569.0, \
       72558117072259733.0, \
     -131963191940828581.0, \
      187463140112902893.0, \
     -210020588912321949.0, \
      186087544263596643.0, \
     -129930094104237331.0, \
       70724351582843483.0, \
      -29417910911251819.0, \
        9038571752734087.0, \
       -1934443196892599.0, \
         257650275915823.0, \
         -16088129229375.0 \
    ] )
  
  elif ( n == 18 ):
  
    d = 64023737057280000.0

    w = np.array ( [ \
         401972381695456831.0, \
       -2735437642844079789.0, \
       13930159965811142228.0, \
      -51150187791975812900.0, \
      141500575026572531760.0, \
     -304188128232928718008.0, \
      518600355541383671092.0, \
     -710171024091234303204.0, \
      786600875277595877750.0, \
     -706174326992944287370.0, \
      512538584122114046748.0, \
     -298477260353977522892.0, \
      137563142659866897224.0, \
      -49070094880794267600.0, \
       13071639236569712860.0, \
       -2448689255584545196.0, \
         287848942064256339.0, \
         -15980174332775873.0 \
    ] )
  
  elif ( n == 20 ):
  
    d = 102181884343418880000.0

    w = np.array ( [ \
          691668239157222107697.0, \
        -5292843584961252933125.0, \
        30349492858024727686755.0, \
      -126346544855927856134295.0, \
       399537307669842150996468.0, \
      -991168450545135070835076.0, \
      1971629028083798845750380.0, \
     -3191065388846318679544380.0, \
      4241614331208149947151790.0, \
     -4654326468801478894406214.0, \
      4222756879776354065593786.0, \
     -3161821089800186539248210.0, \
      1943018818982002395655620.0, \
      -970350191086531368649620.0, \
       387739787034699092364924.0, \
      -121059601023985433003532.0, \
        28462032496476316665705.0, \
        -4740335757093710713245.0, \
          498669220956647866875.0, \
          -24919383499187492303.0 \
      ] )

  else:

    print ''
    print 'BASHFORTH_SET - Fatal error!'
    print '  Illegal value of N = %d' % ( n )
    print '  Legal values are 1 through 10,'
    print '  or 12, 14, 16, 18 or 20.'
    exit ( 'BASHFORTH_SET - Fatal error!' )

  for i in range ( 0, n ):
    w[i] = w[i] / d

  for i in range ( 0, n ):
    x[i] = - float ( i )

  return x, w

def bashforth_set_test ( ):

#*****************************************************************************80
#
## BASHFORTH_SET_TEST tests BASHFORTH_SET.
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
  print 'BASHFORTH_SET_TEST'
  print '  BASHFORTH_SET sets the abscissas and weights'
  print '  for an Adams-Bashforth quadrature rule.'
  print ''
  print '    Order  W             X'
  print ''

  for n in range ( 1, 11 ):

    x, w = bashforth_set ( n )

    print ''
    print '  %8d' % ( n )

    for i in range ( 0, n ):
      print '            %12g  %12g' % ( w[i], x[i] )
#
#  Terminate.
#
  print ''
  print 'BASHFORTH_SET_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  bashforth_set_test ( )
  timestamp ( )
