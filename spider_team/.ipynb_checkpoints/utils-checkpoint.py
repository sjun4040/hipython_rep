
# 공통 유틸리티 함수

def get_valid_number_input(prompt, min_value, max_value):
    try:
        user_input = input(prompt)
        number = int(user_input)
        if min_value <= number <= max_value:
            return number
        else:
            print(f"⚠️ {min_value}부터 {max_value} 사이의 숫자를 입력해주세요.")
            return None
    except ValueError:
        print("⚠️ 숫자만 입력해주세요.")
        return None
