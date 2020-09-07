# Code_Backup for CRONI project

1. Run file : Interface_module.py를 실행 [Version3 기준]

2. Run file 내부 Data_module 및 Model_module과 연계되어 실행

3. Diagnosis_module, Plot_module, Rule_module은 Version3에서는 사용되지 않음.
  - 해당 모듈은 Version1, 2에서 사용되었음 -> Matplotlib를 활용한 plot 구성을 위한 용도일뿐 -> 로직은 추후 참고용
  
4. Total_algorithm은 Version1, 2에서의 Run file임.

5. Interface 구성
![제목 없음](https://user-images.githubusercontent.com/56631737/92341036-72b0d000-f0f7-11ea-9ca7-f9a5568d0543.png)

[Issue]
1. Thread 통신 간 딜레이 되는 현상 있음.
 - ex) 1초가 2초가 되는 경향.. -> 추후 멀티프로세싱 확인 및 수정
 
 2. 전체적인 코드 경량화 작업 수행
  - 사용자 정의 함수간 합칠 수 있는 부분은 합쳐서 
