import unittest
from models.user import User
from models.destination import Destination

class TestUser(unittest.TestCase):
    def setUp(self):
        self.destination_1 = Destination('Rome', 'Italy', 'Capital of Italy')
        self.destination_2 = Destination('Paris', 'France','Capital of France')
        self.user = User('Dave')


    def test_user_name(self):
        self.assertEqual('Dave', self.user.name)

   
    def test_user_id__isNone(self):
        self.assertIsNone(self.user.id)
   
    def test_user_isNotNone(self):
        self.user.id = 1
        self.assertEqual(1, self.user.id)

