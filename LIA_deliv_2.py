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
import matplotlib.pyplot as plt
#question#2
hours_studied, sleep_hours, attendance_percent, previous_scores, exam_scores = np.loadtxt(
    "student_exam_scores.csv", 
    delimiter=",", 
    skiprows=1, 
    usecols=(1,2,3,4,5), 
    unpack=True
)
#question#3
#This code calculates the average score of the dataset by taking the total of the scores through the loop and by dividing it by the length.
total = 0
for score in exam_scores:
    total += score
    
avg_score = total/len(exam_scores)
print(avg_score)
    
    
#Question#4
#plot_1
#This code creates a scatter plot that shows the correlation between the exam scores and hours studied.
#display

plt.scatter(hours_studied, exam_scores)
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.title("Exam Score vs. Study Hours")
plt.show()
# plot_2( pie chart)
#This codes creates a pie chart that shows the percentages of students that have more or less than 6 hours of sleep, those who sleep enough and those who don't
minimum_hours_of_sleep=6
sleep_enough=0
sleep_not_enough=0
for sleep_hour in sleep_hours:
    if sleep_hour >=minimum_hours_of_sleep:
      sleep_enough+=1
    else:
      sleep_not_enough +=1
#display 

labels=["sleep enough(more than 6 hours)"," sleep not enough(less than 6 hours)"]
values=[sleep_enough, sleep_not_enough]

plt.pie(values,labels=labels, autopct='%1.1f%%',colors=['green','red'])
plt.title("The hours slept by students")
plt.show()

#plot_3
#This code plots a histogram that shows the the amount of students with specific scores
#display
plt.hist(exam_scores)
plt.xlabel("Amount of students")
plt.ylabel("Exam scores of students")
plt.title("Exam scores of students")
plt.show()

#plot_4
#This codes creates a bar graph that shows the correlation between hours studied. The same arrays were used previously to plot a scatter graph, clearly the scatter plot is a better option.

plt.bar(hours_studied, exam_scores, color='green')
plt.xlabel("Hours studied")
plt.ylabel("Exam scores")
plt.title("Exam Scores vs Hours Studied")
plt.show()


# plot_5 (Scatter Plot)
#This codes creates a plot showing the corelation the attendance_percent and the exam_scores 



plt.scatter(attendance_percent, exam_scores)
plt.grid(True)
plt.xlabel("attendance_percent")
plt.ylabel("Exam Score")
plt.title("Exam Score vs. Attendance Percent")
plt.show()


# plot_6 
# This code plots a multi-array line plot and shows the correlation between the sleep hours and exam scores vs the hours studied.
plt.plot(hours_studied, exam_scores, color='blue', linestyle='-', label='Exam Score')
plt.plot(hours_studied, sleep_hours, color='red', linestyle='--', label='Sleep Hours')
plt.title('Hours Studied vs Exam Score & Sleep Hours')
plt.xlabel('Hours Studied')
plt.ylabel('Exam Score(%) and Sleep Hours')
plt.legend()
plt.show()

# plot_7 
# This code creates 2 subplots plots side by side. It shows how exam scores are distributed and how students attendance level compare. 
import csv
#   Load data from CSV
exam_scores = []
attendance_percent = []

with open('student_exam_scores.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        exam_scores.append(float(row['exam_score']))
        attendance_percent.append(float(row['attendance_percent']))

#  Step 2: Define bins (labels) and count how many students fall in each 
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

#  Step 3: Subplots (e) 
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




