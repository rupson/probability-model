import math
import random
import matplotlib.pyplot as plt

def generate_empty_dictionary(n):
  count = {}
  for i in range(n):
    count[i+1] = 0
  return count

def generate_unique_values_in_range(n: int, stopAt=None):
  if (stopAt == None):
    stopAt = n
  count = generate_empty_dictionary(stopAt)
  chosen = []
  while len(chosen) < stopAt:
    # print(f"choosing {len(chosen) + 1}th value")
    count[len(chosen)+1] += 1
    num = random.randint(1,n)
    if (num not in chosen):
      chosen.append(num)
      print(f"{math.floor((len(chosen)/stopAt)*100)}% complete...")
    # print(f"counts: {count}")
  return count

def plotCurve(data: dict):
  keys = list(data.keys())
  vals = list(data.values())
  plt.scatter(keys, vals)
  plt.show()
  
def main():
  n = 1000000
  print("generating IDs...")
  generated = generate_unique_values_in_range(n, 40000)
  print("plotting...")
  plotCurve(generated)

if __name__ == "__main__":
  main()