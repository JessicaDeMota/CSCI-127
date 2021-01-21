#Name: Jessica De Mota Munoz
#Email: Jessica.DeMotaMunoz86@myhunter.cuny.edu
#Date: October 31, 2019

import pandas as pd

csvFile = input('Enter CSV file name: ')
permits = pd.read_csv(csvFile)
total_permits = permits['EventID'].size 
print ("There were" ,total_permits, "film permits.")
print (permits['Borough'].value_counts())
print ("The five most popular filming locations were: ")
print (permits['ParkingHeld'].value_counts()[:5])
