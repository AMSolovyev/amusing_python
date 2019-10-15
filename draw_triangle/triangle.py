def draw_triangle(limit, current = 1):
    if current > limit:
        return
        
    print((' ' * int((limit - current) / 2)) + ('*' * current))
    draw_triangle(limit, current + 1)

if __name__ == '__main__':
    draw_triangle(limit = 34)