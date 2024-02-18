import pandas as pd
import numpy as np
import seaborn as sns
import statistics as st
import matplotlib as plt

student_record = {
    'Names' : ['Nanbal', 'Dafam', 'Felix', 'Abel' , 'Ruth', 'Maryam', 'Hamza'],
    'Department': ['Computer Science', 'Computer Science', 'Physics', 'Computer Science' , 'Mathematics', 'Chemistry', 'Mathematics'],
    'Scores': [70, 80, 70, 70, 40, 50, 30]
    
    
}
#Data frame

student_records = pd.DataFrame (data = student_record, columns= ['Names', 'Department', 'Scores'] )
print(student_records)
np.mean(student_records['Scores'])
np.median(student_records['Scores'])
st.mode(student_records['Scores'])
sns.scatterplot( data = student_records, y='Scores' , x='Department')

np.std(student_records['Scores'])
import pandas as pd

employee_data = {
    'Name':['Adamu', 'Bashir', 'Charles', 'Dauda', 'Evelyn'],
    'Age':[25, 30, 35, 40, 45],
    'Salary': [50000, 66000, 75000, 100000, 62000]
    
    
}
employee_data1 = pd.DataFrame(employee_data)
print(employee_data1)
summary_stats = employee_data1.describe()
print(summary_stats)
mean_salary = employee_data1['Salary'].mean()
median_age = employee_data1['Age'].median()
mode_name = employee_data1['Name'].mode()

print('Mean Salary:' , mean_salary)
print('Median Age:' , median_age)
#print('Mode Name:' , mode_name)

from scipy import stats
import matplotlib.pyplot as plt 

Age, Salary = stats.pearsonr(employee_data1["Age"], employee_data1["Salary"])
# Visualize correlation
import seaborn as sns
sns.lmplot(x="Age", y="Salary", data=employee_data1, ci=None)
#plt.show()

employee_data1.plot(x='Name', y='Salary', kind='bar')
plt.xlabel('Name')
plt.ylabel('Salary')
plt.show()
