#!/usr/bin/env python

def initialize ( ):

#*****************************************************************************80
#
## INITIALIZE initializes the random number generator library.
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
#    None
#
  from antithetic_set import antithetic_set
  from cgn_set import cgn_set
  from initialized_set import initialized_set
  from set_initial_seed import set_initial_seed

  g_max = 32
#
#  Remember that we have called INITIALIZE().
#
  initialized_set ( )
#
#  Initialize all generators to have FALSE antithetic value.
#
  value = False
  for g in range ( 1, g_max + 1 ):
    cgn_set ( g )
    antithetic_set ( value )
#
#  Set the initial seeds.
#
  ig1 = 1234567890
  ig2 = 123456789
  set_initial_seed ( ig1, ig2 )
#
#  Initialize the current generator index to 1.
#
  g = 1
  cgn_set ( g )

  print ''
  print 'INITIALIZE - Note:'
  print '  The RNGLIB package has been initialized.'

  return

