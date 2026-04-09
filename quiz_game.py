from quiz import get_default_quizzes


class QuizGame:
    def __init__(self):
        self.quizzes = get_default_quizzes()
        self.best_score = 0

    def play_quiz(self):
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return

        print(f"\n📝 퀴즈를 시작합니다! (총 {len(self.quizzes)}문제)")
        score = 0

        for index, quiz in enumerate(self.quizzes, start=1):
            print("\n----------------------------------------")
            print(f"[문제 {index}]")
            quiz.display()

            while True:
                user_input = input("정답 입력 (1-4): ").strip()

                if user_input == "":
                    print("⚠️ 빈 입력입니다. 1~4 사이의 숫자를 입력하세요.")
                    continue

                if not user_input.isdigit():
                    print("⚠️ 숫자를 입력하세요.")
                    continue

                user_answer = int(user_input)

                if user_answer < 1 or user_answer > 4:
                    print("⚠️ 1~4 사이의 숫자를 입력하세요.")
                    continue

                break

            if quiz.check_answer(user_answer):
                print("✅ 정답입니다!")
                score += 1
            else:
                print(f"❌ 오답입니다! 정답은 {quiz.answer}번입니다.")

        print("\n========================================")
        print(f"🏆 결과: {len(self.quizzes)}문제 중 {score}문제 정답!")
        print("========================================")

    def run(self):
        print("퀴즈 게임 프로젝트 시작")
        self.play_quiz()
