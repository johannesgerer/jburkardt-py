#!/usr/bin/env python
#
def truncated_normal_rule ( *args ):

#*****************************************************************************80
#
## MAIN is the main program for TRUNCATED_NORMAL_RULE.
#
#  Discussion:
#
#    This program computes a truncated normal quadrature rule
#    and writes it to a file.
#
#    The user specifies:
#    * option: 0/1/2/3 for none, lower, upper, double truncation.
#    * N, the number of points in the rule
#    * MU, the mean of the original normal distribution
#    * SIGMA, the standard deviation of the original normal distribution,
#    * A, the left endpoint (for options 1 or 3)
#    * B, the right endpoint (for options 2 or 3)
#    * HEADER, the root name of the output files.
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
  from moment_method              import moment_method
  from normal_ms_moment           import normal_ms_moments
  from r8_huge                    import r8_huge
  from rule_write                 import rule_write
  from sys                        import exit
  from truncated_normal_a_moment  import truncated_normal_a_moments
  from truncated_normal_ab_moment import truncated_normal_ab_moments
  from truncated_normal_b_moment  import truncated_normal_b_moments

  print ''
  print 'TRUNCATED_NORMAL_RULE'
  print '  Python version'
  print ''
  print '  For the (truncated) Gaussian probability density function'
  print '    pdf(x) = exp(-0.5*((x-MU)/SIGMA)^2) / SIGMA / sqrt ( 2 * pi )'
  print '  compute an N-point quadrature rule for approximating'
  print '    Integral ( A <= x <= B ) f(x) pdf(x) dx'
  print ''
  print '  The value of OPTION determines the truncation interval [A,B]:'
  print '  0: (-oo,+oo)'
  print '  1: [A,+oo)'
  print '  2: (-oo,B]'
  print '  3: [A,B]'
  print ''
  print '  The user specifies OPTION, N, MU, SIGMA, A, B and FILENAME.'
  print ''
  print '  HEADER is used to generate 3 files:'
  print ''
  print '    header_w.txt - the weight file'
  print '    header_x.txt - the abscissa file.'
  print '    header_r.txt - the region file, listing A and B.'

  argument_count = ( len ( args ) )

  iarg = 0
#
#  Get OPTION.
#
  if ( argument_count < iarg + 1 ):
    option = eval ( input ( '  Enter OPTION, 0/1/2/3:  ' ) )
  else:
    option = args[iarg]
    iarg = iarg + 1

  if ( option < 0 or 3 < option ):
    print ''
    print 'TRUNCATED_NORMAL_RULE - Fatal error!'
    print '  0 <= OPTION <= 3 was required.'
    exit ( 'TRUNCATED_NORMAL_RULE - Fatal error!' )
#
#  Get N.
#
  if ( argument_count < iarg + 1 ):
    n = eval ( input ( '  Enter the rule order N:  ' ) )
  else:
    n = args[iarg]
    iarg = iarg + 1
#
#  Get MU.
#
  if ( argument_count < iarg + 1 ):
    mu = eval ( input ( '  Enter MU, the mean value of the normal distribution:  ' ) )
  else:
    mu = args[iarg]
    iarg = iarg + 1
#
#  Get SIGMA.
#
  if ( argument_count < iarg + 1 ):
    sigma = eval ( input ( '  Enter SIGMA, the standard deviation:  ' ) )
  else:
    sigma = args[iarg]
    iarg = iarg + 1
#
#  Get A.
#
  if ( option == 1 or option == 3 ):
    if ( argument_count < iarg + 1 ):
      a = eval ( input ( '  Enter the left endpoint A:  ' ) )
    else:
      a = args[iarg]
      iarg = iarg + 1
  else:
    a = - r8_huge ( )
#
#  Get B.
#
  if ( option == 2 or option == 3 ):
    if ( argument_count < iarg + 1 ):
      b = eval ( input ( '  Enter the right endpoint B:  ' ) )
    else:
      b = args[iarg]
      iarg = iarg + 1
  else:
    b = r8_huge ( )
#
#  Get HEADER.
#
  if ( argument_count < iarg + 1 ):
    print ''
    print '  HEADER is the "root name" of the quadrature files.'
    header = input ( '  Enter HEADER as a quoted string:  ' )
  else:
    header = args[iarg]
    iarg = iarg + 1
#
#  Input summary.
#
  print ''
  print '  OPTION = %d' % ( option )
  print '  N = %d' % ( n )
  print '  MU = %g' % ( mu )
  print '  SIGMA = %g' % ( sigma )
  if ( option == 1 or option == 3 ):
    print '  A = %g' % ( a )
  else:
    print '  A = -oo'

  if ( option == 2 or option == 3 ):
    print '  B = %g' % ( b )
  else:
    print '  B = +oo'

  print '  HEADER = "%s"' % ( header )
#
#  Compute the moments.
#
  if ( option == 0 ):
    moment = normal_ms_moments ( 2 * n + 1, mu, sigma )
  elif ( option == 1 ):
    moment = truncated_normal_a_moments ( 2 * n + 1, mu, sigma, a )
  elif ( option == 2 ):
    moment = truncated_normal_b_moments ( 2 * n + 1, mu, sigma, b )
  elif ( option == 3 ):
    moment = truncated_normal_ab_moments ( 2 * n + 1, mu, sigma, a, b )
#
#  Compute the rule.
#
  x, w = moment_method ( n, moment )

  r = np.array ( [ [ a ], [ b ] ] )
#
#  Write the rule.
#
  rule_write ( n, header, x, w, r )
#
#  Terminate.
#
  print ''
  print 'TRUNCATED_NORMAL_RULE:'
  print '  Normal end of execution.'

  return

def option0_test ( ):

#*****************************************************************************80
#
## OPTION0_TEST calls TRUNCATED_NORMAL_RULE with OPTION = 0.
#
#  Discussion:
#
#    This program computes a truncated normal quadrature rule
#    and writes it to a file.
#
#    The user specifies:
#    * option: 0/1/2/3 for none, lower, upper, double truncation.
#    * N, the number of points in the rule
#    * MU, the mean of the original normal distribution
#    * SIGMA, the standard deviation of the original normal distribution,
#    * HEADER, the root name of the output files.
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
  print 'OPTION0_TEST:'
  print '  Get a quadrature rule for the untruncated normal distribution.'

  option = 0
  n = 5
  mu = 1.0
  sigma = 2.0
  header = 'option0'
  truncated_normal_rule ( option, n, mu, sigma, header )
#
#  Terminate.
#
  print ''
  print 'OPTION0_TEST:'
  print '  Normal end of execution.'

  return

def option1_test ( ):

#*****************************************************************************80
#
## OPTION1_TEST calls TRUNCATED_NORMAL_RULE with OPTION = 1.
#
#  Discussion:
#
#    This program computes a truncated normal quadrature rule
#    and writes it to a file.
#
#    The user specifies:
#    * option: 0/1/2/3 for none, lower, upper, double truncation.
#    * N, the number of points in the rule
#    * MU, the mean of the original normal distribution
#    * SIGMA, the standard deviation of the original normal distribution,
#    * A, the lower truncation limit.
#    * HEADER, the root name of the output files.
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
  print 'OPTION1_TEST:'
  print '  Get a quadrature rule for the lower truncated normal distribution.'

  option = 1
  n = 9
  mu = 2.0
  sigma = 0.5
  a = 0.0
  header = 'option1'
  truncated_normal_rule ( option, n, mu, sigma, a, header )
#
#  Terminate.
#
  print ''
  print 'OPTION1_TEST:'
  print '  Normal end of execution.'

  return

def option2_test ( ):

#*****************************************************************************80
#
## OPTION2_TEST calls TRUNCATED_NORMAL_RULE with OPTION = 2.
#
#  Discussion:
#
#    This program computes a truncated normal quadrature rule
#    and writes it to a file.
#
#    The user specifies:
#    * option: 0/1/2/3 for none, lower, upper, double truncation.
#    * N, the number of points in the rule
#    * MU, the mean of the original normal distribution
#    * SIGMA, the standard deviation of the original normal distribution,
#    * B, the upper truncation limit.
#    * HEADER, the root name of the output files.
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
  print 'OPTION2_TEST:'
  print '  Get a quadrature rule for the upper truncated normal distribution.'

  option = 2
  n = 9
  mu = 2.0
  sigma = 0.5
  b = 3.0
  header = 'option2'
  truncated_normal_rule ( option, n, mu, sigma, b, header )
#
#  Terminate.
#
  print ''
  print 'OPTION2_TEST:'
  print '  Normal end of execution.'

  return

def option3_test ( ):

#*****************************************************************************80
#
## OPTION3_TEST calls TRUNCATED_NORMAL_RULE with OPTION = 3.
#
#  Discussion:
#
#    This program computes a truncated normal quadrature rule
#    and writes it to a file.
#
#    The user specifies:
#    * option: 0/1/2/3 for none, lower, upper, double truncation.
#    * N, the number of points in the rule
#    * MU, the mean of the original normal distribution
#    * SIGMA, the standard deviation of the original normal distribution,
#    * A, the lower truncation limit.
#    * B, the upper truncation limit.
#    * HEADER, the root name of the output files.
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
  print 'OPTION3_TEST:'
  print '  Get a quadrature rule for the truncated normal distribution.'

  option = 3
  n = 5
  mu = 100.0
  sigma = 25.0
  a = 50.0
  b = 150.0
  header = 'option3'
  truncated_normal_rule ( option, n, mu, sigma, a, b, header )
#
#  Terminate.
#
  print ''
  print 'OPTION3_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  option0_test ( )
  option1_test ( )
  option2_test ( )
  option3_test ( )
  timestamp ( )
