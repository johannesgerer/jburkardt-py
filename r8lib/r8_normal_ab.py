#!/usr/bin/env python 

def r8_normal_ab ( a, b, seed ):

#*****************************************************************************80
#
## R8_NORMAL_AB returns a scaled pseudonormal R8.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    25 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, the mean of the normal PDF.
#
#    Input, real B, the standard deviation of the normal PDF.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real X, a sample of the standard normal PDF.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  from r8_normal_01 import r8_normal_01

  x, seed = r8_normal_01 ( seed )
  x = a + b * x

  return x, seed

def r8_normal_ab_test ( ):

#*****************************************************************************80
#
## R8_NORMAL_AB_TEST tests R8_NORMAL_AB.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 May 2015
#
#  Author:
#
#    John Burkardt
#
  x_mean = 100.0
  x_std = 10.0
  seed = 123456789
  test_num = 20

  print ''
  print 'R8_NORMAL_AB_TEST'
  print '  R8_NORMAL_AB generates normally distributed values'
  print '  with given mean and standard deviation.'
  print '  Using initial random number seed = %d' % ( seed )
  print '  MEAN = %g' % ( x_mean )
  print '  STD = %g' % ( x_std )
  print ''

  for test in range ( 0, test_num ):

    x, seed = r8_normal_ab ( x_mean, x_std, seed )
    print '  %f' % ( x )
#
#  Terminate.
#
  print ''
  print 'R8_NORMAL_AB_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_normal_ab_test ( )
  timestamp ( )

