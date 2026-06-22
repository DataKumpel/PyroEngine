import pyray as pr


def center_text(text, width, height, font_size):
    x = width // 2 - pr.measure_text(text, font_size) // 2
    y = height // 2
    return x, y


def layout_vertical(area: pr.Rectangle, num_entries: int, spacing: int = 0) -> list[pr.Rectangle]:
    height = area.height // num_entries
    entries = []
    for i in range(num_entries):
        entries.append(pr.Rectangle(area.x, area.y + i * height - spacing // 2, area.width, height - spacing))
    return entries


def layout_horizontal(area: pr.Rectangle, num_entries: int, spacing: int = 0) -> list[pr.Rectangle]:
    width = area.width // num_entries
    entries = []
    for i in range(num_entries):
        entries.append(pr.Rectangle(area.x + i * width - spacing // 2, area.y, width - spacing, area.height))
    return entries
