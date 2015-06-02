#!/usr/bin/env python
#
def rule_write ( order, header, x, w, r ):

#*****************************************************************************80
#
## RULE_WRITE writes a quadrature rule to a file.
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
#    Input, integer ORDER, the order of the rule.
#
#    Input, string HEADER, specifies the output files.
#    write files 'header_w.txt', 'header_x.txt', 'header_r.txt' defining
#    weights, abscissas, and region.
#
#    Input, real X(ORDER), the abscissas.
#
#    Input, real W(ORDER), the weights.
#
#    Input, real R(2), the region.
#
  from r8vec_write import r8vec_write

  filename_x = header + '_x.txt'
  filename_w = header + '_w.txt'
  filename_r = header + '_r.txt'

  print ''
  print '  Creating quadrature files.'
  print ''
  print '  Common header is      "%s".' % ( header )
  print ''
  print '  Weight file will be   "%s".' % ( filename_w )
  print '  Abscissa file will be "%s".' % ( filename_x )
  print '  Region file will be   "%s".' % ( filename_r )

  r8vec_write ( filename_w, order, w )
  r8vec_write ( filename_x, order, x )
  r8vec_write ( filename_r, 2,     r )

  return

def rule_write_test ( ):

#*****************************************************************************80
#
## RULE_WRITE_TEST tests RULE_WRITE.
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
  import numpy as np

  print ''
  print 'RULE_WRITE_TEST:'
  print '  RULE_WRITE writes a quadrature rule to three files.'

  header = 'rule_write_test'
  order = 5
  x = np.array ( [ \
    [ -0.906179845938663992797626878299 ], \
    [ -0.538469310105683091036314420700 ], \
    [  0.000000000000000000000000000000 ], \
    [  0.538469310105683091036314420700 ], \
    [  0.906179845938663992797626878299 ] ] )
  w = np.array ( [ \
    [ 0.236926885056189087514264040720 ], \
    [ 0.478628670499366468041291514836 ], \
    [ 0.568888888888888888888888888889 ], \
    [ 0.478628670499366468041291514836 ], \
    [ 0.236926885056189087514264040720 ] ] )
  r = np.array ( [ [ -1.0 ], [ +1.0 ] ] )

  rule_write ( order, header, x, w, r )

  print ''
  print '  The quadrature rule has been written to files.'
#
#  Terminate.
#
  print ''
  print 'RULE_WRITE_TEST:'
  print '  Normal end of execution.'

  return
  
if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  rule_write_test ( )
  timestamp ( )
