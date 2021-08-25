user = {'name' : 'Ahsan', 'age' : 23}
print(user)
user1 = dict(name = 'Ahsan', age = '23')
print(user1)
user_info = {
    'name' : 'Ahsan',
    'age' : 23,
    'fav_mov' : ['Marjawan', 'Doorbeen'],
    'fav_food' : ['Pizza', 'Zinger']}

#add data in dictionary
user_info['fav_song'] = ['kal ho na ho']
print(user_info)

if "Ahsan" in user_info.values():
    print("present")
else:
    print("Not Present")

#values print krwaye ga keys ki
for i in user_info.values():
    print(i)


# items(keys and values) print krwaye ga tuple ki form me
for i,j in user_info.items():
    print(f"Key is '{i}' and value is '{j}'")




# remove data from dictionary
popped_item = user_info.pop('name')
print(f"popped item is {popped_item}")
print(user_info)

user_info['name'] = 'Ahsan'
more_info = dict(state = 'Punjab', Hobbies = ['footbal', 'Coding'])

user_info.update(more_info)
for n,m in user_info.items():
    print(F"{n} : {m}")