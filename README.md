# Student Performance Analytics System

**Mini Project for Python with AI**

| Student detail | Information |
|---|---|
| Student name | [Enter student name] |
| Roll number | [Enter roll number] |
| Class / department | [Enter class or department] |
| Institution | [Enter institution name] |
| GitHub repository | [Add GitHub repository URL] |

## Project objective

Analyze student marks and attendance data with Python, summarize class and subject performance, assign grades and pass/fail results, and identify the highest-performing students. The program demonstrates data handling and analysis concepts used in an introductory Python project.

## Technologies

- Python 3.10 or later
- pandas
- CSV for the input dataset

## Dataset description

The sample dataset contains 20 students. Its columns are `Student_ID`, `Name`, `Department`, `Python`, `Maths`, `English`, and `Attendance`. Each student’s total and average are calculated from the three subject marks. The supplied output reports marks out of 100 per subject. Keep the source CSV in the project folder as `student_performance.csv` (or update the filename in the script).

## Implementation

1. Load the student records from a CSV file into a pandas DataFrame.
2. Calculate each student's total and average marks across Python, Maths, and English.
3. Assign a letter grade and PASS/FAIL result according to the project's grading rules.
4. Calculate overall and subject averages, rank the top five students, and count pass/fail results.
5. Print a complete student report and summary to the terminal.

### Grading shown in the output

| Grade | Average range |
|---|---:|
| A+ | 90 and above |
| A | 80 to below 90 |
| B | 70 to below 80 |
| C | 60 to below 70 |
| D | 50 to below 60 |
| F | Below 50 |

The displayed results mark a student as FAIL when the average is below 50; otherwise the result is PASS. Dev's average is 48.67, grade F, and result FAIL. The resulting counts are 16 PASS and 4 FAIL.

## Key features

- Student-wise total and average marks
- Letter grades and pass/fail decisions
- Class high, low, and overall average
- Subject-wise averages
- Top five student ranking
- Pass/fail count and a complete report

## Output summary

| Measure | Result |
|---|---:|
| Students | 20 |
| Overall class average | 69.03 |
| Highest student average | 93.67 (Isha) |
| Lowest student average | 35.00 (Vihaan) |
| Python average | 68.30 |
| Maths average | 68.95 |
| English average | 69.85 |
| PASS / FAIL | 16 / 4 |

Top five: Isha (93.67, A+), Kiara (91.67, A+), Diya (90.00, A+), Meera (88.33, A), and Anika (87.67, A).

## Screenshots

### Student marks summary

![Terminal output showing student totals and averages](terminal-1.png)

### Grades, class performance, and subject averages

![Terminal output showing grades and class performance](terminal-2.png)

### Top five students and pass/fail statistics

![Terminal output showing ranking and pass/fail counts](terminal-3.png)

## Setup and run

1. Install Python 3.10 or later.
2. Clone the repository and open a terminal in the project folder.
3. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   # Windows PowerShell
   .venv\Scripts\Activate.ps1
   # macOS or Linux
   source .venv/bin/activate
   ```

4. Install the dependency:

   ```bash
   python -m pip install pandas
   ```

5. Place `student_performance.csv` beside the Python script.
6. Run the program (replace the example filename with the actual script name):

   ```bash
   python student_performance.py
   ```

## Final outcome

The system turns a small student marks dataset into a clear performance report. For this 20-student sample, the class average is 69.03; 16 students pass and 4 fail. The output highlights subject averages and the top five students for quick review.

## Challenges and learning

This project practices reading structured data, selecting and calculating numeric columns, formatting results, sorting students by performance, and applying consistent grade and result rules. A key validation lesson is to check summary counts against individual rows: Dev's 48.67 average must be reported as F / FAIL, which keeps the total at 16 PASS and 4 FAIL.

## GitHub submission checklist

- [ ] Add the Python source file and `student_performance.csv`.
- [ ] Include this README and the project documentation.
- [ ] Include the output screenshots or keep the relative image paths valid.
- [ ] Add the required project title and complete student/institution details.
- [ ] Replace `[Add GitHub repository URL]` with the final repository URL.
- [ ] Run the program from a clean environment and confirm the reported totals.
- [ ] Check that no private data or unrelated files are committed.
- [ ] Commit and push all required files; verify the repository opens correctly.
