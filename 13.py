import json

class UserProfile():
    def __init__(self, name, age, interest):
        self.name = name
        self.age = age
        self.interest = interest
        pass

    def to_dict(self):
        return {'name': self.name, 'age': self.age, "interest": self.interest}
    @classmethod
    def from_dict(self):
        try: 
            data_list = []
            data_list.append("name")
            data_list.append("age")
            data_list.append("interest")
            print(data_list)
        except TypeError:
            print()

    def save_profile(self,filename):
        try:
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(user.to_dict(), f)
        except Exception as e:
            print(f"Error saving profile: {e}")    
    def load_profile(self,filename):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                return UserProfile.from_dict()
        except json.JSONDecodeError:
            print("Файл повреждён или пуст")
            data = []

        

user = UserProfile("Alice", 25, ["Python", "AI"])

user.save_profile("profile.json")
user.load_profile("profile.json")
print(user) 


import pickle
import os

class Task:
    def __init__(self, title, priority, completed=False):
        self.title = title
        self.priority = priority
        self.completed = completed

    def mark_done(self):
        self.completed = True

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.title} (Priority: {self.priority})"

TASKS_FILE = "tasks.pickle"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []

    try:
        with open(TASKS_FILE, "rb") as f:
            return pickle.load(f)
    except EOFError:
        return []

def save_tasks(tasks):
    with open(TASKS_FILE, "wb") as f:
        pickle.dump(tasks, f)

def add_task(title, priority):
    tasks = load_tasks()
    tasks.append(Task(title, priority))
    save_tasks(tasks)

def delete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        del tasks[index]
        save_tasks(tasks)

def complete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index].mark_done()
        save_tasks(tasks)

def show_tasks():
    tasks = load_tasks()
    if not tasks:
        print("Нет задач.")
    else:
        for i, task in enumerate(tasks):
            print(f"{i}. {task}")

# Пример использования
if __name__ == "__main__":
    while True:
        print("\n1. Показать задачи\n2. Добавить задачу\n3. Удалить задачу\n4. Завершить задачу\n5. Выход")
        choice = input("Выберите действие: ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            title = input("Название задачи: ")
            priority = int(input("Приоритет (целое число): "))
            add_task(title, priority)
        elif choice == "3":
            index = int(input("Номер задачи для удаления: "))
            delete_task(index)
        elif choice == "4":
            index = int(input("Номер задачи для завершения: "))
            complete_task(index)
        elif choice == "5":
            break
        else:
            print("Неверный выбор.")

#3
import json

def is_valid_user(user):
    if not isinstance(user, dict):
        return False, "Не словарь"

    if "id" not in user or not isinstance(user["id"], int):
        return False, "id отсутствует или не целое число"

    if "name" not in user or not isinstance(user["name"], str):
        return False, "name отсутствует или не строка"

    if "email" not in user or not isinstance(user["email"], str) or "@" not in user["email"]:
        return False, "email отсутствует, не строка или не содержит '@'"

    return True, None

def load_users(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
        return
    except json.JSONDecodeError:
        print("Ошибка разбора JSON.")
        return

    valid_users = []
    skipped = 0

    for user in data:
        is_valid, error = is_valid_user(user)
        if is_valid:
            valid_users.append(user)
        else:
            print(f"Пропущен пользователь: {user} — ошибка: {error}")
            skipped += 1

    print(f"\nЗагружено пользователей: {len(valid_users)}")
    print(f"Пропущено пользователей: {skipped}")

    return valid_users

# Пример использования
if __name__ == "__main__":
    users = load_users("users.json")
    if users:
        print("\nВалидные пользователи:")
        for u in users:
            print(u)



#4
import pickle
import os
from datetime import datetime

class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.created_at = datetime.now()

    def __str__(self):
        date_str = self.created_at.strftime("%Y-%m-%d %H:%M:%S")
        return f"\n--- {self.title} ---\nДата: {date_str}\n{self.content}\n"

class NoteManager:
    FILE_NAME = "notes.pkl"

    def __init__(self):
        self.notes = self._load_notes()

    def _load_notes(self):
        if not os.path.exists(self.FILE_NAME):
            return []
        try:
            with open(self.FILE_NAME, "rb") as f:
                return pickle.load(f)
        except (EOFError, pickle.UnpicklingError):
            return []

    def _save_notes(self):
        with open(self.FILE_NAME, "wb") as f:
            pickle.dump(self.notes, f)

    def add_note(self, title, content):
        note = Note(title, content)
        self.notes.append(note)
        self._save_notes()

    def delete_note(self, index):
        if 0 <= index < len(self.notes):
            del self.notes[index]
            self._save_notes()

    def show_all_notes(self):
        if not self.notes:
            print("Нет заметок.")
        else:
            for i, note in enumerate(self.notes):
                print(f"{i}. {note}")

# Пример использования
if __name__ == "__main__":
    manager = NoteManager()

    while True:
        print("\n1. Показать все заметки\n2. Добавить заметку\n3. Удалить заметку\n4. Выход")
        choice = input("Выберите действие: ")

        if choice == "1":
            manager.show_all_notes()
        elif choice == "2":
            title = input("Заголовок: ")
            content = input("Текст заметки: ")
            manager.add_note(title, content)
            print("Заметка добавлена.")
        elif choice == "3":
            index = int(input("Введите номер заметки для удаления: "))
            manager.delete_note(index)
            print("Заметка удалена.")
        elif choice == "4":
            break
        else:
            print("Неверный выбор.")
