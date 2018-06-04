'''
Created on Jun 3, 2018

@author: jwang02
'''
import matplotlib.pyplot as plt
from htmltableparser import HTMLTableParser
    
url = "https://www.fantasypros.com/nfl/reports/leaders/qb.php?year=2015"

hp = HTMLTableParser()
table = hp.parse_url(url)[0][1]

print table.to_string()

plt.figure()
avg=table['Avg'].values
plt.hist(avg, bins = 50)
plt.title('Average QB Points Per Game in 2015')
plt.show()

