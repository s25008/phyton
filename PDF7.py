import tkinter as tk
from tkinter import messagebox
import sqlite3

# Połączenie z bazą danych
conn = sqlite3.connect('students.db')
c = conn.cursor()

# Utworzenie tabeli, jeśli nie istnieje
c.execute('''CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                grade REAL
            )''')
conn.commit()


def display_students():
    """Wyświetla dane dotyczące studentów w okienku."""
    result = c.execute("SELECT * FROM students")
    students = result.fetchall()

    # Wyczyszczenie aktualnych danych w okienku
    for widget in students_frame.winfo_children():
        widget.destroy()

    # Wyświetlenie nowych danych w okienku
    for student in students:
        label = tk.Label(students_frame, text=f"ID: {student[0]}, Name: {student[1]}, Grade: {student[2]}")
        label.pack()


def add_student():
    """Dodaje nowego studenta do bazy danych."""
    name = name_entry.get()
    grade = float(grade_entry.get())

    try:
        c.execute("INSERT INTO students (name, grade) VALUES (?, ?)", (name, grade))
        conn.commit()
        messagebox.showinfo("Success", "Student added successfully.")
        name_entry.delete(0, tk.END)
        grade_entry.delete(0, tk.END)
        display_students()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


def delete_student():
    """Usuwa studenta z bazy danych."""
    student_id = int(id_entry.get())

    try:
        c.execute("DELETE FROM students WHERE id=?", (student_id,))
        conn.commit()
        messagebox.showinfo("Success", "Student deleted successfully.")
        id_entry.delete(0, tk.END)
        display_students()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


def edit_student():
    """Edytuje dane studenta w bazie danych."""
    student_id = int(id_entry.get())
    name = name_entry.get()
    grade = float(grade_entry.get())

    try:
        c.execute("UPDATE students SET name=?, grade=? WHERE id=?", (name, grade, student_id))
        conn.commit()
        messagebox.showinfo("Success", "Student edited successfully.")
        id_entry.delete(0, tk.END)
        name_entry.delete(0, tk.END)
        grade_entry.delete(0, tk.END)
        display_students()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


# Tworzenie głównego okna aplikacji
root = tk.Tk()
root.title("Student Database")

# Ramka do wyświetlania studentów
students_frame = tk.Frame(root)
students_frame.pack()

# Pole tekstowe i etykiety dla ID studenta
id_label = tk.Label(root, text="ID:")
id_label.pack()
id_entry = tk.Entry(root)
id_entry.pack()

# Pole tekstowe i etykiety dla imienia studenta
name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

# Pole tekstowe i etykiety dla oceny studenta
grade_label = tk.Label(root, text="Grade:")
grade_label.pack()
grade_entry = tk.Entry(root)
grade_entry.pack()

# Przyciski do wykonywania operacji
add_button = tk.Button(root, text="Add Student", command=add_student)
add_button.pack()

delete_button = tk.Button(root, text="Delete Student", command=delete_student)
delete_button.pack()

edit_button = tk.Button(root, text="Edit Student", command=edit_student)
edit_button.pack()

# Wyświetlanie początkowych danych dotyczących studentów
display_students()

# Główna pętla aplikacji
root.mainloop()

# Zamknięcie połączenia z bazą danych po zamknięciu aplikacji
conn.close()
