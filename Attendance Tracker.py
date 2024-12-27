import tkinter as tk
from tkinter import messagebox
import pandas as pd
import os
from datetime import datetime

CSV_FILE = "students.csv"

# Function to handle the login system
def login():
    if username_entry.get() == "a" and password_entry.get() == "a":
        login_window.destroy()
        show_main_window()
    else:
        messagebox.showerror("Login Failed", "Invalid Username or Password")

# Main window of the application
def show_main_window():
    global main_window
    main_window = tk.Tk()
    main_window.title("Attendance Tracker")
    main_window.geometry("770x250+380+250")
    main_window.resizable(False, False)

    # Button for "Register a student"
    tk.Button(main_window, text="Register a student", width=20, command=register_student,
              font=('comicsansms', 15, "bold"), bg="#4CAF50", fg="white",
              activebackground="#45a049", activeforeground="white", bd=5, relief="raised").grid(row=0, column=1, pady=10)

    # Button for "Mark Attendance"
    tk.Button(main_window, text="Mark Attendance", width=20, command=mark_attendance,
              font=('comicsansms', 15, "bold"), bg="#2196F3", fg="white",
              activebackground="#1976D2", activeforeground="white", bd=5, relief="raised").grid(row=1, column=0, pady=10)

    # Button for "Remove a student"
    tk.Button(main_window, text="Remove a student", width=20, command=remove_student,
              font=('comicsansms', 15, "bold"), bg="#f44336", fg="white",
              activebackground="#e57373", activeforeground="white", bd=5, relief="raised").grid(row=1, column=2, pady=10)

    # Button for exit
    tk.Button(main_window, text="Exit", width=20, command=main_window.quit,
              font=('comicsansms', 15, "bold"), bg="#FF9800", fg="white",
              activebackground="#FF5722", activeforeground="white", bd=5, relief="raised").grid(row=2, column=1, pady=10)

    main_window.mainloop()

# Register student's window
def register_student():
    register_window = tk.Toplevel(main_window)
    register_window.title("Register a Student")
    register_window.geometry("400x250+380+250")
    register_window.resizable(False, False)

    # Label for 'Student Name'
    tk.Label(register_window, text="Student Name:", font=('comicsansms', 12, 'bold')).grid(row=0, column=0, padx=10, pady=10, sticky="w")

    # Entry for student name
    name_entry = tk.Entry(register_window, font=('comicsansms', 12), bd=3, relief="sunken")
    name_entry.grid(row=0, column=1, padx=10, pady=10)

    # Label for 'UID'
    tk.Label(register_window, text="UID:", font=('comicsansms', 12, 'bold')).grid(row=1, column=0, padx=10, pady=10, sticky="w")

    # Entry for UID
    uid_entry = tk.Entry(register_window, font=('comicsansms', 12), bd=3, relief="sunken")
    uid_entry.grid(row=1, column=1, padx=10, pady=10)

    # Function to save the new student
    def save_student():
        name = name_entry.get()
        uid = uid_entry.get()
        if name and uid:
            if os.path.exists(CSV_FILE):
                df = pd.read_csv(CSV_FILE, dtype={'Student Name': str, 'UID': str})
            else:
                # Create DataFrame with correct types
                df = pd.DataFrame(columns=['Student Name', 'UID'], dtype=str)

            if uid in df['UID'].values:
                messagebox.showerror("Error", "UID already exists")
            else:
                new_student = pd.DataFrame({'Student Name': [name], 'UID': [uid]}, dtype=str)
                df = pd.concat([df, new_student], ignore_index=True)
                df.to_csv(CSV_FILE, index=False)
                messagebox.showinfo("Success", "Student Registered Successfully")
                register_window.destroy()
        else:
            messagebox.showerror("Error", "Please fill in both fields")

    # Button for saving the new student information
    save_button = tk.Button(register_window, text="Save", font=('comicsansms', 12, "bold"),
                             bg="#4CAF50", fg="white", activebackground="#45a049",
                             activeforeground="white", bd=5, relief="raised", width=15,
                             command=save_student)
    save_button.grid(row=2, column=1, pady=20)

# Mark attendance
def mark_attendance():
    attendance_window = tk.Toplevel(main_window)
    attendance_window.title("Mark Attendance")
    attendance_window.geometry("350x400+380+200")
    attendance_window.resizable(False, False)

    if os.path.exists(CSV_FILE):
        global df  # Make df a global variable to access it in save_attendance function
        df = pd.read_csv(CSV_FILE, dtype={'Student Name': str, 'UID': str})
    else:
        messagebox.showerror("Error", "No student records found.")
        attendance_window.destroy()
        return

    if df.empty:
        messagebox.showerror("Error", "No student records found.")
        attendance_window.destroy()
        return

    current_date = datetime.now().strftime("%Y-%m-%d")

    # Check if the current date column exists; if not, create it
    if current_date not in df.columns:
        df[current_date] = ""  # Initialize the date column

    tk.Label(attendance_window, text="Student", font=('comicsansms', 15, "bold")).grid(row=0, column=0, padx=10)
    tk.Label(attendance_window, text="Present", font=('comicsansms', 15, "bold")).grid(row=0, column=1)
    tk.Label(attendance_window, text="Absent", font=('comicsansms', 15, "bold")).grid(row=0, column=2)

    attendance_vars = []
    
    for index, row in df.iterrows():
        tk.Label(attendance_window, text=row['Student Name'],padx=10, font=('comicsansms', 12)).grid(row=index + 1, column=0)

        var = tk.StringVar(value=row[current_date] if row[current_date] else None)  # Default to 'A' (Absent) if empty
        attendance_vars.append(var)

        # Create radio buttons for present and absent based on the current attendance
        tk.Radiobutton(attendance_window, text="", variable=var, value="P").grid(row=index + 1, column=1)
        tk.Radiobutton(attendance_window, text="", variable=var, value="A").grid(row=index + 1, column=2)

        # Set the selected state based on the attendance value
        if var.get() == "P":
            tk.Radiobutton(attendance_window, text="", variable=var, value="P", selectcolor="green").select()
        else:
            tk.Radiobutton(attendance_window, text="", variable=var, value="A", selectcolor="red").select()

    def save_attendance():
        for index, var in enumerate(attendance_vars):
            df.at[index, current_date] = var.get()  # Save attendance to the current date column

        # Save the DataFrame back to CSV
        df.to_csv(CSV_FILE, index=False)
        messagebox.showinfo("Success", "Attendance Saved Successfully")
        attendance_window.destroy()

    tk.Button(attendance_window, text="Save", font=('comicsansms', 15, "bold"), command=save_attendance).grid(row=len(df) + 1, column=0, columnspan=3, pady=10)

# Remove a student
def remove_student():
    remove_window = tk.Toplevel(main_window)
    remove_window.title("Remove Student")
    remove_window.geometry("270x400+500+200")
    remove_window.resizable(False, False)

    if os.path.exists(CSV_FILE):
        df = pd.read_csv(CSV_FILE, dtype={'Student Name': str, 'UID': str})
    else:
        messagebox.showerror("Error", "No student records found.")
        remove_window.destroy()
        return

    if df.empty:
        messagebox.showerror("Error", "No student records found.")
        remove_window.destroy()
        return

    for index, row in df.iterrows():
        tk.Label(remove_window, text=row['Student Name'], font=('comicsansms', 12)).grid(row=index, column=0)
        tk.Button(remove_window, text="Remove",
                  command=lambda index=index: remove_student_from_list(index)).grid(row=index, column=1)

    def remove_student_from_list(index):
        df.drop(index=index, inplace=True)
        df.reset_index(drop=True, inplace=True)
        df.to_csv(CSV_FILE, index=False)
        messagebox.showinfo("Success", "Student Removed Successfully")
        remove_window.destroy()
        remove_student()

    remove_window.mainloop()

# Main program starts here
login_window = tk.Tk()
login_window.title("Login")
login_window.geometry("400x200+550+250")
login_window.resizable(False, False)

# Label for username
tk.Label(login_window, text="Username:", font=('comicsansms', 15, "bold")).grid(row=0, column=0, padx=10, pady=10)

# Entry for username
username_entry = tk.Entry(login_window, font=('comicsansms', 12), bd=3, relief="sunken")
username_entry.grid(row=0, column=1, padx=10, pady=10)

# Label for password
tk.Label(login_window, text="Password:", font=('comicsansms', 15, "bold")).grid(row=1, column=0, padx=10, pady=10)

# Entry for password
password_entry = tk.Entry(login_window, show="*", font=('comicsansms', 12), bd=3, relief="sunken")
password_entry.grid(row=1, column=1, padx=10, pady=10)

# Login button
tk.Button(login_window, text="Login", font=('comicsansms', 15, "bold"),
          bg="#4CAF50", fg="white", activebackground="#45a049",
          activeforeground="white", bd=5, relief="raised", command=login).grid(row=2, columnspan=2, pady=10)

login_window.mainloop()
