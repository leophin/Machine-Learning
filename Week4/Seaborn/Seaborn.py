# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CxPfgNtSK_9nrJiUXbGccy5aTgXCeST7
"""

!wget https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv

"""1.Write a program to draw bar plot of sex against survived for a dataset given in the url"""

import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
df = sb.load_dataset('titanic')
sb.barplot(x = "sex", y = "survived", hue = "class", data = df)
plt.show()

!wget https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv

"""2.Write a program to draw a barplot to show count for a deck for a dataset given in the url"""

import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
df = sb.load_dataset('titanic')
sb.countplot(x='class', data = df )
plt.show()

!wget https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv

"""3.Write a program to draw a point plot for sex against survived for a dataset given in url"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
df = sb.load_dataset('titanic')
sb.pointplot(x = 'sex', y = 'survived', data= df,hue = "class")
plt.show()

!wget https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv

"""4.Write a program to draw a scatter plot of “day” against “total bill” for a dataset given in a url"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
df = sb.load_dataset('tips')
sb.stripplot(x="day", y="total_bill",data=df) 
plt.show()

!wget  https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv

"""5.Write a program to draw a violin plot of sex against day  for a  given dataset"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
df = sb.load_dataset('tips')
sb.violinplot(X="time", Y="sex",data=df) 
plt.show()

!wget https://github.com/mwaskom/seaborn-data/blob/master/iris.csv

"""6.Write a program to draw a violin plot of “species” against “sepal length” for a dataset given in a url"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
df = sb.load_dataset('iris')
sb.violinplot(x="species", y="sepal_length",data=df) 
plt.show()

!wget https://raw.githubusercontent.com/resbaz/r-novice-gapminder-files/master/data/gapminder-FiveYearData.csv

"""7.Write a program to draw a box plot of day by tips for a dataset given in a url"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
df = sb.load_dataset('tips')
sb.boxplot(x="day", y="tip",data=df) 
plt.show()

!wget         https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv

"""8.Write a program to draw a swarm plot of total bill against size  for a  given dataset"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
df = sb.load_dataset('tips')
sb.swarmplot(x='total_bill', y = 'size', data =df)
plt.show()

"""9. Write a program to draw swarm plot of “total bill” against day for a dataset given in url"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
df = sb.load_dataset('tips')
sb.swarmplot(x='total_bill', y = 'day', data =df)
plt.show()