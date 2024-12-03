import matplotlib.pyplot as plt
import numpy as np


"""
Hamburgare: 50 SEK
Pommes frites: 25 SEK
Läsk: 20 SEK
Milkshake: 30 SEK
Sallader: 45 SEK
McNuggets: 35 SEK
"""



sales_data = [
{"Hamburgare": 150, "Pommes frites": 200, "Läsk": 180, "Milkshake": 40, "Sallader": 30, "McNuggets": 100},
{"Hamburgare": 170, "Pommes frites": 220, "Läsk": 190, "Milkshake": 50, "Sallader": 35, "McNuggets": 105},
{"Hamburgare": 160, "Pommes frites": 210, "Läsk": 185, "Milkshake": 45, "Sallader": 33, "McNuggets": 110},
{"Hamburgare": 180, "Pommes frites": 230, "Läsk": 200, "Milkshake": 55, "Sallader": 40, "McNuggets": 115},
{"Hamburgare": 170, "Pommes frites": 220, "Läsk": 195, "Milkshake": 50, "Sallader": 38, "McNuggets": 120},
{"Hamburgare": 190, "Pommes frites": 240, "Läsk": 210, "Milkshake": 60, "Sallader": 42, "McNuggets": 125},
{"Hamburgare": 185, "Pommes frites": 235, "Läsk": 205, "Milkshake": 58, "Sallader": 40, "McNuggets": 130},
{"Hamburgare": 175, "Pommes frites": 225, "Läsk": 190, "Milkshake": 52, "Sallader": 36, "McNuggets": 120},
{"Hamburgare": 165, "Pommes frites": 215, "Läsk": 185, "Milkshake": 48, "Sallader": 34, "McNuggets": 110},
{"Hamburgare": 180, "Pommes frites": 230, "Läsk": 200, "Milkshake": 55, "Sallader": 39, "McNuggets": 115}
]

result = []

for items in sales_data:
    test = (items ["Hamburgare"] * 50, items ["Pommes frites"] * 25, items ["Läsk"] * 20, items ["Milkshake"] * 30, items ["Sallader"] * 45, items ["McNuggets"] * 35)
    result.append(sum(test))
print(result)
xpoints = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
ypoints = np.array(result)

plt.plot(xpoints, ypoints)
plt.show()
