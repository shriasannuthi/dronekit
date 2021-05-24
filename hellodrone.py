
print ("Start simulator (SITL)")
import dronekit_sitl
sitl = dronekit_sitl.start_default()
connection_string = sitl.connection_string()

# Import DroneKit-Python
from dronekit import VehicleMode,connect

# Connect to the Vehicle.
print(f"Connecting to vehicle on: {connection_string}")
vehicle = connect(connection_string, wait_ready=True)

# Get some vehicle attributes (state)
print ("Get some vehicle attribute values:")
print (f" GPS: {vehicle.gps_0}")
print (f" Battery: {vehicle.battery}")
print (f" Last Heartbeat: {vehicle.last_heartbeat}")
print (f" Is Armable?: {vehicle.is_armable}" )
print (f" System status: {vehicle.system_status.state}" )
print (f" Mode: {vehicle.mode.name}")   # settable

# Close vehicle object before exiting script
vehicle.close()

# Shut down simulator
sitl.stop()
print("Completed")