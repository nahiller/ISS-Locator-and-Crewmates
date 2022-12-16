import unittest
from unittest.mock import patch
from src.iss_astronaut_service import *

class ISSAstronautServiceTests(unittest.TestCase): 

    def test_get_response_returns_response_from_the_webservice_for_astronauts_names(self):
        self.assertEqual('success', get_response()['message'])
        
    def test_parse_response_returns_astronauts_names_from_the_given_sample_data(self):
        
        result = parse_response({"number": 14, "message": "success", "people": [{"craft": "ISS", "name": "Kjell Lindgren"}]})

        self.assertEqual(["Kjell Lindgren"], result)
    
    def test_parse_response_returns_astronauts_names_from_a_different_given_sample_data(self):
        sample_json =  {"number": 14, "message": "success", "people": [{"craft": "ISS", "name": "Kjell Lindgren"}, 
            {"craft": "ISS", "name": "Bob Hines"}, {"craft": "ISS", "name": "Samantha Cristoforetti"}, 
            {"craft": "ISS", "name": "Jessica Watkins"}, {"craft": "Tiangong", "name": "Cai Xuzhe"}, 
            {"craft": "Tiangong", "name": "Chen Dong"}, {"craft": "Tiangong", "name": "Liu Yang"}, 
            {"craft": "ISS", "name": "Sergey Prokopyev"}, {"craft": "ISS", "name": "Dmitry Petelin"}, 
            {"craft": "ISS", "name": "Frank Rubio"}, {"craft": "Endurance", "name": "Nicole Mann"}, 
            {"craft": "Endurance", "name": "Josh Cassada"}, {"craft": "Endurance", "name": "Koichi Wakata"}, 
            {"craft": "Endurance", "name": "Anna Kikina"}]}
        
        result = parse_response(sample_json)

        self.assertEqual(['Kjell Lindgren', 'Bob Hines', 'Samantha Cristoforetti', 'Jessica Watkins', 'Sergey Prokopyev', 'Dmitry Petelin', 'Frank Rubio'], result)

    def test_get_astronauts_names_calls_parse_response_and_get_response_functions(self):
        with patch("src.iss_astronaut_service.get_response", return_value = {"number": 14, "message": "success", "people": [{"craft": "ISS", "name": "Kjell Lindgren"}, 
            {"craft": "ISS", "name": "Bob Hines"}, {"craft": "ISS", "name": "Samantha Cristoforetti"}, 
            {"craft": "ISS", "name": "Jessica Watkins"}, {"craft": "Tiangong", "name": "Cai Xuzhe"}, 
            {"craft": "Tiangong", "name": "Chen Dong"}, {"craft": "Tiangong", "name": "Liu Yang"}, 
            {"craft": "ISS", "name": "Sergey Prokopyev"}, {"craft": "ISS", "name": "Dmitry Petelin"}, 
            {"craft": "ISS", "name": "Frank Rubio"}, {"craft": "Endurance", "name": "Nicole Mann"}, 
            {"craft": "Endurance", "name": "Josh Cassada"}, {"craft": "Endurance", "name": "Koichi Wakata"}, 
            {"craft": "Endurance", "name": "Anna Kikina"}]}):

            result = get_astronauts_names()
    
        self.assertEqual(['Kjell Lindgren', 'Bob Hines', 'Samantha Cristoforetti', 'Jessica Watkins', 'Sergey Prokopyev', 'Dmitry Petelin', 'Frank Rubio'], result)

    @patch("src.iss_astronaut_service.get_response")
    def test_get_astronauts_names_throws_an_exception_if_service_is_unreachable(self, mock_get_response):
        mock_get_response.side_effect = Exception('service unreachable')
        
        self.assertRaisesRegex(Exception, 'service unreachable', get_astronauts_names)
 
    @patch("src.iss_astronaut_service.get_response")
    def test_get_astronauts_names_throws_an_exception_if_service_fails_to_respond(self, mock_get_response):
        mock_get_response.side_effect = Exception('access error')

        self.assertRaisesRegex(Exception, 'access error', get_astronauts_names)


if __name__ == '__main__':
    unittest.main()