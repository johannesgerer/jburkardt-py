#! /usr/bin/env python
#
def i4_partition_conj ( n, iarray1, mult1, npart1 ):

#*****************************************************************************80
#
#% I4_PARTITION_CONJ computes the conjugate of a partition.
#
#  Discussion:
#
#    A partition of an integer N is a set of positive integers which
#    add up to N.  The conjugate of a partition P1 of N is another partition
#    P2 of N obtained in the following way:
#
#      The first element of P2 is the number of parts of P1 greater than
#      or equal to 1.
#
#      The K-th element of P2 is the number of parts of P1 greater than
#      or equal to K.
#
#    Clearly, P2 will have no more than N elements it may be surprising
#    to find that P2 is guaranteed to be a partition of N.  However, if
#    we symbolize the initial partition P1 by rows of X's, then we can
#    see that P2 is simply produced by grouping by columns:
#
#        6 3 2 2 1
#      5 X X X X X
#      4 X X X X
#      2 X X
#      1 X
#      1 X
#      1 X
#
#  Example:
#
#    14 = 5 + 4 + 2 + 1 + 1 + 1
#
#    The conjugate partition is:
#
#    14 = 6 + 3 + 2 + 2 + 1
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
#  Parameters
#
#    Input, integer N, the integer to be partitioned.
#
#    Input, integer IARRAY1(NPART1).  IARRAY1 contains the parts of
#    the partition.  The value of N is represented by
#
#      sum ( 1 <= I <= NPART1 ) MULT1(I) * IARRAY1(I).
#
#    Input, integer MULT1(NPART1).  MULT1 counts the multiplicity of
#    the parts of the partition.  MULT1(I) is the multiplicity
#    of the part IARRAY1(I), for I = 1 to NPART1.
#
#    Input, integer NPART1, the number of "parts" in the partition.
#
#    Output, integer IARRAY2(N).  IARRAY contains the parts of
#    the conjugate partition in entries 1 through NPART2.
#
#    Output, integer MULT2(N).  MULT2 counts the multiplicity of
#    the parts of the conjugate partition in entries 1 through NPART2.
#
#    Output, integer NPART2, the number of "parts" in the conjugate partition.
#
  import numpy as np

  iarray2 = np.zeros ( n )
  mult2 = np.zeros ( n )
  npart2 = 0

  itest = 0

  while ( True ):

    itest = itest + 1

    itemp = 0

    for i in range ( 0, npart1 ):
      if ( itest <= iarray1[i] ):
        itemp = itemp + mult1[i]

    if ( itemp <= 0 ):
      break

    if ( 0 < npart2 ):
      if ( itemp == iarray2[npart2-1] ):
        mult2[npart2-1] = mult2[npart2-1] + 1
      else:
        npart2 = npart2 + 1
        iarray2[npart2-1] = itemp
        mult2[npart2-1] = 1
    else:
      npart2 = npart2 + 1
      iarray2[npart2-1] = itemp
      mult2[npart2-1] = 1

  return iarray2, mult2, npart2

def i4_partition_conj_test ( ):

#*****************************************************************************80
#
#% I4_PARTITION_CONJ_TEST tests I4_PARTITION_CONJ.
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
  from i4_partition_print import i4_partition_print

  n = 14
  npart1 = 4

  a1 = np.array ( [ 2, 5, 1, 4 ] )
  mult1 = np.array ( [ 1, 1, 3, 1 ] )

  print ''
  print 'I4_PARTITION_CONJ_TEST'
  print '  I4_PARTITION_CONJ conjugates an integer partition.'
  print ''
  print '  Original partition:'
  print ''

  i4_partition_print ( n, npart1, a1, mult1 )

  a2, mult2, npart2 = i4_partition_conj ( n, a1, mult1, npart1 )

  print ''
  print '  Conjugate partition:'
  print ''

  i4_partition_print ( n, npart2, a2, mult2 )
#
#  Terminate.
#
  print ''
  print 'I4_PARTITION_CONJ_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_partition_conj_test ( )
  timestamp ( )

