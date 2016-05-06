from thesystem import simulate_film, m0_filename, ps, nm
from nmag.common import *

# Details about the pulse

# The pulse_boundary is a region of 10 nm thickness starting from the back of the film (x=-5000 nm)
pulse_boundary = -5000.0e-9 + 10e-9 # float in nm

# pulse moves in the positive y direction
pulse_direction = [0, 1, 0]
pulse_amplitude = SI(1e5, 'A/m')
pulse_duration = 1*ps

# Function which sets the magnetisation to zero
# Gets the simulation object, sim, as an argument and uses it with method set_H_ext to set the 
# applied magnetic field to zero everywhere.
def switch_off_pulse(sim):
  sim.set_H_ext([0.0, 0.0, 0.0], unit=pulse_amplitude)

# Function which sets the pulse as a function of time/space
# This function is to be given to set_H_ext method since the pulse is localized and non-uniform in space
def switch_on_pulse(sim):
  def H_ext(r):
    # Checks whether the x component in the given point is lower than pulse_amplitude and sets the applied field to a value different
    # from zero only if that is really the case
    if r[0] < pulse_boundary:
      return pulse_direction
    else:
      return [0.0, 0.0, 0.0]

  sim.set_H_ext(H_ext, unit=pulse_amplitude)

# Here we run the simulation: do=[....] is used to set the pulse
#   save=[...] is used to save the data.

# simulate_film function which was defined in thesystem.py sets up the system and materials
s = simulate_film('dynamics', 0.005)

# Sets the initial magnetization configuration from the file saved in part 1
s.load_m_from_h5file(m0_filename)

# Carrying out the time integration by calling the relax method of the object s
# save saves the fields every 0.5 ps
s.relax(save=[('fields', every('time', 0.5*ps))],

	# pulse is switched on at 0 ps
        do=[(switch_on_pulse, at('time', 0*ps)),

	    # pulse is switched off after the pulse_duration has passed
            (switch_off_pulse, at('time', pulse_duration)),

	    # the simulation terminates at time t = 2000 ps
            ('exit', at('time', 2000*ps))])

