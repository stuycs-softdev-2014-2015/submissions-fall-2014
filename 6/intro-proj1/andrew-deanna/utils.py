import random

def findPrice(size,issues):
  if size == "full":
    if issues == 1:
      return 500
    if issues > 1 and issues < 7:
      return 450
    if issues > 6:
      return 400
    if issues == 16:
      return 240


  if size == "half":
    if issues == 1:
      return 350
    if issues > 1 and issues < 7:
      return 300
    if issues > 6:
      return 250
    if issues == 16:
      return 130


  if size == "quarter":
    if issues == 1:
      return 200
    if issues > 1 and issues < 7:
      return 160
    if issues > 6:
      return 120
    if issues == 16:
      return 70


  if size == "eighth":
    if issues == 1:
      return 120
    if issues > 1 and issues < 7:
      return 85
    if issues > 6:
      return 60
    if issues == 16:
      return 40

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
