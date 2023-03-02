def shopping(items, payment='card', shop='local'):
    result = ""
    result = result + "Idę na zakupy do %s.\n" % shop
    result = result + "Kupię następujące rzeczy:\n"
    for item in items:
        result = result + " - %s\n" % item
    result = result + "By zapłacić, używam %s." % payment
    return result

items = ["cola", "whiskey", "lód"]
text = shopping(items, 'card', 'small local shop')
print(text)

#print("Pokarze wszystko co wpiszesz!")
#text = input()
#print("Oto twój tekst: ***%s***" % text)

items_text = "cola,whiskey,lód"
items = items_text.split(',')
print(type(items))
print(len(items))

print("Witaj, ten program pomoże Ci sprawdzić czy jesteś pełnoletni/a")
adult = None
sex = input("Podaj proszę swoją płeć [M/K]: ")
if sex== 'M':
    age = int(input("Twój wiek? "))
    adult = age >= 18
elif sex == 'K':
    print("Kobiet o wiek się nie pyta, więc zrobię to delikatnie.")
    over18_yesno = input("Czy miałaś już osiemnastkę? [T/N]?")
    adult = (over18yesno =='T')
else:
    print("Nie ma takiej płci!")
    exit(1)
print("Już wiem. Twoja pełnoletniość w boolean to %s" % str(adult))