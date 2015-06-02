#!/usr/bin/env python

#*****************************************************************************80
#
## POLYNOMIAL_TEST tests the POLYNOMIAL library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    28 October 2014
#
#  Author:
#
#    John Burkardt
#
from i4_choose               import i4_choose_test
from i4_fall                 import i4_fall_test
from i4_uniform_ab           import i4_uniform_ab_test
from i4vec_concatenate       import i4vec_concatenate_test
from i4vec_permute           import i4vec_permute_test
from i4vec_print             import i4vec_print_test
from i4vec_sort_heap_index_a import i4vec_sort_heap_index_a_test
from i4vec_sum               import i4vec_sum_test
from i4vec_uniform_ab        import i4vec_uniform_ab_test
from mono_next_grlex         import mono_next_grlex_test
from mono_rank_grlex         import mono_rank_grlex_test
from mono_total_next_grlex   import mono_total_next_grlex_test
from mono_unrank_grlex       import mono_unrank_grlex_test
from mono_upto_enum          import mono_upto_enum_test
from mono_value              import mono_value_test
from perm_uniform            import perm_uniform_test
from polynomial_add          import polynomial_add_test
from polynomial_axpy         import polynomial_axpy_test
from polynomial_compress     import polynomial_compress_test
from polynomial_dif          import polynomial_dif_test
from polynomial_mul          import polynomial_mul_test
from polynomial_print        import polynomial_print_test
from polynomial_scale        import polynomial_scale_test
from polynomial_sort         import polynomial_sort_test
from polynomial_value        import polynomial_value_test
from r8vec_concatenate       import r8vec_concatenate_test
from r8vec_permute           import r8vec_permute_test
from r8vec_print             import r8vec_print_test
from timestamp               import timestamp

timestamp ( )
print ''
print 'POLYNOMIAL_TEST'
print '  Python version:'
print '  Test the POLYNOMIAL library.'

i4_choose_test ( )
i4_fall_test ( )
i4_uniform_ab_test ( )

i4vec_concatenate_test ( )
i4vec_permute_test ( )
i4vec_print_test ( )
i4vec_sort_heap_index_a_test ( )
i4vec_sum_test ( )
i4vec_uniform_ab_test ( )

r8vec_concatenate_test ( )
r8vec_permute_test ( )
r8vec_print_test ( )

perm_uniform_test ( )

mono_upto_enum_test ( )
mono_next_grlex_test ( )
mono_rank_grlex_test ( )
mono_total_next_grlex_test ( )
mono_unrank_grlex_test ( )
mono_value_test ( )

polynomial_add_test ( )
polynomial_axpy_test ( )
polynomial_compress_test ( )
polynomial_dif_test ( )
polynomial_mul_test ( )
polynomial_print_test ( )
polynomial_scale_test ( )
polynomial_sort_test ( )
polynomial_value_test ( )
#
#  Terminate.
#
print ''
print 'POLYNOMIAL_TEST:'
print '  Normal end of execution.'
print ''
timestamp ( )
