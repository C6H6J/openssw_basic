# 5명의 학생의 세개의 교과목 (영어, C-언어, 파이썬)에 대하여 
# 키보드로부터 학번, 이름, 영어점수, C-언어 점수, 파이썬 점수를 입력받아
# 총점, 평균, 학점, 등수를 계산하는 프로그램 작성


people = 5
student = [[] for j in range(people)]


#   입력함수
def get_info():

    for i in range(people):
          student[i].append(input(f"학생{i+1}의 학번: "))
          student[i].append(input(f"학생{i+1}의 이름: "))
          student[i].append(input(f"학생{i+1}의 영어점수: "))
          student[i].append(input(f"학생{i+1}의 C-언어 점수: "))
          student[i].append(input(f"학생{i+1}의 파이썬 점수: "))


#   총점/평균 계산 함수
def calc_tot_avg():
    for i  in range(people):
          sum = int(student[i][2]) + int(student[i][3]) + int(student[i][4])
          avg = int(round(sum / 3.0))
          student[i].append(sum)
          student[i].append(avg)


#   학점계산 함수
def calc_grade():
    
    for i  in range(people):
          
          tot = student[i][6]
          
          if tot >= 90:
             if tot >= 95:
                 student[i].append('A+')
             else:
                 student[i].append('A')
             student[i].append('A')
          elif tot >= 80:
             if tot >= 85:
                 student[i].append('B+')
             else:
                 student[i].append('B')
          elif tot >= 70:
             if tot >= 75:
                 student[i].append('C+')
             else:
                 student[i].append('C')
          elif tot >= 60:
             student[i].append('D')
          else:
             student[i].append('F')

    
#   등수계산 함수
def calc_rank():
      
      for i  in range(people):
            rank = 1
            tot = student[i][5]

            for j in range(people):
                if tot < student[j][5]:
                  rank += 1

            student[i].append(rank)
            

#   출력 함수
def out_info(student_list):
      
      print("\t 성적관리 프로그램\n")
      print(" =============================================================================\n\n")
      print("학번\t이름\t영어\tC-언어\t파이썬\t총점\t평균\t학점\t등수\n\n")
      print(" =============================================================================\n\n")

      for student in student_list:
        for info in student:
            print(f"{info}\t", end="")  
        print("\n\n")

#   main
get_info()
calc_tot_avg()
calc_grade()
calc_rank()
out_info(student)


    





