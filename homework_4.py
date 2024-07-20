team1_num = 6
print('В команде Мастера кода участников: %s!' % team1_num)
team2_num = 6
print('В команде Волшебники данных участников: %s!' % team2_num)
print('Итого сегодня в командах участников: %s и %s!' %(team1_num, team1_num))
score1 = 40
print('Команда Мастера кода решила задач: {}!'.format(score1))
score2 = 42
print('Команда Волшебники данных решила задач: {}!'.format(score2))
team1_time = 1552.512
print('Мастера кода решили задачи за {} с !'.format(team1_time))
team2_time = 2153.31451
print('Волшебники данных решили задачи за {} с !'.format(team2_time))
tasks_total = 82
print(f'Команды решили {score1} и {score2} задач.')

challenge_result = 'Мастера кода' if team1_time / score1 < team2_time / score2 else ('Волшебники данных'
    if team1_time / score1 > team2_time / score2 else 'Ничья!')
print(f'Результат битвы: победа команды {challenge_result}!')
time_avg = (team1_time + team2_time) / tasks_total

print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')
