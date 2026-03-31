number = int(input("4자리 정수 입력:") )
n1 = number % 10
n10 =(number % 100)//10
n100 = (number % 1000) // 100
n1000 = number // 1000

print(n1 + n10 + n100 + n1000)