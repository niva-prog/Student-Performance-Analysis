import pandas as pd
import matplotlib.pyplot as plt

# 1. Load student data
data = pd.read_csv("student_data.csv")

# 2. Display data
print("\n--- Student Performance Data ---")
print(data)

# 3. Average marks
average = data["Exam_Mark"].mean()
print("\nAverage Exam Mark:", average)

# 4. Highest and lowest marks
highest = data["Exam_Mark"].max()
lowest = data["Exam_Mark"].min()

print("Highest Exam Mark:", highest)
print("Lowest Exam Mark:", lowest)

# 5. Pass and fail count
pass_count = (data["Exam_Mark"] >= 50).sum()
fail_count = (data["Exam_Mark"] < 50).sum()

print("\nPassed Students:", pass_count)
print("Failed Students:", fail_count)

# 6. Students needing improvement
improvement = data[data["Exam_Mark"] < 60]

print("\n--- Students Needing Improvement ---")
print(improvement[["Student_ID", "Exam_Mark"]])

# 7. ONE Colorful Bar Chart
plt.figure(figsize=(8, 5))

plt.bar(
    data["Student_ID"],
    data["Exam_Mark"],
    color=["red", "blue", "green", "orange", "purple"],
    edgecolor="black"
)

plt.xlabel("Student ID")
plt.ylabel("Exam Marks")
plt.title("Student Exam Performance")

plt.grid(axis="y")
plt.show()

# 8. Conclusion
print("\n--- Project Conclusion ---")
print("This project analyzes student performance using")
print("attendance, study hours, assignment marks, and exam marks.")
print("It helps identify high-performing students")
print("and students who need academic improvement.")

print("\nProject completed successfully!")
