#!/usr/bin/env python

# reaction_diffusion.py
#
#  Modified:
#
#    14 December 2011
#
#  Reference:
#
#    Anders Logg, Garth Wells,
#    DOLFIN: Automated Finite Element Computing,
#    ACM Transactions on Mathematical Software,
#    Volume 37, Number 2, Article 20, April 2010.
#
from dolfin import *

mesh = UnitSquare ( 32, 32 );
V = FunctionSpace ( mesh, "CG", 2 )

v = TestFunction ( V )
u = TrialFunction ( V )
f = Expression ( "sin( x[0] ) * cos ( x[1] )" )

A = assemble ( dot ( grad ( v ), grad ( u ) ) * dx + v * u * dx )
b = assemble ( v * f * dx )

u_h = Function ( V )

solve ( A, u_h.vector(), b )

plot ( u_h )
file = File ( 'reaction_diffusion_solution.pvd' )
file << u_h

plot ( mesh )
file = File ( 'reaction_diffusion_mesh.pvd' )
file << mesh

interactive ( )

