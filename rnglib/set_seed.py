#!/usr/bin/env python

def set_seed ( cg1, cg2 ):

#*****************************************************************************80
#
## SET_SEED resets the initial seed and state of the current generator.
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
#    Input, integer CG1, CG2, the CG values for generator G.
#    1 <= CG1 < 2147483563
#    1 <= CG2 < 2147483399
#
  from sys import exit

  m1 = 2147483563
  m2 = 2147483399

  if ( cg1 < 1 or m1 <= cg1 ):
    print ''
    print 'SET_SEED - Fatal error!'
    print '  Input parameter CG1 out of bounds.'
    exit ( 'SET_SEED - Fatal error!' )

  if ( cg2 < 1 or m2 <= cg2 ):
    print ''
    print 'SET_SEED - Fatal error!'
    print '  Input parameter CG2 out of bounds.'
    exit ( 'SET_SEED - Fatal error!' )
#
#  Check whether the package must be initialized.
#
  if ( not initialized_get ( ) ):
    print ''
    print 'SET_SEED - Note:'
    print '  Initializing RNGLIB package.'
    initialize ( )
#
#  Retrieve the current generator index.
#
  g = cgn_get ( )
#
#  Set the seeds.
#
  cg_set ( g, cg1, cg2 )
#
#  Initialize the generator.
#
  t = 0
  init_generator ( t )

  return

