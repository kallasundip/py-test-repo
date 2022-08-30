"""
    Write a code that takes three parameters where:

    x is the start of the range (inclusive).
    y is the end of the range (inclusive).
    n is the divisor to be checked against.

    Return an ordered list with numbers in the range that are divisible by the third parameter n. Return an empty list if there are no numbers that are divisible by n.
"""


class ListAndTuples:

    def divisor(self):
        list = [1, 10, 3]
        x, y, n = list  # unpaking
        result = []
        for item in range(x, y):
            if item % n == 0:
                result.append(item)
        return result

    def sumof_budget(self):
        people1 = {"name": "John", "age": 21, "budget": 23000}
        people2 = {"name": "Steve", "age": 32, "budget": 40000}
        people3 = {"name": "Martin", "age": 16, "budget": 2700}

        # budget1 = people1["budget"]
        # budget2 = people2["budget"]
        # budget3 = people3["budget"]
        # sum = budget1+budget2+budget3
        # print(sum)

        total = 0
        total_list = [people1, people2, people3]
        for people in total_list:
            total += people["budget"]
        return total


run = ListAndTuples()
# print(run.divisor())
total_budget = run.sumof_budget()
print(total_budget)
