import pdb

from models.country import Country
from models.destination import Destination
from models.user import User
from models.visit import Visit
from models.wishlists import Wishlist

import repositories.country_repository as country_repo
import repositories.destination_respository as destination_repo
import repositories.user_repository as user_repo
import repositories.visit_repository as visit_repo
import repositories.wishlist_repo as wishlist_repo



# # TEST Country

country_1 = Country('Italy')
country_2 = Country('France')
country_3 = Country('America')

country_repo.save(country_1) 
country_repo.save(country_2)
country_repo.save(country_3)



# # DROP tables
# country_repo.delete_all() #working
# destination_repo.delete_all() # working
# user_repo.delete_all()



# # TEST Destination

destination_1 = Destination('Rome',country_1,'Home of the Romans')
destination_2 = Destination('Florence',country_1, 'Home of the Medici')
destination_3 = Destination('Paris',country_2, 'Capital of France')
destination_4 = Destination('Walt Disney World',country_3, 'Disney park in Orlando')
destination_5 = Destination('New York',country_3, 'The city that never sleeps')
destination_6 = Destination('Hollywood',country_3, 'Home of movies')
destination_7 = Destination('Indianapolis Motor Speedway',country_3, 'The Racing Capital Of The World')

 
destination_repo.save(destination_1)  
destination_repo.save(destination_2)  
destination_repo.save(destination_3)  
destination_repo.save(destination_4)  
destination_repo.save(destination_5)  
destination_repo.save(destination_6)  
destination_repo.save(destination_7)  

 

dest1 = destination_repo.select_all() # working
print(dest1[0].__dict__)  

dest2 = destination_repo.select(3) # working
print(dest2.__dict__) 



# # TEST Users

user_1 = User('Dave')
user_2 = User('John')
user_3 = User('Simon')
user_4 = User('Jack')
user_5 = User('Steve')
user_6 = User('Luke')

user_repo.save(user_1)
user_repo.save(user_2)
user_repo.save(user_3)
user_repo.save(user_4)
user_repo.save(user_5)
user_repo.save(user_6)




# # TEST VISITS

visit_1 = Visit(user_1,country_2,'15/01/2023', 5,'We visited Notre Dame')
visit_2 = Visit(user_3,country_1,'05/02/2023', 4,'The Vatican was huge')
visit_3 = Visit(user_1,country_1,'23/01/2023',5,'Florence was amazing')
visit_4 = Visit(user_4,country_3,'09/02/2023',3,'The magic kingdom was great')

visit_repo.save(visit_1)
visit_repo.save(visit_2)
visit_repo.save(visit_3)
visit_repo.save(visit_4)



# TEST WISHLIST

wishlist_item1 = Wishlist(user_1, destination_6)

wishlist_repo.save(wishlist_item1)


pdb.set_trace()


