# 영수증 정렬 함수
def align_text(text, width, align='left'):
    text_width = wcswidth(text)
    space = width - text_width
    if space <= 0:
        return text
    if align == 'left':
        return text + ' ' * space
    elif align == 'right':
        return ' ' * space + text
    elif align == 'center':
        left = space // 2
        right = space - left
        return ' ' * left + text + ' ' * right