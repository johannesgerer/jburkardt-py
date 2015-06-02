#!/usr/bin/env python

def init_generator ( t ):

#*****************************************************************************80
#
## INIT_GENERATOR sets the current generator to initial, last or new seed.
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
#    Input, integer T, the seed type:
#    0, use the seed chosen at initialization time.
#    1, use the last seed.
#    2, use a new seed set 2^30 values away.
#
  from cg_set import cg_set
  from cgn_get import cgn_get
  from ig_get import ig_get
  from initialize import initialize
  from initialized_get import initialized_get
  from lg_get import lg_get
  from lg_set import lg_set
  from multmod import multmod

  a1_w = 1033780774
  a2_w = 1494757890
  m1 = 2147483563
  m2 = 2147483399
#
#  Check whether the package must be initialized.
#
  if ( not initialized_get ( ) ):
    print ''
    print 'INIT_GENERATOR - Note:'
    print '  Initializing RNGLIB package.'
    initialize ( )
#
#  Get the current generator index.
#
  g = cgn_get ( )
#
#  0: Restore the initial seed.
#
  if ( t == 0 ):

    [ ig1, ig2 ] = ig_get ( g )
    lg1 = ig1
    lg2 = ig2
    lg_set ( g, lg1, lg2 )
#
#  1: Restore the last seed.
#
  elif ( t == 1 ):

    [ lg1, lg2 ] = lg_get ( g );
#
#  Advance to a new seed.
#
  elif ( t == 2 ):

    [ lg1, lg2 ] = lg_get ( g )
    lg1 = multmod ( a1_w, lg1, m1 )
    lg2 = multmod ( a2_w, lg2, m2 )
    lg_set ( g, lg1, lg2 )

  else:

    print ''
    print 'INIT_GENERATOR - Fatal error!'
    print '  Input parameter T out of bounds.'
    exit ( 'INIT_GENERATOR - Fatal error!' )
#
#  Store the new seed.
#
  cg1 = lg1
  cg2 = lg2
  cg_set ( g, cg1, cg2 )

  return

