# 5명의 학생의 세개의 교과목 (영어, C-언어, 파이썬)에 대하여 
# 키보드로부터 학번, 이름, 영어점수, C-언어 점수, 파이썬 점수를 입력받아
# 총점, 평균, 학점, 등수를 계산하는 프로그램 작성
# -입력 함수, 총점/평균 계산 함수, 학점계산 함수, 등수계산 함수, 출력 함수
# -삽입 함수, 삭제 함수, 탐색함수(학번, 이름), 정렬(총점)함수, 80점이상 학생 수 카운트 함수

students = []

#   입력 함수
def get_info():

    student_info = {}
    student_info['학번'] = input("학번을 입력하세요: ")
    student_info['이름'] = input("이름을 입력하세요: ")
    student_info['영어'] = int(input("영어 점수를 입력하세요: "))
    student_info['C언어'] = int(input("C언어 점수를 입력하세요: "))
    student_info['파이썬'] = int(input("파이썬 점수를 입력하세요: "))
    students.append(student_info)

         
#   총점/평균 계산 함수
def calc_total_average():

    for student_info in students:
         total = student_info['영어'] + student_info['C언어'] + student_info['파이썬']
         average = round(total / 3.0, 2)
         student_info['총점'] = total
         student_info['평균'] = average


#   학점 계산 함수
def calc_grade(average):

    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'
    

#   등수 계산 함수 (총점 정렬)
def calc_rank():

    students.sort(key=lambda x: x['총점'], reverse = True)  #학생들을 총점 순서대로 내림차순 정렬
    rank = 1
    prev_score = students[0]['총점']
    for student_info in students:
        if student_info['총점'] < prev_score:
            rank += 1
            prev_score = student_info['총점']
        student_info['등수'] = rank


#   출력 함수
def out_student():

    print("학생 정보 출력")
    print("=============================================================================\n")
    print("학번\t이름\t영어\tC언어\t파이썬\t총점\t평균\t학점\t등수\n")
    print("=============================================================================\n\n")
    
    for student_info in students:
        print("\t".join(str(value) for key, value in student_info.items() if key in ['학번', '이름', '영어', 'C언어', '파이썬', '총점', '평균', '학점', '등수']))
        print("\n")


#   평균 80점 이상 학생 수 카운트 함수
def count_80():
    calc_total_average()
    count = 0
    for student_info in students:
        if student_info['평균'] >= 80:
            count += 1
    return count


#   삭제 함수
def delete():
    stnum = input("삭제하려는 학생의 학번을 입력하세요: ")
    for i, student_info in enumerate(students):
        if student_info['학번'] == stnum:
            del students[i]
            print(student_info['이름'], "학생의 학생 정보가 성공적으로 삭제되었습니다.")
            calc_rank()     #학생 정보 삭제 후 등수 재산출
            return
    print("{} 학생의 정보가 존재하지 않습니다.".format(stnum))


#   탐색 함수
def search():
    stnum = input("탐색하려는 학생의 학번을 입력하세요: ")
    name = input("탐색하려는 학생의 이름을 입력하세요: ")

    found = False
    for student_info in students:
        if student_info['학번'] == stnum and student_info['이름'] == name:
            found = True
            print("학번:",student_info['학번'])
            print("이름:",student_info['이름'])
            print("영어:",student_info['영어'])
            print("C언어:",student_info['C언어'])
            print("파이썬:",student_info['파이썬'])
            print("총점:",student_info['총점'])
            print("평균:",student_info['평균'])
            print("학점:",student_info['학점'])
            print("등수:",student_info['등수'])
            break

    if not found:
        print("해당 학생을 찾을 수 없습니다.")



#   실행
while True:
    print("\n=== 메뉴 ===")
    print("1. 학생 정보 입력")
    print("2. 학생 정보 출력")
    print("3. 80점 이상 학생 수")
    print("4. 학생 정보 삭제")
    print("5. 학생 정보 탐색")
    print("0. 종료")

    choice = input("원하는 작업을 선택하세요: ")
    print("\n")

    if choice == '1':
        get_info()
        calc_total_average()
        for student_info in students:
            student_info['학점'] = calc_grade(student_info['평균'])
        calc_rank()
    elif choice == '2':
        out_student()
    elif choice == '3':
        print("평균 80점 이상 학생 수: ",count_80())
    elif choice == '4':
        delete()
    elif choice == '5':
        search()
    elif choice == '0':
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 입력입니다. 다시 시도하세요.")
