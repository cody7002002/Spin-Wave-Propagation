# This script is used to compute the equilibrium configuration for the
# magnetization, which is then used in the second part of the simulation,
# where the dynamics are actually studied.

from thesystem import simulate_film, m0_filename, ps
from nmag.common import *

#Invokes the simulate_film function from thesystem.py which loads the mesh and material info
#The function returns the simulation object which is stored inside the variable s
s = simulate_film(name='relaxation', damping=0.5) # NOTE the high damping!

#Sets the magnetization along the x axis of the film
s.set_m([1, 0, 0])

#Relaxing the system to find the equilibrium magnetization
s.relax(save=[('fields', at('time', 0*ps) | at('convergence'))])

#Saving the relax configuration to the file m0_filename which is specified in thesystem.py
s.save_restart_file(m0_filename)

