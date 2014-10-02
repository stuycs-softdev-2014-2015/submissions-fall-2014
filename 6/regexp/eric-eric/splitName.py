def splitName(list):
    ans = []
    for element in list:
        current = element.split(" ")

        for word in current:
            ans.append(word)
    print ans
    return
