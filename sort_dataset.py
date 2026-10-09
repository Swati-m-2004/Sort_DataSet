"""
Task 20: Sort Dataset
Internship Track: AI & ML

Demonstrates:
1. Ascending sorting
2. Descending sorting
3. Sorting numerical and categorical columns
4. Sorting by multiple columns
5. Saving sorted datasets to CSV files

Requirements:
    pip install pandas

Run:
    python sort_dataset.py
"""

import pandas as pd


def main():
    # Sample employee dataset (embedded directly in the program).
    data = {
        "Employee_ID": [105, 102, 109, 101, 107, 104, 103, 108, 106, 110],
        "Name": [
            "Swati", "Arun", "Meera", "Kiran", "Priya",
            "Ravi", "Ananya", "Rahul", "Divya", "Sanjay"
        ],
        "Department": [
            "AI", "HR", "IT", "IT", "AI",
            "HR", "IT", "AI", "HR", "IT"
        ],
        "Age": [22, 25, 24, 23, 26, 21, 24, 27, 22, 25],
        "Salary": [42000, 35000, 51000, 48000, 46000, 33000, 52000, 45000, 37000, 49000],
        "Performance_Score": [88, 76, 92, 85, 90, 72, 95, 87, 80, 89],
    }

    df = pd.DataFrame(data)

    print("=" * 72)
    print("TASK 20: SORT DATASET")
    print("=" * 72)
    print("\nOriginal Dataset:")
    print(df.to_string(index=False))

    # 1. Ascending sort: numerical column (Age, smallest to largest).
    age_ascending = df.sort_values(by="Age", ascending=True)
    print("\n\n1. Employees sorted by Age (Ascending):")
    print(age_ascending.to_string(index=False))
    age_ascending.to_csv("employees_age_ascending.csv", index=False)

    # 2. Descending sort: numerical column (Salary, largest to smallest).
    salary_descending = df.sort_values(by="Salary", ascending=False)
    print("\n\n2. Employees sorted by Salary (Descending):")
    print(salary_descending.to_string(index=False))
    salary_descending.to_csv("employees_salary_descending.csv", index=False)

    # 3. Ascending sort: categorical/text column (Name, A to Z).
    name_ascending = df.sort_values(by="Name", ascending=True)
    print("\n\n3. Employees sorted by Name (A to Z):")
    print(name_ascending.to_string(index=False))
    name_ascending.to_csv("employees_name_ascending.csv", index=False)

    # 4. Descending sort: categorical/text column (Department, Z to A).
    department_descending = df.sort_values(by="Department", ascending=False)
    print("\n\n4. Employees sorted by Department (Z to A):")
    print(department_descending.to_string(index=False))
    department_descending.to_csv("employees_department_descending.csv", index=False)

    # 5. Multi-column sort: Department A-Z, then Salary highest-to-lowest.
    multiple_columns = df.sort_values(
        by=["Department", "Salary"],
        ascending=[True, False]
    )
    print("\n\n5. Employees sorted by Department (A-Z), then Salary (High to Low):")
    print(multiple_columns.to_string(index=False))
    multiple_columns.to_csv("employees_multi_column_sorted.csv", index=False)

    print("\n\nDone! Five sorted CSV files have been saved in the current folder.")


if __name__ == "__main__":
    main()
