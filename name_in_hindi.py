from faker import Faker 
fake = Faker('hi_IN')      #'hi_IN' changed the language 
for i in range(0, 10): 
    print('Name->', fake.name(), 'Country->', fake.country()) 
  