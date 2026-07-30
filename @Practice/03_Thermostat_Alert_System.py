# Smart Thermostat Alert System
# If the device_status is "active"
# And temperature > 35 → Warn: "High temperature"
# Else → "Temperature normal"
# If the device is off → "Device is offline"


device_status = "active"
temperature = 36

if device_status == "active":
    if temperature > 35:
        print("High temperature")
    else:
        print("Temperature normal")
elif device_status == "off":
    print("Device is offline")
else:
    print("Device is not active")   
