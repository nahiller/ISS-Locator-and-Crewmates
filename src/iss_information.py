def get_location(iss_service): 
    try:   
        return iss_service()
    except Exception as exception:
        return str(exception)

def get_astronauts(iss_service):
    try:
        names = iss_service()
        return sorted(names, key = lambda input_names: input_names.split()[-1])
    except Exception as exception:
        return str(exception)