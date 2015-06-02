#! /usr/bin/env python
#
def i4_partition_print ( n, npart, a, mult ):

#*****************************************************************************80
#
## I4_PARTITION_PRINT prints a partition of an integer.
#
#  Discussion:
#
#    A partition of an integer N is a representation of the integer as
#    the sum of nonzero integers:
#
#      N = A1 + A2 + A3 + ...
#
#    It is standard practice to gather together all the values that 
#    are equal, and replace them in the sum by a single term, multiplied
#    by its "multiplicity":
#
#      N = M1 * A1 + M2 * A2 + ... + M(NPART) * A(NPART)
#    
#    In this representation, every A is a unique positive number, and 
#    no M is zero (or negative).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the integer to be partitioned.
#
#    Input, integer NPART, the number of "parts" in the partition.
#
#    Input, integer A(NPART), the parts of the partition.  
#
#    Input, integer MULT(NPART), the multiplicies of the parts.
#
  print '  %d = ' % ( n )

  for i in range ( 0, npart ):

    if ( i == 0 ):
      print '   ',
    else:
      print '  +',

    print '%d * %d' % ( mult[i], a[i] )

  return

def i4_partition_print_test ( ):

#*****************************************************************************80
#
## I4_PARTITION_PRINT_TEST tests I4_PARTITION_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 14
  npart = 4

  a = np.array ( [ 2, 5, 1, 4 ] )
  mult = np.array ( [ 1, 1, 3, 1 ] )

  print ''
  print 'I4_PARTITION_PRINT_TEST'
  print '  I4_PARTITION_PRINT prints an integer partition.'

  print ''
  i4_partition_print ( n, npart, a, mult )
#
#  Terminate.
#
  print ''
  print 'I4_PARTITION_PRINT_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_partition_print_test ( )
  timestamp ( )
