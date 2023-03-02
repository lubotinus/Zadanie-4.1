import logging
logging.basicConfig(level=logging.DEBUG)
def algoritm(number1, number2, operator):
   
   if operator == 1:
      logging.debug(f"Dodaje {number1} i {number2}")
      print(f"Wynik to  {float(number1) + float(number2)}")
   if operator == 2:
      logging.debug(f"Odejmuje {number1} i {number2}")
      print(f" Wynik to {float(number1) - float(number2)}")
   if operator == 3:
      logging.debug(f"Mnoże {number1} i {number2}")
      print(f" Wynik to {float(number1) * float(number2)}")
   if operator == 4:
      logging.debug(f"Dziele {number1} i {number2}")
      print(f" Wynik to {float(number1) / float(number2)}")
   
def check_input(input):
   try:
      val = int(input)
   except ValueError:
      try:
         val = float(input)
      except ValueError:
         print("No.. input is not a number. It's a string")

oper = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "))
num1 = input("Podaj składnik 1. ")
check_input(num1)
num2 = input("Podaj składnik 2. ")
check_input(num2)
algoritm(num1, num2, oper)
    
