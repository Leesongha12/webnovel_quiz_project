from quiz import get_default_quizzes


class QuizGame:
    def __init__(self):
        self.quizzes = get_default_quizzes()
        self.best_score = 0

    def show_menu(self):
        print("\n========================================")
        print("        🎯 나만의 퀴즈 게임 🎯")
        print("========================================")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 목록")
        print("3. 점수 확인")
        print("4. 종료")
        print("========================================")

    def get_menu_choice(self):
        while True:
            user_input = input("선택: ").strip()

            if user_input == "":
                print("⚠️ 빈 입력입니다. 1~4 사이의 숫자를 입력하세요.")
                continue

            if not user_input.isdigit():
                print("⚠️ 잘못된 입력입니다. 1~4 사이의 숫자를 입력하세요.")
                continue

            choice = int(user_input)

            if choice < 1 or choice > 4:
                print("⚠️ 잘못된 입력입니다. 1~4 사이의 숫자를 입력하세요.")
                continue

            return choice

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
        if score > self.best_score:
            self.best_score = score
            print("🎉 새로운 최고 점수입니다!")
        print("========================================")

    def show_quiz_list(self):
        if not self.quizzes:
            print("\n등록된 퀴즈가 없습니다.")
            return

        print(f"\n📋 등록된 퀴즈 목록 (총 {len(self.quizzes)}개)")
        print("----------------------------------------")
        for index, quiz in enumerate(self.quizzes, start=1):
            print(f"[{index}] {quiz.question}")
        print("----------------------------------------")

    def show_best_score(self):
        if self.best_score == 0:
            print("\n🏆 아직 퀴즈를 풀지 않았습니다.")
        else:
            print(f"\n🏆 최고 점수: {self.best_score}점")

    def run(self):
        while True:
            self.show_menu()
            choice = self.get_menu_choice()

            if choice == 1:
                self.play_quiz()
            elif choice == 2:
                self.show_quiz_list()
            elif choice == 3:
                self.show_best_score()
            elif choice == 4:
                print("\n프로그램을 종료합니다.")
                break
