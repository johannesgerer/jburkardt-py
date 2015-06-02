#!/usr/bin/env python

def wathen_test09 ( ):

#*****************************************************************************80
#
## WATHEN_TEST09 uses SPY to display the sparsity of the Wathen matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
  from matplotlib.pyplot import figure
  from matplotlib.pyplot import show
  from matplotlib.pyplot import savefig
  from wathen_ge import wathen_ge
  from wathen_order import wathen_order

  print ''
  print 'WATHEN_TEST09'
  print '  Display the sparsity of the Wathen matrix.'

  fig = figure ( )
  nx = 1
  ny = 1
  n = wathen_order ( nx, ny )
  seed = 123456789
  a, seed = wathen_ge ( nx, ny, n, seed )
  ax1 = fig.add_subplot ( 231 )
  ax1.spy ( a, markersize = 4 )

  nx = 2
  ny = 2
  n = wathen_order ( nx, ny )
  seed = 123456789
  a, seed = wathen_ge ( nx, ny, n, seed )
  ax2 = fig.add_subplot ( 232 )
  ax2.spy ( a, markersize = 4 )

  nx = 3
  ny = 3
  n = wathen_order ( nx, ny )
  seed = 123456789
  a, seed = wathen_ge ( nx, ny, n, seed )
  ax3 = fig.add_subplot ( 233 )
  ax3.spy ( a, markersize = 4 )

  nx = 4
  ny = 4
  n = wathen_order ( nx, ny )
  seed = 123456789
  a, seed = wathen_ge ( nx, ny, n, seed )
  ax4 = fig.add_subplot ( 234 )
  ax4.spy ( a, markersize = 4 )

  nx = 5
  ny = 5
  n = wathen_order ( nx, ny )
  seed = 123456789
  a, seed = wathen_ge ( nx, ny, n, seed )
  ax5 = fig.add_subplot ( 235 )
  ax5.spy ( a, markersize = 4 )

  nx = 6
  ny = 6
  n = wathen_order ( nx, ny )
  seed = 123456789
  a, seed = wathen_ge ( nx, ny, n, seed )
  ax6 = fig.add_subplot ( 236 )
  ax6.spy ( a, markersize = 4 )

  fig.suptitle ( 'WATHEN Matrix Sparsity Pattern' )

  show ( )

  filename = 'wathen_spy.png'
  fig.savefig ( filename )
  print ''
  print '  Graphics file saved as "%s"' % ( filename )

  return

if ( __name__ == '__main__' ):
  wathen_test09 ( )

