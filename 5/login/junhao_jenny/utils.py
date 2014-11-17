# passwords must have more than 4 characters
# include at least 1 number
def isValidPass(pword):
    if (len(pword)>4):
        for char in pword:
            if char.isdigit():
                return True
    return False


# not implemented, but could be useful
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
