import numpy as np
from astropy.constants import c, k_B

import mpol  # TODO: remove for fit_runner (already in fit.py)
mpol.enable_logging()

# convert from arcseconds to radians
arcsec = np.pi / (180.0 * 3600)  # [radians]  = 1/206265 radian/arcsec

deg = np.pi / 180  # [radians]

kB = k_B.cgs.value  # [erg K^-1] Boltzmann constant
cc = c.cgs.value # [cm s^-1]
c_ms = c.value # [m s^-1]
