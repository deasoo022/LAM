x1 = int(input("x1의 값을 작성해주세요: "))
x2 = int(input("x2의 값을 작성해주세요: "))
x3 = int(input("x3의 값을 작성해주세요: "))
y1 = int(input("y1의 값을 작성해주세요: "))
y2 = int(input("y2의 값을 작성해주세요: "))
y3 = int(input("y3의 값을 작성해주세요: "))

avgx = ((x1 + x2 + x3 )/ 3)
avgy = ((y1 + y2 + y3)/ 3)

long = (((x1 - x2)**2 + (y1 - y2)**2)**2/1) + (((x2 - x3)**2 + (y2 - y3)**2)**2/1) + (((x1 - x3)**2 + (y1 - y3)**2)**2/1)

print("x좌표 평균:" , avgx)
print("y좌표 평균",avgy)
print("삼각형 둘레",long) 