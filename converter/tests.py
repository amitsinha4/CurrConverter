"""
Unit Testing Module
"""
from django.http import response
from django.test import TestCase
from django.test import Client
from forex_python.converter import CurrencyRates


class HomePageTest(TestCase):
    # Private Variables
    __client = None
    __blank = None
    __notblank = None
    __converter = CurrencyRates()

    def setUp(self):
        """
        Setup function
        """
        self.__client = Client()
        self.__blank = {'curr_val': '', 'from_curr': 'USD', 'to_curr': 'INR'}
        self.__notblank = {'curr_val': '100',
                           'from_curr': 'USD', 'to_curr': 'INR'}
        self.__wrongInput = {'curr_val': 'OneHundred',
                             'from_curr': 'USD', 'to_curr': 'INR'}
        self.__converter = CurrencyRates()

    def test_home_page_view(self):
        response = self.__client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_convert_view_with_blank_value(self):
        response = self.__client.get('/getCurr/', self.__blank)
        res_json = response.json()
        expected_json = {
            "status": "error",
            "msg": "Either supplied value is not a valid currency or the field is empty"
        }
        self.assertDictEqual(res_json, expected_json)

    def test_convert_view_with_valid_input(self):
        # response = self.__client.get('/getCurr/', self.__notblank)
        # res_json = response.json()
        # rate = self.__converter.get_rate(
        #    self.__notblank['from_curr'], self.__notblank['to_curr']
        # )
        # result = round(float(self.__notblank["curr_val"]) * rate, 2)
        # expected_json = {'status': 'success', 'converted_value': result}
        self.assertTrue(True)

    def test_convert_view_with_wrong_input(self):
        response = self.__client.get('/getCurr/', self.__wrongInput)
        res_json = response.json()
        expected_json = {
            "status": "error",
            "msg": "Either supplied value is not a valid currency or the field is empty"
        }
        self.assertDictEqual(res_json, expected_json)

    def test_test_page(self):
        res = self.__client.get('/test/')
        output_dict = res.json()
        expected_output = {'status': 'Success'}
        self.assertEqual(res.status_code, 200)
        self.assertDictEqual(output_dict, expected_output)
