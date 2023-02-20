import unittest
from models.destination import Destination

class TestDestination(unittest.TestCase):
    def setUp(self):
        self.destination_1 = Destination('Rome','Italy','Capital of Italy')


    def test_destination_name(self):
        self.assertEqual('Rome', self.destination_1.name)

    def test_destination_country(self):
        self.assertEqual('Italy', self.destination_1.country)    

    def test_destination_info(self):
        self.assertEqual('Capital of Italy', self.destination_1.information)

    def test_destination_id__isNone(self):
        self.assertIsNone(self.destination_1.id)
   
    def test_destination_id__isNotNone(self):
        self.destination_1.id = 1
        self.assertEqual(1, self.destination_1.id)

  

