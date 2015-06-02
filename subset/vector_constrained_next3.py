#! /usr/bin/env python
#
def vector_constrained_next3 ( n, x_min, x_max, x, more ):

#*****************************************************************************80
#
## VECTOR_CONSTRAINED_NEXT3 returns the "next" constrained vector.
#
#  Discussion:
#
#    This routine addresses the same problem as VECTOR_CONSTRAINED_NEXT2,
#    and differs only in that real arithmetic is used, rather than
#    integer arithmetic.  Integer arithmetic allows us to do an exact
#    calculation, but we run into overflow problems in simple cases
#    where N is 10 and the X_MAX entries are of order 10, for instance.
#
#    We consider all vectors of dimension N whose components
#    satisfy X_MIN(1:N) <= X(1:N) <= X_MAX(1:N).
#
#    We are only interested in the subset of these vectors which
#    satisfy the following constraint:
#
#      sum ( 1 <= I <= N ) ( X(I) / X_MAX(I) ) <= 1
#
#  Example:
#
#    N = 3
#    X_MIN:   1   1   1
#    X_MAX:   5   6   4
#
#    P = 120
#
#    #  X(1)  X(2)  X(3)  CONSTRAINT
#
#    1    1     1     1      0.62
#    2    2     1     1      0.82
#    3    1     2     1      0.78
#    4    2     2     1      0.98
#    5    1     3     1      0.95
#    6    1     1     2      0.87
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of components in the vector.
#
#    Input, integer X_MIN(N), X_MAX(N), the minimum and maximum
#    values allowed in each component.
#
#    Input, integer X(N).  On first call (with MORE = FALSE),
#    the input value of X is not important.  On subsequent calls, the
#    input value of X should be the output value from the previous call.
#    On output, (with MORE = TRUE), the value of X will be the "next"
#    vector in the reverse lexicographical list of vectors that satisfy
#    the condition.  However, on output with MORE = FALSE, the vector
#    X is meaningless, because there are no more vectors in the list.
#
#    Input, logical MORE.  On input, if the user has set MORE
#    FALSE, the user is requesting the initiation of a new sequence
#    of values.  If MORE is TRUE, then the user is requesting "more"
#    values in the current sequence.  On output, if MORE is TRUE,
#    then another value was found and returned in X, but if MORE is
#    FALSE, then there are no more values in the sequence, and X is
#    NOT the next value.
#
#    Output, integer X(N).  On first call (with MORE = FALSE),
#    the input value of X is not important.  On subsequent calls, the
#    input value of X should be the output value from the previous call.
#    On output, (with MORE = TRUE), the value of X will be the "next"
#    vector in the reverse lexicographical list of vectors that satisfy
#    the condition.  However, on output with MORE = FALSE, the vector
#    X is meaningless, because there are no more vectors in the list.
#
#    Output, real CONSTRAINT, the constraint value for X.  
#    Valid vectors X will have a CONSTRAINT value between 
#      product(X_MIN(1:N)) / product(X_MAX(1:N))
#    and 1.0.
#
#    Output, logical MORE.  On input, if the user has set MORE
#    FALSE, the user is requesting the initiation of a new sequence
#    of values.  If MORE is TRUE, then the user is requesting "more"
#    values in the current sequence.  On output, if MORE is TRUE,
#    then another value was found and returned in X, but if MORE is
#    FALSE, then there are no more values in the sequence, and X is
#    NOT the next value.
#
  if ( not more ):

    for i in range ( 0, n ):
      x[i] = x_min[i]

    constraint = 0.0
    for i in range ( 0, n ):
      constraint = constraint + float ( x[i] ) / float ( x_max[i] )

    if ( 1.0 < constraint ):
      more = False
    else:
      more = True

    return x, constraint, more

  else:

    j = 0

    while ( True ):

      if ( x[j] < x_max[j] ):

        x[j] = x[j] + 1

        constraint = 0.0
        for i in range ( 0, n ):
          constraint = constraint + float ( x[i] ) / float ( x_max[i] )

        if ( constraint <= 1.0 ):
          break

      x[j] = x_min[j]

      j = j + 1

      if ( n - 1 < j ):
        more = False
        break

  return x, constraint, more

def vector_constrained_next3_test ( ):

#*****************************************************************************80
#
## VECTOR_CONSTRAINED_NEXT3_TEST tests VECTOR_CONSTRAINED_NEXT3.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from i4vec_transpose_print import i4vec_transpose_print

  n_max = 3

  print ''
  print 'VECTOR_CONSTRAINED_NEXT3_TEST'
  print '  VECTOR_CONSTRAINED_NEXT3:'
  print '  Consider vectors:'
  print '    X_MIN(1:N) <= X(1:N) <= X_MAX(1:N),'
  print '  Set'
  print '    CONSTRAINT = sum ( X(1:N) / X_MAX(1:N) )'
  print '  Accept only vectors for which:'
  print '    CONSTRAINT <= 1'

  x_min = np.array ( [ 1, 1, 1 ] )
  x_max = np.array ( [ 5, 6, 4 ] )

  for n in range ( 2, n_max + 1 ):

    more = False

    i4vec_transpose_print ( n, x_min, '  XMIN:' )
    i4vec_transpose_print ( n, x_max, '  XMAX:' )

    i = 0
    x_prod = np.prod ( x_max )

    print ''
    print '  Maximum allowed CONSTRAINT = P =        %d' % ( x_prod )
    print ''

    x = np.zeros ( n )

    while ( True ):

      x, constraint, more = vector_constrained_next3 ( n, x_min, x_max, x, \
        more )

      if ( not more ):
        break

      i = i + 1
      print '  %8d' % ( i ),
      for j in range ( 0, n ):
        print '  %8d' % ( x[j] ),
      print '  %12g' % ( constraint )
#
#  Terminate.
#
  print ''
  print 'VECTOR_CONSTRAINED_NEXT3_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  vector_constrained_next3_test ( )
  timestamp ( )

