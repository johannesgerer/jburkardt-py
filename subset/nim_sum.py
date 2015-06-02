#! /usr/bin/env python

def nim_sum ( i, j ):

#*****************************************************************************80
#
## NIM_SUM computes the Nim sum of two integers.
#
#  Discussion:
#
#    If K is the Nim sum of I and J, then each bit of K is the exclusive
#    OR of the corresponding bits of I and J.
#
#  Example:
#
#     I     J     K     I base 2    J base 2    K base 2
#   ----  ----  ----  ----------  ----------  ----------
#      0     0     0           0           0           0
#      1     0     1           1           0           1
#      1     1     0           1           1           0
#      2     7     5          10         111         101
#     11    28    23        1011       11100       10111
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer I, J, the integers to be Nim-summed.
#
#    Output, integer K, the Nim sum of I and J.
#
  from ubvec_to_ui4 import ubvec_to_ui4
  from ubvec_xor import ubvec_xor
  from ui4_to_ubvec import ui4_to_ubvec

  nbits = 32

  ivec = ui4_to_ubvec ( i, nbits )
  jvec = ui4_to_ubvec ( j, nbits )

  kvec = ubvec_xor ( nbits, ivec, jvec )

  k = ubvec_to_ui4 ( nbits, kvec )

  return k

def nim_sum_test ( ):

#*****************************************************************************80
#
## NIM_SUM_TEST tests NIM_SUM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 May 2015
#
#  Author:
#
#    John Burkardt
#
  from i4_uniform_ab import i4_uniform_ab
  from ubvec_print import ubvec_print
  from ui4_to_ubvec import ui4_to_ubvec

  n = 32
  ihi = 1000
  ilo = 0
  ntest = 5

  print ''
  print 'NIM_SUM_TEST'
  print '  NIM_SUM computes the Nim sum of two integers.'
  print ''
  print '    I    J    Nim(I+J)'
  print ''

  seed = 123456789

  for i in range ( 0, ntest ):

    i1, seed = i4_uniform_ab ( ilo, ihi, seed )
    i1vec = ui4_to_ubvec ( i1, n )

    i2, seed = i4_uniform_ab ( ilo, ihi, seed )
    i2vec = ui4_to_ubvec ( i2, n )

    i3 = nim_sum ( i1, i2 )
    i3vec = ui4_to_ubvec ( i3, n )

    print ''
    print '  I1, I2, I3 in decimal:'
    print ''
    print '  %3d' % ( i1 )
    print '  %3d' % ( i2 )
    print '  %3d' % ( i3 )
    print ''
    print '  I1, I2, I3 in binary:'
    print ''
    ubvec_print ( n, i1vec, '' )
    ubvec_print ( n, i2vec, '' )
    ubvec_print ( n, i3vec, '' )
#
#  Terminate.
#
  print ''
  print 'NIM_SUM_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  nim_sum_test ( )
  timestamp ( )

