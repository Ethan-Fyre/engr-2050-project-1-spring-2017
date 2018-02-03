# ENGR2050_01_jasayles.py
# Ethan Sayles
# Jan 25, 2017
# Purpose: Write a function that unzips a list into individual lists, and print them to the screen

'''
Method 1 for unzipping a list
@param The list to be unzipped
@return nothing
'''
def unzip(zipped_list):    
    output = []                            #The list to be printed
    for i in range(len(zipped_list[0])):   #Iterate through the zipped list and add the components to output
        for x in zipped_list:
            output.append(x[i])
        print (output)                     #Print the unzipped list and reset output to []
        output = []

'''
Method 2 for unzipping a list
@param The list to be unzipped
@return nothing
'''
def unzipper(zipped_list):
    output = []                            #The list whose components will be printed
    for i in range(len(zipped_list[0])):   #Make output = [[], [], ... ,[]] as many elements as items in each element of zipped_list
        output.append(list())
    for x in zipped_list:                  #Add each element to the corresponding element in output 
        for j in range(len(output)):
            output[j].append(x[j])
    for x in output:                       #Print the individual lists inslide utput
        print (x)
        
if __name__ == '__main__':
    print ('using method 1: ')
    unzip([(1, 'A', 'f'), (2, 'C', 'o'), (3, 'M', 'u'), (4, 'E', 'r')])
    print ('using method 2: ')
    unzipper([('T', 'I', 'F'),('H', 'S', 'U'), ('I', ' ', 'N'), ('S', ' ', '!')])
