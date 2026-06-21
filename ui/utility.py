import pyray as pr


def center_text(text, width, height, font_size):
    x = width // 2 - pr.measure_text(text, font_size) // 2
    y = height // 2
    return x, y
