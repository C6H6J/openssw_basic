#   성적관리프로그램 (객체지향 프로그램으로 수정하기)    

class Student:
    def __init__(self):
        self.info = {}
        
    #   학생 정보 입력 함수
    def get_info(self):
        self.info['학번'] = input("학번을 입력하세요: ")
        self.info['이름'] = input("이름을 입력하세요: ")
        self.info['영어'] = input("영어 점수를 입력하세요: ")
        self.info['C언어'] = input("C언어 점수를 입력하세요: ")
        self.info['파이썬'] = input("파이썬 점수를 입력하세요: ")
        
    #   총점 및 평균 계산 함수
    def calc_total_average(self):
        self.info['총점'] = int(self.info['영어']) + int(self.info['C언어']) + int(self.info['파이썬'])
        self.info['평균'] = round(self.info['총점'] / 3.0, 1)
        
    #   학점 계산 함수
    def calc_grade(self):
        if self.info['평균'] >= 90:
            self.info['학점'] = 'A'
        elif self.info['평균'] >= 80:
            self.info['학점'] = 'B'
        elif self.info['평균'] >= 70:
            self.info['학점'] = 'C'
        elif self.info['평균'] >= 60:
            self.info['학점'] = 'D'
        else:
            self.info['학점'] = 'F'
        
    #   학생 정보 출력 함수
    def out_student(self):
        print("학번:", self.info['학번'])
        print("이름:", self.info['이름'])
        print("영어:", self.info['영어'])
        print("C언어:", self.info['C언어'])
        print("파이썬:", self.info['파이썬'])
        print("총점:", self.info['총점'])
        print("평균:", self.info['평균'])
        print("학점:", self.info['학점'])
        print("등수:", self.info['등수'])
        
        
students = []

#   출력 함수
def out_student():

    print("학생 정보 출력")
    print("=============================================================================\n")
    print("학번\t이름\t영어\tC언어\t파이썬\t총점\t평균\t학점\t등수\n")
    print("=============================================================================\n\n")
    
    for student in students:
        print("\t".join(str(value) for key, value in student.info.items() if key in ['학번', '이름', '영어', 'C언어', '파이썬', '총점', '평균', '학점', '등수']))


#   등수 계산 함수 (총점 정렬)
def calc_rank():
    students.sort(key=lambda x: x.info['총점'], reverse = True)  #학생들을 총점 순서대로 내림차순 정렬
    rank = 1
    prev_score = students[0].info['총점']
    for s in students:
        if s.info['총점'] < prev_score:
            rank += 1
            prev_score = s.info['총점']
        s.info['등수'] = rank


#   삭제 함수
def delete_student():
    del_num = input("삭제할 학생의 학번을 입력하세요: ")
    for i in range(len(students)):
        if students[i].info['학번'] == del_num:
            del students[i]
            break
    else:
        print("{} 학생의 정보가 없습니다.".format(del_num))
 
        
#   탐색 함수
def search_student():
    search_num = input("탐색할 학생의 학번을 입력하세요: ")
    for i in range(len(students)):
        if students[i].info['학번'] == search_num:
            students[i].out_student()
            break
    else:
        print("{} 학생의 정보가 없습니다.".format(search_num))
        
#   평균 80점 이상 학생 수 카운트 함수
def count_80():
    count = 0
    for s in students:
        if s.info['평균'] >= 80:
            count += 1
    return count

#  메인 함수
def main():
    while True:
        print("1. 학생 정보 입력")
        print("2. 학생 정보 출력")
        print("3. 학생 정보 삭제")
        print("4. 학생 정보 탐색")
        print("5. 학생 평균 80점 이상 학생 수 출력")
        print("0. 종료")
        
        menu = int(input("메뉴를 선택하세요: "))
        
        if menu == 1:
            s = Student()
            s.get_info()
            s.calc_total_average()
            s.calc_grade()
            students.append(s)
            calc_rank()
            print("\n")
        elif menu == 2:
            out_student()
            print("\n")
        elif menu == 3:
            delete_student()
            calc_rank()
        elif menu == 4:
            search_student()
            print("\n")
        elif menu == 5:
            print("평균 80점 이상 학생 수: ", count_80())
            print("\n")
        elif menu == 0:
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 시도하세요.")
            
#   메인 함수 실행
main()