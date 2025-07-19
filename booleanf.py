from math import log

def num(x):
    s = 0
    for i in range(len(x)):
        s += x[i] * pow(2, i)
    return s


def f_win(e_v, k, win):
    e_v = e_v[k-1:k-1+win]
    for i in range(win // 2):
        e_v[i + win // 2] = (e_v[i + win // 2] + e_v[i]) % 2
    return e_v

def polinom(e_v):
    f_v = e_v[::]
    for i in range(int(log(len(f_v), 2))):
        win = pow(2, i + 1)
        k = 1
        while k < len(f_v):
            f_v[k - 1:k - 1 + win] = f_win(f_v, k, win)
            k += win
    return f_v

def f(f_v, x):
    return f_v[num(x)]


if __name__ == '__main__':
    n = int(input("number of values "))
    d = int(input("number of degree "))
    e = 0
    # for i in range(pow(2, n)):
    #     iv = '0' * (n - len( bin(i)[2:])) + bin(i)[2:]
    #     iv = [ord(x) - ord('0') for x in iv]
    #     iv = iv[::-1]
    #     cur = iv[::]
    # print(iv)
    # cur = [0 for _ in range(n)]
    iv = [0 for _ in range(n)]
    count = 0
    for j in range(pow(2, pow(2, n-1) - 2)):
        cur = iv
        s = set()
        s.add(num(cur))
        # s = list()
        # s.append(cur)
        r = '0' * (pow(2, n-1) - 2 - len(bin(j)[2:])) + bin(j)[2:]
        t = '1' + r[::-1] + '1'
        f_v = []
        for elem in t:
            if elem == '1':
                f_v.append(1)
                f_v.append(0)
            else:
                f_v.append(0)
                f_v.append(1)
        print(f_v)
        # f_v = '0' * (n - 2 - len(bin(j)[2:])) + bin(j)[2:]
        # f_v = [ord(x) - ord('0') for x in f_v]
        # f_v = f_v[::-1]
        # fl1 = False
        # for i in range(len(f_v) // 2):
        #     if f_v[2 * i] == f_v[2 * i + 1]:
        #         fl1 = True
        # if fl1:
        #     continue
        pol = polinom(f_v)
        fl = False
        # print(pol, f_v)
        q = 0
        for k in range(pow(2, n)):
            if pol[k] == 1:
                if bin(k)[2:].count('1') > q:
                    q = bin(k)[2:].count('1')
                if bin(k)[2:].count('1') > d:
                    fl = True
                    break
        if fl or q == 1:
            continue
        while True:
            new_b = f(f_v, cur)
            cur = cur[1:]
            cur.append(new_b)
            if num(cur) in s:
                # print(iv, f_v, s, pol)
                # print(iv, len(s))
                # print(len(s), f_v, e)
                if len(s) >= e:
                    e = len(s)
                    if e == pow(2, n):
                        print(11111111)
                        print(f_v)
                        count += 1
                        # exit()
                cur = iv
                break
            # if cur in s:
            #     print(iv, f_v, s, pol)
            #     cur = iv
            #     break
            else:
                s.add(num(cur))
                # s.append(cur)
    print(e)
    print(count)