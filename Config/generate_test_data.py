import random
from faker import Faker
fake = Faker("en")


def unique_random_word():
    return fake.word()


def first_name():
    return fake.first_name_male()


def last_name():
    return fake.last_name_male()


def name_prefix():
    prefixes = ["Mr", "Mrs", "Miss", "Ms", "Master", "Fr", "Rev", "Dr"]
    prefix = random.choice(prefixes)
    return prefix


def phone_number():
    return random.randint(100000000, 999999999)


def street_address_line_1():
    street_address_line1 = fake.street_address()
    street_address_line1 = "".join([i for i in street_address_line1 if not i.isdigit()])
    street_address_line1 = street_address_line1.strip() + " Street"
    return street_address_line1


def street_address_line_2():
    return str(random.randint(1, 99999))


def city():
    return fake.city()


def postcode():
    return fake.postcode()
