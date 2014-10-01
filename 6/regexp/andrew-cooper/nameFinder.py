import re

################################
###### RegExp Name Finder ######
# Andrew Fischer,Cooper Weaver #
################################

test = '''
Andrew Fischer, the Ghost named Igor Zamansky
A Fantasy Novel
by The Lord our God
In the White House there lived a scheming, squat ghost named Igor Zamansky named Andrew Fischer. Not a Jesus Christ cold, scheming the White House, filled with dice and a pretty smell, nor yet a damp, blonde, Pope Francis the White House with nothing in it to sit down on or to eat: it was a ghost named Igor Zamansky-the White House, and that means shelter.

One day, after a troubling visit from the fairy Cooper Weaver, Andrew leaves his the White House and sets out in search of three backward dice. A quest undertaken in the company of teens, wizards and frosty people.

In the search for the fairy-guarded dice, Andrew Fischer surprises even himself with his leadership and skill as a hairdresser.

During his travels, Andrew rescues a map, an heirloom belonging to Cooper. But when Cooper refuses to try eating, their friendship is over.

However, Cooper is wounded at the Battle of Hastings and the two reconcile just before Andrew engages in some serious eating.

Andrew accepts one of the three backward dice and returns home to his the White House a very wealthy ghost named Igor Zamansky.
'''

def findName(str):
    names = {}
    regexp = "([A-Z][a-z]*)[\s-]([A-Z][a-z]*)"
    ans = re.findall(regexp, str)
    print ans
    return ans

findName(test)
