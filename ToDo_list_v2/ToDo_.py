import json
from datetime import datetime, date


class Task:
    def __init__(self, task_id, title, description, due_date):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date

    def to_dict(self):
        return {
            'task_id': self.task_id,
            'title': self.title,
            'description': self.description,
            'due_date': self.due_date.isoformat(),
        }


class ToDoList:
    def __init__(self):
        self.tasks = []

    def load(self):
        try:
            with open('tasks.json', 'r') as file:
                tasks_data = json.load(file)
                for task_data in tasks_data:
                    due_date = datetime.fromisoformat(task_data['due_date']).date()
                    task = Task(task_data['task_id'], task_data['title'], task_data['description'], due_date)
                    self.tasks.append(task)
        except FileNotFoundError:
            print("Nie znaleziono pliku. Tworzę nowy plik z zadaniami.")

    def save_to_file(self):
        tasks_data = [task.to_dict() for task in self.tasks]
        with open('tasks.json', 'w') as file:
            json.dump(tasks_data, file, indent=4)

    def add(self):
        if self.tasks:
            max_id = max(self.tasks, key=lambda x: x.task_id).task_id
            task_id = max_id + 1
        else:
            task_id = 1
        title = input("Podaj tytuł zadania: ")
        description = input("Podaj opis zadania: ")
        due_date_str = input("Podaj termin wykonania (DD-MM-YYYY): ")
        due_date = datetime.strptime(due_date_str, "%d-%m-%Y").date()
        task = Task(task_id, title, description, due_date)
        self.tasks.append(task)
        print(f"Dodano zadanie: {title}")

    def remove(self):
        task_id = int(input("Podaj id zadania do usunięcia: "))
        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                print(f"Usunięto zadanie o id: {task_id}")
                return
        print(f"Nie znaleziono zadania o id: {task_id}")

    def update(self):
        task_id = int(input("Podaj id zadania do aktualizacji: "))
        for task in self.tasks:
            if task.task_id == task_id:
                title = input("Podaj nowy tytuł zadania: ")
                description = input("Podaj nowy opis zadania: ")
                due_date_str = input("Podaj nowy termin wykonania zadania (DD-MM-YYYY): ")
                due_date = datetime.strptime(due_date_str, "%d-%m-%Y").date()
                task.title = title
                task.description = description
                task.due_date = due_date
                print(f"Aktualizowano zadanie o id: {task_id}")
                return
        print(f"Nie znaleziono zadania o id: {task_id}")

    def display(self):
        if self.tasks:
            for task in self.tasks:
                print(f"id: {task.task_id}, tytuł: {task.title}, termin wykonania: {task.due_date}")
                show_description = input("Czy wyświetlić opis zadania? (T/N): ")
                if show_description.lower() == "t":
                    print(f"Opis zadania: {task.description}")
        else:
            print("Brak zapisanych zadań.")

    def save(self):
        self.save_to_file()
        print("Zapisano zadania do pliku.")

    def run(self):
        self.load()

        while True:
            print("""
            Witaj w liście ToDo!
            Wybierz jedną z opcji:
            1. Dodaj zadanie
            2. Usuń zadanie
            3. Aktualizuj zadanie
            4. Wyświetl zadania
            5. Zapisz zadania do pliku
            6. Wyjdź z programu
            """)
            choice = input("Twój wybór: ")

            if choice == "1":
                self.add()
            elif choice == "2":
                self.remove()
            elif choice == "3":
                self.update()
            elif choice == "4":
                self.display()
            elif choice == "5":
                self.save_to_file()
                print("Zapisano zadania do pliku.")
            elif choice == "6":
                self.save()
                print("Koniec programu.")
                break
            else:
                print("Nieprawidłowy wybór. Wybierz opcję od 1 do 6.")


todo_list = ToDoList()
todo_list.run()
