# Web Novel Quiz Project

## 1. 프로젝트 개요

본 프로젝트는 Python을 활용하여 제작한 콘솔 기반 퀴즈 게임입니다.  
사용자는 퀴즈를 풀고, 문제를 추가하며, 데이터를 저장하고 다시 불러올 수 있습니다.  

본 과제의 핵심은 단순 기능 구현이 아니라  
**클래스 설계, 데이터 저장 구조, Git 활용, 예외 처리**를 실제 코드로 구현하는 것입니다.

---

## 2. 기능 구현 증빙

### 2-1. 메뉴 및 기능 실행 구조

```python
def run(self):
    while True:
        self.show_menu()
        choice = self.get_menu_choice()

        if choice == 1:
            self.play_quiz()
        elif choice == 2:
            self.add_quiz()
        elif choice == 3:
            self.show_quiz_list()
        elif choice == 4:
            self.show_best_score()
        elif choice == 5:
            print("종료합니다.")
            break
```

👉 while True를 통해 프로그램이 종료 전까지 반복 실행됨

---

### 2-2. 입력 검증 처리

```python
def get_menu_choice(self):
    while True:
        user_input = input("선택: ").strip()

        if not user_input.isdigit():
            print("⚠️ 숫자를 입력하세요.")
            continue

        choice = int(user_input)

        if 1 <= choice <= 5:
            return choice
        else:
            print("⚠️ 1~5 사이 숫자 입력")
```

👉 잘못된 입력 방지 (문자, 범위 초과 등)

---

### 2-3. JSON 저장 기능

```python
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
```

---

### 2-4. JSON 불러오기 + 손상 대응

```python
def load_data(self):
    try:
        with open(self.file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except:
        print("파일 손상 → 기본 데이터 복구")
        self.quizzes = get_default_quizzes()
        return
```

👉 JSON 손상 시 복구 처리

---

## 3. 기본 퀴즈 5개 증빙

```python
def get_default_quizzes():
    return [
        Quiz("북부 대공 특징?", [...], 3),
        Quiz("로판 생존 전략?", [...], 2),
        Quiz("기다무 뜻?", [...], 3),
        Quiz("전문가물 정의?", [...], 2),
        Quiz("상태창 역할?", [...], 2)
    ]
```

👉 최소 5개 이상 포함됨

---

## 4. 클래스 설계 구조

### Quiz 클래스 (단일 책임)
```python
class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer
```

👉 역할: “문제 데이터 관리”

---

### QuizGame 클래스 (전체 제어)
```python
class QuizGame:
```

👉 역할:
- 사용자 입력 처리
- 게임 흐름 제어
- 데이터 저장/로드

---

## 5. 설계 기준 (중요)

| 요소 | 이유 |
|------|------|
| 클래스 분리 | 역할 분리 (SRP 원칙) |
| JSON 사용 | 데이터 영속성 확보 |
| 리스트 구조 | 퀴즈 확장성 |
| 반복문 기반 메뉴 | CLI 환경 최적화 |

---

## 6. 데이터 구조 설계 이유

```json
{
    "quizzes": [],
    "best_score": 0
}
```

👉 이유:

- quizzes → 문제 확장 가능
- best_score → 별도 관리 (성능 효율)

---

## 7. Git 작업 증빙

### git log

```bash
git log --oneline
```

예시:

```
ec9749a Feat: 퀴즈 기능 구현
e30408d Feat: 퀴즈 데이터 연결
dfcf8ac Feat: Quiz 클래스 추가
baf8f7f Init
```

---

### 브랜치 사용

```bash
git checkout -b feature/play-quiz
git merge feature/play-quiz
```

---

### clone / pull

```bash
git clone ...
git pull
```

---

## 8. 프로그램 실행 결과

```
1. 퀴즈 풀기
2. 퀴즈 추가
3. 목록
4. 점수
5. 종료
```

---

## 9. 핵심 기술 적용 이유

### 클래스 사용 이유
- 데이터와 기능을 묶기 위함

### JSON 선택 이유
- 파일 기반 저장 가능
- DB 없이 구현 가능

### 예외 처리
- 사용자 입력 오류 방지
- 파일 손상 대응

---

## 10. 심층 분석 (인터뷰 대비)

### Q1. 데이터 많아지면?
→ JSON은 비효율 → DB 필요

### Q2. JSON 깨지면?
→ try-except 복구 처리

### Q3. 기능 추가 시?
→ QuizGame에 기능만 추가하면 확장 가능

---

## 11. 1주차와 연계

1주차에서 Git과 개발 환경을 구축하고,  
2주차에서는 이를 활용하여 실제 프로그램을 구현했습니다.

---

## 12. 결론

본 프로젝트를 통해  
단순 코드 작성이 아니라

- 설계
- 데이터 관리
- 예외 처리
- Git 흐름

을 종합적으로 학습할 수 있었습니다.
