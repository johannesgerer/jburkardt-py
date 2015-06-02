#!/usr/bin/env python
#
def hyper_1f1_values ( n_data ):

#*****************************************************************************80
#
## HYPER_1F1_VALUES returns some values of the hypergeometric 1F1 function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      fx = Hypergeometric1F1 [ a, b, x ]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz, Irene Stegun,
#    Handbook of Mathematical Functions,
#    National Bureau of Standards, 1964,
#    ISBN: 0-486-61272-4,
#    LC: QA47.A34.
#
#    Shanjie Zhang, Jianming Jin,
#    Computation of Special Functions,
#    Wiley, 1996,
#    ISBN: 0-471-11963-6,
#    LC: QA351.C45
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Cambridge University Press, 1999,
#    ISBN: 0-521-64314-7,
#    LC: QA76.95.W65.
#
#    Daniel Zwillinger, editor,
#    CRC Standard Mathematical Tables and Formulae,
#    30th Edition,
#    CRC Press, 1996,
#    ISBN: 0-8493-2479-3,
#    LC: QA47.M315.
#
#  Parameters:
#
#    Input/output, integer N_DATA.  The user sets N_DATA to 0 before the
#    first call.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, real A, B, X, the parameters.
#
#    Output, real F, the value of the function.
#
  import numpy as np

  n_max = 24

  a_vec = np.array ( (\
    -2.500, \
    -0.500, \
     0.500, \
     2.500, \
    -2.500, \
    -0.500, \
     0.500, \
     2.500, \
    -2.500, \
    -0.500, \
     0.500, \
     2.500, \
     0.825, \
     1.100, \
     1.650, \
     3.300, \
     0.825, \
     1.100, \
     1.650, \
     3.300, \
     0.825, \
     1.100, \
     1.650, \
     3.300 ))
  b_vec = np.array ( (\
     3.3, \
     1.1, \
     1.1, \
     3.3, \
     3.3, \
     1.1, \
     1.1, \
     3.3, \
     3.3, \
     1.1, \
     1.1, \
     3.3, \
     6.7, \
     6.7, \
     6.7, \
     6.7, \
     6.7, \
     6.7, \
     6.7, \
     6.7, \
     6.7, \
     6.7, \
     6.7, \
     6.7 ))
  f_vec = np.array ( (\
     0.81879926689265186854, \
     0.88283984828032972070, \
     1.1245023764952626690, \
     1.2101049301639599598, \
     0.12723045536781567174, \
     0.12326016871544045107, \
     2.3297954665128293051, \
     3.3890020264468009733, \
    -0.18819510282516768874, \
    -1.0764203806547022727, \
     5.7521824680907968433, \
     9.9998567403304086593, \
     1.0317208964319891384, \
     1.0424867029249952040, \
     1.0643112000949092012, \
     1.1321844369742336326, \
     1.2328402688568452181, \
     1.3200654482027340732, \
     1.5104811522310825217, \
     2.2307520785940524365, \
     1.5197286298183137741, \
     1.7364938170250847619, \
     2.2492330307668135926, \
     4.6377737119178965298 ))
  x_vec = np.array ( (\
     0.25, \
     0.25, \
     0.25, \
     0.25, \
     1.55, \
     1.55, \
     1.55, \
     1.55, \
     2.85, \
     2.85, \
     2.85, \
     2.85, \
     0.25, \
     0.25, \
     0.25, \
     0.25, \
     1.55, \
     1.55, \
     1.55, \
     1.55, \
     2.85, \
     2.85, \
     2.85, \
     2.85 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    a = 0.0
    b = 0,0
    x = 0.0
    f = 0.0
  else:
    a = a_vec[n_data]
    b = b_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, a, b, x, f

def hyper_1f1_values_test ( ):

#*****************************************************************************80
#
## HYPER_1F1_VALUES_TEST demonstrates the use of HYPER_1F1_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'HYPER_1F1_VALUES_TEST:'
  print '  HYPER_1F1_VALUES stores values of the hypergeometric function 1F1'
  print ''
  print '     A     B        X               F'
  print ''

  n_data = 0

  while ( True ):

    n_data, a, b, x, f = hyper_1f1_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %12g  %12g  %12g  %24.16g' % ( a, b, x, f )

  print ''
  print 'HYPER_1F1_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  hyper_1f1_values_test ( )
  timestamp ( )
