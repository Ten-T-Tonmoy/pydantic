import numpy as plt
import matplotlib.pyplot as np


# given

# frequencies: f=2.4 GHzf=2.4 GHz and f=5 GHzf=5 GHz
# Transmit power: Pt=0 dBm=1 mW Pt =0 dBm=1 mW
# System loss: 0
# Transmitted  antenna gain Gt=1 dBi
#  Received antenna gain Gr=1dBi


# light_of_speed
c = 3e8
# given
Pt = 0  # at dBm
Gt = 1
Gr = 1
# to linear
# Glin=10^Gdb/10   * 10^-3 for Watts
Gt = 10 ** (Gt / 10)
Gr = 10 ** (Gr / 10)
Pt = 10 ** (Pt / 10) / 1000

# frequencies = [2.4e9, 5e9]
distances = plt.linspace(1, 100, 500)


def friss_free_space_equation(Pt, Gt, Gr, f, d):

    wave_length = c / f
    power_received = Pt * Gt * Gr * (wave_length / (4 * plt.pi * d)) ** 2
    power_received_dBm = 10 * plt.log10(power_received * 1000)
    return power_received_dBm


# since linspace thats why auto applied np
pt_dBm = 0
power_received_at_24GHz = friss_free_space_equation(Pt, Gt, Gr, 2.4e9, distances)
power_received_at_5GHz = friss_free_space_equation(Pt, Gt, Gr, 5e9, distances)

np.figure(figsize=(8, 5))
np.plot(distances, power_received_at_24GHz, label="2.4 GHz")
np.plot(distances, power_received_at_5GHz, label="5 GHz")
np.xlabel("Distance (m)")
np.ylabel("Received Power (dBm)")
np.title("Received Power vs Distance (dBm)")
np.legend()
np.grid(True)
np.show()
