def check_triangle(side_a, side_b, side_c) -> bool:
    if side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a:
        print("Possible triangle")
        return True
    else:
        print("Impossible triangle")
        return False


if __name__ == '__main__':
    side_a = float(input("input side a: "))
    side_b = float(input("input side b: "))
    side_c = float(input("input side c: "))
    answer = check_triangle(side_a, side_b, side_c)
    print(answer)
