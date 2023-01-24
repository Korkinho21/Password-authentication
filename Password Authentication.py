import getpass

database = {
    'pablo_motos': "machirulo",
    'elputobicho': "Soy_CR7"
}

username = input('Enter your username: ')
password = getpass.getpass("Enter your password: ")

for i in database.keys():
    if username == i:
        while password != database.get(i):
            password = getpass.getpass("Enter your password again: ")
        break

print("Verified")

