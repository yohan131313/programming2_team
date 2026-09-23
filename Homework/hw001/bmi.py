# 초기 data 리스트 초기화
data = []

# haelth.txt 연결
import os
file_path = os.path.join(os.path.dirname(__file__), "health.txt")
with open(file_path, "r", encoding="utf-8") as file:

    # 연결된 내용 한줄씩 자르고 4가지 변수로 분리
    for line in file:
        PhoneNumber, Name, Height, Weight = line.strip().split(",")

        # 계산을 위해 키와 몸무게 실수로 전환
        Height = float(Height)
        Weight = float(Weight)

        # bmi 계산식
        Bmi = Weight / ((Height / 100) ** 2)

        # 계산된 bmi를 6가지 소견으로 나누는 조건문
        if Bmi < 18.5:
            Opinion = "저체중"
        elif Bmi < 23:
            Opinion = "정상"
        elif Bmi < 25:
            Opinion = "과체중"
        elif Bmi < 30:
            Opinion = "1단계 비만"
        elif Bmi < 35:
            Opinion = "2단계 비만"
        else:
            Opinion = "3단계 비만"

        #turtle graphics에 보여줄 6가지 변수를 리스트째 data에 넣음으로서 data를 2차원 리스트로 정리
        data.append([PhoneNumber, Name, Height, Weight, Bmi, Opinion])

# 터틀 그래픽 기본 베이스
import turtle

t = turtle.Turtle()
t.hideturtle()

# 항목 이름
t.penup()
t.goto(-450, 200)
t.write("전화번호")

t.goto(-280, 200)
t.write("이름")

t.goto(-170, 200)
t.write("키(cm)")

t.goto(-70, 200)
t.write("몸무게(kg)")

t.goto(100, 200)
t.write("BMI")

t.goto(180, 200)
t.write("소견")

# 사람들의 정보 출력(여러명 가능)
# 필수로 넣기 => for person in data:
y = 160
for person in data:     # 리스트 활용
    t.goto(-450, y)
    t.write(person[0])

    t.goto(-280, y)
    t.write(person[1])

    t.goto(-170, y)
    t.write(person[2])

    t.goto(-70, y)
    t.write(person[3])

    t.goto(100, y)
    t.write(f"{person[4]:.2f}")     # bmi 수치 소수점 2자리까지 출력

    t.goto(180, y)
    t.write(person[5])

    y = y - 40

turtle.done()