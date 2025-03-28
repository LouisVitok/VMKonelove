new_len_lrp = 0


class LRP:
    def __init__(self, start: int, polinom: int, outd=0):
        self.pol = polinom
        self.pos = 1 << 31
        self.n = 31
        if outd == 0:
            if polinom > start:
                while True:
                    if (self.pos & self.pol) == (1 << 31):
                        break
                    else:
                        self.pol = (self.pol << 1) % (2 ** 32)
                        self.n -= 1
            else:
                self.st = start
                while True:
                    if (self.pos & self.st) == (1 << 31):
                        break
                    else:
                        self.st = (self.st << 1) % (2 ** 32)
                        self.n -= 1
        else:
            self.n = outd

        global new_len_lrp
        new_len_lrp = self.n + 1

        self.pol_arr = self.conversion(polinom, self.n)

        self.cur_arr = self.conversion(start, self.n)
        self.start_arr = [self.cur_arr[i] for i in range(self.n)]
        self.lst = [self.cur_arr[i] for i in range(self.n)]

        self.new_b = self.generation(self.cur_arr, self.pol_arr, self.n) % 2

        self.cur_arr = self.shift(self.cur_arr, self.n, self.new_b)
        self.lst.append(self.new_b)

        number = 0
        while self.cur_arr != self.start_arr:
            if number > 2 ** self.n:
                break
            number += 1
            self.new_b = self.generation(self.cur_arr, self.pol_arr, self.n) % 2

            self.cur_arr = self.shift(self.cur_arr, self.n, self.new_b)
            self.lst.append(self.new_b)

    def shift(self, seq, n, new_):
        for i in range(n - 1):
            seq[i] = seq[i + 1]
        seq[n - 1] = new_
        return seq

    def conversion(self, a, w):
        j = 0
        a_arr = [0 for _ in range(w)]
        cat = 1 << (w - 1)
        while a != 0:
            a_arr[w - j - 1] = (a & cat) >> (w - 1)
            a = (a << 1) % (cat << 1)
            j += 1
        return a_arr

    def generation(self, lrp, pol, n):
        new_ = 0
        for i in range(n):
            new_ += lrp[i] * pol[i]
        return new_

    def __add__(self, other):
        sum_lst = []
        for i in range(len(self.lst)):
            sum_lst.append((self.lst[i] + other.lst[i]) % 2)
        return sum_lst

    def writ(self):
        print(''.join([str(x) for x in self.lst]))

    def __contains__(self, item):
        if len(self.lst) >= len(item):
            all_seq = [self.lst[i:i+len(item)] for i in range(len(self.lst) - len(item) + 1)]
            return item in all_seq
        return False

    def __getitem__(self, item):
        return self.lst[item]

# print("Input start of firts LFSR")
# a = int(input())
# print("Input polinom of firts LFSR")
# b = int(input())
# print("Input start of second LFSR")
# c = int(input())
# print("Input polinom of second LFSR")
# d = int(input())
b = 2053
d = 3330
k = 0
for a in range(1, 2048):
    for c in range(1, 2048):

        first = LRP(a, b)
        second = LRP(c, d)
        sum_ = first + second
        fix_new_len = new_len_lrp + 16
        print(a, c, fix_new_len, sum_[0:fix_new_len])
        st = sum_[0:fix_new_len]
        st_n = 0
        for i in range(fix_new_len):
            st_n += (2 ** i) * st[i]
        for i in range(1, 2 ** fix_new_len - 1):
            rez = LRP(st_n, i, fix_new_len)
            # if sum_[:len(sum_) - fix_new_len + 1] in rez:
            #     print(a, c, i, sum_[:len(sum_) - fix_new_len + 1], st_n)
            #     rez.writ()
            #     k += 1
            #     break
            fl = True
            for i in range(len(sum_) - fix_new_len + 1):
                if sum_[i] == rez[i]:
                    continue
                else:
                    fl = False
                    break
            if fl:
                print(a, c, i, sum_[:len(sum_) - fix_new_len + 1], st_n)
                rez.writ()
                k += 1
                break

print(k)
        # rez = LRP(st_n, 7759, fix_new_len)
        # if sum_[:len(sum_) - fix_new_len + 1] in rez:
        #     print(a, c, 7759, sum_[:len(sum_) - fix_new_len + 1], st_n)
        #     rez.writ()
        #     break

# print("Input start of firts LFSR")
# a = int(input())
# print("Input polinom of firts LFSR")
# b = int(input())
# print("Input start of second LFSR")
# c = int(input())
# print("Input polinom of second LFSR")
# d = int(input())
#
# first = LRP(a, b)
# second = LRP(c, d)
# sum_ = first + second
# fix_new_len = new_len_lrp + 4
# print(a, c, fix_new_len)
# st = sum_[0:fix_new_len]
# st_n = 0
# print(sum_[:len(sum_) - fix_new_len + 1])
# for i in range(fix_new_len):
#     st_n += (2 ** i) * st[i]
# for i in range(2, 2 ** fix_new_len - 1):
#     rez = LRP(st_n, i, fix_new_len)
#     if sum_[:len(sum_) - fix_new_len + 1] in rez:
#         print(a, c, i)
#         rez.writ()
#         break