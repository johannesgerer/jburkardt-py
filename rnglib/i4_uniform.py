#!/usr/bin/env python

def i4_uniform ( ):

#*****************************************************************************80
#
## I4_UNIFORM generates a random positive integer.
#
#  Discussion:
#
#    This procedure returns a random integer following a uniform distribution
#    over (1, 2147483562) using the current generator.
#
#    The original name of this function was "random()", but this conflicts
#    with a standard library function name in C.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 May 2013
#
#  Author:
#
#    Original Pascal version by Pierre L'Ecuyer, Serge Cote.
#    PYTHON version by John Burkardt.
#
#  Reference:
#
#    Pierre LEcuyer, Serge Cote,
#    Implementing a Random Number Package with Splitting Facilities,
#    ACM Transactions on Mathematical Software,
#    Volume 17, Number 1, March 1991, pages 98-111.
#
#  Parameters:
#
#    Output, integer VALUE, the random integer.
#
  from antithetic_get import antithetic_get
  from cg_get import cg_get
  from cg_set import cg_set
  from cgn_get import cgn_get
  from i4_division import i4_division
  from initialize import initialize
  from initialized_get import initialized_get

  a1 = 40014
  a2 = 40692
  m1 = 2147483563
  m2 = 2147483399
#
#  Check whether the package must be initialized.
#
  if ( not initialized_get ( ) ):
    print ''
    print 'I4_UNIFORM - Note:'
    print '  Initializing RNGLIB package.'
    initialize ( )
#
#  Get the current generator index.
#
  g = cgn_get ( )
#
#  Retrieve the seeds for the current generator.
#
  [ cg1, cg2 ] = cg_get ( g )
#
#  Update the seeds.
#
  k = i4_division ( cg1, 53668 )
  cg1 = a1 * ( cg1 - k * 53668 ) - k * 12211

  if ( cg1 < 0 ):
    cg1 = cg1 + m1

  k = i4_division ( cg2, 52774 )
  cg2 = a2 * ( cg2 - k * 52774 ) - k * 3791

  if ( cg2 < 0 ):
    cg2 = cg2 + m2
#
#  Store the updated seeds.
#
  cg_set ( g, cg1, cg2 )
#
#  Construct the random integer from the seeds.
#
  z = cg1 - cg2

  if ( z < 1 ):
    z = z + m1 - 1
#
#  If the generator is in antithetic mode, we must reflect the value.
#
  value = antithetic_get ( )

  if ( value ):
    z = m1 - z

  return z

