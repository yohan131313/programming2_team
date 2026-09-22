









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


turtle.done()