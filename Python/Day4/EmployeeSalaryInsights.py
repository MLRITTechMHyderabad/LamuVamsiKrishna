import pandas as pd

data = {
    'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hannah'],
    'Department': ['HR', 'IT', 'IT', 'HR', 'Finance', 'Finance', 'IT', 'HR'],
    'Age': [25, 32, 29, 41, 37, 45, 26, 38],
    'Salary': [50000, 70000, 65000, 80000, 75000, 90000, 62000, 85000],
    'Experience': [2, 7, 5, 15, 10, 20, 3, 12]
}

df = pd.DataFrame(data)

print(df)

#1.	Find the average salary of employees in each department.
avg=df.groupby("Department")["Salary"].mean()
print(avg)

#1.	Find the average salary of employees in each department.
high=df.groupby("Department")["Salary"].max()
print(high)

#3.	Determine how many employees have more than 5 years of experience and earn a salary above $65,000.
ex=df[ (df["Experience"]>5) & (df["Salary"]>65000) ]
print(ex)


#4.	Add a new column “Seniority”:
# df["Seniority"]=["Junior","Mid-Level","Senior"]
def determine_seniority(exp):
    if exp < 5:
        return 'Junior'
    elif 5 <= exp <= 10:
        return 'Mid-Level'
    else:
        return 'Senior'

df['Seniority'] = df['Experience'].apply(determine_seniority)
print(df)

#5.	Sort employees by salary in descending order, showing only “IT” department employees.
sort=df[(df["Department"]=="IT")]
s=(sort.sort_values(by='Salary',ascending=False))
print(s)
