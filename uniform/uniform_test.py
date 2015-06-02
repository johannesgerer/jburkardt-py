#!/usr/bin/env python

def uniform_test ( ):

#*****************************************************************************80
#
## UNIFORM_TEST tests the UNIFORM library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    27 December 2014
#
#  Author:
#
#    John Burkardt
#
  from bvec_print          import bvec_print_test
  from bvec_uniform        import bvec_uniform_test
  from c4_uniform_01       import c4_uniform_01_test
  from c4mat_print         import c4mat_print_test
  from c4mat_print_some    import c4mat_print_some_test
  from c4mat_uniform_01    import c4mat_uniform_01_test
  from c4vec_print         import c4vec_print_test
  from c4vec_uniform_01    import c4vec_uniform_01_test
  from c8_uniform_01       import c8_uniform_01_test
  from c8mat_print         import c8mat_print_test
  from c8mat_print_some    import c8mat_print_some_test
  from c8mat_uniform_01    import c8mat_uniform_01_test
  from c8vec_print         import c8vec_print_test
  from c8vec_uniform_01    import c8vec_uniform_01_test
  from ch_uniform_ab       import ch_uniform_ab_test
  from congruence          import congruence_test
  from get_seed            import get_seed_test
  from i4_gcd              import i4_gcd_test
  from i4_huge             import i4_huge_test
  from i4_modp             import i4_modp_test
  from i4_seed_advance     import i4_seed_advance_test
  from i4_sign             import i4_sign_test
  from i4_uniform_0i       import i4_uniform_0i_test
  from i4_uniform_ab       import i4_uniform_ab_test1
  from i4_uniform_ab       import i4_uniform_ab_test2
  from i4mat_print         import i4mat_print_test
  from i4mat_print_some    import i4mat_print_some_test
  from i4mat_uniform_ab    import i4mat_uniform_ab_test
  from i4vec_print         import i4vec_print_test
  from i4vec_uniform_ab    import i4vec_uniform_ab_test
  from l4_uniform          import l4_uniform_test
  from l4mat_print         import l4mat_print_test
  from l4mat_print_some    import l4mat_print_some_test
  from l4mat_uniform       import l4mat_uniform_test
  from l4vec_print         import l4vec_print_test
  from l4vec_uniform       import l4vec_uniform_test
  from lcrg_anbn           import lcrg_anbn_test
  from lcrg_seed           import lcrg_seed_test
  from power_mod           import power_mod_test
  from r4_uniform_01       import r4_uniform_01_test
  from r4_uniform_ab       import r4_uniform_ab_test
  from r4mat_print         import r4mat_print_test
  from r4mat_print_some    import r4mat_print_some_test
  from r4mat_uniform_01    import r4mat_uniform_01_test
  from r4mat_uniform_ab    import r4mat_uniform_ab_test
  from r4vec_print         import r4vec_print_test
  from r4vec_uniform_01    import r4vec_uniform_01_test
  from r4vec_uniform_ab    import r4vec_uniform_ab_test
  from r8_uniform_01       import r8_uniform_01_test
  from r8_uniform_ab       import r8_uniform_ab_test
  from r8col_uniform_abvec import r8col_uniform_abvec_test
  from r8mat_print         import r8mat_print_test
  from r8mat_print_some    import r8mat_print_some_test
  from r8mat_uniform_01    import r8mat_uniform_01_test
  from r8mat_uniform_ab    import r8mat_uniform_ab_test
  from r8row_uniform_abvec import r8row_uniform_abvec_test
  from r8vec_print         import r8vec_print_test
  from r8vec_uniform_01    import r8vec_uniform_01_test
  from r8vec_uniform_ab    import r8vec_uniform_ab_test
  from r8vec_uniform_abvec import r8vec_uniform_abvec_test
  from timestamp           import timestamp_test

  print ''
  print 'UNIFORM_TEST'
  print '  Python version:'
  print '  Test the UNIFORM library.'
#
#  Support functions:
#
  bvec_print_test ( )
  c4mat_print_test ( )
  c4mat_print_some_test ( )
  c4vec_print_test ( )
  c8mat_print_test ( )
  c8mat_print_some_test ( )
  c8vec_print_test ( )
  congruence_test ( )
  get_seed_test ( )
  i4_gcd_test ( )
  i4_huge_test ( )
  i4_modp_test ( )
  i4_seed_advance_test ( )
  i4_sign_test ( )
  i4mat_print_test ( )
  i4mat_print_some_test ( )
  i4vec_print_test ( )
  l4mat_print_test ( )
  l4mat_print_some_test ( )
  l4mat_uniform_test ( )
  l4vec_print_test ( )
  lcrg_anbn_test ( )
  lcrg_seed_test ( )
  power_mod_test ( )
  r4mat_print_test ( )
  r4mat_print_some_test ( )
  r4vec_print_test ( )
  r8mat_print_test ( )
  r8mat_print_some_test ( )
  r8vec_print_test ( )
  timestamp_test ( )
#
#  Main UNIFORM functions.
#
  bvec_uniform_test ( )

  c4_uniform_01_test ( )
  c4mat_uniform_01_test ( )
  c4vec_uniform_01_test ( )

  c8_uniform_01_test ( )
  c8mat_uniform_01_test ( )
  c8vec_uniform_01_test ( )

  ch_uniform_ab_test ( )

  i4_uniform_0i_test ( )
  i4_uniform_ab_test1 ( )
  i4_uniform_ab_test2 ( )
  i4mat_uniform_ab_test ( )
  i4vec_uniform_ab_test ( )

  l4_uniform_test ( )
  l4mat_uniform_test ( )
  l4vec_uniform_test ( )

  r4_uniform_01_test ( )
  r4_uniform_ab_test ( )
  r4mat_uniform_01_test ( )
  r4mat_uniform_ab_test ( )
  r4vec_uniform_01_test ( )
  r4vec_uniform_ab_test ( )
  r4vec_uniform_01_test ( )
  r4vec_uniform_ab_test ( )

  r8_uniform_01_test ( )
  r8_uniform_ab_test ( )
  r8mat_uniform_01_test ( )
  r8mat_uniform_ab_test ( )
  r8vec_uniform_01_test ( )
  r8vec_uniform_ab_test ( )

  r8col_uniform_abvec_test ( )
  r8row_uniform_abvec_test ( )
  r8vec_uniform_abvec_test ( )
#
#  Terminate.
#
  print ''
  print 'UNIFORM_TEST:'
  print '  Normal end of execution.'

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  uniform_test ( )
  timestamp ( )
