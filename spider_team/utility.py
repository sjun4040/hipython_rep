# 유틸리티 함수
# yes or no
def get_yes_or_no_input(msg):
    while True:
        user_input = input('>>>' + msg + " (yes/no): ").strip().lower()
        if user_input in ['yes', 'no']:
            return user_input
        else:
            print("⚠️'yes' 또는 'no'만 입력할 수 있어요.")