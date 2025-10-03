import psutil
RAM = psutil.virtual_memory()
Battery = psutil.sensors_battery()
CPU = psutil.cpu_percent()
#------------------------------------------------------#
print("\n-CPU Infos-")

print(f"CPU Usage: %{psutil.cpu_percent(interval=1)}")
#------------------------------------------------------#
print("\n-RAM Infos-")

print(f" Total RAM: {RAM.total}")
print(f" RAM Percent: {RAM.percent}")
print(f" RAM Available: {RAM.available}")
print(f" RAM Used: {RAM.used}")
#-------------------------------------------------------#
print("\n-Battery Infos-")

print(f" Battery Percent: %{Battery.percent}")
print(f" Is Battery Plugged In: {Battery.power_plugged}")