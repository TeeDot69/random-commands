import psutil

battery = psutil.sensors_battery()
if battery:
    print(f"Battery Percentage: {battery.percent}%")
else:
    print("Battery info not available (try enabling battery permissions in Termux).")
