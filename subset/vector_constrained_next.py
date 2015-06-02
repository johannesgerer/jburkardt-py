#! /usr/bin/env python
#
def vector_constrained_next ( n, x_min, x_max, x, more ):

#*****************************************************************************80
#
## VECTOR_CONSTRAINED_NEXT returns the "next" constrained vector.
#
#  Discussion:
#
#    We consider all vectors of dimension N whose components
#    satisfy X_MIN(1:N) <= X(1:N) <= X_MAX(1:N).
#
#    We are only interested in the subset of these vectors which
#    satisfy the following constraint:
#
#      sum ( 1 <= I <= N ) ( ( X(I) - 1 ) / X_MAX(I) ) <= 1
#
#    We can carry out this check using integer arithmetic if we
#    multiply through by P = product ( X_MAX(1:N) ):
#
#      sum ( 1 <= I <= N ) ( ( X(I) - 1 ) * ( P / X_MAX(I) ) ) <= P.
#
#    This routine returns, one at a time, and in right-to-left
#    lexicographic order, exactly those vectors which satisfy
#    the constraint.
#
#  Example:
#
#    N = 3
#    X_MIN:   2   2   1
#    X_MAX:   4   5   3
#
#    P = 60
#
#    #  X(1)  X(2)  X(3)  CONSTRAINT
#
#    1    2     2     1       27
#    2    3     2     1       42
#    3    4     2     1       57
#    4    2     3     1       39
#    5    3     3     1       54
#    6    2     4     1       51
#    7    2     2     2       47
#    8    2     3     2       59
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 May 2015
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
#    Output, integer CONSTRAINT, the constraint value for X.  Valid vectors X
#    will have a CONSTRAINT value between product(X_MIN(1:N)) (automatically)
#    and product(X_MAX(1:N)) (because we skip over vectors with a
#    constraint larger than this value).
#
#    Output, logical MORE.  On input, if the user has set MORE
#    FALSE, the user is requesting the initiation of a new sequence
#    of values.  If MORE is TRUE, then the user is requesting "more"
#    values in the current sequence.  On output, if MORE is TRUE,
#    then another value was found and returned in X, but if MORE is
#    FALSE, then there are no more values in the sequence, and X is
#    NOT the next value.
#
  import numpy as np

  x_prod = np.prod ( x_max )

  if ( not more ):

    for i in range ( 0, n ):
      x[i] = x_min[i]

    constraint = 0.0
    for i in range ( 0, n ):
      constraint = constraint + ( x[i] - 1 ) * ( x_prod / x_max[i] )

    if ( x_prod < constraint ):
      more = False
    else:
      more = True

  else:

    i = 0

    while ( True ):

      if ( x[i] < x_max[i] ):

        x[i] = x[i] + 1

        constraint = 0.0
        for i in range ( 0, n ):
          constraint = constraint + ( x[i] - 1 ) * ( x_prod / x_max[i] )

        if ( constraint <= x_prod ):
          break

      x[i] = x_min[i]

      i = i + 1

      if ( n - 1 < i ):
        more = False
        break

  return x, constraint, more

def vector_constrained_next_test ( ):

#*****************************************************************************80
#
## VECTOR_CONSTRAINED_NEXT_TEST tests VECTOR_CONSTRAINED_NEXT
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from i4vec_transpose_print import i4vec_transpose_print

  n = 3

  print ''
  print 'VECTOR_CONSTRAINED_NEXT_TEST'
  print '  VECTOR_CONSTRAINED_NEXT:'
  print '  Consider vectors:'
  print '    X_MIN(1:N) <= X(1:N) <= X_MAX(1:N),'
  print '  Set'
  print '    P = Product X_MAX(1:N)'
  print '  Accept only vectors for which:'
  print '    sum ( (X(1:N)-1) * P / X_MAX(1:N) ) <= P'

  more = False
  x_min = np.array ( [ 2, 2, 1 ] )
  x_max = np.array ( [ 4, 5, 3 ] )

  i4vec_transpose_print ( n, x_min, '  XMIN:' )
  i4vec_transpose_print ( n, x_max, '  XMAX:' )

  i = 0
  x_prod = np.prod ( x_max )

  print ''
  print '  Maximum allowed CONSTRAINT = P =        %d' % ( x_prod )
  print ''

  x = np.zeros ( n )

  while ( True ):

    x, constraint, more = vector_constrained_next ( n, x_min, x_max, x, more )

    if ( not more ):
      break

    i = i + 1
    print '  %8d:  %8d  %8d  %8d  %12d' % ( i, x[0], x[1], x[2], constraint )
#
#  Terminate.
#
  print ''
  print 'VECTOR_CONSTRAINED_NEXT_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  vector_constrained_next_test ( )
  timestamp ( )

