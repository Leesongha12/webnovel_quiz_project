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


def get_default_quizzes():
    return [
        Quiz(
            "웹소설에서 자주 등장하는 '북부 대공' 캐릭터의 특징으로 가장 적절한 것은?",
            [
                "밝고 사교적인 성격으로 파티를 즐긴다",
                "따뜻하고 감정 표현이 풍부하다",
                "냉정하고 과묵하며 강한 권력을 가진다",
                "평범한 시민 출신으로 모험을 떠난다"
            ],
            3
        ),
        Quiz(
            "'로맨스 판타지' 장르에서 여주인공이 원작의 악녀나 조연으로 빙의했을 때, 생존을 위해 가장 먼저 취하는 공통적인 행동은?",
            [
                "원작 남주와 결혼하기",
                "파혼 선언 및 자산 확보",
                "마법 학교 입학",
                "황제 암살 계획"
            ],
            2
        ),
        Quiz(
            "웹소설 플랫폼에서 유료 회차를 결제하기 전, 무료로 제공되는 회차를 다 읽고 다음 회차를 기다리는 독자를 일컫는 말은?",
            [
                "유료 독자",
                "연독자",
                "기다무 이용자",
                "하차 독자"
            ],
            3
        ),
        Quiz(
            "현대 판타지 장르 중, 주인공이 특정 직업군(의사, 변호사, 요리사 등)에서 압도적인 능력을 발휘하는 서사를 무엇이라 하는가?",
            [
                "무협물",
                "전문가물",
                "아포칼립스물",
                "영지물"
            ],
            2
        ),
        Quiz(
            "다음 중 '회빙환(회귀, 빙의, 환생)' 서사에서 주인공의 성장을 시각적으로 보여주기 위해 가장 자주 사용되는 장치는?",
            [
                "종이 지도",
                "상태창(시스템창)",
                "전령구",
                "수정구슬"
            ],
            2
        )
    ]
