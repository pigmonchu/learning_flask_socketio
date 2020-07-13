from tests.tests_base import TestBase
import unittest
from flask import url_for
import json

class TestAPIAdd(TestBase):
    def test_hi_ha_contact(self):
        response = self.client.post(url_for('operations.add'), content_type='application/json')
        self.assertEqual(400, response.status_code)

    def test_add_2_numbers(self):
        data = json.dumps({
            "op1": 1,
            "op2": 2
        })
        print(data)

        response = self.client.post(url_for('operations.add'), data=data, content_type='application/json')
        self.assertEqual(200, response.status_code)
        json_data = response.get_json()
        self.assertEqual(json_data.get('status'), "success")
        self.assertEqual(json_data.get('result'), 3)

if __name__ == '__main__':
    unittest.main()
