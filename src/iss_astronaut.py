import iss_time_service, iss_astronaut_service, iss_information

def print_iss_information():
    astronauts_names = iss_information.get_astronauts(iss_astronaut_service.get_astronauts_names)
    time_and_location = iss_information.get_location(iss_time_service.get_location)

    if type(time_and_location) is not list:
        print(time_and_location)
        return
    elif type(astronauts_names) is not list:
        print(astronauts_names)
        return
        
    print("ISS location as", time_and_location[0], "CT flying over", time_and_location[1]) 
    print("\nThere are " + str(len(astronauts_names)) + " people on ISS at this time:", *astronauts_names, sep='\n') 