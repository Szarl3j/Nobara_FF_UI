import psutil

cpu = psutil.cpu_percent()
ram = psutil.virtual_memory().percent

print(f"CPU:{cpu}% RAM:{ram}%")