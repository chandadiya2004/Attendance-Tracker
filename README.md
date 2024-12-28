![Attendance Tracker](https://pikaso.cdnpk.net/private/production/1303507632/render.jpeg?token=exp=1764633600~hmac=fd50ca7476a65444efffaf80c322a98bed38cfd28bb67fd255ff8d8f911f410f)

# Attendance Tracker
The Attendance Tracker is a Python-based graphical user interface (GUI) application that streamlines the process of tracking and managing student attendance. Developed using the Tkinter library, this program is designed to provide an intuitive platform for teachers or administrators to register students, record attendance, and maintain detailed records stored in CSV format.

# Key Features:
Secure User Authentication: The application starts with a login system that ensures only authorized users can access attendance data, providing an extra layer of security.

Effortless Student Registration: Teachers can easily add new students by inputting their names and unique IDs (UID). The system verifies that the UID is not duplicated, helping maintain an organized and consistent student database.

Daily Attendance Logging: Attendance can be marked every day for the registered students. The system automatically associates the attendance status with the current date for seamless tracking over time.

Dynamic Date Integration: Each time attendance is recorded, a new column is created in the CSV file corresponding to the current date. This dynamic approach makes it easier to manage historical attendance data.

Clear Attendance Indicators: Attendance is tracked with a simple system of 'P' for Present and 'A' for Absent, ensuring clear and easily understandable records.

Student Removal: If needed, students can be removed from the attendance list, keeping the roster current and up to date.

# Requirements:
Python 3.x

Tkinter (usually included with Python)

Pandas (install via pip install pandas)


This application is designed to simplify the administrative burden of tracking student attendance, while offering an easy-to-use and effective solution for educators and school administrators.
