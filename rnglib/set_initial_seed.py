#!/usr/bin/env python

def set_initial_seed ( ig1, ig2 ):

#*****************************************************************************80
#
## SET_INITIAL_SEED resets the initial seed and state for all generators.
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
#    Input, integer IG1, IG2, the initial seed values
#    for the first generator.
#    1 <= IG1 < 2147483563
#    1 <= IG2 < 2147483399
#
  from cgn_set import cgn_set
  from ig_set import ig_set
  from init_generator import init_generator
  from initialized_get import initialized_get
  from multmod import multmod
  from sys import exit

  a1_vw = 2082007225
  a2_vw = 784306273
  g_max = 32
  m1 = 2147483563
  m2 = 2147483399

  if ( ig1 < 1 or m1 <= ig1 ):
    print ''
    print 'SET_INITIAL_SEED - Fatal error!'
    print '  Input parameter IG1 out of bounds.'
    exit ( 'SET_INITIAL_SEED - Fatal error!' )

  if ( ig2 < 1 or m2 <= ig2 ):
    print ''
    print 'SET_INITIAL_SEED - Fatal error!'
    print '  Input parameter IG2 out of bounds.'
    exit ( 'SET_INITIAL_SEED - Fatal error!' )
#
#  Because INITIALIZE calls SET_INITIAL_SEED, it's not easy to correct
#  the error that arises if SET_INITIAL_SEED is called before INITIALIZE.
#  So don't bother trying.
#
  if ( not initialized_get ( ) ):
    print ''
    print 'SET_INITIAL_SEED - Fatal error!'
    print '  The RNGLIB package has not been initialized.'
    exit ( 'SET_INITIAL_SEED - Fatal error!' )
#
#  Set the initial seed, then initialize the first generator.
#
  g = 1
  cgn_set ( g )

  ig_set ( g, ig1, ig2 )

  t = 0
  init_generator ( t )
#
#  Now do similar operations for the other generators.
#
  for g in range ( 2, g_max + 1 ):
    cgn_set ( g )
    ig1 = multmod ( a1_vw, ig1, m1 )
    ig2 = multmod ( a2_vw, ig2, m2 )
    ig_set ( g, ig1, ig2 )
    init_generator ( t )
#
#  Now choose the first generator.
#
  g = 1
  cgn_set ( g )

  return

