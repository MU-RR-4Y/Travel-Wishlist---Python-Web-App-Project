import unittest
from models.visit import Visit
from models.country import Country
from models.user import User

class TestVisit(unittest.TestCase):
    def setUp(self):
        self.country = Country('Italy')
        self.user = User('Dave')
        self.visit = Visit(self.user, self.country,'20/01/2023', 4, 'Rome was amazing')

    def test_visit_user(self):
        self.assertEqual('Dave', self.visit.user.name)

    def test_visit_country(self):
        self.assertEqual('Italy', self.visit.country.name)

    def test_visit_date(self):
        self.assertEqual('20/01/2023', self.visit.date)
    
    def test_visit_rating(self):
        self.assertEqual(4, self.visit.rating)

    def test_visit_comment(self):
        self.assertEqual('Rome was amazing',self.visit.comment)

