import random

def findPrice(size,issues):
  if size == "full":
    if issues == "1":
      return 500
    elif issues == "2" or issues == "3" or issues == "4" or issues == "5" or issues == "6":
      return 450
    elif issues == "16":
      return 240
    else:
      return 400


  if size == "half":
    if issues == 1:
      return 350
    elif issues == "2" or issues == "3" or issues == "4" or issues == "5" or issues == "6":
      return 300
    elif issues == "16":
      return 130
    else:
      return 250


  if size == "quarter":
    if issues == "1":
      return 200
    elif issues == "2" or issues == "3" or issues == "4" or issues == "5" or issues == "6":
      return 160
    elif issues == "16":
      return 70
    else:
      return 120


  if size == "eighth":
    if issues == 1:
      return 120
    elif issues == "2" or issues == "3" or issues == "4" or issues == "5" or issues == "6":
      return 85
    elif issues == "16":
      return 40
    else:
      return 60

  else:
    return -1


def getImg(size):
  if size == "full":
    return "Full"
  if size == "half":
    return "Half"
  if size == "quarter":
    return "Quarter"
  if size == "eighth":
    return "Eighth"
  else:
    return "AdSizes"
