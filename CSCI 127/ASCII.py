#Jessica De Mota Munoz
#jessica.demotamunoz86@myhunter.cuny.edu
#September,16,2019

#you need a variable that defines the user input in order to use it 
greeting = input("Put a message here to show user: ")
#a chatbox will appear that will allow you to write the statement that you want
print(greeting)
#once your print the greeting you shall strip a characther out in each
#this will allow you to strip each characther and convert it into the number it associates with
#each characther has a number assigned to iy
#this allows to store space allowing to encode new symbols.
#put it into a for loop so it can take out each characther. 
for c in greeting:
    print(ord(c))
                
