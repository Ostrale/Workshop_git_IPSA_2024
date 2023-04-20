# %%

# PROJET WORKSHOP GIT IPSA 2024

# %%

import numpy as np
import xarray as xr
from datetime import datetime


time = np.array(datetime.now())
time = 0
x = 0
y = 0
angle = 0

array = np.array([time, angle, x, y])
position = [x, y, time]

lon = x
lat = y

ds = xr.Dataset(
    data_vars=dict(
        position=(["x", "y", "time"], position),
    ),
    coords=dict(
        lon=(["x"], lon),
        lat=(["y"], lat),
        time=time,
    ),
    attrs=dict(description="Weather related data."),
    )



