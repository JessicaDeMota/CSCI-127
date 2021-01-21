#Jessica De Mota Munoz
#September, 18, 2019
#jessica.demotamunoz86@myhunter.cuny.edu

# we need a user input because we need to be able to run this program with any word.
word =input("Enter a message ")

#Whatever word we type we are going take the chr and that we get from it and translate it so we leave this as an open quotation to represent nothing
translation = " "
# we create a for loop to take each word through this loop
#this loop will take each index and convert it to its matching number in the ASCII table.
#we use the number and place it into an if else statement
for i in word:
    number = ord(i)
#the reason as to why we use 110 is because the characthers go up to 122 and we need to add each characther by 13.
# we only want to go up to our highest lowercase letter which is lowercase letter z in this case we put it into an if else statement for if lower than 110 we add by 13 if not we then subatract it by 13
    if (number<110):
        translation = translation+chr(number+13)
    else:
        translation = translation+chr(number-13)
#now we must print our word and our translation.        
print("Your word..")
print(translation)


    
    
