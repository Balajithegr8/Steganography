#importing pyplot which is important for plotting the graph
from matplotlib import pyplot as plt

# function to split the list in half in which former half will be x coordinates and latter half will be y coordinated 

def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]

#dictionary to encrypt the message

encrypter = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26} 

#dictionary to decrypt the message

decrypter = {1:'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'F', 7:'G', 8:'H', 9:'I', 10:'J', 11:'K', 12:'L', 13:'M', 14:'N', 15:'O', 16:'P', 17:'Q', 18:'R', 19:'S', 20:'T', 21:'U', 22:'V', 23:'W', 24:'X', 25:'Y', 26:'Z'}

temp = []
untemp=[]

message = input("Give the phrase you want to encrypt in an graph : ")

#Making all the text in upper case

message = message.upper()

for i in range(len(message)):
    if (message[i].isalpha() == True):          #checking if all the text is aplhabets only
        temp.append(encrypter[message[i]])      # appending the encrpted msg in temp

if(len(temp)%2 ==0):
    X_values, Y_values = split_list(temp)       #calling split_list function 

else:
    last=temp.pop()                             # popping the last element of the odd len list to make it even
    X_values, Y_values = split_list(temp)

lines=plt.plot(X_values,Y_values)               #plotting the graph with the x and y values
 
plt.show()                                      #displaying the graph

k=lines[0].get_data()                           #retiving the data from the graph

l=[]

for i in range(len(k)):
    for o in range(len(k[i])):    
        l.append(k[i][o])

for i in range(len(l)):
    untemp.append(decrypter[l[i]])              #decrypting the encrypted message
print(" ")
print("The decoded message is :")
for i in range(len(untemp)):
    print(untemp[i],end="")                     #printing the actual message

if((len(message)- message.count(" "))%2 != 0):
    print(chr(last+64))                         #printing the last character which was popped off the odd len list 


#Thanks for reading this program
