def symb_leg(a, b):
    if a % b == 0:
        return 0
    elif a == 1:
        return 1
    elif a == -1:
        return pow(-1, (b - 1) / 2)
    else:
        if a % 2 == 0:
            return symb_leg((a // 2), b) * pow(-1, (b * b - 1) / 8)
        else:
            return symb_leg(b - int(b / a) * a, a) * pow(-1, (b - 1) * (a - 1) / 4)


def find_non_ded(p):
    for i in range(1, p - 1):
        if symb_leg(i, p) == -1:
            return i


if __name__ == "__main__":
    a = int(input("Input deduction a: "))
    p = int(input("Input primal p: "))

    types = 0
    m = 0
    s = 0

    if p % 8 == 5:
        types = 1
        m = p // 8
    elif p % 4 == 3:
        types = 2
        m = p // 4
    elif p % 4 == 1:
        types = 3
        m = 0
        e = p - 1
        while e % 2 == 0:
            m += 1  # m is have to be >= 2
            e //= 2
        s = e
        t = (s + 1) // 2

    if symb_leg(a, p) == 1:
        first_sol = 0
        second_sol = 0
        if types == 1:
            if pow(a, 2 * m + 1, p) == 1:
                first_sol = pow(a, m + 1, p)
            else:
                first_sol = pow(pow(2, 2 * m + 1, p) * pow(a, m + 1, p), 1, p)
        elif types == 2:
            first_sol = pow(a, m + 1, p)
        else:
            b = find_non_ded(p)
            h = pow(b, s, p)
            c = pow(a, s, p)

            lst_j = []
            for i in range(0, m - 1):
                if i == 0:
                    eps = pow(c, pow(2, m - 2), p)
                    if eps == p - 1:
                        eps = -1
                    j_prev = pow((1 - eps) // 2, 1, p)
                    lst_j.append(j_prev)
                else:
                    sum_ = 0
                    for k in range(0, len(lst_j)):
                        sum_ += lst_j[k] * pow(2, m - i + k - 1)
                    eps = pow(pow(c, pow(2, m - 2 - i), p) * pow(h, sum_, p), 1, p)
                    if eps == p - 1:
                        eps = -1
                    j_prev = pow((1 - eps) // 2, 1, p)
                    lst_j.append(j_prev)
            j = 0
            for k in range(0, len(lst_j)):
                j += lst_j[k] * pow(2, k)

            first_sol = pow(pow(a, t, p) * pow(h, j, p), 1, p)
        second_sol = p - first_sol

        print(f"Equation has solution: {first_sol} mod {p}, {second_sol} mod {p}")
    elif symb_leg(a, p) == 0:
        print("Equation has solution: 0")
    else:
        print("Oh no, your equation has no solution")