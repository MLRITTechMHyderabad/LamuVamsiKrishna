import pandas as pd

data = {
    'Student': ['John', 'Sara', 'Mike', 'Anna', 'David', 'Emily', 'Chris', 'Sophia'],
    'Subject': ['Math', 'Science', 'Math', 'Science', 'Math', 'Science', 'Math', 'Science'],
    'Marks': [85, 72, 90, 65, 78, 88, 92, 55],
    'Attendance': [92, 80, 95, 70, 85, 90, 97, 60]
}

df = pd.DataFrame(data)
print(df)

#1.	Find the average marks for each subject.
avg=df.groupby("Subject")["Marks"].mean()
print(avg)


#2.	Identify students who scored above 85 and had less than 90% attendance
ss=df[(df["Marks"]>85) & (df["Attendance"]<90)]
print(ss)


# 3: Add a "Grade" column based on marks
def assign_grade(mark):
    if mark >= 90:
        return 'A'
    elif 80 <= mark < 90:
        return 'B'
    elif 70 <= mark < 80:
        return 'C'
    else:
        return 'D'

df['Grade'] = df['Marks'].apply(assign_grade)
print(df)


# 4.Count how many students received each grade.
grade_counts = df['Grade'].value_counts()
print(grade_counts)


# 5.Find out if attendance affects performance by calculating the correlation between marks and attendance.
correlation = df['Marks'].corr(df['Attendance'])
print(correlation)