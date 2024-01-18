class Planner:
    def __init__(self):
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def remove_event(self, event):
        self.events.remove(event)

    def view_events(self):
        num = 1
        for e in self.events:
            print(str(num) + ". " + str(e.time) + " - " + e.description)
            num += 1

    def is_duplicate(self, event):
        for e in self.events:
            if e.time == event.time:
                return True
            else:
                return False


class Event:
    def __init__(self, time, description):
        self.time = time
        self.description = description


planner = Planner()


def interactiveMenu():
    while True:
        print("\nОберіть опцію:")
        print("1. Додати подію")
        print("2. Видалити подію")
        print("3. Переглянути події")
        choice = input("Ваш вибір: ")
        if choice == "1":
            time = input("Введіть час запланованої події: ")
            description = input("Введіть опис до події: ")
            if planner.is_duplicate(Event(time, description)):
                tocontinue = input("Подія на цей час вже існує. Продовжити? y/n: ")
                if tocontinue == "y":
                    planner.add_event(Event(time, description))
                    print("Подію успішно додано")
                else:
                    print("Рішення скасовано.")
            else:
                planner.add_event(Event(time, description))
                print("Подію успішно додано")

        elif choice == "2":
            if planner.events:
                print("Виберіть номер події, яку ви хочете видалити:")
                planner.view_events()
                try:
                    user_num = int(input("Ваш вибір: "))
                    if 1 <= user_num <= len(planner.events):
                        planner.remove_event(planner.events[user_num - 1])
                        print("Подію успішно видалено")
                    else:
                        print("Некоректний номер події. Ваш вибір: ")
                except ValueError:
                    print("Введіть коректне число.")
            else:
                print("Подій немає. Створіть подію")

        elif choice == "3":
            print("Список подій:")
            if planner.events:
                planner.view_events()
            else:
                print("Подій немає. Створіть подію")
        else:
            print("Введіть число від 1 до 3.")


interactiveMenu()
