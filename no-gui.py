import subprocess

# Set the emulator name and path to the emulator executable
emulator_name = "Pixel_4_V2_API_33"
emulator_executable = "/Users/datax/Library/Android/sdk/emulator/emulator"

# Define the command to start the emulator without a GUI
command = [emulator_executable, "-avd", emulator_name, "-no-window"]

# Use the subprocess module to start the emulator
process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Wait for the emulator to start up
output, error = process.communicate()
if error:
    print("Error starting emulator:", error.decode())
else:
    print("Emulator started successfully:", output.decode())

# appium --address 127.0.0.1 --port 4723 --default-capabilities '{"platformName": "Android", "deviceName": "Android emulator", "appPackage": "com.example.android.myApp", "appActivity": ".MainActivity"}'
