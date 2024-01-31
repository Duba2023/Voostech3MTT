#List of Students

students_data = [
    ( 'John', '100', 19, 'Computer Science') ,
     ( 'ALi', '200', 20, 'Mathmatics') ,
     ( 'Mary', '100', 19, 'Biology')
    
]

type(students_data)

# Printing the first index in the students list
students_data[0]

#converting list to set
for data in students_data:
    data = set(data)
    print(type(data))

#Removing Mary from the set
data.remove('Mary')

# Adding Marry to the Set
data.add('Mary')

# Adding a new to row to the set
students_data.insert(3, ['Abba' , '500Level', 24, 'Mathmatics'] )

 for tupleO in students_data:
        print(*tupleO)

# Using a Heading for all the datasets in the tuples
heading = [ 'Names' ,  'Level' ,'Age' , 'Department']
print(f' {heading[0] : <10} {heading[1] : <10} {heading[2] : <10} {heading[3] : <10}')
for tupleO in students_data:
        print(f' {tupleO[0] : <10} {tupleO[1] : <10} {tupleO[2] : <10}  {tupleO[3] : <10}')

#Set of CLothes and Shoes
clothes = {
    'Jeans', 'T-shirt' , 'Polo Shirt', 'Shadda', 'Abaya Gown'
}

shoes = {
    'Sandals', ' Skin Cover Shoe', 'Canvas', 'Slippers'
}

#Union of the two existing sets
wears =clothes.union(shoes)

#converting sets into list
wears = list(wears)


# An online store   
    
wear = input("Search for our Wears before placing an order!")
#Checking whether the wear you are looking for exist
if wear in wears:
    print(f'We have {wear} in our Shop, you can place your order')
        
else:
    print(f'OOPS !! {wear} is not ready for now, please check back later')
    #exit(1)
