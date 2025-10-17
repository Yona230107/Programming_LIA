# LIA deliverable_2
# Study of a dataset that has information about students:
# - their results
# - their sleep hours
# - class attendance +
# ----------------------Students ----------------------
# Roni Azoulay - 6299165
# Audrey Birmbaum - 6299087
# Yona Lasry - 6307274
import numpy as np
#question#2
hours_studied, sleep_hours, attendance_percent, previous_scores, exam_scores = np.loadtxt(
    "student_exam_scores.csv", 
    delimiter=",", 
    skiprows=1, 
    usecols=(1,2,3,4,5), 
    unpack=True
)
#question#3
total = 0
for score in exam_scores:
    total += score
    
avg_score = total/len(exam_scores)
print(avg_score)
# This code calculates the average score of the dataset.     
    
#question#4
#plot 1
import matplotlib.pyplot as plt
plt.scatter(hours_studied, exam_scores)
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.title("Exam Score vs. Study Hours")
plt.show()
# plot #2(pie chart)

minimum_hours_of_sleep=6
sleep_enough=0
sleep_not_enough=0
for sleep_hour in sleep_hours:
    if sleep_hour >=minimum_hours_of_sleep:
      sleep_enough+=1
    else:
      sleep_not_enough +=1
#plot pie chart
import matplotlib.pyplot as plt
labels=["sleep enough(more than 6 hours)"," sleep not enough(less than 6 hours)"]
values=[sleep_enough, sleep_not_enough]

plt.pie(values,labels=labels, autopct='%1.1f%%',colors=['green','red'])
plt.title("The hours slept by students")
plt.show()

#plot number 3: histogram
plt.hist(exam_scores)
plt.xlabel("Amount of students")
plt.ylabel("Exam scores of students")
plt.title("Exam scores of students")
plt.show()

#plot number 4: bar graph

plt.bar(hours_studied, exam_scores, color='green')
plt.xlabel("Hours studied")
plt.ylabel("Exam scores")
plt.title("Exam Scores vs Hours Studied")
plt.show()

# plot 5 (Scatter Plot)attendance_percent Vs.Exam Scores

import matplotlib.pyplot as plt
plt.scatter(attendance_percent, exam_scores)
plt.xlabel("attendance_percent")
plt.ylabel("Exam Score")
plt.title("Exam Score vs. Attendance Percent")
plt.grid(True)
plt.show()

# plot 6 (Multi-array line plot) Exam Score and Sleep Hours vs Hours Studied
import matplotlib.pyplot as plt
plt.plot(hours_studied, exam_scores, color='blue', linestyle='-', label='Exam Score')
plt.plot(hours_studied, sleep_hours, color='red', linestyle='--', label='Sleep Hours')
plt.title('Hours Studied vs Exam Score & Sleep Hours')
plt.xlabel('Hours Studied')
plt.ylabel('Exam Score(%) and Sleep Hours')
plt.legend()
plt.show()

# plot 7 
import csv
import matplotlib.pyplot as plt

# --- Step 1: Load data from CSV ---
exam_scores = []
attendance_percent = []

with open('student_exam_scores.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        exam_scores.append(float(row['exam_score']))
        attendance_percent.append(float(row['attendance_percent']))

# --- Step 2: Define bins (labels) and count how many students fall in each ---
attendance_labels = ['90–100%', '80–89%', '70–79%', '60–69%', '<60%']
attendance_counts = [0, 0, 0, 0, 0]

for percent in attendance_percent:
    if percent >= 90:
        attendance_counts[0] += 1
    elif percent >= 80:
        attendance_counts[1] += 1
    elif percent >= 70:
        attendance_counts[2] += 1
    elif percent >= 60:
        attendance_counts[3] += 1
    else:
        attendance_counts[4] += 1

# --- Step 3: Subplots (e) ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

# Left: Histogram of exam scores
ax1.hist(exam_scores, bins=10, color='skyblue', edgecolor='black')
ax1.set_title('Exam Score Distribution')
ax1.set_xlabel('Exam Score (%)')
ax1.set_ylabel('Frequency')

# Right: Bar chart of attendance ranges
ax2.bar(attendance_labels, attendance_counts, color='orange', edgecolor='black')
ax2.set_title('Attendance Percentage Ranges')
ax2.set_xlabel('Attendance Range')
ax2.set_ylabel('Number of Students')

plt.tight_layout()
plt.show()
