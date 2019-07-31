def strong_password(password):
    password = str(password)
    UPS = re.compile(r'[A-Z]')
    UPST = UPS.search(password)
    Lowercase = re.compile(r'[a-z]')
    Lowercasetest = Lowercase.search(password)
    digit = re.compile(r'\d')
    DigitTest = digit.search(password)
    if len(password)<8:
        return 'WEAAAKKKKKKKKKKKKKKKKKKKK'
    elif UPS == None: 
        return 'WEAKKKKK'
    elif Lowercasetest == None:
        return 'weaaaaak'
    elif DigitTest == None:
        return 'W3ak'
    else:
        return 'Strong password for strong man'
print('What is your password?')
password = input()
print(strong_password(password))
