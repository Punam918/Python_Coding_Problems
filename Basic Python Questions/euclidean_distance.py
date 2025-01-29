import math

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def main():
    x1, y1 = map(float, input("Enter the first coordinate (x1 y1): ").split())
    x2, y2 = map(float, input("Enter the second coordinate (x2 y2): ").split())
    
    distance = euclidean_distance((x1, y1), (x2, y2))
    print(f"The Euclidean distance between ({x1}, {y1}) and ({x2}, {y2}) is {distance}")

if __name__ == "__main__":
    main()