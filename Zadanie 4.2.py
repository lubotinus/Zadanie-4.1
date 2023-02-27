def polindrom(text):
    for i in range(0, int(len(text)/2)):
        if text[i] != text[len(text)-1-i]:
         return False
    return True
                  
if polindrom("kajak"):
    print("True")
else:
    print("False")
