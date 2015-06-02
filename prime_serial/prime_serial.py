#!/usr/bin/env python
#
#*****************************************************************************80

def prime_serial ( ):

#*****************************************************************************80
#
## MAIN is the main program for PRIME_SERIAL_PRB.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 October 2012
#
#  Author:
#
#    John Burkardt
#
  from time import time, ctime

  print ctime ( time ( ) )

  print ""
  print "PRIME_SERIAL"
  print "  PYTHON version"
  print "  Count the primes between N_LO and N_HI."

  n_lo = 1
  n_hi = 131072
  n_factor = 2

  prime_number_sweep ( n_lo, n_hi, n_factor )
#
#  Terminate.
#
  print ""
  print "PRIME_SERIAL"
  print "  Normal end of execution."
  print ""
  print ctime ( time ( ) )

  return

#*****************************************************************************80

def prime_number_sweep ( n_lo, n_hi, n_factor ):

#*****************************************************************************80
#
## PRIME_NUMBER_SWEEP does repeated timed calls to PRIME_NUMBER.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 October 2012
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N_LO, the first value of N.
#
#    Input, integer N_HI, the last value of N.
#
#    Input, integer N_FACTOR, the factor by which to increase N
#    after each iteration.
#
  from time import time

  print ""
  print "PRIME_NUMBER_SWEEP"
  print "  Call PRIME_NUMBER to count the primes from 1 to N."
  print ""
  print "         N         Pi       Time"
  print ""

  n = n_lo

  while n <= n_hi:
    wtime = time ( )
    primes = prime_number ( n )
    wtime = time ( ) - wtime
    print ( '{0:10d} {1:10d} {2:10.5f}'.format ( n, primes, wtime ) )
    n = n * n_factor

  return

#*****************************************************************************80

def prime_number ( n ):

#*****************************************************************************80
#
## PRIME_NUMBER returns the number of primes between 1 and N.
#
#  Discussion:
#
#    A naive algorithm is used.
#
#    Mathematica can return the number of primes less than or equal to N
#    by the command PrimePi[N].
#
#                N  PRIME_NUMBER
#
#                1           0
#               10           4
#              100          25
#            1,000         168
#           10,000       1,229
#          100,000       9,592
#        1,000,000      78,498
#       10,000,000     664,579
#      100,000,000   5,761,455
#    1,000,000,000  50,847,534
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 October 2012
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the maximum number to check.
#
#    Output, integer TOTAL, the number of prime numbers up to N.
#
  total = 0

  for i in range ( 2, n + 1 ):

    prime = 1

    for j in range ( 2, i ):
      if ( i % j ) == 0:
        prime = 0
        break

    total = total + prime

  return total

#*****************************************************************************80

prime_serial ( )
