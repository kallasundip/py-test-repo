
class Century:
    def year_century(self):
        year = int(input("Enter Year: "))
        final_year = 1101
        for item in range(1001, 2020):
            if item <= year < final_year:
                print(f"{(str(final_year))[:2]}th Century")
                break
            final_year += 100

    def remove_first_last_char(self):
        name = "Hello World"
        size = len(name)
        name_modify = name[1:size]
        print(name_modify)
        # print(name)
        # print(name[1:len(name) - 1])



    def sum_two_values(self):
        chocolatePrice = '₹35'
        lemonPrice = '₹20'
        total = int(chocolatePrice[1:len(chocolatePrice)]) + int(lemonPrice[1:len(lemonPrice)])
        return total


runner = Century()
# runner.year_century()
runner.remove_first_last_char()
# total_value = runner.sum_two_variabes()
# print(total_value)
