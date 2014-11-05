# passwords must have more than 5 characters
# include at least 1 upper and lowercase letter
# include at least 1 number
def isValidPass(pword):
    hasUpper = False
    hasLower = False
    hasNumber = False
    if (len(pword)>5):
        for letter in pword:
            if letter.isupper():
                hasUpper=True
            if letter.islower():
                hasLower=True
            if letter.isdigit():
                hasNumber=True
    if (hasUpper and hasLower and hasNumber):
        return True
    else:
        return False


# taken from previous assignment; could be useful
def isValidEmail(email):
    hasUser = False
    hasAtSymbol = False
    hasDomain = False #ex: gmail                                                
    hasPeriod = False
    hasEnding = False #ex: com                                                  
    if '@' in email:
        hasAtSymbol = True
        atIndex = email.find('@')
        username = email[:atIndex]
        if len(username) > 0:
            hasUser = True
        if '.' in atIndex[atIndex:]:
            hasPeriod = True
            periodIndex = email[atIndex:].find('.')
            if periodIndex > atIndex+1:
                hasDomain = True
            if len(email[periodIndex:]) > 1:
                hasEnding = True
    if hasUser and hasAtSymbol and hasDomain and hasPeriod and hasEnding:
        return True
    return False
