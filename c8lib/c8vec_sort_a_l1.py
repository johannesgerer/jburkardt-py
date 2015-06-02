#! /usr/bin/env python
#
def c8vec_sort_a_l1 ( n, x ):

#*****************************************************************************80
#
## C8VEC_SORT_A_L1 ascending sorts a C8VEC by L1 norm.
#
#  Discussion:
#
#    The L1 norm of A+Bi is abs(A) + abs(B).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 September 2006
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of entries in the array.
#
#    Input, complex X(N), an unsorted array.
#
#    Output, complex X(N), the sorted array.
#
  from sort_safe_rc import sort_safe_rc
  from c8_le_l1 import c8_le_l1

  if ( 1 < n ):

    i = 0
    indx = 0
    isgn = 0
    j = 0
    i_save = 0
    j_save = 0
    k_save = 0
    l_save = 0
    n_save = 0

    while ( True ):

      [ indx, i, j, i_save, j_save, k_save, l_save, n_save ] = sort_safe_rc ( \
        n, indx, isgn, i_save, j_save, k_save, l_save, n_save )

      if ( 0 < indx ):

        temp = x[i-1]
        x[i-1] = x[j-1]
        x[j-1] = temp

      elif ( indx < 0 ):

        if ( c8_le_l1 ( x[i-1], x[j-1] ) ):
          isgn = -1
        else:
          isgn = +1

      elif ( indx == 0 ):

        break

  return x

def c8vec_sort_a_l1_test ( ):

#*****************************************************************************80
#
## C8VEC_SORT_A_L1_TEST tests C8VEC_SORT_A_L1;
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 March 2015
#
#  Author:
#
#    John Burkardt
#
  from c8_norm_l1 import c8_norm_l1
  from c8vec_print import c8vec_print
  from c8vec_uniform_01 import c8vec_uniform_01

  print ''
  print 'C8VEC_SORT_A_L1_TEST'
  print '  C8VEC_SORT_A_L1 sorts a C8VEC by L1 norm.'

  n = 10
  seed = 123456789
  a, seed = c8vec_uniform_01 ( n, seed )
 
  c8vec_print ( n, a, '  The unsorted vector:' )

  a = c8vec_sort_a_l1 ( n, a )

  print ''
  print '   I                  A(I)                   ||A(I)||'
  print ''

  for i in range ( 0, n ):
    print '  %2d  (%14.6g,%14.6g)  %14.6g' \
      % ( i, a.real[i], a.imag[i], c8_norm_l1 ( a[i] ) )

  print ''
  print 'C8VEC_SORT_A_L1_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  c8vec_sort_a_l1_test ( )
  timestamp ( )

