#! /usr/bin/env python

def md ( d_num = 3, p_num = 500, step_num = 500, dt = 0.1 ):

#*****************************************************************************80
#
## MD is the main program for the molecular dynamics simulation.
#
#  Discussion:
#
#    MD implements a simple molecular dynamics simulation.
#
#    The velocity Verlet time integration scheme is used.
#
#    The particles interact with a central pair potential.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer D_NUM, the spatial dimension.  
#    A value of 2 or 3 is usual.
#    The default value is 3.
#
#    Input, integer P_NUM, the number of particles.  
#    A value of 1000 or 2000 is small but "reasonable".
#    The default value is 500.
#
#    Input, integer STEP_NUM, the number of time steps.  
#    A value of 500 is a small but reasonable value.
#    The default value is 500.
#
#    Input, real DT, the time step.
#    A value of 0.1 is large; the system will begin to move quickly but the
#    results will be less accurate.
#    A value of 0.0001 is small, but the results will be more accurate.
#    The default value is 0.1.
#
  import numpy as np

  mass = 1.0
#
#  Report to the user.
#
  print ''
  print 'MD'
  print '  Python version'
  print '  A molecular dynamics program.'
  print ''
  print '  D_NUM, the spatial dimension, is %d' % ( d_num )
  print '  P_NUM, the number of particles in the simulation is %d.' % ( p_num )
  print '  STEP_NUM, the number of time steps, is %d.' % ( step_num )
  print '  DT, the time step size, is %g seconds.' % ( dt )

  print ''
  print '  At each step, we report the potential and kinetic energies.'
  print '  The sum of these energies should be a constant.'
  print '  As an accuracy check, we also print the relative error'
  print '  in the total energy.'
  print ''
  print '      Step      Potential       Kinetic        (P+K-E0)/E0'
  print '                Energy P        Energy K       Relative Energy Error'
  print ''

  step_print_index = 0
  step_print_num = 10
  step_print = 0

  for step in range ( 0, step_num + 1 ):

    if ( step == 0 ):
      pos, vel, acc = initialize ( p_num, d_num )
    else:
      pos, vel, acc = update ( p_num, d_num, pos, vel, force, acc, mass, dt )

    force, potential, kinetic = compute ( p_num, d_num, pos, vel, mass )

    if ( step == 0 ):
      e0 = potential + kinetic

    if ( step == step_print ):
      rel = ( potential + kinetic - e0 ) / e0
      print '  %8d  %14f  %14f  %14g' % ( step, potential, kinetic, rel )
      step_print_index = step_print_index + 1
      step_print = ( step_print_index * step_num ) // step_print_num

  return

def compute ( p_num, d_num, pos, vel, mass ):

#*****************************************************************************80
#
## COMPUTE computes the forces and energies.
#
#  Discussion:
#
#    The potential function V(X) is a harmonic well which smoothly
#    saturates to a maximum value at PI/2:
#
#      v(x) = ( sin ( min ( x, PI/2 ) ) )^2
#
#    The derivative of the potential is:
#
#      dv(x) = 2.0 * sin ( min ( x, PI/2 ) ) * cos ( min ( x, PI/2 ) )
#            = sin ( 2.0 * min ( x, PI/2 ) )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer P_NUM, the number of particles.
#
#    Input, integer D_NUM, the number of spatial dimensions.
#
#    Input, real POS(D_NUM,P_NUM), the positions.
#
#    Input, real VEL(D_NUM,P_NUM), the velocities.
#
#    Input, real MASS, the mass of each particle.
#
#    Output, real FORCE(D_NUM,P_NUM), the forces.
#
#    Output, real POTENTIAL, the total potential energy.
#
#    Output, real KINETIC, the total kinetic energy.
#
  import numpy as np
  from math import sin
  from math import sqrt

  r8_pi = 3.141592653589793

  force = np.zeros ( [ d_num, p_num ] )
  rij = np.zeros ( d_num )

  potential = 0.0

  for i in range ( 0, p_num ):
#
#  Compute the potential energy and forces.
#
    for j in range ( 0, p_num ):

      if ( i != j ):
#
#  Compute RIJ, the displacement vector.
#
        for k in range ( 0, d_num ):
          rij[k] = pos[k,i] - pos[k,j]
#
#  Compute D and D2, a distance and a truncated distance.
#
        d = 0.0
        for k in range ( 0, d_num ):
          d = d + rij[k] ** 2
        d = sqrt ( d )
        d2 = min ( d, r8_pi / 2.0 )
#
#  Attribute half of the total potential energy to particle J.
#
        potential = potential + 0.5 * sin ( d2 ) * sin ( d2 )
#
#  Add particle J's contribution to the force on particle I.
#
        for k in range ( 0, d_num ):
          force[k,i] = force[k,i] - rij[k] * sin ( 2.0 * d2 ) / d
#
#  Compute the kinetic energy.
#
  kinetic = 0.0
  for k in range ( 0, d_num ):
    for j in range ( 0, p_num ):
      kinetic = kinetic + vel[k,j] ** 2

  kinetic = 0.5 * mass * kinetic

  return force, potential, kinetic

def initialize ( p_num, d_num ):

#*****************************************************************************80
#
## INITIALIZE initializes the positions, velocities, and accelerations.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer P_NUM, the number of particles.
#
#    Input, integer D_NUM, the number of spatial dimensions.
#
#    Output, real POS(D_NUM,P_NUM), the positions.
#
#    Output, real VEL(D_NUM,P_NUM), the velocities.
#
#    Output, real ACC(D_NUM,P_NUM), the accelerations.
#
  import numpy as np
#
#  Positions.
#
  seed = 123456789
  pos, seed = r8mat_uniform_ab ( d_num, p_num, 0.0, 10.0, seed )
#
#  Velocities.
#
  vel = np.zeros ( [ d_num, p_num ] )
#
#  Accelerations.
#
  acc = np.zeros ( [ d_num, p_num ] )

  return pos, vel, acc

def r8mat_uniform_ab ( m, n, a, b, seed ):

#*****************************************************************************80
#
## R8MAT_UNIFORM_AB returns a scaled pseudorandom R8MAT.
#
#  Discussion:
#
#    An R8MAT is an array of R8's.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    08 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Paul Bratley, Bennett Fox, Linus Schrage,
#    A Guide to Simulation,
#    Second Edition,
#    Springer, 1987,
#    ISBN: 0387964673,
#    LC: QA76.9.C65.B73.
#
#    Bennett Fox,
#    Algorithm 647:
#    Implementation and Relative Efficiency of Quasirandom
#    Sequence Generators,
#    ACM Transactions on Mathematical Software,
#    Volume 12, Number 4, December 1986, pages 362-376.
#
#    Pierre L'Ecuyer,
#    Random Number Generation,
#    in Handbook of Simulation,
#    edited by Jerry Banks,
#    Wiley, 1998,
#    ISBN: 0471134031,
#    LC: T57.62.H37.
#
#    Peter Lewis, Allen Goodman, James Miller,
#    A Pseudo-Random Number Generator for the System/360,
#    IBM Systems Journal,
#    Volume 8, Number 2, 1969, pages 136-143.
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns in the array.
#
#    Input, real A, B, the range of the pseudorandom values.
#
#    Input, integer SEED, the integer "seed" used to generate
#    the output random number.
#
#    Output, real R(M,N), an array of random values between 0 and 1.
#
#    Output, integer SEED, the updated seed.  This would
#    normally be used as the input seed on the next call.
#
  import numpy as np
  from sys import exit

  i4_huge = 2147483647

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ''
    print 'R8MAT_UNIFORM_AB - Fatal error!'
    print '  Input SEED = 0!'
    sys.exit ( 'R8MAT_UNIFORM_AB - Fatal error!' )

  r = np.zeros ( ( m, n ) )

  for j in range ( 0, n ):
    for i in range ( 0, m ):

      k = ( seed // 127773 )

      seed = 16807 * ( seed - k * 127773 ) - k * 2836

      seed = ( seed % i4_huge )

      if ( seed < 0 ):
        seed = seed + i4_huge

      r[i][j] = a + ( b - a ) * seed * 4.656612875E-10

  return r, seed

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

def update ( p_num, d_num, pos, vel, f, acc, mass, dt ):

#*****************************************************************************80
#
## UPDATE updates positions, velocities and accelerations.
#
#  Discussion:
#
#    The time integration is fully parallelizable.
#
#    A velocity Verlet algorithm is used for the updating.
#
#    x(t+dt) = x(t) + v(t) * dt + 0.5 * a(t) * dt * dt
#    v(t+dt) = v(t) + 0.5 * ( a(t) + a(t+dt) ) * dt
#    a(t+dt) = f(t) / m
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer P_NUM, the number of particles.
#
#    Input, integer D_NUM, the number of spatial dimensions.
#
#    Input, real POS(D_NUM,P_NUM), the positions.
#
#    Input, real VEL(D_NUM,P_NUM), the velocities.
#
#    Input, real F(D_NUM,P_NUM), the forces.
#
#    Input, real ACC(D_NUM,P_NUM), the accelerations.
#
#    Input, real MASS, the mass of each particle.
#
#    Input, real DT, the time step.
#
#    Output, real POS(D_NUM,P_NUM), the updated positions.
#
#    Output, real VEL(D_NUM,P_NUM), the updated velocities.
#
#    Output, real ACC(D_NUM,P_NUM), the updated accelerations.
#
  rmass = 1.0 / mass
#
#  Update positions.
#
  for i in range ( 0, d_num ):
    for j in range ( 0, p_num ):
      pos[i,j] = pos[i,j] + vel[i,j] * dt + 0.5 * acc[i,j] * dt * dt
#
#  Update velocities.
#
  for i in range ( 0, d_num ):
    for j in range ( 0, p_num ):
      vel[i,j] = vel[i,j] + 0.5 * dt * ( f[i,j] * rmass + acc[i,j] )
#
#  Update accelerations.
#
  for i in range ( 0, d_num ):
    for j in range ( 0, p_num ):
      acc[i,j] = f[i,j] * rmass

  return pos, vel, acc

def md_test ( ):

#*****************************************************************************80
#
## MD_TEST tests MD.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    24 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  from time import clock

  timestamp ( )
  print ''
  print 'MD_TEST'
  print '  Test the MD molecular dynamics program.'

  d_num = 3
  p_num = 500
  step_num = 500
  dt = 0.1

  wtime1 = clock ( )

  md ( d_num, p_num, step_num, dt )

  wtime2 = clock ( )

  print ''
  print '    Elapsed wall clock time = %g seconds.' % ( wtime2 - wtime1 )
#
#  Terminate.
#
  print ''
  print 'MD_TEST'
  print '  Normal end of execution.'
  print ''
  timestamp ( )

if ( __name__ == '__main__' ):
  md_test ( )

