immutable_var_tuple = 1,  2, 'a', 'b'
print(immutable_var_tuple)


#mutable_list_tuple = immutable_var_tuple + ('Modified',)
#print(mutable_list_tuple) # кортеж

mutable_list = [1,  2, 'a', 'b']
mutable_list = mutable_list + ['Modified']
print(mutable_list)
