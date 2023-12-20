import pandas as pd

x = {'Student': ['David','Samuel', 'Terry', 'Evan'], 'Age': [27, 24, 22, 32], 'Country': ['UK', 'Canada', 'China', 'USA'],
      'Course':['Python', 'Data Structures', 'Machine Learning', 'Web Development'],'Marks':[85,72,89,76]}

#casting the dictionary to a DataFrame
df = pd.DataFrame(x)

#display the result df
print(df)
b=df[['Marks']]
print(b)
c=df[['Country','Course']]
print(c)
x=df['Student']
print(x)
print(df.iloc[0, 0])       #index selection
df2=df
df2=df2.set_index("Student")    #set index instead of 0 1 2...
print(df2.loc['David', 'Country'])   #str selection
print(df2.iloc[0,2])

print(df.iloc[0:2,0:3])   # 0:2 index > 0 1
print(df.loc[0:2,'Age':'Course']) # 0:2 not index is a number of colum > 3 elements 0 1 2
print(df.loc[2:3,'Student':'Country'])


