def iterate_arguments(item, items):
    # item = 123
    # items = 5
    total_item = []
    for num in range(items):
        total_item.append(item)
    return total_item


rp = iterate_arguments("Hello", 5)
print(rp)


