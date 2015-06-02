#!/usr/bin/env python
#
def trinomial ( i, j, k ):

#*****************************************************************************80
#
## TRINOMIAL computes a trinomial coefficient.
#
#  Discussion:
#
#    The trinomial coefficient is a generalization of the binomial
#    coefficient.  It may be interpreted as the number of combinations of
#    N objects, where I objects are of type 1, J of type 2, and K of type 3.
#    and N = I + J + K.
#
#    T(I,J,K) = N! / ( I! J! K! )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer I, J, K, the factors.
#    All should be nonnegative.
#
#    Output, integer VALUE, the trinomial coefficient.
#
  from sys import exit
#
#  Each factor must be nonnegative.
#
  if ( i < 0 or j < 0 or k < 0 ):
    print ''
    print 'TRINOMIAL - Fatal error!'
    print '  Negative factor encountered.'
    exit ( 'TRINOMIAL - Fatal error!' )

  value = 1

  t = 1

  for l in range ( 1, i + 1 ):
#   value = value * t // l
    t = t + 1

  for l in range ( 1, j + 1 ):
    value = value * t // l
    t = t + 1

  for l in range ( 1, k + 1 ):
    value = value * t // l
    t = t + 1
  
  return value

def trinomial_test ( ):

#*****************************************************************************80
#
## TRINOMIAL_TEST tests TRINOMIAL.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    11 April 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'TRINOMIAL_TEST'
  print '  TRINOMIAL evaluates the trinomial coefficient:'
  print ''
  print '  T(I,J,K) = (I+J+K)! / I! / J! / K!'
  print ''
  print '     I     J     K    T(I,J,K)'
  print ''
 
  for k in range ( 0, 5 ):
    for j in range ( 0, 5 ):
      for i in range ( 0, 5 ):
        t = trinomial ( i, j, k )
        print '  %4d  %4d  %4d  %8d' % ( i, j, k, t )
#
#  Terminate.
#
  print ''
  print 'TRINOMIAL_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  trinomial_test ( )
  timestamp ( )
