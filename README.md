# Spin-Wave-Propagation
This code is to be used with the NMAG micromagnetic simulation package developed at the University of Southampton with substantial contributions from Hans Fangohr, Thomas Fischbacher, Matteo Franchin. More information can be found at http://nmag.soton.ac.uk/nmag/

In this simulation a magnetic field is pulsed to a 10nm thick area on one end of a 10 micron by 1 micron by 0.1 micron permalloy film so that we can observe dispersion curves and how spin waves propagate throughout the material over time. The goal of this simulation is to act as a stepping stone toward creating spin waves in potentially larger structures composed of many layers of different magnetic materials.
![real-space](50ps_real_space.png?raw=true "rea-space")
![rec-space](50ps_rec_space_0-0.10.png?raw=true "reciprocal-space")

In thesystem.py the material parameters and geometry of the system are defined. In relaxation.py the system is relaxed to it's equilibrium magnetization which is then used in dynamics.py as the beginning state of the system before the localized magnetic field is pulsed.

The film was originally created using AutoDesk inventor. The structure was then exported as a CAD file to be used by NETGEN to create a mesh needed for the NMAG simulation.

![mesh](mesh.png?raw=true "film mesh")
