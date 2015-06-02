#!/usr/bin/env python

def r4_uniform_01 ( ):

#*****************************************************************************80
#
## R4_UNIFORM_01 returns a uniform random real number in [0,1].
#
#  Discussion:
#
#    This procedure returns a random floating point number from a uniform
#    distribution over (0,1), not including the endpoint values, using the
#    current random number generator.
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
#    MATLAB version by John Burkardt.
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
#    Output, real R4_UNIFORM_01, a uniform random value in [0,1].
#
  from i4_uniform import i4_uniform
  from initialize import initialize
  from initialized_get import initialized_get
#
#  Check whether the package must be initialized.
#
  if ( not initialized_get ( ) ):
    print ''
    print 'R4_UNIFORM_01 - Note:'
    print '  Initializing RNGLIB package.'
    initialize ( )
#
#  Get a random positive integer.
#
  i = i4_uniform ( )
#
#  Scale it to a random real in [0,1].
#
  value = i * 4.656613057E-10

  return value

