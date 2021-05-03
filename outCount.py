import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

scenario = ["A","B","C","D","E","F"]
vehicleType = ["HDV","CAV2","CAV4"]
sims = ["0","20","40","60","80","100"]
colours = ("#4472C4", "#ED7D31", "#00B050", "#7030A0", "#00B0F0", "#FF0000")
k = 0
colliderSpeedArr = [0] * 6
victimSpeedArr = []
colliders = np.array([[0,0,0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]])


for i in sims:
    print("--------{}--------".format(scenario[k]))
    df = pd.read_csv("colout{}.csv".format(i))
    step = np.array(df.iloc[:, 0]).reshape(-1, 1)
    collider = np.array(df.iloc[:, 6])
    victim = np.array(df.iloc[:, 7])
    colliderSpeed = np.array(df.iloc[:, 8])
    colliderSpeedArr[k] = np.average(colliderSpeed)
    victimSpeed = np.array(df.iloc[:, 9])
    cols = np.array([0,0,0])
    for l in victim:
        if(l == "HDV"):
            cols[0] = cols[0] + 1
        elif(l == "CAV2"):
            cols[1] = cols[1] + 1 
        elif(l == "CAV4"):
            cols[2] = cols[2] + 1
    colliders[k] = cols
    nCollisions = list(range(0, len(step)))
    plt.scatter(step, nCollisions, label = "Scenario {}".format(scenario[k]) ,marker = "+", color = "{}".format(colours[k]))
    k = k+1
    print("Colliders = ", Counter(collider))
    print("Victims = ", Counter(victim))
    print("Average Collider Speed = ", np.average(colliderSpeed))
    print("Average Victim Speed = ", np.average(victimSpeed))

print(colliders)
plt.title("Collisions vs Step")
plt.legend()
plt.xlabel('Step'); plt.ylabel('Number of Collisions')
plt.show()
#print(colliderSpeed)

#plt.plot(sims, colliderSpeedArr, label = "" ,marker = "+")
#plt.show()
# k = 0
# for i in colliders:
#     print(i)
#     plt.scatter(vehicleType, i, label = "Scenario {}".format(scenario[k]) ,marker = "+", color = "{}".format(colours[k]))
#     k=k+1

# plt.legend()
# plt.show()
