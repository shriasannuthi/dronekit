from dronekit import VehicleMode,connect
import time

vehicle=connect('127.0.0.1:14550',wait_ready=True)

def arm_and_takeoff(altitude):
    #preflight check
    while not vehicle.is_armable: #to check if vehicle can be armed
        print("[INFO] waiting to initialize...")
        time.sleep(1) #1 second delay
    print("[INFO] arming motors")
    #end of preflight check
    
    vehicle.mode = VehicleMode("GUIDED") #changing the mode
    vehicle.armed = True #written out of the loop

    while not vehicle.armed: #checking if the vehicle is armed
        print("[INFO] waiting to arm")
        time.sleep(1)

    print("[INFO] Taking off...")
    vehicle.simple_takeoff(altitude)

    while True:
        print('[INFO] Altitude {}m'.format(vehicle.location.global_relative_frame.alt)) #accesing and printing the altitude at that time
        if vehicle.location.global_relative_frame.alt >= 0.95*altitude: #should be greater than 95% of the altitude
            print('[INFO] Target altitude reached')
            break
        time.sleep(1)


arm_and_takeoff(50) #altitude=50 metres

