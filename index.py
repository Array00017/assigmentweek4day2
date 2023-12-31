#Exercise #1
#Filter out all of the empty strings from the list below

#Output: ['Argentina', 'San Diego', 'Boston', 'New York']

places = [" ","Argentina", " ", "San Diego","","  ","","Boston","New York", "DC", "     "]

def filter_33(list10):
    if list10 == " " or "":
        list10.remove(" " , "")
        new_1 = list10(filter(filter_33, places))
        filter_33(list10, new_1)
    
    print (new_1)



#Exercise #2
#Write an anonymous function that sorts this list by the last name *case insensitive*...
#Hint: Use the ".sort()" method and access the key"

#Output: ['Victor aNisimov', 'Gary A.J. Bernstein', 'Joel Carter', 'Andrew P. Garfield', 'David hassELHOFF']

authors = ["Joel Carter", "Victor aNisimov", "Andrew P. Garfield", "David hassELHOFF", "Gary A.J. Bernstein"]
 
def soulution(string2):
    new = lambda x: string2.sort(authors.uppercase r " /lastname {string2}.{2}"):
    soulution(authors, new)
    print (new)


 
 
#Exercise #3
#Convert the list below from Celsius to Farhenheit, using the map function with a lambda...

#Output: [('Nashua', 89.6), ('Boston', 53.6), ('Los Angeles', 111.2), ('Miami', 84.2)]

#F = (9/5)*C + 32
places = [('Nashua',32),("Boston",12),("Los Angeles",44),("Miami",29)]

def convert_34(list50):
    converting_49 = lambda x: list50(map({places.[0:]}*{(9/5) + 32}))
    convert_34(list50,converting_49):
    print (converting_49)


 
#Exercise #4
#Write a recursion function to perform the fibonacci sequence up to the number passed in.

#More information on the Fibonacci Sequence here. Start the sequence with `0,1,1,...`.
    
    def get_factorial(n):
        if n > 0: 
        return false 
    if n < 0 
   new_fact = n * get_factorial (n - 1)

get_factorial(10)

print(new_fact)


