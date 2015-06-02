#!/usr/bin/env python
#
def r8_cube_root ( x ):

#*****************************************************************************80
#
## R8_CUBE_ROOT returns the cube root of an R8.
#
#  Discussion:
#
#    This routine is designed to avoid the possible problems that can occur
#    when formulas like 0.0**(1/3) or (-1.0)**(1/3) are to be evaluated.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    24 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the number whose cube root is desired.
#
#    Output, real VALUE, the cube root of X.
#
  if ( 0.0 < x ):
    value = x ** ( 1.0 / 3.0 )
  elif ( x == 0.0 ):
    value = 0.0;
  else:
    value = - ( abs ( x ) ) ** ( 1.0 / 3.0 )

  return value

def r8_cube_root_test ( ):

#*****************************************************************************80
#
## R8_CUBE_ROOT_TEST tests R8_CUBE_ROOT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 July 2014
#
#  Author:
#
#    John Burkardt
#
  from r8_uniform_ab import r8_uniform_ab

  print ''
  print 'R8_CUBE_ROOT_TEST'
  print '  R8_CUBE_ROOT computes the cube root of an R8.'
  print ''
  print '       X               Y               Y^3'
  print ''

  a = -10.0
  b = +10.0
  seed = 123456789

  for i in range ( 0, 10 ):
    x1, seed = r8_uniform_ab ( a, b, seed )
    y = r8_cube_root ( x1 )
    x2 = y ** 3
    print '  %14.6g  %14.6g  %14.6g' % ( x1, y, x2 )
#
#  Terminate.
#
  print ''
  print 'R8_CUBE_ROOT_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_cube_root_test ( )
  timestamp ( )
