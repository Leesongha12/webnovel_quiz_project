import json
import os
from quiz import Quiz, get_default_quizzes


class QuizGame:
    def __init__(self):
        self.file_path = "state.json"
        self.quizzes = []
        self.best_score = 0
        self.load_data()

    def load_data(self):
        if not os.path.exists(self.file_path):
            print("📂 저장 파일이 없어 기본 퀴즈를 불러옵니다.")
            self.quizzes = get_default_quizzes()
            return

        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            self.best_score = data.get("best_score", 0)

            self.quizzes = []
            for q in data.get("quizzes", []):
                self.quizzes.append(
                    Quiz(q["question"], q["choices"], q["answer"])
                )

            print(f"📂 저장된 데이터를 불러왔습니다. (퀴즈 {len(self.quizzes)}개, 최고점수 {self.best_score})")

        except:
            print("⚠️ 파일이 손상되었습니다. 기본 데이터로 복구합니다.")
            self.quizzes = get_default_quizzes()
            self.best_score = 0

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

    def add_quiz(self):
        print("\n📌 새로운 퀴즈를 추가합니다.")

        question = input("문제를 입력하세요: ").strip()
        choices = []

        for i in range(4):
            choice = input(f"선택지 {i+1}: ").strip()
            choices.append(choice)

        while True:
            answer = input("정답 번호 (1-4): ").strip()

            if not answer.isdigit():
                print("⚠️ 숫자를 입력하세요.")
                continue

            answer = int(answer)

            if 1 <= answer <= 4:
                break
            else:
                print("⚠️ 1~4 사이 숫자 입력")

        self.quizzes.append(Quiz(question, choices, answer))
        self.save_data()

        print("✅ 퀴즈가 추가되었습니다!")

    def show_menu(self):
        print("\n========================================")
        print("        🎯 나만의 퀴즈 게임 🎯")
        print("========================================")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")
        print("========================================")

    def get_menu_choice(self):
        while True:
            user_input = input("선택: ").strip()

            if not user_input.isdigit():
                print("⚠️ 1~5 사이 숫자 입력")
                continue

            choice = int(user_input)

            if 1 <= choice <= 5:
                return choice
            else:
                print("⚠️ 1~5 사이 숫자 입력")

    def play_quiz(self):
        score = 0

        for quiz in self.quizzes:
            quiz.display()
            user_answer = int(input("정답: "))

            if quiz.check_answer(user_answer):
                score += 1

        print(f"결과: {score} / {len(self.quizzes)}")

        if score > self.best_score:
            self.best_score = score
            print("🎉 최고 점수 갱신!")

        self.save_data()

    def show_quiz_list(self):
        for i, q in enumerate(self.quizzes, 1):
            print(f"{i}. {q.question}")

    def show_best_score(self):
        print(f"🏆 최고 점수: {self.best_score}")

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
