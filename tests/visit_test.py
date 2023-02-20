import unittest
from models.visit import Visit
from models.destination import Destination
from models.user import User

class TestVisit(unittest.TestCase):
    def setUp(self):
        self.destination = Destination('Rome', 'Italy','Capital of Italy')
        self.user = User('Dave')
        self.visit = Visit(self.user, self.destination,'20/01/2023', 4, 'Rome was amazing')

    def test_visit_user(self):
        self.assertEqual('Dave', self.visit.user.name)

    def test_visit_destinaton(self):
        self.assertEqual('Rome', self.visit.destination.name)

    def test_visit_date(self):
        self.assertEqual('20/01/2023', self.visit.date)
    
    def test_visit_rating(self):
        self.assertEqual(4, self.visit.rating)

    def test_visit_comment(self):
        self.assertEqual('Rome was amazing',self.visit.comment)

