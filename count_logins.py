def count_logins(username, logins_list):
    counter = 0  # Переменная для подсчёта входов
    
    for user in logins_list:  # Перебираем всех пользователей в списке
        if user == username:  # Если имя совпадает с искомым
            counter += 1  # Увеличиваем счётчик
    
    return counter  # Возвращаем итоговое количество входов

# Пример списка логинов за день
logins = ["alice", "bob", "alice", "charlie", "alice", "bob", "alice", "dave"]

# Отмеченный пользователь
flagged_user = "alice"

# Подсчёт входов
login_count = count_logins(flagged_user, logins)

# Вывод результата
print(f"Пользователь '{flagged_user}' входил в систему {login_count} раз(а).")
