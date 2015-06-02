#!/usr/bin/env python

def advance_state ( k ):

#*****************************************************************************80
#
## ADVANCE_STATE advances the state of the current generator.
#
#  Discussion:
#
#    This procedure advances the state of the current generator by 2^K
#    values and resets the initial seed to that value.
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
#    Input, integer K, indicates that the generator is to be
#    advanced by 2^K values.
#    0 <= K.
#
  from cg_get import cg_get
  from cg_set import cg_set
  from cgn_get import cgn_get
  from initialize import initialize
  from initialized_get import initialized_get
  from multmod import multmod
  from sys import exit

  a1 = 40014
  a2 = 40692
  m1 = 2147483563
  m2 = 2147483399

  if ( k < 0 ):
    print ''
    print 'ADVANCE_STATE - Fatal error!'
    print '  Input exponent K is out of bounds.'
    exit ( 'ADVANCE_STATE - Fatal error!' )
#
#  Check whether the package must be initialized.
#
  if ( not initialized_get ( ) ):
    print ''
    print 'ADVANCE_STATE - Note:'
    print '  Initializing RNGLIB package.'
    initialize ( )
#
#  Get the current generator index.
#
  g = cgn_get ( )

  b1 = a1
  b2 = a2

  for i in range ( 1, k + 1 ):
    b1 = multmod ( b1, b1, m1 )
    b2 = multmod ( b2, b2, m2 )

  [ cg1, cg2 ] = cg_get ( g )
  cg1 = multmod ( b1, cg1, m1 )
  cg2 = multmod ( b2, cg2, m2 )
  cg_set ( g, cg1, cg2 )

  return

