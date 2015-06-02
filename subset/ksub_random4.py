#!/usr/bin/env python

def ksub_random4 ( n, k, seed ):

#*****************************************************************************80
#
## KSUB_RANDOM4 selects a random subset of size K from a set of size N.
#
#  Discussion:
#
#    This routine is somewhat impractical for the given problem, but
#    it is included for comparison, because it is an interesting
#    approach that is superior for certain applications.
#
#    The approach is mainly interesting because it is "incremental";
#    it proceeds by considering every element of the set, and does not
#    need to know how many elements there are.
#
#    This makes this approach ideal for certain cases, such as the
#    need to pick 5 lines at random from a text file of unknown length,
#    or to choose 6 people who call a certain telephone number on a
#    given day.  Using this technique, it is possible to make the
#    selection so that, whenever the input stops, a valid uniformly
#    random subset has been chosen.
#
#    Obviously, if the number of items is known in advance, and
#    it is easy to extract K items directly, there is no need for
#    this approach, and it is less efficient since, among other costs,
#    it has to generate a random number for each item, and make an
#    acceptance/rejection test.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Tom Christiansen and Nathan Torkington,
#    "8.6: Picking a Random Line from a File",
#    Perl Cookbook, pages 284-285,
#    O'Reilly, 1999.
#
#  Parameters:
#
#    Input, integer N, the size of the set from which subsets are drawn.
#
#    Input, integer K, number of elements in desired subsets.  K must
#    be between 0 and N.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, integer A(K), contains the indices of the selected items.
#
#    Output, integer SEED, a seed for the random number generator.
#
  import numpy as np
  from i4_uniform_ab import i4_uniform_ab
  from r8_uniform_01 import r8_uniform_01

  a = np.zeros ( k )

  next = 0
#
#  Here, we use a DO WHILE to suggest that the algorithm
#  proceeds to the next item, without knowing how many items
#  there are in total.
#
#  Note that this is really the only place where N occurs,
#  so other termination criteria could be used, and we really
#  don't need to know the value of N!
#
  while ( next < n ):

    if ( next < k ):

      i = next
      a[i] = next

    else:

      r, seed = r8_uniform_01 ( seed )

      if ( r * ( next + 1 ) <= k ):
        i4_lo = 0
        i4_hi = k - 1
        i, seed = i4_uniform_ab ( i4_lo, i4_hi, seed )
        a[i] = next

    next = next + 1

  return a, seed

def ksub_random4_test ( ):

#*****************************************************************************80
#
## KSUB_RANDOM4_TEST tests KSUB_RANDOM4.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 May 2015
#
#  Author:
#
#    John Burkardt
#
  k = 3
  n = 100

  print ''
  print 'KSUB_RANDOM4_TEST'
  print '  KSUB_RANDOM4 generates a random K subset of an N set.'
  print '  Set size is N =    %d' % ( n )
  print '  Subset size is K = %d' % ( k )
  print ''

  seed = 123456789

  for i in range ( 0, 10 ):

    a, seed = ksub_random4 ( n, k, seed )

    for j in range ( 0, k ):
      print '  %3d' % ( a[j] ),
    print ''
#
#  Terminate.
#
  print ''
  print 'KSUB_RANDOM4_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  ksub_random4_test ( )
  timestamp ( )
