#!/usr/bin/env python

#*****************************************************************************80
#
## MONOMIAL_TEST tests the MONOMIAL library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    27 October 2014
#
#  Author:
#
#    John Burkardt
#
from i4_choose                 import i4_choose_test
from i4_uniform_ab             import i4_uniform_ab_test
from i4vec_print               import i4vec_print_test
from i4vec_sum                 import i4vec_sum_test
from i4vec_uniform_ab          import i4vec_uniform_ab_test
from mono_between_enum         import mono_between_enum_test
from mono_between_next_grevlex import mono_between_next_grevlex_test
from mono_between_next_grlex   import mono_between_next_grlex_test
from mono_between_random       import mono_between_random_test
from mono_next_grevlex         import mono_next_grevlex_test
from mono_next_grlex           import mono_next_grlex_test
from mono_print                import mono_print_test
from mono_rank_grlex           import mono_rank_grlex_test
from mono_total_enum           import mono_total_enum_test
from mono_total_next_grevlex   import mono_total_next_grevlex_test
from mono_total_next_grlex     import mono_total_next_grlex_test
from mono_total_random         import mono_total_random_test
from mono_unrank_grlex         import mono_unrank_grlex_test
from mono_upto_enum            import mono_upto_enum_test
from mono_upto_next_grevlex    import mono_upto_next_grevlex_test
from mono_upto_next_grlex      import mono_upto_next_grlex_test
from mono_upto_random          import mono_upto_random_test
from mono_value                import mono_value_test
from timestamp                 import timestamp

timestamp ( )
print ''
print 'MONOMIAL_TEST'
print '  Python version:'
print '  Test the MONOMIAL library.'

i4_choose_test ( )
i4_uniform_ab_test ( )

i4vec_sum_test ( )
i4vec_uniform_ab_test ( )

mono_between_enum_test ( )
mono_total_enum_test ( )
mono_upto_enum_test ( )
mono_next_grevlex_test ( )
mono_next_grlex_test ( )
mono_between_next_grevlex_test ( )
mono_between_next_grlex_test ( )
mono_total_next_grevlex_test ( )
mono_total_next_grlex_test ( )
mono_upto_next_grevlex_test ( )
mono_upto_next_grlex_test ( )
mono_rank_grlex_test ( )
mono_unrank_grlex_test ( )
mono_between_random_test ( )
mono_total_random_test ( )
mono_upto_random_test ( )
mono_value_test ( )
mono_print_test ( )
#
#  Terminate.
#
print ''
print 'MONOMIAL_TEST:'
print '  Normal end of execution.'
print ''
timestamp ( )
