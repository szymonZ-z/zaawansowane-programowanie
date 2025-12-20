from utils.Student import Student
from utils.Library import Library, Book, Employee, Order
from utils.Property import Flat, House

# Zadanie 1

st1 = Student("Andrzej", [100, 99, 98, 99, 60])
st2 = Student("Janusz", [34, 66, 10, 34, 60])

print(f'Student 1: {st1.is_passed()}, Student 2: {st2.is_passed()}')

# Zadanie 2

lib1 = Library('Katowice', 'Wojewodzka 12', '40-400', '10-18', '2239429')
lib2 = Library('Chorzów', 'Jana Pawła 2 3', '40-200', '10-20', '2239423')

book1 = Book(lib1, '1525-12-11', 'Hieronim', 'Anonim', 102)
book2 = Book(lib1, '1925-10-01', 'Bogusław', 'Jurek', 12)
book3 = Book(lib1, '2025-01-11', 'Anthony', 'Kowalsky', 954)
book4 = Book(lib2, '1995-12-31', 'Mike', 'Smith', 34)
book5 = Book(lib2, '1999-11-11', 'Janusz', 'Nowak', 188)

emp1 = Employee('Zdzisław', 'Zastaw', '1999-12-22', '1992-12-12', 'Mysłowice', 'Emilii Plater 21', '43-443', '32225266')
emp2 = Employee('Agnieszka', 'Orała', '2025-12-02', '1990-12-31', 'Opole', 'Grzegżółki 43', '43-443', '32265455')
emp3 = Employee('Rafał', 'Wyszoń', '2022-11-23', '2001-05-12', 'Katowice', 'Topolowa 11', '43-443', '316552255')

student1 = 'Jarek Wojtasik'
student2 = 'Antoni Górka'
student3 = 'Jadwiga Niechciała'

order1 = Order(emp1, student1, [book1, book2, book3], '2023-02-22')
order2 = Order(emp2, student3, [book4, book5], '2025-09-17')

print(order1)
print(order2)

# Zadanie 3

flat = Flat(12, 45, 2, 1000000.0, 'Katowiece, ul. Bogucicka 4')
house = House(400, 200, 10, 20000, 'Olsztyn, ul. Długa 50')

print(flat)
print(house)
