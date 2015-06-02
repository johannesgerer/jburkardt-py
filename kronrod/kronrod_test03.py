#!/usr/bin/env python

def kronrod_test03 ( ):

#*****************************************************************************80
#
## KRONROD_TEST03 uses the program to estimate an integral.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    30 April 2013
#
#  Author:
#
#    John Burkardt
#
  from f import f
  from kronrod import kronrod

  exact = 1.5643964440690497731

  print ''
  print 'KRONROD_TEST03'
  print '  Call Kronrod to estimate the integral of a function.'
  print '  Keep trying until the error is small.'
#
#  TOL just tells KRONROD how carefully it must compute X, W1 and W2.
#  It is NOT a statement about the accuracy of your integral estimate!
#
  tol = 0.000001
#
#  Start the process with a 1 point rule.
#
  n = 1

  while ( 1 ):

    [ x, w1, w2 ] = kronrod ( n, tol )
#
#  Compute the estimates.
#  There are two complications here:
#
#  1) Both rules use all the points.  However, the lower order rule uses
#     a zero weight for the points it doesn't need.
#
#  2) The points X are all positive, and are listed in descending order.
#     this means that 0 is always in the list, and always occurs as the
#     last member.  Therefore, the integral estimates should use the
#     function value at 0 once, and the function values at the other
#     X values "twice", that is, once at X and once at -X.
#
    i1 = w1[n+1-1] * f ( x[n+1-1] )
    i2 = w2[n+1-1] * f ( x[n+1-1] )

    for i in range ( 1, n + 1 ):
      i1 = i1 + w1[i-1] * ( f ( - x[i-1] ) + f ( x[i-1] ) )
      i2 = i2 + w2[i-1] * ( f ( - x[i-1] ) + f ( x[i-1] ) )

    if ( abs ( i1 - i2 ) < 0.0001 ):
      print ''
      print '  Error tolerance satisfied with N = %d' % ( n )
      print '  Coarse integral estimate = %14.6g' % ( i1 )
      print '  Fine   integral estimate = %14.6g' % ( i2 )
      print '  Error estimate = %g' % ( abs ( i2 - i1 ) )
      print '  Actual error =   %g' % ( abs ( exact - i2 ) )
      break

    if ( 25 < n ):
      print ''
      print '  Error tolerance failed even for n = %d' % ( n )
      print '  Canceling iteration, and accepting bad estimates!'
      print '  Coarse integral estimate = %14.6g' % ( i1 )
      print '  Fine   integral estimate = %14.6g' % ( i2 )
      print '  Error estimate = %g' % ( abs ( i2 - i1 ) )
      print '  Actual error =   %g' % ( abs ( exact - i2 ) )
      break

    n = 2 * n + 1

  return

