from src.iss_time_service import *
import unittest
from unittest.mock import patch

class ISSTimeServiceTests(unittest.TestCase): 
    def test_get_response_returns_from_the_webservice_for_time_and_location(self):
        self.assertEqual('success', get_response()['message'])

    def test_parse_response_returns_timestamp_and_location_from_the_given_sample_data(self):
        sample_json = {"message": "success", "iss_position": {"longitude": "2.0644", "latitude": "-50.5711"}, "timestamp": 1665615352}

        result = parse_response(sample_json)

        self.assertEqual([1665615352, [2.0644, -50.5711]], result)

    def test_parse_response_returns_timestamp_and_location_from_a_different_given_sample_data(self):
        sample_json = {"message": "success", "iss_position": {"longitude": "-9.3535", "latitude": "-48.2274"}, "timestamp": 1665615226}
        
        result = parse_response(sample_json)
        
        self.assertEqual([1665615226, [-9.3535, -48.2274]], result)

    def test_get_location_calls_get_response_and_parse_response(self):
        with patch("src.iss_time_service.get_response", return_value = 
            {"message": "success", "iss_position": {"longitude": "-95.3584", "latitude": "29.7499"}, "timestamp": 1665615352}):
            result = get_location()

        self.assertEqual([convert_timestamp_to_ct_time(1665615352), 'Houston, Texas'], result)
    
    def test_get_location_returns_time_in_ct_instead_of_timestamp(self):
        with patch("src.iss_time_service.get_response", return_value = 
            {"message": "success", "iss_position": {"longitude": "-95.3584", "latitude": "29.7499"}, "timestamp": 1665615352}):
            result = get_location()

        self.assertEqual(convert_timestamp_to_ct_time(1665615352), result[0])
    
    def test_get_location_returns_time_in_ct_instead_of_timestamp_another_test_that_returns_time_in_am(self):
        with patch("src.iss_time_service.get_response", return_value = 
            {"message": "success", "iss_position": {"longitude": "-95.3584", "latitude": "29.7499"}, "timestamp": 1665414356}):
            result = get_location()

        self.assertEqual(convert_timestamp_to_ct_time(1665414356), result[0])
    
    def test_get_location_returns_location_with_city_and_state(self):
        with patch("src.iss_time_service.get_response", return_value = 
            {"message": "success", "iss_position": {"longitude": "-95.3584", "latitude": "29.7499"}, "timestamp": 1665615352}):
            result = get_location()

        self.assertEqual('Houston, Texas', result[1])

    def test_get_location_returns_None_when_there_is_no_city_state_at_the_coordinates(self):
        with patch("src.iss_time_service.get_response", return_value = 
            {"message": "success", "iss_position": {"longitude": "95.3584", "latitude": "-40"}, "timestamp": 1665615352}):
            result = get_location()

        self.assertEqual('None', result[1])    

    @patch("src.iss_time_service.get_response")
    def test_get_location_throws_an_exception_if_service_is_unreachable(self, mock_get_response):
        mock_get_response.side_effect = Exception("service unreachable")

        self.assertRaisesRegex(Exception, "service unreachable", get_location)
    
    @patch("src.iss_time_service.get_response")
    def test_get_location_throws_an_exception_if_service_is_returns_an_access_error(self, mock_get_response):
        mock_get_response.side_effect = Exception("access error")

        self.assertRaisesRegex(Exception, "access error", get_location)


if __name__ == '__main__':
    unittest.main()
