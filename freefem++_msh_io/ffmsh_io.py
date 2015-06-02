#! /usr/bin/env python
#
def ffmsh_2d_data_example ( v_num, e_num, t_num ):

#*****************************************************************************80
#
## FFMSH_2D_DATA_EXAMPLE returns example FFMSH data.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer V_NUM, the number of vertices.
#
#    Input, integer E_NUM, the number of boundary edges.
#
#    Input, integer T_NUM, the number of triangles.
#
#    Output, real V_XY(2,V_NUM), vertex coordinates.
#
#    Output, integer V_L(V_NUM), vertex labels.
#
#    Output, integer E_V(2,E_NUM), edge vertices.
#
#    Output, integer E_L(E_NUM), vertex labels.
#
#    Output, integer T_V(3,T_NUM), triangle vertices.
#
#    Output, integer T_L(T_NUM), triangle labels.
#
  import numpy as np

  v_l = np.array ( [ \
    1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1 ] );

  v_xy = np.array ( [ \
    [ -0.309016994375,  0.951056516295 ], \
    [ -0.809016994375,  0.587785252292 ], \
    [ -0.321175165867,  0.475528256720 ], \
    [  0.309016994375,  0.951056516295 ], \
    [ -1.000000000000,  0.000000000000 ], \
    [  0.809016994375,  0.587785252292 ], \
    [ -0.333333334358,  0.000000000000 ], \
    [  0.237841829972,  0.293892623813 ], \
    [ -0.809016994375, -0.587785252292 ], \
    [ -0.321175165867, -0.475528259963 ], \
    [  1.000000000000,  0.000000000000 ], \
    [  0.206011327827, -0.391856835534 ], \
    [ -0.309016994375, -0.951056516295 ], \
    [  0.809016994375, -0.587785252292 ], \
    [  0.309016994375, -0.951056516295 ] \
  ] )

  v_xy = v_xy.T

  e_l = np.array ( [ \
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ] )

  e_v = np.array ( [ \
    [ 11,  6 ], \
    [  6,  4 ], \
    [  4,  1 ], \
    [  1,  2 ], \
    [  2,  5 ], \
    [  5,  9 ], \
    [  9, 13 ], \
    [ 13, 15 ], \
    [ 15, 14 ], \
    [ 14, 11 ] \
  ] )

  e_v = e_v.T

  t_l = np.array ( [ \
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ] )

  t_v = np.array ( [ \
    [   1,  3,  4 ], \
    [   7,  2,  5 ], \
    [   9,  7,  5 ], \
    [   8,  6,  4 ], \
    [  12,  8,  7 ], \
    [  12, 11,  8 ], \
    [   3,  1,  2 ], \
    [   7,  3,  2 ], \
    [   7,  8,  3 ], \
    [   4,  3,  8 ], \
    [   6,  8, 11 ], \
    [  12,  7, 10 ], \
    [  11, 12, 14 ], \
    [  10,  9, 13 ], \
    [  12, 10, 13 ], \
    [   7,  9, 10 ], \
    [  12, 13, 15 ], \
    [  14, 12, 15 ] \
  ] )

  t_v = t_v.T

  return v_xy, v_l, e_v, e_l, t_v, t_l

def ffmsh_2d_data_print ( title, v_num, e_num, t_num, v_xy, v_l, e_v, \
  e_l, t_v, t_l ):

#*****************************************************************************80
#
## FFMSH_2D_DATA_PRINT prints FFMSH data.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, string TITLE, a title.
#
#    Input, integer V_NUM, the number of vertices.
#
#    Input, integer E_NUM, the number of boundary edges.
#
#    Input, integer T_NUM, the number of triangles.
#
#    Input, real V_XY(2,V_NUM), vertex coordinates.
#
#    Input, integer V_L(V_NUM), vertex labels.
#
#    Input, integer E_V(2,E_NUM), edge vertices.
#
#    Input, integer E_L(E_NUM), vertex labels.
#
#    Input, integer T_V(3,T_NUM), triangle vertices.
#
#    Input, integer T_L(T_NUM), triangle labels.
#
  print ''
  print title
  
  i4vec_print (              v_num, v_l,  '  Vertex labels:' )
  r8mat_transpose_print ( 2, v_num, v_xy, '  Vertex coordinates:' )
  i4vec_print (              e_num, e_l,  '  Edge labels:' )
  i4mat_transpose_print ( 2, e_num, e_v,  '  Edge vertices:' )
  i4vec_print (              t_num, t_l,  '  Triangle labels:' )
  i4mat_transpose_print ( 3, t_num, t_v,  '  Triangle vertices:' )

  return

def ffmsh_2d_data_read ( ffmsh_filename, v_num, e_num, t_num ):

#*****************************************************************************80
#
## FFMSH_2D_DATA_READ reads data from an FFMSH file.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, string FFMSH_FILENAME, the FFMSH filename.
#
#    Input, integer V_NUM, the number of vertices.
#
#    Input, integer E_NUM, the number of boundary edges.
#
#    Input, integer T_NUM, the number of triangles.
#
#    Output, real V_XY(2,V_NUM), vertex coordinates.
#
#    Output, integer V_L(V_NUM), vertex labels.
#
#    Output, integer E_V(2,E_NUM), edge vertices.
#
#    Output, integer E_L(E_NUM), vertex labels.
#
#    Output, integer T_V(3,T_NUM), triangle vertices.
#
#    Output, integer T_L(T_NUM), triangle labels.
#
  import numpy as np

  ffmsh_unit = open ( ffmsh_filename, 'r' )

  line = ffmsh_unit.readline ( )
  words = line.strip().split()
  v_num2 = int ( words[0] )
  t_num2 = int ( words[1] )
  e_num2 = int ( words[2] )
#
#  Read Vertex X, Y, Label
#
  v_xy = np.zeros ( [ 2, v_num ] )
  v_l = np.zeros ( v_num )

  for j in range ( 0, v_num ):
    line = ffmsh_unit.readline ( )
    words = line.strip().split()
    v_xy[0,j] = float ( words[0] )
    v_xy[1,j] = float ( words[1] )
    v_l[j] = int ( words[2] )
#
#  Read Triangle V1, V2, V3, Label
#
  t_v = np.zeros ( [3, t_num ] )
  t_l = np.zeros ( t_num )

  for j in range ( 0, t_num ):
    line = ffmsh_unit.readline ( )
    words = line.strip().split()
    t_v[0,j] = int ( words[0] )
    t_v[1,j] = int ( words[1] )
    t_v[2,j] = int ( words[2] )
    t_l[j] = int ( words[3] )
#
#  Read Edge V1, V2, Label
#
  e_v = np.zeros ( [ 2, e_num ] )
  e_l = np.zeros ( e_num )

  for j in range ( 0, e_num ):
    line = ffmsh_unit.readline ( )
    words = line.strip().split()
    e_v[0,j] = int ( words[0] )
    e_v[1,j] = int ( words[1] )
    e_l[j] = int ( words[2] )

  ffmsh_unit.close ( )

  return v_xy, v_l, e_v, e_l, t_v, t_l

def ffmsh_2d_size_example ( ):

#*****************************************************************************80
#
## FFMSH_2D_SIZE_EXAMPLE returns sizes for the 2D example.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, integer V_NUM, the number of vertices.
#
#    Output, integer E_NUM, the number of boundary edges.
#
#    Output, integer T_NUM, the number of triangles.
#
  e_num = 10
  t_num = 18
  v_num = 15

  return v_num, e_num, t_num

def ffmsh_2d_size_print ( title, v_num, e_num, t_num ):

#*****************************************************************************80
#
## FFMSH_2D_SIZE_PRINT prints the sizes of an FFMSH.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, string TITLE, a title.
#
#    Input, integer V_NUM, the number of vertices.
#
#    Input, integer E_NUM, the number of boundary edges.
#
#    Input, integer T_NUM, the number of triangles.
#
  print ''
  print title
  print ''
  print '  Number of vertices = %d' % ( v_num )
  print '  Number of boundary edges = %d' % ( e_num )
  print '  Number of triangles = %d' % ( t_num )

  return

def ffmsh_2d_size_read ( ffmsh_filename ):

#*****************************************************************************80
#
## FFMSH_2D_SIZE_READ reads sizes from a FFMSH file.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, string FFMSH_FILENAME, the FFMSH filename.
#
#    Output, integer V_NUM, the number of vertices.
#
#    Output, integer E_NUM, the number of boundary edges.
#
#    Output, integer T_NUM, the number of triangles.
#
  ffmsh_unit = open ( ffmsh_filename, 'r' )

  line = ffmsh_unit.readline ( )

  words = line.strip().split()

  v_num = int ( words[0] )
  t_num = int ( words[1] )
  e_num = int ( words[2] )

  ffmsh_unit.close ( )

  return v_num, e_num, t_num

def ffmsh_2d_write ( ffmsh_filename, v_num, e_num, t_num, v_xy, v_l, \
  e_v, e_l, t_v, t_l ):

#*****************************************************************************80
#
## FFMSH_2D_WRITE writes FFMSH data to a file.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, string FFMSH_FILENAME, the name of the file.
#
#    Input, integer V_NUM, the number of vertices.
#
#    Input, integer E_NUM, the number of boundary edges.
#
#    Input, integer T_NUM, the number of triangles.
#
#    Input, real V_XY(2,V_NUM), vertex coordinates.
#
#    Input, integer V_L(V_NUM), vertex labels.
#
#    Input, integer E_V(2,E_NUM), edge vertices.
#
#    Input, integer E_L(E_NUM), vertex labels.
#
#    Input, integer T_V(3,T_NUM), triangle vertices.
#
#    Input, integer T_L(T_NUM), triangle labels.
#

#
#  Open the file.
#
  ffmsh_unit = open ( ffmsh_filename, 'wt' )
#
#  Write the data.
#
  ffmsh_unit.write ( \
    repr ( v_num ) + '  ' \
  + repr ( t_num ) + '  ' \
  + repr ( e_num ) + '\n' )

  for j in range ( 0, v_num ):
    ffmsh_unit.write ( \
      repr ( v_xy[0,j] ) + '  ' \
    + repr ( v_xy[1,j] ) + '  ' \
    + repr ( v_l[j] ) + '\n' )

  for j in range ( 0, t_num ):
    ffmsh_unit.write ( \
      repr ( t_v[0,j] ) + '  ' \
    + repr ( t_v[1,j] ) + '  ' \
    + repr ( t_v[2,j] ) + '  ' 
    + repr ( t_l[j] )   + '\n' )

  for j in range ( 0, e_num ):
    ffmsh_unit.write ( \
      repr ( e_v[0,j] ) + '  ' \
    + repr ( e_v[1,j] ) + '  ' \
    + repr ( e_l[j] )   + '\n' )

  ffmsh_unit.close ( )

  return

def i4mat_transpose_print ( m, n, a, title ):

#*****************************************************************************80
#
## I4MAT_TRANSPOSE_PRINT prints an I4MAT, transposed.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 November 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the number of rows in A.
#
#    Input, integer N, the number of columns in A.
#
#    Input, integer A(M,N), the matrix.
#
#    Input, string TITLE, a title.
#
  i4mat_transpose_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

def i4mat_transpose_print_test ( ):

#*****************************************************************************80
#
## I4MAT_TRANSPOSE_PRINT_TEST tests I4MAT_TRANSPOSE_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 November 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ''
  print 'I4MAT_TRANSPOSE_PRINT_TEST:'
  print '  Test I4MAT_TRANSPOSE_PRINT, which prints an I4MAT, tranposed.'

  m = 5
  n = 3
  a = np.array ( ( \
    ( 11, 12, 13 ), \
    ( 21, 22, 23 ), \
    ( 31, 32, 33 ), \
    ( 41, 42, 43 ), \
    ( 51, 52, 53 ) ) )
  title = '  A 5 x 3 integer matrix:'
  i4mat_transpose_print ( m, n, a, title )

  print ''
  print 'I4MAT_TRANSPOSE_PRINT_TEST:'
  print '  Normal end of execution.'

  return

def i4mat_transpose_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## I4MAT_TRANSPOSE_PRINT_SOME prints a portion of an I4MAT, transposed.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns of the matrix.
#
#    Input, integer A(M,N), an M by N matrix to be printed.
#
#    Input, integer ILO, JLO, the first row and column to print.
#
#    Input, integer IHI, JHI, the last row and column to print.
#
#    Input, string TITLE, a title.
#
  incx = 5

  print ''
  print title

  if ( m <= 0 or n <= 0 ):
    print ''
    print '  (None)'
    return

  for i2lo in range ( max ( ilo, 0 ), min ( ihi, m - 1 ), incx ):

    i2hi = i2lo + incx - 1
    i2hi = min ( i2hi, m - 1 )
    i2hi = min ( i2hi, ihi )
    
    print ''
    print '  Row: ',

    for i in range ( i2lo, i2hi + 1 ):
      print '%7d  ' % ( i ),

    print ''
    print '  Col'

    j2lo = max ( jlo, 0 )
    j2hi = min ( jhi, n - 1 )

    for j in range ( j2lo, j2hi + 1 ):

      print ' %4d: ' % ( j ),
      
      for i in range ( i2lo, i2hi + 1 ):
        print '%7d  ' % ( a[i,j] ),

      print ''

  return

def i4mat_transpose_print_some_test ( ):

#*****************************************************************************80
#
## I4MAT_TRANSPOSE_PRINT_SOME_TEST tests I4MAT_TRANSPOSE_PRINT_SOME.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ''
  print 'I4MAT_TRANSPOSE_PRINT_SOME_TEST'
  print '  I4MAT_TRANSPOSE_PRINT_SOME prints some of an I4MAT, transposed.'

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11, 12, 13, 14, 15, 16 ], 
    [ 21, 22, 23, 24, 25, 26 ], 
    [ 31, 32, 33, 34, 35, 36 ], 
    [ 41, 42, 43, 44, 45, 46 ] ], dtype = np.int32 )
  i4mat_transpose_print_some ( m, n, v, 0, 3, 2, 5, \
    '  Here is I4MAT, rows 0:2, cols 3:5:' )

  print ''
  print 'I4MAT_TRANSPOSE_PRINT_SOME_TEST:'
  print '  Normal end of execution.'

  return

def i4vec_print ( n, a, title ):

#*****************************************************************************80
#
## I4VEC_PRINT prints an I4VEC.
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
#  Parameters:
#
#    Input, integer N, the dimension of the vector.
#
#    Input, integer A(N), the vector to be printed.
#
#    Input, string TITLE, a title.
#
  print ''
  print title
  print ''
  for i in range ( 0, n ):
    print '%6d  %6d' % ( i, a[i] )

def i4vec_print_test ( ):

#*****************************************************************************80
#
## I4VEC_PRINT_TEST tests I4VEC_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ''
  print 'I4VEC_PRINT_TEST'
  print '  I4VEC_PRINT prints an I4VEC.'

  n = 4
  v = np.array ( [ 91, 92, 93, 94 ], dtype = np.int32 )
  i4vec_print ( n, v, '  Here is an I4VEC:' )

  print ''
  print 'I4VEC_PRINT_TEST:'
  print '  Normal end of execution.'

  return

def r8mat_transpose_print ( m, n, a, title ):

#*****************************************************************************80
#
## R8MAT_TRANSPOSE_PRINT prints an R8MAT, transposed.
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
#  Parameters:
#
#    Input, integer M, the number of rows in A.
#
#    Input, integer N, the number of columns in A.
#
#    Input, real A(M,N), the matrix.
#
#    Input, string TITLE, a title.
#
  r8mat_transpose_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

  return

def r8mat_transpose_print_test ( ):

#*****************************************************************************80
#
## R8MAT_TRANSPOSE_PRINT_TEST tests R8MAT_TRANSPOSE_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ''
  print 'R8MAT_TRANSPOSE_PRINT_TEST'
  print '  R8MAT_TRANSPOSE_PRINT prints an R8MAT.'

  m = 4
  n = 3
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0 ], 
    [ 21.0, 22.0, 23.0 ], 
    [ 31.0, 32.0, 33.0 ], 
    [ 41.0, 42.0, 43.0 ] ], dtype = np.float64 )
  r8mat_transpose_print ( m, n, v, '  Here is an R8MAT, transposed:' )

  print ''
  print 'R8MAT_TRANSPOSE_PRINT_TEST:'
  print '  Normal end of execution.'

  return

def r8mat_transpose_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## R8MAT_TRANSPOSE_PRINT_SOME prints a portion of an R8MAT, transposed.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 November 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns of the matrix.
#
#    Input, real A(M,N), an M by N matrix to be printed.
#
#    Input, integer ILO, JLO, the first row and column to print.
#
#    Input, integer IHI, JHI, the last row and column to print.
#
#    Input, string TITLE, a title.
#
  incx = 5

  print ''
  print title

  if ( m <= 0 or n <= 0 ):
    print ''
    print '  (None)'
    return

  for i2lo in range ( max ( ilo, 0 ), min ( ihi, m - 1 ), incx ):

    i2hi = i2lo + incx - 1
    i2hi = min ( i2hi, m - 1 )
    i2hi = min ( i2hi, ihi )
    
    print ''
    print '  Row: ',

    for i in range ( i2lo, i2hi + 1 ):
      print '%7d       ' % ( i ),

    print ''
    print '  Col'

    j2lo = max ( jlo, 0 )
    j2hi = min ( jhi, n - 1 )

    for j in range ( j2lo, j2hi + 1 ):

      print '%7d :' % ( j ),
      
      for i in range ( i2lo, i2hi + 1 ):
        print '%12g  ' % ( a[i,j] ),

      print ''

  return

def r8mat_transpose_print_some_test ( ):

#*****************************************************************************80
#
## R8MAT_TRANSPOSE_PRINT_SOME_TEST tests R8MAT_TRANSPOSE_PRINT_SOME.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ''
  print 'R8MAT_TRANSPOSE_PRINT_SOME_TEST'
  print '  R8MAT_TRANSPOSE_PRINT_SOME prints some of an R8MAT, transposed.'

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [ 21.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [ 31.0, 32.0, 33.0, 34.0, 35.0, 36.0 ], 
    [ 41.0, 42.0, 43.0, 44.0, 45.0, 46.0 ] ], dtype = np.float64 )
  r8mat_transpose_print_some ( m, n, v, 0, 3, 2, 5, '  R8MAT, rows 0:2, cols 3:5:' )

  print ''
  print 'R8MAT_TRANSPOSE_PRINT_SOME_TEST:'
  print '  Normal end of execution.'

  return

def timestamp ( ):

#*****************************************************************************80
#
## TIMESTAMP prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  import time

  t = time.time ( )
  print time.ctime ( t )

  return None

def timestamp_test ( ):

#*****************************************************************************80
#
## TIMESTAMP_TEST tests TIMESTAMP.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    03 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  print ''
  print 'TIMESTAMP_TEST:'
  print '  Python version:'
  print '  TIMESTAMP prints a timestamp of the current date and time.'
  print ''

  timestamp ( )

  print ''
  print 'TIMESTAMP_TEST:'
  print '  Normal end of execution.'

def ffmsh_io_test ( ):

#*****************************************************************************80
#
## FFMSH_IO_TEST tests FFMSH_IO.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    28 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  print ''
  print 'FFMSH_IO_TEST:'
  print '  Python version:'
  print '  Test the FFMSH_IO library.'
  print ''

  ffmsh_io_test01 ( )
  ffmsh_io_test02 ( )
  ffmsh_io_test03 ( )

  print ''
  print 'FFMSH_IO_TEST:'
  print '  Normal end of execution.'

def ffmsh_io_test01 ( ):

#*****************************************************************************80
#
## FFMSH_IO_TEST01 gets the example 2D data and prints it.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    27 December 2014
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'FFMSH_IO_TEST01:'
  print '  Get example 2D data and print it.'
#
#  Get the sizes.
#
  v_num, e_num, t_num = ffmsh_2d_size_example ( )
#
#  Print the sizes.
#
  ffmsh_2d_size_print ( '  Example Sizes:', v_num, e_num, t_num )
#
#  Get the data.
#
  [ v_xy, v_l, e_v, e_l, t_v, t_l ] \
    = ffmsh_2d_data_example ( v_num, e_num, t_num )
#
#  Print the data.
#
  ffmsh_2d_data_print ( '  Example data:', v_num, e_num, t_num, v_xy, \
    v_l, e_v, e_l, t_v, t_l )

  return

def ffmsh_io_test02 ( ):

#*****************************************************************************80
#
## FFMSH_IO_TEST02 gets the example 2D data and writes it to a file.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    28 December 2014
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'FFMSH_IO_TEST02:'
  print '  Get example 2D data and write it to a file.'
#
#  Get the sizes.
#
  v_num, e_num, t_num = ffmsh_2d_size_example ( );
#
#  Print the sizes.
#
  ffmsh_2d_size_print ( '  Example Sizes:', v_num, e_num, t_num )
#
#  Get the data.
#
  v_xy, v_l, e_v, e_l, t_v, t_l \
    = ffmsh_2d_data_example ( v_num, e_num, t_num )
#
#  Write the sizes and data.
#
  filename = 'output.msh'

  ffmsh_2d_write ( filename, v_num, e_num, t_num, v_xy, \
    v_l, e_v, e_l, t_v, t_l )

  print ''
  print '  The data was written to "%s"' % ( filename )

def ffmsh_io_test03 ( ):

#*****************************************************************************80
#
## FFMSH_IO_TEST03 gets the example 2D data and prints it.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    28 December 2014
#
#  Author:
#
#    John Burkardt
#
  filename = 'input.msh'

  print ''
  print 'FFMSH_IO_TEST03:'
  print '  Read 2D data from a file and print it.'
#
#  Read the sizes.
#
  v_num, e_num, t_num = ffmsh_2d_size_read ( filename )
#
#  Print the sizes.
#
  ffmsh_2d_size_print ( filename, v_num, e_num, t_num )
#
#  Read the data.
#
  v_xy, v_l, e_v, e_l, t_v, t_l \
    = ffmsh_2d_data_read ( filename, v_num, e_num, t_num )
#
#  Print the data.
#
  ffmsh_2d_data_print ( filename, v_num, e_num, t_num, v_xy, \
    v_l, e_v, e_l, t_v, t_l )

if ( __name__ == '__main__' ):
  timestamp ( )
  ffmsh_io_test ( )
  timestamp ( )

