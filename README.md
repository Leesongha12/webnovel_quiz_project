# Web Novel Quiz Project

## 1. 프로젝트 개요

본 프로젝트는 Python을 활용하여 제작한 콘솔 기반 퀴즈 게임입니다.  
사용자는 메뉴를 통해 퀴즈를 풀고, 새로운 퀴즈를 추가하며, 등록된 퀴즈 목록과 최고 점수를 확인할 수 있습니다.  
또한 JSON 파일을 활용하여 프로그램 종료 후에도 데이터가 유지되도록 구현하였습니다.

본 프로젝트는 2주차 과제로, 1주차에서 구축한 개발 환경과 Git 사용 경험을 기반으로 실제 프로그램을 구현하는 것을 목표로 합니다.

---

## 2. 퀴즈 주제 선정 이유

퀴즈 주제는 웹소설 장르 상식으로 선정하였습니다.  
평소 웹소설을 자주 접해 해당 분야에 대한 이해도가 높았기 때문에 문제를 직접 구성하기에 적합하다고 판단했습니다.  
또한 하나의 장르로 통일된 문제를 구성하면 프로그램의 일관성과 완성도를 높일 수 있다고 생각했습니다.

---

## 3. 실행 방법

아래 명령어를 입력하여 프로그램을 실행할 수 있습니다.

```bash
python main.py
4. 기능 목록
퀴즈 풀기
퀴즈 추가
퀴즈 목록 확인
최고 점수 확인
프로그램 종료
JSON 파일을 통한 데이터 저장 및 불러오기
5. 파일 구조
webnovel_quiz_project/
├── main.py
├── quiz.py
├── quiz_game.py
├── state.json
├── README.md
└── docs/
    └── screenshots/
6. 핵심 코드 설명
6-1. Quiz 클래스

퀴즈 하나를 표현하는 클래스입니다.

class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def display(self):
        print(self.question)
        for i, choice in enumerate(self.choices, start=1):
            print(f"{i}. {choice}")

    def check_answer(self, user_answer):
        return user_answer == self.answer
6-2. QuizGame 클래스 (일부)

게임 전체 흐름을 관리하는 클래스입니다.

class QuizGame:
    def __init__(self):
        self.file_path = "state.json"
        self.quizzes = []
        self.best_score = 0
6-3. JSON 저장 기능
def save_data(self):
    data = {
        "quizzes": [
            {
                "question": q.question,
                "choices": q.choices,
                "answer": q.answer
            } for q in self.quizzes
        ],
        "best_score": self.best_score
    }

    with open(self.file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
6-4. JSON 불러오기 기능
def load_data(self):
    with open(self.file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
7. 데이터 파일 설명

프로젝트 루트에 위치한 state.json 파일은 퀴즈 데이터와 최고 점수를 저장하는 역할을 합니다.

데이터 구조 예시
{
    "quizzes": [
        {
            "question": "웹소설에서 자주 등장하는 '북부 대공' 캐릭터의 특징으로 가장 적절한 것은?",
            "choices": [
                "밝고 사교적인 성격으로 파티를 즐긴다",
                "따뜻하고 감정 표현이 풍부하다",
                "냉정하고 과묵하며 강한 권력을 가진다",
                "평범한 시민 출신으로 모험을 떠난다"
            ],
            "answer": 3
        }
    ],
    "best_score": 5
}
8. 프로그램 실행 예시
========================================
        🎯 나만의 퀴즈 게임 🎯
========================================
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 종료
========================================
선택:
9. 핵심 개념 정리 (과제 요구 반영)
9-1. 클래스와 객체 (OOP)
클래스: 객체를 만들기 위한 설계도
객체: 클래스 기반으로 생성된 실제 데이터

→ 본 프로젝트에서:

Quiz = 하나의 문제
QuizGame = 전체 게임 시스템
9-2. JSON 데이터 저장
JSON은 데이터를 저장하기 위한 형식
프로그램 종료 후에도 데이터를 유지할 수 있음

→ 본 프로젝트:

퀴즈 목록 저장
최고 점수 저장
9-3. 파일 입출력
with open("state.json", "r") as f:
    data = json.load(f)

→ 파일을 읽고 데이터를 가져오는 과정

9-4. 예외 처리 및 입력 검증
잘못된 입력 방지
프로그램 안정성 확보

예:

숫자가 아닌 입력 처리
범위 밖 숫자 처리
9-5. Git 활용 (과제 핵심)

본 프로젝트에서는 Git을 활용하여 다음을 수행했습니다.

기능 단위 커밋
브랜치 생성 및 병합
clone / pull 사용
10. Git 작업 흐름
git init
git add .
git commit -m "Init"

git checkout -b feature/play-quiz
git commit -m "Feat: 퀴즈 기능"
git checkout main
git merge feature/play-quiz

git clone ...
git pull
11. 학습 내용 정리

이 프로젝트를 통해 다음 내용을 학습할 수 있었습니다.

Python 기본 문법 (조건문, 반복문, 함수)
클래스와 객체 기반 설계
JSON 파일 저장 및 불러오기
사용자 입력 검증
Git을 활용한 협업 및 버전 관리
12. 1주차와의 연계

1주차에서는 개발 환경 구축과 Git 기본 명령어를 학습하였고,
2주차에서는 이를 기반으로 실제 Python 프로그램을 구현하였습니다.

이를 통해 이론적인 학습을 실제 코드로 확장하는 경험을 할 수 있었습니다.

13. 결론

본 프로젝트를 통해 단순한 문법 학습을 넘어,
프로그램 설계, 데이터 저장, 사용자 입력 처리, Git 활용까지
하나의 완성된 프로그램을 구축하는 경험을 할 수 있었습니다.
