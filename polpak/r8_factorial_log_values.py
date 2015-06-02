#!/usr/bin/env python
#
def r8_factorial_log_values ( n_data ):

#*****************************************************************************80
#
## R8_FACTORIAL_LOG_VALUES returns values of log(n!).
#
#  Discussion:
#
#    The function log(n!) can be written as
#
#     log(n!) = sum ( 1 <= i <= n ) log ( i )
#
#    In Mathematica, the function can be evaluated by:
#
#      Log[n!]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#    Daniel Zwillinger, editor,
#    CRC Standard Mathematical Tables and Formulae,
#    30th Edition,
#    CRC Press, 1996.
#
#  Parameters:
#
#    Input/output, integer N_DATA.  The user sets N_DATA to 0 before the
#    first call.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, integer N, the argument of the function.
#
#    Output, real F, the value of the function.
#
  import numpy as np

  n_max = 27

  f_vec = np.array ( ( \
     0.0000000000000000E+00, \
     0.0000000000000000E+00, \
     0.6931471805599453E+00, \
     0.1791759469228055E+01, \
     0.3178053830347946E+01, \
     0.4787491742782046E+01, \
     0.6579251212010101E+01, \
     0.8525161361065414E+01, \
     0.1060460290274525E+02, \
     0.1280182748008147E+02, \
     0.1510441257307552E+02, \
     0.1750230784587389E+02, \
     0.1998721449566189E+02, \
     0.2255216385312342E+02, \
     0.2519122118273868E+02, \
     0.2789927138384089E+02, \
     0.3067186010608067E+02, \
     0.3350507345013689E+02, \
     0.3639544520803305E+02, \
     0.3933988418719949E+02, \
     0.4233561646075349E+02, \
     0.5800360522298052E+02, \
     0.1484777669517730E+03, \
     0.3637393755555635E+03, \
     0.6050201058494237E+03, \
     0.2611330458460156E+04, \
     0.5912128178488163E+04 ))

  n_vec = np.array ( ( \
       0, \
       1, \
       2, \
       3, \
       4, \
       5, \
       6, \
       7, \
       8, \
       9, \
      10, \
      11, \
      12, \
      13, \
      14, \
      15, \
      16, \
      17, \
      18, \
      19, \
      20, \
      25, \
      50, \
     100, \
     150, \
     500, \
    1000 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    f = 0
  else:
    n = n_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, n, f

def r8_factorial_log_values_test ( ):

#*****************************************************************************80
#
## R8_FACTORIAL_LOG_VALUES_TEST tests R8_FACTORIAL_LOG_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'R8_FACTORIAL_LOG_VALUES_TEST:'
  print '  R8_FACTORIAL_LOG_VALUES returns values of the log factorial function.'
  print ''
  print '          N          R8_FACTORIAL_LOG(N)'
  print ''

  n_data = 0

  while ( True ):

    n_data, n, fn = r8_factorial_log_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %8d  %14.6g' % ( n, fn )

  print ''
  print 'R8_FACTORIAL_LOG_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_factorial_log_values_test ( )
  timestamp ( )

