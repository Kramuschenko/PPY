import smtplib
from email.mime.text import MIMEText

def read_file(filename):
    data = {}
    with open(filename, 'r') as file:
        for line in file:
            fields = line.strip().split(',')

            if len(fields) == 4:
                email, first_name, last_name, points = fields
                student_data = {'email': email, 'first_name': first_name, 'last_name': last_name, 'points': points,
                                'grade': '', 'status': ''}

            elif len(fields) == 5:
                email, first_name, last_name, points, grade = fields
                student_data = {'email': email, 'first_name': first_name, 'last_name': last_name, 'points': points,
                                'grade': grade, 'status': ''}

            elif len(fields) == 6:
                email, first_name, last_name, points, grade, status = fields
                student_data = {'email': email, 'first_name': first_name, 'last_name': last_name, 'points': points,
                                'grade': grade, 'status': status}

            else:
                continue
            data[email] = student_data
    return data


def grade_students(data):
    for email, student_data in data.items():
        if student_data['status'] not in ['GRADED', 'MAILED']:
            points = int(student_data['points'])
            if 90 < points <= 100:
                grade = 5
            elif 80 < points < 91:
                grade = 4.5
            elif 70 < points < 81:
                grade = 4
            elif 60 < points < 71:
                grade = 3.5
            elif 50 < points < 61:
                grade = 3
            else:
                grade = 2
            student_data['grade'] = grade
            student_data['status'] = 'GRADED'

def delete_student(data):
    email = input("Podaj adres email studenta, którego chcesz usunąć: ")
    if email in data:
        del data[email]
        print(f"Usunięto studenta o adresie email {email}")
    else:
        print(f"Nie znaleziono studenta o adresie email {email}")


def add_student(data):
    email = input("Podaj adres email studenta: ")
    if email in data:
        print(f"Student o adresie email {email} już istnieje")
        return
    first_name = input("Podaj imię studenta: ")
    last_name = input("Podaj nazwisko studenta: ")
    points = input("Podaj liczbę punktów: ")
    student_data = {'email': email, 'first_name': first_name, 'last_name': last_name, 'points': points, 'grade': '', 'status': ''}
    data[email] = student_data
    print(f"Dodano studenta {first_name} {last_name} z adresem email {email}")


def print_students(data):
    for email, student_data in data.items():
        print(student_data['first_name'], student_data['last_name'], student_data['points'], student_data['grade'],
              student_data['status'])


def send_email(data):
    for email, student_data in data.items():
        if student_data['status'] == 'GRADED':
            grade_ = student_data['grade']
            name_ = student_data['first_name']
            last_name_ = student_data['last_name']
            body = (f"Ocena: {grade_} dla {name_} {last_name_}")
            msg = MIMEText(body)
            msg['Subject'] = "Wystawianie ocen"
            msg['From'] = "sender"
            msg['To'] = ', '.join([student_data['email']])
            smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            mail = 's24124@pjwstk.edu.pl'
            smtp_server.login(mail, '')
            smtp_server.sendmail(mail, [student_data['email']], msg.as_string())
            smtp_server.quit()
            student_data['status'] = 'MAILED'


def main():
    data = read_file('students.txt')
    print(data)
    while True:
        print("\n--- Menu ---")
        print("1. Wypisz studentów")
        print("2. Wystaw oceny")
        print("3. Usuń studenta")
        print("4. Dodaj studenta")
        print("5. Send mail")
        print("0. Wyjdź")

        choice = input("\nWybierz opcję: ")
        if choice == "1":
            print_students(data)
        elif choice == "2":
            grade_students(data)
        elif choice == "3":
            delete_student(data)
        elif choice == "4":
            add_student(data)
        elif choice == "5":
            send_email(data)
        elif choice == "0":
            break
        else:
            print("Nieprawidłowa opcja")


if __name__ == '__main__':
    main()