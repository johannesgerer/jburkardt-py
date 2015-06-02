#! /usr/bin/env python
#
def compnz_to_ksub ( nc, kc, ac ):

#*****************************************************************************80
#
## COMPNZ_TO_KSUB converts a (nonzero) composition to a K-subset.
#
#  Discussion:
#
#    There is a bijection between K subsets and nonzero compositions.
#
#    Let AC be a nonzero composition of NC into KC parts.
#
#    Then let
#      NS = NC - 1
#      KS = KC - 1
#    and define
#      AS(I) = sum ( AC(1:I) ), for I = 1 : KS.
#      
#    Then AS is a KS subset of the integers 1 through NS.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 May 2015
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

  ns = nc - 1
  ks = kc - 1
  bs = np.zeros ( ks )
  t = 0
  for i in range ( 0, ks ):
    t = t + ac[i]
    bs[i] = t

  return ns, ks, bs

def compnz_to_ksub_test ( ):

#*****************************************************************************80
#
## COMPNZ_TO_KSUB_TEST tests COMPNZ_TO_KSUB.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    08 May 2015
#
#  Author:
#
#    John Burkardt
#
  from compnz_random import compnz_random

  print ''
  print 'COMPNZ_TO_KSUB_TEST'
  print '  COMPNZ_TO_KSUB returns the K subset corresponding'
  print '  to a nonzero composition.'

  nc = 10
  kc = 5
  seed = 123456789

  print ''
  print '  The composition sums to %d' % ( nc )
  print '  and contains %d parts.' % ( kc )

  for i in range ( 0, 5 ):

    print ''

    ac, seed = compnz_random ( nc, kc, seed )
   
    print '  COMPNZ:',
    for j in range ( 0, kc ):
      print '  %2d' % ( ac[j] ),
    print ''

    ns, ks, bs = compnz_to_ksub ( nc, kc, ac )
    print '  KSUB:  ',
    for j in range ( 0, ks ):
      print '  %2d' % ( bs[j] ),
    print ''
#
#  Terminate.
#
  print ''
  print 'COMPNZ_TO_KSUB_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  compnz_to_ksub_test ( )
  timestamp ( )
