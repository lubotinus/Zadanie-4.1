def polindrom(text):
    if text.isalnum()==True:
        return text == text[::-1]
    else:
       return False
                  
if polindrom("kajak"):
    print("True")
else:
    print("False")
