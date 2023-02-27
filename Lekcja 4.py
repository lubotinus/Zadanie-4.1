def shoppnig():
    shopping_items = [
      "jajka",
        "bułka",
        "ser feta",
        "masło",
        "pomidor"  
    ]
    shopping_cart = "Koszyk zawiera: "
    for item in shopping_items:
        shopping_cart += item + '\n'
    return shopping_cart

print(shoppnig())

def no_result_function():
    print("Test")
    return None

print(type(no_result_function()))

def day_times():
    return "morning", "afternoon", "1evening", "night"

times = day_times()
print(times)
print(type(times))

first, second, third, fourth = day_times()
print("Trzeci element to %s" % third)


