from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

np.random.seed(42)
temp = np.random.normal(loc=35,scale=10,size=(365),)
print(f"Temperature data (first 10 days):",np.round(temp[:10],2))

# Min / Max temperatures
max_temp = np.max(temp)
min_temp = np.min(temp)
print(f"Maximum Temperature: {max_temp:.2f} °C")
print(f"Minimum Temperature: {min_temp:.2f} °C")

# Calculate average temperature per month.
days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
months_avg = []
start_day = 0

for days in days_in_months:
    months_data = temp[start_day:start_day + days]
    avg = np.mean(months_data)
    months_avg.append(round(avg,2))
    start_day += days
print("Average temperature per month:")

for i, avg in enumerate(months_avg,start=1):
    print(f"Month {i}: {avg} °C")

# Find days with extreme temperatures (above threshold)
def extreme_temp(t):
    if t > 37 :
        return "Extreme Temperatures"                  # This line and line 33 are connected.
    else:
        return "Normal"
labels = np.array([extreme_temp(t)for t in temp])
print(f"Total extreme days: {np.sum(labels == 'Extreme Temperatures')}") # Wrok base on True,False


# We also use this extreme days directly using NumPy filtering like this:
# extreme_days = np.sum(temp > 37)
# print(f"Total extreme days: {extreme_days}")

sns.displot(temp,kind="kde")
plt.title("Temperature Distribution Over 1 Year")
plt.xlabel("Temperature (°C)")
plt.ylabel("Density")
plt.show()


