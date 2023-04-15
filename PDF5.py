import csv

students = {}

# zad1
with open('students.txt') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        email, first_name, last_name, points = row[:4]
        if email not in students:
            students[email] = {'email': email,
                               'first_name': first_name,
                               'last_name': last_name,
                               'points': int(points),
                               'status': 'NONE'}
        if len(row) > 4:
            students[email]['status'] = row[4]

print(students)

# zad2
def liczenie_oceny():
    for email, data in students.items():
        if data['status'] not in ['GRADED', 'MAILED']:
            if data['points'] <= 50:
                grade = 2
            elif data['points'] <= 60:
                grade = 3
            elif data['points'] <= 70:
                grade = 3.5
            elif data['points'] <= 80:
                grade = 4
            elif data['points'] <= 90:
                grade = 4.5
            else:
                grade = 5
        students[email]['status'] = 'GRADED'
        students[email]['grade'] = grade


print(students)


# zad3
def add_student(email, first_name, last_name, points):
    if email in students:
        print('Student o takim adresie email już istnieje!')
    else:
        students[email] = {'email': email,
                           'first_name': first_name,
                           'last_name': last_name,
                           'points': int(points),
                           'status': '',
                           }

def remove_student(email):
    if email in students:
        del students[email]
    else:
        print('Nie ma studenta o takim adresie email!')

add_student('jan.kowalski@stud.uni.edu.pl', 'Jan', 'Kowalski', 75)

remove_student('anna.nowak@stud.uni.edu.pl')

liczenie_oceny()

print(students)

# zad4
import smtplib

def send_email(email, grade):
    if email in students and students[email]['status'] != 'MAILED':
        smtp_server = 'smtp.gmail.com'
        port = 587
        sender_email = 'adamowskia696@gmail.com'
        sender_password = 'omaanlvbbmjlmoks'
        receiver_email = email
        message = f'Szanowny/a {students[email]["first_name"]} {students[email]["last_name"]},\n\n' \
                  f'Zostanie Ci wystawiona ocena {grade} z przedmiotu Podstawy Programowania Python.\n\n' \
                  f'Pozdrawiam,\n' \
                  f'XYZ'
        try:
            server = smtplib.SMTP(smtp_server, port)
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, message)
            server.quit()
            students[email]['status'] = 'MAILED'
            print(f'Wysłano email na adres {email}')
        except:
            print('Wystąpił błąd podczas wysyłania emaila!')


print(students)

def save_students_to_file(students):
    with open('students.txt', mode='w') as file:
        for email, data in students.items():
            file.write(f'{email},{data["first_name"]},{data["last_name"]},{data["grade"]},{data["status"]}\n')

for email in students:
    if students[email]['status'] != 'MAILED':
        send_email(students[email]['email'], students[email]["grade"])
        save_students_to_file(students)
