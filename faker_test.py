from faker import Faker

fake = Faker()
print(fake.name())
print(fake.address())
print(fake.email())
print(fake.text())
print(fake.url())

str = ""
for i in range(0,5):
    str += fake.text() + " "

print(str)