#!/usr/bin/env python

def function_args ( *args ):

#*****************************************************************************80
#
## FUNCTION_ARGS accepts and prints an arbitrary number of arguments.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    23 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, *ARGS, an arbitrary number of arguments.
#
  print ''
  print 'FUNCTION_ARGS:'
  print '  Number of arguments on this call was %d' % ( len ( args ) )
  print ''

  for count, thing in enumerate ( args ):
    print '  {0}. {1}'.format ( count, thing )

  return

def function_args_test ( ):

#*****************************************************************************80
#
## FUNCTION_ARGS_TEST tests FUNCTION_ARGS.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    23 March 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'FUNCTION_ARGS_TEST:'
  print '  FUNCTION_ARGS demonstrates how to count and print function arguments'
  print '  when the number of arguments may vary.'

  function_args ( )
  function_args ( 1.1, - 2.2, 3.3 )
  function_args ( 1, 'two', 3.3, ( 4, 5 ) )
#
#  Terminate.
#
  print ''
  print 'FUNCTION_ARGS_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  function_args_test ( )
  timestamp ( )

