import random
from faker import Faker
fake = Faker("en")


def generate_random_word():
    return fake.word()


def generate_first_name():
    return fake.first_name_male()


def generate_last_name():
    return fake.last_name_male()


def generate_name_prefix():
    prefixes = ["Mr", "Mrs", "Miss", "Ms", "Master", "Fr", "Rev", "Dr"]

    return random.choice(prefixes)


def generate_phone_number():
    return random.randint(100000000, 999999999)


def generate_street_address_line1():
    street_address_line_1 = fake.street_address()

    street_address_line_1 = "".join([i for i in street_address_line_1 if not i.isdigit()])
    street_address_line_1 = street_address_line_1.strip() + " Street"

    return street_address_line_1


def generate_street_address_line2():
    return str(random.randint(1, 99999))


def generate_city():
    return fake.city()


def generate_postcode():
    return fake.postcode()
