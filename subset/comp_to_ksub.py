#! /usr/bin/env python
#
def comp_to_ksub ( nc, kc, ac ):

#*****************************************************************************80
#
## COMP_TO_KSUB converts a composition to a K-subset.
#
#  Discussion:
#
#    There is a bijection between K subsets and compositions.
#
#    Because we allow a composition to have entries that are 0, we need
#    to implicitly add 1 to each entry before establishing the bijection.
#
#    Let AC be a composition of NC into KC parts.
#
#    Then let
#      NS = NC + KC - 1
#      KS = KC - 1
#    and define
#      AS(I) = sum ( AC(1:I) + 1 ), for I = 1 : KS.
#      
#    Then AS is a KS subset of the integers 1 through NS.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer NC, the composition sum.
#
#    Input, integer KC, the number of parts of the composition.
#
#    Input, integer AC(KC), the parts of the composition.
#
#    Output, integer NS, the size of the set.
#
#    Output, integer KS, the size of the subset.
#
#    Output, integer BS(KS), the entries of the K-subset, in increasing order.
#
  import numpy as np

  ns = nc + kc - 1
  ks = kc - 1
  bs = np.zeros ( ks )
  t = 0
  for i in range ( 0, ks ):
    t = t + ac[i] + 1
    bs[i] = t

  return ns, ks, bs

def comp_to_ksub_test ( ):

#*****************************************************************************80
#
## COMP_TO_KSUB_TEST tests COMP_TO_KSUB.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 May 2015
#
#  Author:
#
#    John Burkardt
#
  from comp_random import comp_random

  print ''
  print 'COMP_TO_KSUB_TEST'
  print '  COMP_TO_KSUB returns the K subset corresponding to a composition.'

  nc = 10
  kc = 5
  seed = 123456789

  for i in range ( 0, 5 ):

    print ''

    ac, seed = comp_random ( nc, kc, seed )
    print '  COMP:  ',
    for j in range ( 0, kc ):
      print '  %2d' % ( ac[j] ),
    print ''

    ns, ks, bs = comp_to_ksub ( nc, kc, ac );
    print '  KSUB:  ',
    for j in range ( 0, ks ):
      print '  %2d' % ( bs[j] ),
    print ''
#
#  Terminate.
#
  print ''
  print 'COMP_TO_KSUB_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  comp_to_ksub_test ( )
  timestamp ( )
