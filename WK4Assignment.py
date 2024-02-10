#Dictionary
provision_store = {
    'Rice':'foreign', 'Beans': 'local', 'Spaghetti':'Local', 'Indomie' : 'Local'
}

#for loop to check items
for key, value in provision_store.items():
    if value =='foreign':
        print(f'{value} products are the products my doctor recommend')
        break
    else:
        print(f'{value} products are not good for my health')
        break
    #print(key)


#Fuction
def provision_store1():
    
    provision_store
    provision = input('Please enter the item you wanted to buy')
    if provision in provision_store:
        print(f'{provision} is available in our store')
        
    else:
        print(f'{provision} is not available at the moment , please check back later')
      
    return provision_store1
   #function call
provision_store1()
