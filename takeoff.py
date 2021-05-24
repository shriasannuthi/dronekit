from dronekit import VehicleMode,connect #importing VehicalMode from dronekit
import time #for getting delay of 1sec

vehicle = connect('127.0.0.1:14550',wait_ready=True)  #(IP(client),will allow us to wait for the connection and then let us connect to all the attributes of the vehical)

def arm_and_takeoff(altitude):  #creating function for takeoff
    while not vehicle.is_armable: #loop checking if the vehicle is armable or not
        print("[INFO] waiting to initialize...")
        time.sleep(1) #delay of 1 sec
    print("[INFO] The vehicle is armable")

    vehicle.mode = VehicleMode("GUIDED") #we'll be guiding the vehicle
    vehicle.armed  = True #arming the vehicle

    while not vehicle.armed: #checking if the vehicle is armed or not
        print("[INFO] waiting to arm")
        time.sleep(1) #delay of 1 sec

    print("[INFO] Taking  off...") 
    vehicle.simple_takeoff(altitude) #parameter is the desired altitude #DKPY 2.0

    while True:
        print("[INFO] Altitude {}".format(vehicle.location.global_relative_frame.alt)) #prints the current alt on cmd wrt to the home location/relative location 
        if vehicle.location.global_relative_frame.alt >= 0.95 * altitude: #if the vehicle reaches 95% of the desired alt,then print the next line
            print("[INFO] Target altitude reached")
            break 
        time.sleep(1) #delay of 1 sec

arm_and_takeoff(50) #calling the func