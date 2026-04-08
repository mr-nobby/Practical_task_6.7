print("Начался восьмичасовой рабочий день. ")
the_bell = 0 # Звонк от Жены
working_hours = 8 # Рабочие  часы
max_tasks = 0 # Максимальное количество задач

while working_hours != 0:

   tasks = int (input("Сколько задач решит Максим ? "))
   max_tasks += tasks
   working_hours -= 1

   if the_bell == 0:
       the_bell = int(input("Звонит жена. Взять трубку?  (1 — да, 0 — нет): "))
   else:
       the_bell = 1

   if working_hours == 0:
       print("Рабочий день закончился. \nВсего выполнено задач: ",max_tasks)
       if the_bell == 1:
           print("Звонила Жена и попросила зайти в магазин.")



