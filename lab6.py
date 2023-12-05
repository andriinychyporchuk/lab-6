def main(): 
    schedule = load_schedule()

    while True:
        print("\nОберіть дію:")
        print("1. Переглянути розклад")
        print("2. Додати нове тренування")
        print("3. Зберегти розклад у файл")
        print("4. Переглянути розклади у файлі")
        print("5. Видалити тренування")
        print("6. Видалити розклад")
        print("q. Вийти з програми")

        choice = input("Ваш вибір: ")

        if choice == '1':
            show_schedule(schedule)
        elif choice == '2':
            add_training(schedule)
        elif choice == '3':
            save_schedule(schedule)
        elif choice == '4':
            show_all_schedules()
        elif choice == '5':
            delete_training(schedule)
        elif choice == '6':
            delete_schedule()
        elif choice == '7':
            choose_day_for_training(schedule)
        elif choice.lower() == 'q':
            break
        else:
            print("Невірний вибір. Спробуйте знову.")

def load_schedule():
    try:
        with open('schedule.txt', 'r') as file:
            lines = file.readlines()
            schedule = []
            for line in lines:
                day, activity, time = line.strip().split(',')
                schedule.append({'day': day, 'activity': activity, 'time': time})
    except FileNotFoundError:
        schedule = []
    return schedule

def save_schedule(schedule):
    with open('schedule.txt', 'w') as file:
        for training in schedule:
            line = f"{training['day']},{training['activity']},{training['time']}\n"
            file.write(line)
            print(f"Збережено: {line.strip()}")

def show_schedule(schedule):
    if not schedule:
        print("Розклад порожній. Додайте тренування.")
    else:
        print("Розклад тренувань:")
        for training in schedule:
            print(f"{training['day']}: {training['activity']} о {training['time']}")

def add_training(schedule):
    print("Оберіть день тренування:")
    print("1. Понеділок")
    print("2. Вівторок")
    print("3. Середа")
    print("4. Четвер")
    print("5. П'ятниця")
    print("6. Субота")
    print("7. Неділя")

    day_choice = input("Ваш вибір: ")

    if day_choice.isdigit() and 1 <= int(day_choice) <= 7:
        day = get_day_name(int(day_choice))
        activity = input("Введіть назву тренування: ")

        while True:
            time = input("Введіть час тренування у форматі HH:MM: ")
            if validate_time_format(time):
                break
            else:
                print("Невірний формат часу. Спробуйте знову.")

        new_training = {
            'day': day,
            'activity': activity,
            'time': time
        }

        schedule.append(new_training)
        print("Тренування додано до розкладу.")
    else:
        print("Невірний вибір дня. Спробуйте знову.")

def delete_training(schedule):
    show_schedule(schedule)
    if not schedule:
        print("Розклад порожній. Немає тренувань для видалення.")
        return

    print("Оберіть день тренування для видалення:")
    print("1. Понеділок")
    print("2. Вівторок")
    print("3. Середа")
    print("4. Четвер")
    print("5. П'ятниця")
    print("6. Субота")
    print("7. Неділя")

    day_choice = input("Ваш вибір: ")

    if day_choice.isdigit() and 1 <= int(day_choice) <= 7:
        day = get_day_name(int(day_choice))
        day_schedule = [training for training in schedule if training['day'] == day]

        if not day_schedule:
            print(f"На {day} немає тренувань для видалення.")
            return

        print(f"\nТренування на {day}:")
        for idx, training in enumerate(day_schedule, start=1):
            print(f"{idx}. {training['activity']} о {training['time']}")

        training_to_delete = input("Введіть номер тренування, яке ви хочете видалити: ")
        if training_to_delete.isdigit() and 1 <= int(training_to_delete) <= len(day_schedule):
            del schedule[schedule.index(day_schedule[int(training_to_delete) - 1])]
            print("Тренування видалено.")
        else:
            print("Невірний номер тренування. Видалення скасовано.")
    else:
        print("Невірний вибір дня. Спробуйте знову.")

def delete_schedule():
    confirmation = input("Ви впевнені, що хочете видалити весь розклад? (y/n): ")
    if confirmation.lower() == 'y':
        with open('schedule.txt', 'w') as file:
            file.write("[]")
        print("Розклад видалено.")
    else:
        print("Видалення розкладу скасовано.")

def validate_time_format(time):
    try:
        # Перевірка правильності формату часу
        hours, minutes = map(int, time.split(':'))
        if 0 <= hours <= 23 and 0 <= minutes <= 59:
            return True
        else:
            return False
    except ValueError:
        return False

def show_all_schedules():
    try:
        with open('schedule.txt', 'r') as file:
            print("Зміст файлу schedule.txt:")
            print(file.read())
    except FileNotFoundError:
        print("Файл з розкладами не знайдено.")

def get_day_name(day_number):
    days = {
        1: 'Понеділок',
        2: 'Вівторок',
        3: 'Середа',
        4: 'Четвер',
        5: 'Пятниця',
        6: 'Субота',
        7: 'Неділя'
    }
    return days.get(day_number)

if __name__ == "__main__":
    main()