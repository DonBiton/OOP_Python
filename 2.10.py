# import math

# # Given constants
# Is = -7.6e-6
# e = 1.6e-19  # Elemental charge in Coulombs
# k = 1.38e-23  # Boltzmann constant in J/K
# T = 293  # Temperature in Kelvin

# # Calculate the expression
# result = Is * (math.exp(e * 1 / (k * T)) - 1)

# # Convert result to mA and µA
# result_mA = result * 1000  # Convert to milliamps (mA)
# result_uA = result * 1e6   # Convert to microamps (µA)

# # Print the results
# print(f"Result in Amperes: {result}")
# print(f"Result in milliamps (mA): {result_mA}")
# print(f"Result in microamps (µA): {result_uA}")


import math

# Given constants
I_s = 7.6e-6  # Saturation current in Amperes
e = 1.6e-19  # Elemental charge in Coulombs
k = 1.38e-23  # Boltzmann constant in J/K
T = 293  # Temperature in Kelvin
U = -0.1  # Voltage in Volts

# Calculate the current I
I = I_s * (math.exp(e * U / (k * T)) - 1)

# Convert result to mA and µA
result_mA = I * 1000  # Convert to milliamps (mA)
result_uA = I * 1e6   # Convert to microamps (µA)

# Print the results
print(f"Result in Amperes: {I}")
print(f"Result in milliamps (mA): {result_mA}")
print(f"Result in microamps (µA): {result_uA}")
