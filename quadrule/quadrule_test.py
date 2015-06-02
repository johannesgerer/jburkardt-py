#!/usr/bin/env python

def quadrule_test ( ):

#*****************************************************************************80
#
## QUADRULE_TEST tests the QUADRULE library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    18 April 2015
#
#  Author:
#
#    John Burkardt
#
  from bashforth_set            import bashforth_set_test
  from chebyshev1_compute       import chebyshev1_compute_test
  from chebyshev3_compute       import chebyshev3_compute_test
  from clenshaw_curtis_compute  import clenshaw_curtis_compute_test
  from clenshaw_curtis_set      import clenshaw_curtis_set_test
  from fejer1_compute           import fejer1_compute_test
  from fejer1_set               import fejer1_set_test
  from fejer2_compute           import fejer2_compute_test
  from fejer2_set               import fejer2_set_test
  from legendre_set             import legendre_set_test01
  from moulton_set              import moulton_set_test
  from timestamp                import timestamp_test

  print ''
  print 'QUADRULE_TEST'
  print '  Python version:'
  print '  Test the QUADRULE library.'

  bashforth_set_test ( )

  chebyshev1_compute_test ( )
  chebyshev3_compute_test ( )

  clenshaw_curtis_compute_test ( )
  clenshaw_curtis_set_test ( )

  fejer1_compute_test ( )
  fejer1_set_test ( )

  fejer2_compute_test ( )
  fejer2_set_test ( )

  legendre_set_test01 ( )

  moulton_set_test ( )

  timestamp_test ( )
#
#  Terminate.
#
  print ''
  print 'QUADRULE_TEST:'
  print '  Normal end of execution.'

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  quadrule_test ( )
  timestamp ( )
