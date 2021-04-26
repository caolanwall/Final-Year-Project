import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

sims = ["0","20","40","60","80","100"]
vehicleType = ["HDV","CAV2","CAV4"]
colours = ("#4472C4", "#ED7D31", "#00B050", "red", "purple", "green")
k = 0

for i in sims:
    print("--------{}--------".format(i))
    df = pd.read_csv("colout{}.csv".format(i))
    step = np.array(df.iloc[:, 0]).reshape(-1, 1)
    collider = np.array(df.iloc[:, 6])
    victim = np.array(df.iloc[:, 7])
    colliderSpeed = np.array(df.iloc[:, 8])
    victimSpeed = np.array(df.iloc[:, 9])
    print("Colliders = ", Counter(collider))
    print("Victims = ", Counter(victim))
    print("Average Collider Speed = ", np.average(colliderSpeed))
    print("Average Victim Speed = ", np.average(victimSpeed))
    nCollisions = list(range(0, len(step)))
    plt.scatter(step, nCollisions, label = "{}% Penetration Rate".format(i) ,marker = "+", color = "{}".format(colours[k]))
    k = k+1

plt.title("Collisions vs Step")
plt.legend()
plt.xlabel('Step'); plt.ylabel('Number of Collisions')
plt.show()
