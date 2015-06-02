#!/usr/bin/env python

def r8_divide_i4 ( i, j ):

%*****************************************************************************80
%
%% R8_DIVIDE_I4 returns an I4 fraction as an R8.
%
%  Discussion:
%
%    In MATLAB, this function doesn't really serve any purpose.
%
%  Licensing:
%
%    This code is distributed under the GNU LGPL license. 
%
%  Modified:
%
%    24 July 2014
%
%  Author:
%
%    John Burkardt
%
%  Parameters:
%
%    Input, integer I, J, the numerator and denominator.
%
%    Output, real VALUE, the value of (I/J).
%
  value = i / j

  return value

