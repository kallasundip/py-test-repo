""" -- Python dictionary is a key value pairs where each key associated a value
    -- In python we use {} to define a dictionary
    --  empty_dic = {} """


def dictionary():
    empty_dict = {}
    print(type(empty_dict))
    person = {"first_name" : "raj",
              "last_name" : "kumar",
              "age" : 29,
              "favorite_colour" : "blue",
              "gender" : "male",
              "place" : "hyd"}
    print(person["first_name"])
    print(person["age"])
    value = person["age"]
    print(value)
    print(person.get("favorite_colour"))
    person["gender"] = "female"
    print(person.get("gender"))
    print(person.get("place"))
    print(person)
    del person["place"]
    print("location deleted", person)

    """ -- looping all key value pairs in dictionary """
    print(person.items())
    print("--------------")
    for key, value in person.items():
        print(f"{key}, {value}")

    for key in person.keys():
        print(f"key values in person:- {key}")

    for value in person.values():
        print(f"value values in person:- {value}")


dictionary()
