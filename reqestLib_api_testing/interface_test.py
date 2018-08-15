import requests
import unittest
# search event api

class GetEventListTest(unittest.TestCase):

    def setUp(self):
        self.url = 'http://127.0.0.1:8000/api/get_event_list/'

    def test_get_event_null_by_eid(self):
        r = requests.get(self.url, params={'eid': ''})
        result = r.json()

    # assert the return values from api

        self.assertEqual(result['status'], 10021)
        self.assertEqual(result['message'], 'parameter error')

    def test_get_event_error_by_eid(self):
        r = requests.get(self.url, params={'eid': '901'})
        result = r.json()
        self.assertEqual(result['status'], 10022)
        self.assertEqual(result['message'], 'query result is empty')

    def test_get_event_success_by_eid(self):
        r = requests.get(self.url, params={'eid': 1})
        result = r.json()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'success')
        self.assertEqual(result['data']['name'], 'Apple Representation')
        self.assertEqual(result['data']['address'], '11346 blr driv, CA')
        self.assertEqual(result['data']['start_time'], '2018-09-01T12:00:00Z')

    def test_get_event_null_by_name(self):
        r = requests.get(self.url, params={'name': ''})
        result = r.json()
        self.assertEqual(result['status'], 10021)
        self.assertEqual(result['message'], 'parameter error')

    def test_get_event_error_by_name(self):
        r = requests.get(self.url, params={'name': "iphone XS"})
        result = r.json()
        self.assertEqual(result['status'], 10022)
        self.assertEqual(result['message'], 'query result is empty')

    def test_get_event_success_by_name(self):
        r = requests.get(self.url, params={'name': 'xiaomi Max event'})
        result = r.json()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'success')
        self.assertEqual(result['data'][0]['limit'], 2000)
        self.assertEqual(result['data'][0]['address'], 'Beijing exhibition center')


if __name__ == '__main__':
    unittest.main(verbosity=2)
