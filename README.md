# Spin-Wave-Propagation
This code is to be used with the NMAG micromagnetic simulation package developed at the University of Southampton with substantial contributions from Hans Fangohr, Thomas Fischbacher, Matteo Franchin. More information can be found at http://nmag.soton.ac.uk/nmag/

The purpose of this simulation is to pulse a magnetic field to a small area on one end of the film and observe how spin waves propagate throughout the material over time. The goal of this simulation is to act as a stepping stone toward creating spin waves in potentially larger structures composed of many layers of different magnetic materials.

In thesystem.py the material parameters and geometry of the system are defined. In relaxation.py the system is relaxed to it's equilibrium magnetization which is then used in dynamics.py as the beginning state of the system before the localized magnetic field is pulsed.
