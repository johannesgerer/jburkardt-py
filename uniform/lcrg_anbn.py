#!/usr/bin/env python

def lcrg_anbn ( a, b, c, n ):

#*****************************************************************************80
#
## LCRG_ANBN computes the "N-th power" of a linear congruential generator.
#
#  Discussion:
#
#    We are considering a linear congruential random number generator.
#    The LCRG takes as input an integer value called SEED, and returns
#    an updated value of SEED,
#
#      SEED(out) = ( a * SEED(in) + b ) mod c.
#
#    and an associated pseudorandom real value
#
#      U = SEED(out) / c.
#
#    In most cases, a user is content to call the LCRG repeatedly, with
#    the updating of SEED being taken care of automatically.
#
#    The purpose of this routine is to determine the values of AN and BN
#    that describe the LCRG that is equivalent to N applications of the
#    original LCRG.
#
#    One use for such a facility would be to do random number computations
#    in parallel.  If each of N processors is to compute many random values,
#    you can guarantee that they work with distinct random values
#    by starting with a single value of SEED, using the original LCRG to generate
#    the first N-1 "iterates" of SEED, so that you now have N "seed" values,
#    and from now on, applying the N-th power of the LCRG to the seeds.
#
#    If the K-th processor starts from the K-th seed, it will essentially
#    be computing every N-th entry of the original random number sequence,
#    offset by K.  Thus the individual processors will be using a random
#    number stream as good as the original one, and without repeating, and
#    without having to communicate.
#
#    To evaluate the N-th value of SEED directly, we start by ignoring
#    the modular arithmetic, and working out the sequence of calculations
#    as follows:
#
#      SEED(0)   =     SEED.
#      SEED(1)   = a * SEED      + b
#      SEED(2)   = a * SEED(1)   + b = a^2 * SEED           + a * b + b
#      SEED(3)   = a * SEED(2)   + b = a^3 * SEED + a^2 * b + a * b + b
#      ...
#      SEED(N-1) = a * SEED(N-2) + b
#
#      SEED(N) = a * SEED(N-1) + b = a^N * SEED
#                                    + ( a^(n-1) + a^(n-2) + ... + a + 1 ) * b
#
#    or, using the geometric series,
#
#      SEED(N) = a^N * SEED + ( a^N - 1) / ( a - 1 ) * b
#              = AN * SEED + BN
#
#    Thus, from any SEED, we can determine the result of N applications of the
#    original LCRG directly if we can solve
#
#      ( a - 1 ) * BN = ( a^N - 1 ) * b in modular arithmetic,
#
#    and evaluate:
#
#      AN = a^N
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Barry Wilkinson, Michael Allen,
#    Parallel Programming:
#    Techniques and Applications Using Networked Workstations and Parallel Computers,
#    Prentice Hall,
#    ISBN: 0-13-140563-2,
#    LC: QA76.642.W54.
#
#  Parameters:
#
#    Input, integer A, the multiplier for the LCRG.
#
#    Input, integer B, the added value for the LCRG.
#
#    Input, integer C, the base for the modular arithmetic.
#    For 32 bit arithmetic, this is often 2^31 - 1, or 2147483647.  It is
#    required that 0 < C.
#
#    Input, integer N, the "index", or number of times that the
#    LCRG is to be applied.  It is required that 0 <= N.
#
#    Output, integer AN, BN, the multiplier and added value for
#    the LCRG that represent N applications of the original LCRG.
#
  import congruence
  import power_mod
  from sys import exit

  if ( n < 0 ):
    print ''
    print 'LCRG_ANBN - Fatal error!'
    print '  Illegal input value of N = %d' % ( n )
    exit ( 'LCRG_ANGN - Fatal error!' )

  if ( c <= 0 ):
    print ''
    print 'LCRG_ANBN - Fatal error!'
    print '  Illegal input value of C = %d' % ( c )
    exit ( 'LCRG_ANGN - Fatal error!' )

  if ( n == 0 ):
    an = 1
    bn = 0
  elif ( n == 1 ):
    an = a
    bn = b
  else:
#
#  Compute A^N.
#
    an = power_mod.power_mod ( a, n, c );
#
#  Solve
#    ( a - 1 ) * BN = ( a^N - 1 ) mod B
#  for BN.
#
    am1 = a - 1
    anm1tb = ( an - 1 ) * b

    [ bn, ierror ] = congruence.congruence ( am1, c, anm1tb )

    if ( ierror != 0 ):
      print ''
      print 'LCRG_ANBN - Fatal error!'
      print '  An error occurred in the CONGRUENCE routine.'
      print '  The error code was IERROR = %d' % ( ierror )
      exit ( 'LCRG_ANGN - Fatal error!' )

  return an, bn

def lcrg_anbn_test ( ):

#*****************************************************************************80
#
## LCRG_ANBN_TEST tests LCRG_ANBN.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
  from lcrg_evaluate import lcrg_evaluate
  import numpy as np

  print ''
  print 'LCRG_ANBN_TEST'
  print '  LCRG_ANBN determines a linear congruential random'
  print '  number generator equivalent to N steps of a given one.'
#
#  These parameters define the old (1969) IBM 360 random number generator:
#
  a = 16807
  b = 0
  c = 2147483647

  print ''
  print '  LCRG parameters:'
  print ''
  print '  A  = %d' % ( a )
  print '  B  = %d' % ( b )
  print '  C  = %d' % ( c )

  print ''
  print '             N             A             B'
  print ''

  for n in range ( 0, 11 ):
    [ an, bn ] = lcrg_anbn ( a, b, c, n )
    print '  %12d  %12d  %12d' % ( n, an, bn )


  print ''
  print '                           N            In           Out'
  print ''

  k = 0
  u = 12345
  print '                %12d                %12d' % ( k, u )
  for k in range ( 1, 12 ):
    v = lcrg_evaluate ( a, b, c, u )
    print '                %12d  %12d  %12d' % ( k, u, v )
    u = v
#
#  Now try to replicate these results using N procesors.
#
  n = 4

  [ an, bn ] = lcrg_anbn ( a, b, c, n )

  print ''
  print '  LCRG parameters:'
  print ''
  print '  AN = %d' % ( an )
  print '  BN = %d' % ( bn )
  print '  C  = %d' % ( c )
  print ''
  print '             J             N            In           Out'
  print ''

  x = np.zeros ( n )

  x[0] = 12345;
  for j in range ( 1, n ):
    x[j] = lcrg_evaluate ( a, b, c, x[j-1] )

  for j in range ( 0, n ):
    print '  %12d  %12d                %12d' % ( j, j, x[j] )

  y = np.zeros ( n )

  for k in range ( n, 12, n ):
    for j in range ( 0, n ):
      y[j] = lcrg_evaluate ( an, bn, c, x[j] )
      print '  %12d  %12d  %12d  %12d' % ( j, k+j, x[j], y[j] )
      x[j] = y[j];
#
#  Terminate.
#
  print ''
  print 'LCRG_ANBN_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  lcrg_anbn_test ( )
  timestamp ( )
