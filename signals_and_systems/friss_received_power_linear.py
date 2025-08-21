import numpy as np
import matplotlib.pyplot as plt


# given

# frequencies: f=2.4 GHzf=2.4 GHz and f=5 GHzf=5 GHz
# Transmit power: Pt=0 dBm=1 mW Pt =0 dBm=1 mW
# System loss: 0
# Transmitted  antenna gain Gt=1 dBi
#  Received antenna gain Gr=1dBi


# light_of_speed
c = 3e8
# given
Pt = 0
Gt = 1
Gr = 1
# to linear
# Glin=10^Gdb/10   * 10^-3 for Watts
Pt = 10 ** (Pt / 10) / 1000
Gt = 10 ** (Gt / 10)
Gr = 10 ** (Gr / 10)

# frequencies = [2.4e9, 5e9]
distances = np.linspace(1, 100, 500)


def friss_free_space_equation(Pt, Gt, Gr, f, d):
    wave_length = c / f
    power_received = Pt * Gt * Gr * (wave_length / (4 * np.pi * d)) ** 2
    return power_received


power_received_at_24GHz = friss_free_space_equation(Pt, Gt, Gr, 2.4e9, distances)
power_received_at_5GHz = friss_free_space_equation(Pt, Gt, Gr, 5e9, distances)


plt.figure(figsize=(8,5))
plt.plot(distances, power_received_at_24GHz, label="at 2.4 GHz")
plt.plot(distances, power_received_at_5GHz, label="at 5 GHz")
plt.xlabel("Distance (m)")
plt.ylabel("Received Power (W)")
plt.title("Received Power vs Distance (Linear Scale)")
plt.legend()
plt.grid(True)
plt.show()