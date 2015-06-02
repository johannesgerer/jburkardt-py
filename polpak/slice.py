#!/usr/bin/env python

def slice ( dim_num, slice_num ):

#*****************************************************************************80
#
## SLICE: maximum number of pieces created by a given number of slices.
#
#  Discussion:
#
#    If we imagine slicing a pizza, each slice produce more pieces.  
#    The position of the slice affects the number of pieces created, but there
#    is a maximum.  
#
#    This function determines the maximum number of pieces created by a given
#    number of slices, applied to a space of a given dimension.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    26 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Robert Banks,
#    Slicing Pizzas, Racing Turtles, and Further Adventures in 
#    Applied Mathematics,
#    Princeton, 1999,
#    ISBN13: 9780691059471,
#    LC: QA93.B358.
#
#  Parameters:
#
#    Input, integer DIM_NUM, the spatial dimension.
#
#    Input, integer SLICE_NUM, the number of slices.
#
#    Input, integer VALUE, the maximum number of pieces that can
#    be created by the given number of slices applied in the given dimension.
#
  from i4_choose import i4_choose

  value = 0
  j_hi = min ( dim_num, slice_num ) + 1
  for j in range ( 0, j_hi ):
    value = value + i4_choose ( slice_num, j )

  return value

def slice_test ( ):

#*****************************************************************************80
#
## SLICE_TEST tests SLICE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 February 2015
#
#  Author:
#
#    John Burkardt
#
  dim_max = 5
  slice_max = 8

  print ''
  print 'SLICE_TEST:'
  print '  SLICE determines the maximum number of pieces created'
  print '  by SLICE_NUM slices in a DIM_NUM space.'
  print ''
  print '  SLICES',
  for slice_num in range ( 1, slice_max + 1 ):
    print '  %4d' % ( slice_num ),
  print ''

  print '  DIM'

  for dim_num in range ( 1, dim_max + 1 ):
    print '  %2d  : ' % ( dim_num ),
    for slice_num in range ( 1, slice_max + 1 ):
      value = slice ( dim_num, slice_num )
      print '  %4d' % ( value ),
    print ''

  print ''
  print 'SLICE_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  slice_test ( )
  timestamp ( )




