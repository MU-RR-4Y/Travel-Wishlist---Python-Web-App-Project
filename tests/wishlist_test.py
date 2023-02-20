import unittest
from models.wishlists import Wishlist
from models.destination import Destination
from models.user import User

class TestWishlist(unittest.TestCase):
    def setUp(self):
        self.destination = Destination('Rome', 'Italy','Capital of Italy')
        self.user = User('Dave')
        self.wishlist = Wishlist(self.user, self.destination)

    def test_visit_user(self):
        self.assertEqual('Dave', self.wishlist.user.name)

    def test_visit_destinaton(self):
        self.assertEqual('Rome', self.wishlist.destination.name)

   