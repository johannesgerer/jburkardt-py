#! /usr/bin/env python
#
def ksub_to_compnz ( ns, ks, bs ):

#*****************************************************************************80
#
## KSUB_TO_COMPNZ converts a K-subset to a nonzero composition.
#
#  Discussion:
#
#    There is a bijection between K subsets and nonzero compositions.
#
#    Let BS be a KS subset of a set of the integers 1 through NS.
#
#    Then let 
#      NC = NS + 1, 
#      KC = KS + 1, 
#    and define
#      AC(1) = BS(1);
#      AC(2:KC-1) = BS(2:KC-1) - BS(1:KC-2);
#      AC(KC) = NC - BS(KS).
#
#    Then AC is a composition of NC into KC parts.
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
#    Input, integer NS, the size of the set.
#
#    Input, integer KS, the size of the subset.
#
#    Input, integer BS(KS), the entries of the K-subset, in increasing order.
#
#    Output, integer NC, the composition sum.
#
#    Output, integer KC, the number of parts of the composition.
#
#    Output, integer AC(KC), the parts of the composition.
#
  import numpy as np

  nc = ns + 1
  kc = ks + 1
  ac = np.zeros ( kc )

  ac[0] = bs[0]
  for i in range ( 1, kc - 1 ):
    ac[i] = bs[i] - bs[i-1]

  ac[kc-1] = nc - bs[ks-1]

  return nc, kc, ac

def ksub_to_compnz_test ( ):

#*****************************************************************************80
#
## KSUB_TO_COMPNZ_TEST tests KSUB_TO_COMPNZ.
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
  from ksub_random2 import ksub_random2

  print ''
  print 'KSUB_TO_COMPNZ_TEST'
  print '  KSUB_TO_COMPNZ returns the nonzero composition'
  print '  corresponding to a K subset.'

  ns = 14
  ks = 4
  seed = 123456789

  for i in range ( 0, 5 ):

    print ''

    bs, seed = ksub_random2 ( ns, ks, seed )
    print '  KSUB:  ',
    for j in range ( 0, ks ):
      print '  %2d' % ( bs[j] ),
    print ''

    nc, kc, ac = ksub_to_compnz ( ns, ks, bs )
    print '  COMPNZ:',
    for j in range ( 0, kc ):
      print '  %2d' % ( ac[j] ),
    print ''
    

#  Terminate.
#
  print ''
  print 'KSUB_TO_COMPNZ_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  ksub_to_compnz_test ( )
  timestamp ( )
