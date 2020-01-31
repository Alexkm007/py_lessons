import sys
if len(sys.argv)== 2:
    digit_string = sys.argv[1]
else:
    print("Параметр не обнаружен, работа прекращена")
    sys.exit()

if not digit_string.isdigit():
    print("Парметр должен быть целым числом")
    sys.exit()
summ = 0
for i in digit_string:
    summ+=int(i)
print(summ)
