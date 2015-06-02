#! /usr/bin/env python
#
def wilk12 ( ):

#*****************************************************************************80
#
## WILK12 returns the WILK12 matrix.
#
#  Formula:
#
#    12 11  0  0  0  0  0  0  0  0  0  0
#    11 11 10  0  0  0  0  0  0  0  0  0
#    10 10 10  9  0  0  0  0  0  0  0  0
#     9  9  9  9  8  0  0  0  0  0  0  0
#     8  8  8  8  8  7  0  0  0  0  0  0
#     7  7  7  7  7  7  6  0  0  0  0  0
#     6  6  6  6  6  6  6  5  0  0  0  0
#     5  5  5  5  5  5  5  5  4  0  0  0
#     4  4  4  4  4  4  4  4  4  3  0  0
#     3  3  3  3  3  3  3  3  3  3  2  0
#     2  2  2  2  2  2  2  2  2  2  2  1
#     1  1  1  1  1  1  1  1  1  1  1  1
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is integral, therefore det ( A ) is integral, and 
#    det ( A ) * inverse ( A ) is integral.
#
#    det ( A ) = 1.
#
#    A is lower Hessenberg.
#
#    The smaller eigenvalues are very ill conditioned.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    James Wilkinson,
#    Rounding Errors in Algebraic Processes,
#    Prentice Hall, 1963,
#    page 151.
#
#  Parameters:
#
#    Output, real A(12,12), the matrix.
#
  import numpy as np

  n = 12
  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      if ( j <= i + 1 ):
        a[i,j] = n - max ( i, j )

  return a

def wilk12_condition ( ):

#*****************************************************************************80
#
## WILK12_CONDITION returns the L1 condition of the WILK12 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Output, real VALUE, the L1 condition.
#
  a_norm = 78.0
  b_norm = 87909427.13689443
  value = a_norm * b_norm

  return value

def wilk12_determinant ( ):

#*****************************************************************************80
#
## WILK12_DETERMINANT returns the determinant of the WILK12 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Output, real VALUE, the determinant.
#
  value = 1.0

  return value

def wilk12_determinant_test ( ):

#*****************************************************************************80
#
## WILK12_DETERMINANT_TEST tests WILK12_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 February 2015
#
#  Author:
#
#    John Burkardt
#
  from wilk12 import wilk12
  from r8mat_print import r8mat_print

  print ''
  print 'WILK12_DETERMINANT_TEST'
  print '  WILK12_DETERMINANT computes the determinant of the WILK12 matrix.'
  print ''

  n = 12
  a = wilk12 ( )
  r8mat_print ( n, n, a, '  WILK12 matrix:' )

  value = wilk12_determinant ( )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'WILK12_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def wilk12_eigen_right ( ):

#*****************************************************************************80
#
## WILK12_EIGEN_RIGHT returns the right eigenvectors of the WILK12 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real X(12,12), the right eigenvector matrix.
#
  import numpy as np

  x = np.array ( [ \
    [  0.075953934362606,  0.139678536121698, \
       0.212972721043730,  0.286424756003626, \
       0.349485357102525,  0.392486174053140, \
       0.408397328102426,  0.393960067241308, \
       0.350025473229225,  0.281131870150006, \
       0.194509944233873,  0.098787565402021 ], \
    [  0.047186270176379,  0.035170881219766, \
      -0.019551243493406, -0.113663824929275, \
      -0.229771631994320, -0.342302599090153, \
      -0.425606879283194, -0.461118871576638, \
      -0.441461339130489, -0.370865208095037, \
      -0.262574394436703, -0.134619530658877 ], \
    [  0.087498415888682,  0.002474434526797, \
      -0.095923839958749, -0.124601769209776, \
      -0.044875899531161,  0.121565513387420, \
       0.312274076477727,  0.458792947263280, \
       0.515554022627437,  0.471997957002961, \
       0.348267903145709,  0.181505588624358 ], \
    [  0.356080027225304, -0.163099766915005, \
      -0.325820728704039, -0.104423010988819, \
       0.176053383568728,  0.245040317292912, \
       0.069840787629820, -0.207165420169259, \
      -0.418679217847974, -0.475318237218216, \
      -0.383234018094179, -0.206444528035974 ], \
    [ -0.709141914617340,  0.547208974924657, \
       0.370298143032545, -0.087024255226817, \
      -0.174710647675812, -0.026657290116937, \
       0.077762060814618,  0.057335745807230, \
      -0.018499801182824, -0.070417566622935, \
      -0.072878348819266, -0.042488463457934 ], \
    [ -0.713561589955660,  0.677624765946043, \
       0.144832629941422, -0.095987754186127, \
      -0.033167043991408,  0.015790103726845, \
       0.009303310423290, -0.002909858414229, \
      -0.003536176142936,  0.000317090937139, \
       0.002188160441481,  0.001613099168127 ], \
    [  0.694800915350134, -0.717318445412803, \
      -0.021390540433709,  0.047257308713196, \
       0.000033398195785, -0.003862799912030, \
       0.000145902034404,  0.000419891505074, \
      -0.000039486945846, -0.000069994145516, \
       0.000013255774472,  0.000029720715023 ], \
    [  0.684104842982405, -0.728587222991804, \
       0.028184117194646,  0.019000894182572, \
      -0.002364147875169, -0.000483008341150, \
       0.000145689574886,  0.000006899341493, \
      -0.000009588938470,  0.000001123011584, \
       0.000000762677095, -0.000000504464129 ], \
    [  0.679348386306787, -0.732235872680797, \
       0.047657921019166,  0.006571283153133, \
      -0.001391439772868,  0.000028271472280, \
       0.000025702435813, -0.000004363907083, \
      -0.000000016748075,  0.000000170826901, \
      -0.000000050888575,  0.000000010256625 ], \
    [  0.677141058069838, -0.733699103817717, \
       0.056254187307821,  0.000845330889853, \
      -0.000600573479254,  0.000060575011829, \
      -0.000000899585454, -0.000000703890529, \
       0.000000147573166, -0.000000020110423, \
       0.000000002229508, -0.000000000216223 ], \
    [  0.675994567035284, -0.734406182106934, \
       0.060616915148887, -0.002116889869553, \
      -0.000112561724387,  0.000026805640571, \
      -0.000002875297806,  0.000000236938971, \
      -0.000000016773740,  0.000000001068110, \
      -0.000000000062701,  0.000000000003446 ], \
    [ -0.675318870608569,  0.734806603365595, \
      -0.063156546323253,  0.003858723645845, \
      -0.000198682768218,  0.000009145253582, \
      -0.000000387365950,  0.000000015357316, \
      -0.000000000576294,  0.000000000020662, \
      -0.000000000000713,  0.000000000000023 ] ] );

  x = np.transpose ( x )

  return x

def wilk12_eigenvalues ( ):

#*****************************************************************************80
#
## WILK12_EIGENVALUES returns the eigenvalues of the WILK12 matrix.
#
#  Formula:
#
#    32.2288915
#    20.1989886
#    12.3110774
#     6.96153309
#     3.51185595
#     1.55398871
#     0.643505319
#     0.284749721
#     0.143646520
#     0.081227659240405
#     0.049507429185278
#     0.031028060644010
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real LAM(12), the eigenvalues.
#
  import numpy as np

  lam = np.array ( [ \
   [ 32.2288915 ], \
   [ 20.1989886 ], \
   [ 12.3110774 ], \
   [  6.96153309 ], \
   [  3.51185595 ], \
   [  1.55398871 ], \
   [  0.643505319 ], \
   [  0.284749721 ], \
   [  0.143646520 ], \
   [  0.081227659240405 ], \
   [  0.049507429185278 ], \
   [  0.031028060644010 ] ] )

  return lam

def wilk12_test ( ):

#*****************************************************************************80
#
## WILK12_TEST tests WILK12.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 February 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'WILK12_TEST'
  print '  WILK12 computes the WILK12 matrix.'

  n = 12
  a = wilk12 ( )
  r8mat_print ( n, n, a, '  WILK12 matrix:' )

  print ''
  print 'WILK12_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  wilk12_test ( )
  timestamp ( )
