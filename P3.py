import math
def find_hypothenuse(a,b):
    temp1 =a*a
    temp2 =b*b
    hypothenuse=math.sqrt(temp1 + temp2)
    return hypothenuse

print "hypothenuse 3,4-", find_hypothenuse(3,4)

def print_name(name):
    print 'person name-' +name

print_name('Jose')
print_name('ned')

