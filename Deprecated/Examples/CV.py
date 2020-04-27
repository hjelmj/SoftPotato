#### Simulation of cyclic voltammetry
'''
    Copyright (C) 2020 Oliver Rodriguez
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''
#### @author oliverrdz
#### https://oliverrdz.xyz

## Import required modules:
import waveforms as wf
import solver as sol
import plots as plot

## User parameters for the potential waveform:
Eini = -0.5     # V, initial potential
Efin = 0.5      # V, final potential for one sweep
sr = 1          # V/s, scan rate
dE = 0.01       # V, step potential
ns = 2          # number of sweeps
tini = 0        # initial time

## User parameters for the simulation:
n = 1           # number of electrons
A = 1           # cm2, geometrical area
E0 = 0          # V, standard potential
COb = 0         # mol/cm3, bulk concentration of O
CRb = 5e-6      # mol/cm3, bulk concentraion of R
DO = 1e-5       # cm2/s, diffusion coefficient of O
DR = 1e-5       # cm2/s, diffusion coefficient of R
ks = 1e3        # cm/s, standard rate constant
alpha = 0.5     # transfer coefficient

## Creating potential waveform:
t, E = wf.sweep(Eini, Efin, sr, dE, ns, tini)

## Solving:
i, x, cR, cO = sol.fd(t, E, n, A, E0, COb, CRb, DO, DR, ks, alpha)

## Plotting:
plot.Et(t, E) # Waveform
plot.iE(E, i) # Voltammogram
plot.Cx(x, cR) # Concentration profile for R
plot.Cx(x, cO) # Concentration profile for O