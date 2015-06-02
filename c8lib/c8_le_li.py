#!/usr/bin/env python

def c8_le_li ( c1, c2 ):

#*****************************************************************************80
#
## C8_LE_LI := C1 <= C1 for C8's, and the Loo norm.
#
#  Discussion:
#
#    The Loo norm can be defined here as:
#
#      C8_NORM_LI(C) = max ( abs ( real (C) ) + abs ( imag (C) ) )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, complex C1, C2, the values to be compared.
#
#    Output, boolean VALUE, is TRUE if C1 <= C2.
#
  from c8_imag import c8_imag
  from c8_real import c8_real

  if ( max ( abs ( c8_real ( c1 ) ), abs ( c8_imag ( c1 ) ) ) \
    <= max ( abs ( c8_real ( c2 ) ), abs ( c8_imag ( c2 ) ) ) ) :
    value = True
  else:
    value = False

  return value

def c8_le_li_test ( ):

#*****************************************************************************80
#
## C8_LE_LI_TEST tests C8_LE_LI.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    19 February 2015
#
#  Author:
#
#    John Burkardt
#
  from c8_uniform_01 import c8_uniform_01

  print ''
  print 'C8_LE_LI_TEST'
  print '  C8_LE_LI evalues (C1 <= C2) using the Loo norm.'
  print ''
  print '       C1=C8_UNIFORM_01          C2=C8_UNIFORM_01          L3=C8_LE_LI(C1,C2)'
  print '     ---------------------     ---------------------     ---------------------'
  print ''

  seed = 123456789

  for i in range ( 0, 10 ):
    c1, seed = c8_uniform_01 ( seed )
    c2, seed = c8_uniform_01 ( seed )
    l3 = c8_le_li ( c1, c2 )
    print '  (%12f,%12f)  (%12f,%12f)  %s' \
      % ( c1.real, c1.imag, c2.real, c2.imag, l3 )

  print ''
  print 'C8_LE_LI_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  c8_le_li_test ( )
  timestamp ( )

