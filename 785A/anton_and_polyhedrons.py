""" Created by Shahen Kosyan on 3/15/17 """

if __name__ == "__main__":
    n = int(input())
    figures = []

    values = {
        'Tetrahedron': 4,
        'Cube': 6,
        'Octahedron': 8,
        'Dodecahedron': 12,
        'Icosahedron': 20
    }

    total = 0
    i = 0
    
    while i < n:
        figures.append(input())
        total += values[figures[i]]
        i += 1

    print(total)
