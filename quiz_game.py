from quiz import get_default_quizzes


class QuizGame:
    def __init__(self):
        self.quizzes = get_default_quizzes()
        self.best_score = 0

    def run(self):
        print("퀴즈 게임 프로젝트 시작")
        print(f"기본 퀴즈 개수: {len(self.quizzes)}")
