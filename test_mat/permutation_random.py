#! /usr/bin/env python
#
def permutation_random ( n, key ):

#*****************************************************************************80
#
## PERMUTATION_RANDOM returns the PERMUTATION_RANDOM matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Albert Nijenhuis, Herbert Wilf,
#    Combinatorial Algorithms,
#    Academic Press, 1978, second edition,
#    ISBN 0-12-519260-6.
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, integer KEY, a positive value that selects the data.
#
#    Output, real A(N,N), the matrix.
#
  from i4_uniform_ab import i4_uniform_ab
  from identity import identity

  a = identity ( n, n )

  seed = key

  for i in range ( 0, n ):
    i4_lo = i
    i4_hi = n - 1
    i2, seed = i4_uniform_ab ( i4_lo, i4_hi, seed )
    if ( i2 != i ):
      for j in range ( 0, n ):
        t = a[i,j]
        a[i,j] = a[i2,j]
        a[i2,j] = t

  return a

def permutation_random_determinant ( n, key ):

#*****************************************************************************80
#
## PERMUTATION_RANDOM_DETERMINANT: determinant of PERMUTATION_RANDOM matrix.
#
#  Discussion:
#
#    This routine will only work properly if it is given as input the
#    same value of SEED that was given to PERMUTATION_RANDOM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, integer KEY, a positive value that selects the data.
#
#    Output, real VALUE, the determinant.
#
  from sys import exit

  a = permutation_random ( n, key )

  value = 1.0

  for i in range ( 0, n ):

    found = False

    for i2 in range ( i, n ):

      if ( a[i2,i] == 1.0 ):
        found = True
        if ( i2 != i ):
          for j in range ( 0, n ):
            t       = a[i2,j]
            a[i2,j] = a[i,j]
            a[i,j]  = t
          value = - value

    if ( not found ):
      print ''
      print 'PERMUTATION_RANDOM_DETERMINANT - Fatal error!'
      print '  Permutation matrix is illegal.'
      exit ( 'PERMUTATION_RANDOM_DETERMINANT - Fatal error!' )

  return value

def permutation_random_inverse ( n, key ):

#*****************************************************************************80
#
## PERMUTATION_RANDOM_INVERSE: inverse of PERMUTATION_RANDOM matrix.
#
#  Discussion:
#
#    This routine will only work properly if it is given as input the
#    same value of SEED that was given to PERMUTATION_RANDOM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 October 2007
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, integer KEY, a positive value that selects the data.
#
#    Output, real A(N,N), the inverse matrix.
#
  import numpy as np

  a = permutation_random ( n, key )
 
  a = np.transpose ( a )

  return a

def permutation_random_test ( ):

#*****************************************************************************80
#
## PERMUTATION_RANDOM_TEST tests PERMUTATION_RANDOM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 March 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'PERMUTATION_RANDOM_TEST'
  print '  PERMUTATION_RANDOM computes the PERMUTATION_RANDOM matrix.'

  n = 5

  key = 123456789
  a = permutation_random ( n, key )
  r8mat_print ( n, n, a, '  PERMUTATION_RANDOM matrix:' )

  print ''
  print 'PERMUTATION_RANDOM_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  permutation_random_test ( )
  timestamp ( )
