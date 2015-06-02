#!/usr/bin/env python

def suppress_spaces ( ):

#*****************************************************************************80
#
## SUPPRESS_SPACES demonstrates how to suppress Python's spacing convention.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import sys

  print ''
  print 'SUPPRESS_SPACES'
  print '  Demonstrate Python\'s output spacing convention,'
  print '  and how to suppress it.'

  n = 9
  b = np.array ( [ 1, 1, 0, 1, 0, 0, 1, 1, 1 ] )

  print ''
  print '  Suppose we want to print a string of binary digits,'
  print '  each stored in a separate entry of a vector.'
  print '  A print statement inside a loop might do it.'
  print ''

  for i in range ( 0, n ):
    print '%d' % ( b[i] ),
  print ''

  print ''
  print '  But suppose we want the digits right next to each other?'
  print '  We are annoyed now, that Python\'s print command, '
  print '  trying to be helpful, automatically inserts spaces.'
  print '  Try sys.stdout.write(str(VARIABLE)) instead.'
  print ''

  for i in range ( 0, n ):
    sys.stdout.write ( str ( b[i] ) ),
  print ''
#
#  Terminate.
#
  print ''
  print 'SUPPRESS_SPACES'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  suppress_spaces ( )
  timestamp ( )
