# with open('./about.txt','w') as file:
#     file.write('I am Khant Min Htet')
    
# #w=write
# #a=

# #other work

# with open('./about.txt','a') as file:
#     file.write('\n I am 22 years old')

list=['I am Khant Min Htet','\n I am 22 years old']

with open('./about.txt','a') as file:
    file.writelines(list)
    
