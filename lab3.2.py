import sys

def calculate_similar_rectangle(width, height, scale_factor):
    new_width = width * scale_factor
    new_height = height * scale_factor
    print(f"Розміри подібного прямокутника: {new_width} x {new_height}")

width = float(sys.argv[1])
height = float(sys.argv[2])
scale_factor = float(sys.argv[3])


calculate_similar_rectangle(width, height, scale_factor)