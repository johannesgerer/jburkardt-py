#!/usr/bin/env python
#
def quadrature_set ( quad_num ):

#*****************************************************************************80
#
## QUADRATURE_SET sets abscissas and weights for Gauss-Legendre quadrature.
#
#  Discussion:
#
#    The integration interval is [ -1, 1 ].
#
#    The weight function w(x) = 1.0
#
#    The integral to approximate:
#
#      Integral ( -1 <= X <= 1 ) F(X) dX
#
#    Quadrature rule:
#
#      Sum ( 1 <= I <= QUAD_NUM ) QUAD_W(I) * F ( QUAD_X(I) )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 November 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer QUAD_NUM, the order of the rule.
#    QUAD_NUM must be between 1 and 6.
#
#    Output, real QUAD_W(QUAD_NUM), the weights of the rule.
#
#    Output, real QUAD_X(QUAD_NUM), the abscissas of the rule.
#
  from sys import exit
  import numpy as np

  if ( quad_num == 1 ):

    quad_x = np.array ( [ \
      0.0 ] )

    quad_w = np.array ( [ \
      2.0 ] )

  elif ( quad_num == 2 ):

    quad_x = np.array ( [ \
      - 0.577350269189625764509148780502, \
        0.577350269189625764509148780502 ] )

    quad_w = np.array ( [ \
      1.0, \
      1.0 ] )

  elif ( quad_num == 3 ):

    quad_x = np.array ( [ \
      - 0.774596669241483377035853079956, \
        0.0, \
        0.774596669241483377035853079956 ] )

    quad_w = np.array ( [ \
      5.0 / 9.0, \
      8.0 / 9.0, \
      5.0 / 9.0 ] )

  elif ( quad_num == 4 ):

    quad_x = np.array ( [ \
      - 0.861136311594052575223946488893, \
      - 0.339981043584856264802665759103, \
        0.339981043584856264802665759103, \
        0.861136311594052575223946488893 ] )

    quad_w = np.array ( [ \
      0.347854845137453857373063949222, \
      0.652145154862546142626936050778, \
      0.652145154862546142626936050778, \
      0.347854845137453857373063949222 ] )

  elif ( quad_num == 5 ):

    quad_x = np.array ( [ \
      - 0.906179845938663992797626878299, \
      - 0.538469310105683091036314420700, \
        0.0, \
        0.538469310105683091036314420700, \
        0.906179845938663992797626878299 ] )

    quad_w = np.array ( [ \
      0.236926885056189087514264040720, \
      0.478628670499366468041291514836, \
      0.568888888888888888888888888889, \
      0.478628670499366468041291514836, \
      0.236926885056189087514264040720 ] )

  elif ( quad_num == 6 ):
    quad_x = np.array ( [ \
      - 0.932469514203152027812301554494, \
      - 0.661209386466264513661399595020, \
      - 0.238619186083196908630501721681, \
        0.238619186083196908630501721681, \
        0.661209386466264513661399595020, \
        0.932469514203152027812301554494 ] )

    quad_w = np.array ( [ \
      0.171324492379170345040296142173, \
      0.360761573048138607569833513838, \
      0.467913934572691047389870343990, \
      0.467913934572691047389870343990, \
      0.360761573048138607569833513838, \
      0.171324492379170345040296142173 ] )

  else:

    print ''
    print 'QUADRATURE_SET - Fatal error!'
    print '  The requested order %d is not available.' % ( quad_num )
    exit ( 'QUADRATURE_SET - Fatal error!' )

  return quad_w, quad_x

def quadrature_set_test ( ):

#*****************************************************************************80
#
## QUADRATURE_SET_TEST tests QUADRATURE_SET.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 November 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ''
  print 'QUADRATURE_SET_TEST'
  print '  QUADRATURE_SET returns points and weights for a quadrature rule.'

  quad_num = 4
  quad_w, quad_x = quadrature_set ( quad_num )

  print ''
  print '   I      W[i]    X[i]'
  print ''
  for i in range ( 0, quad_num ):
    print '  %2d  %8.4f  %8.4f' % ( i, quad_w[i], quad_x[i] )

  print ''
  print 'QUADRATURE_SET_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp

  timestamp ( )
  quadrature_set_test ( )
  timestamp ( )

