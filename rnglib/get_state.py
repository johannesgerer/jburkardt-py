#!/usr/bin/env python

def get_state ( ):

#*****************************************************************************80
#
## GET_STATE returns the state of the current generator.
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
#    Output, integer CG1, CG2, the CG values for the current generator.
#
  from cg_get import cg_get
  from cgn_get import cgn_get
  from initialize import initialize
  from initialized_get import initialized_get
#
#  Check whether the package must be initialized.
#
  if ( not initialized_get ( ) ):
    print ''
    print 'GET_STATE - Note:'
    print '  Initializing RNGLIB package.'
    initialize ( )
#
#  Get the current generator index.
#
  g = cgn_get ( )
#
#  Retrieve the seed values for this generator.
#
  [ cg1, cg2 ] = cg_get ( g )

  return cg1, cg2

