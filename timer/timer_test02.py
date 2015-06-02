#!/usr/bin/env python

def timer_test02 ( ) :

#*****************************************************************************80
#
## TIMER_TEST02 uses TIME to time the NUMPY.RANDOM.RANDOM_SAMPLE() function.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 May 2013
#
#  Author:
#
#    John Burkardt
#
  from time import time
  import numpy as np

  n_log_min = 10
  n_log_max = 22
  n_min = 2 ** n_log_min
  n_max = 2 ** n_log_max
  n_rep = 5
  n_test = 1

  print
  print 'TIMER_TEST02'
  print '  Use TIME() to time the RANDOM_SAMPLE function:'
  print
  print '    x = numpy.random.random_sample ( ( n, 1 ) );'
  print
  print '  Data vectors will be of minimum size %d' % ( n_min )
  print '  Data vectors will be of maximum size %d' % ( n_max )
  print '  Number of repetitions of the operation: %d' % ( n_rep )
  print
  print '  Timing results in seconds:'
  print
  print '      Size         Rep #1         Rep #2         Rep #3        ',
  print 'Rep #4         Rep #5'
  print

  for n_log in range ( n_log_min, n_log_max + 1 ):

    n = 2 ** ( n_log )

    print '  %8d' % ( n ),

    for i_rep in range ( 0, n_rep ):

      seconds = time ( )

      x = np.random.random_sample ( ( n, 1 ) );

      seconds = time ( ) - seconds

      print '  %12f' % ( seconds ),

    print

  return

