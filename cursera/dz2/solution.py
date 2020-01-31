import sys
if len(sys.argv)== 2:
    digit_string = sys.argv[1]
else:
    print("Параметр не обнаружен, работа прекращена")
    sys.exit()

if not digit_string.isdigit():
    print("Парметр должен быть целым числом")
    sys.exit()
i = int(digit_string)
k=1
while k <= i:
    str1 = " "*(i-k)
    str2 = "#"*k
    if k !=i:
        print(str1+str2)
    else:
        print(str1 + str2,end="")
    k+=1