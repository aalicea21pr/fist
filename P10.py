animals=['cat','dog','mouse','cow']
for animal in animals:
    print animal

horizontal="cat dog mouse caw"
horizontal = ""
for animal in animals:
    horizontal=horizontal +' ' +animal
print horizontal

ages=[18,21,14,7,90,12]
total_age=0
for age in ages:
    total_age +=age
print'total age ',total_age
print'average age:', total_age/len(ages)
print'len:',len(ages)



