import numpy as np
import matplotlib.pyplot as plt

# 1) Load the data
data = np.loadtxt("step_temp_toteng_press.dat", comments="#")
steps  = data[:, 0]
temps  = data[:, 1]
toteng = data[:, 2]
press  = data[:, 3]

# -------- Plot 1: Temperature vs Step --------
plt.figure()
plt.plot(steps, temps, "-")
plt.xlabel("Step")
plt.ylabel("Temperature (K)")
plt.title("Temperature vs Step")
plt.tight_layout()
plt.savefig('temperature-ts.png')
plt.close()
# -------- Plot 2: Total Energy vs Step --------
plt.figure()
plt.plot(steps, toteng, "-")
plt.xlabel("Step")
plt.ylabel("Total Energy")
plt.title("Total Energy vs Step")
plt.tight_layout()
plt.savefig('tot_ener-ts.png')
plt.close()
# -------- Plot 3: Pressure vs Step --------
plt.figure()
plt.plot(steps, press, "-")
plt.xlabel("Step")
plt.ylabel("Pressure")
plt.title("Pressure vs Step")
plt.tight_layout()
plt.savefig("pressure-ts.png")
plt.close()

# -------- Plot 4: Pressure vs Temperature --------
plt.figure()
plt.plot(temps, press, ".-")
plt.xlabel("Temperature (K)")
plt.ylabel("Pressure")
plt.title("Pressure vs Temperature")
plt.tight_layout()
plt.savefig("pressure-vs-temperature.png")
plt.close()
