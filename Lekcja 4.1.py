def add(a, b):
    print(a+b)

add(2, 6)

def say_hello(first_name, second_name, gender = "Mr"):
    print(f"Hello {gender} {second_name} {first_name}")

say_hello("Dmitry", "Barankov", "Sir")

def shopping(items, /, payment = ' card ', *, shop = ' location '):
    shopping_cart = "Koszek zawiera: "
    for item in items:
        shopping_cart += item + payment + shop + '\n'
    return shopping_cart

shopping_items = [
    "jajka",
    "bułka",
    "ser feta",
    "masło",
    "pomidor"
]

basket = shopping(shopping_items, ' visa ', shop = ' supermarket ')
print(basket)

def coun_them_all(*args, **kwargs):
    positional_args_count = len(args)
    kwargs_leng = len(kwargs)
    print(f"If I recive {positional_args_count} positional arguments, and named args {kwargs}")

coun_them_all(1, 2, 3, "test", r=1, e=45)

shopping_items = [
    ("ziemniak", 2.5, 0.51),
    ("cebula", 3, 1.60),
    ("ser", 0.8, 15.50)
]
def get_index_1_tuple_element(given_tuple):
    return given_tuple[1]
sorted_items = sorted(shopping_items, key=get_index_1_tuple_element)
print(sorted_items)

sorted_items1 = sorted(shopping_items, key=lambda given_tuples1: given_tuples1[2])
print(sorted_items1)
