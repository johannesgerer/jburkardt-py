#!/usr/bin/env python

def initialized_get ( ):

#*****************************************************************************80
#
## INITIALIZED_GET gets the INITIALIZED value.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, bool INITIALIZED, is true if the package has been initialized.
#
  from initialized_memory import initialized_memory

  i = -1
  initialized = []
  initialized = initialized_memory ( i, initialized )

  return initialized

