""" -- List is a order of collection of items
    -- Strings are immutable we can not modify original values """


def list_items():
    numbers = [1, 3, 2, 7, 9, 4]
    print(numbers)
    print(numbers[0])
    print(numbers[1])
    print(numbers[0:])
    numbers.remove(4)
    print(numbers)
    del numbers[0]
    print("Delete numbers from list: ", numbers)

    colours = ['red', 'green', 'blue']
    print(colours)
    print(colours[1])
    print(colours[1:])

    coordinates = [[0, 0], [50, 50], [100, 100], [200, 200]]
    print(coordinates)
    print(coordinates[0])
    print(coordinates[1])
    print("Length of coordinates: ", len(coordinates))


# list_items()

def sort_key(company):
    print("----------", company[2])
    return company[0]


def sort_method_list():
    guests = ["James", "Mary", "John", "Patrica", "Robert", "Jennifer"]
    guests.sort()
    print(guests)
    guests.sort(reverse=True)
    print(f"Guests in descending order:- {guests}")

    print("----")
    num = [2, 7, 3, 1, 4, 9, 5, 8, 0]
    num.sort()
    print(f"Arrange number in ascending order: {num}")

    print("--------------------")
    """ List of Tuples """
    companies = [('zolo', 2019, 443.43),
                 ('google', 2019, 134.81),
                 ('Apple', 2019, 260.2),
                 ('Facebook', 2019, 70.7)]
    print(f"list of companies:- {companies}")
    print(companies[2])
    print(f"type of compines: {type(companies)}")

    companies.sort(key=sort_key)
    print(companies)
    print("--------------")


sort_method_list()


def list_unpack():
    colours = ["green", "red", "blue", "orange"]
    green, red, *other = colours
    print(green)
    print(red)
    print(other)


# list_unpack()


""" -- iterator over a list"""
def list_iterator():
    cities = ['Coimbatore', 'Chennai', 'Hyderabad', 'Vijayawada']
    result = cities.index("Chennai")
    print(f"Index fo Chennai:- {result}")
    for city in cities:
        print(city)

    """ need to access indexes of elements inside the loop. In these cases, you can use the enumerate() function. """
    print("-----------")
    for city in enumerate(cities):
        print(city)

    for index, city in enumerate(cities):
        print(f"Index and City:- {index}: {city}")

list_iterator()
