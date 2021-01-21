#Jessica De Mota Munoz 
#jessica.demotamunoz86@myhunter.cuny.edu
#November 7th 2019
#this program displays attendance

import pandas as pd
import matplotlib.pyplot as plt



present = input("Enter name of input file: ")
out = input("Enter name of output file: ")
readPresent = pd.read_csv(present)
readPresent["Date"] = pd.to_datetime(readPresent["Date"].apply(str))
readPresent["% Attending"] = 100*readPresent["Present"]/readPresent["Enrolled"]
readPresent.plot(x = "Date", y = "% Attending")
fig = plt.gcf()
fig.savefig(out)
