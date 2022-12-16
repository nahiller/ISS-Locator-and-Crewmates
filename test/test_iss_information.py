import unittest
from src.iss_information import *

class ISSInformationTests(unittest.TestCase): 
    def test_Canary(self):
        self.assertTrue(True)

    def test_get_location_returns_time_and_location_sent_by_service(self):
        iss_service = lambda: ("11:50PM", "Houston, TX")
    
        result = get_location(iss_service)
    
        self.assertEqual(("11:50PM", "Houston, TX"), result)

    def test_get_location_returns_string_when_exception_is_thrown_service_unreachable(self):
        iss_service = lambda: exec('raise Exception("network error: service unreachable")')
    
        result = get_location(iss_service)
    
        self.assertEqual("network error: service unreachable", result)
    
    def test_get_location_returns_string_when_exception_is_thrown_service_failed_to_respond(self):
        iss_service = lambda: exec('raise Exception("service failed to respond")')

        result = get_location(iss_service)
    
        self.assertEqual("service failed to respond", result)

    def test_get_astronauts_returns_empty_list_if_service_gives_empty_list(self):
        iss_service = lambda: []
    
        result = get_astronauts(iss_service)
    
        self.assertEqual([], result)

    def test_get_astronauts_returns_1_name_if_service_gives_1_name(self):
        iss_service = lambda: ["Michael Jackson"]
    
        result = get_astronauts(iss_service)
    
        self.assertEqual(["Michael Jackson"], result)
    
    def test_get_astronauts_returns_2_names_in_sorted_order_if_service_gives_names_in_sorted_order(self):
        iss_service = lambda: ["Michael Jackson", "LeBron James"]
    
        result = get_astronauts(iss_service)
    
        self.assertEqual(["Michael Jackson", "LeBron James"], result)

    def test_get_astronauts_returns_2_names_in_sorted_order_if_service_gives_names_in_unsorted_order(self):
        iss_service = lambda: ["LeBron James", "Michael Jackson"]
    
        result = get_astronauts(iss_service)
    
        self.assertEqual(["Michael Jackson", "LeBron James"], result)

    def test_get_astronauts_returns_network_error_if_service_throws_exception(self):
        iss_service = lambda: exec('raise Exception("network error: service unreachable")')
    
        result = get_astronauts(iss_service)
    
        self.assertEqual("network error: service unreachable", result)

    def test_get_astronauts_returns_service_failed_to_respond_if_service_throws_exception(self):
        iss_service = lambda: exec('raise Exception("service failed to respond")')

        result = get_astronauts(iss_service)
    
        self.assertEqual("service failed to respond", result)


if __name__ == '__main__':
    unittest.main()