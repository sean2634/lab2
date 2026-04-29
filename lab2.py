import statistics
def display_main_menu():
    print ("Enter some numbers seperated by commas")

def get_user_input():
    x = input('Enter numbers: ')
    numbers = [int(num) for num in x.split(",")]
    return numbers

def calc_avg_temp(numbers):
    avgtemp = sum(numbers)/len(numbers)
    return avgtemp

def calc_min_max_temp(numbers):
    return min(numbers), max(numbers)


def main():
    numbers = get_user_input()
    avgtemp = calc_avg_temp(numbers)
    minmax = calc_min_max_temp(numbers)
    print (avgtemp)
    print (minmax)
    print (statistics.median(numbers))
if __name__ == "__main__":
    main()