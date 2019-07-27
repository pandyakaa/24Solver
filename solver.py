''' 24 Game Solver '''

from itertools import permutations, product

# Some utils
ops = ['+','-','/','*']

# For permuting number and ops
def numiter(a,b,c,d) :
    newlist = []
    newlist.append(a)
    newlist.append(b)
    newlist.append(c)
    newlist.append(d)

    listnum = permutations(newlist)

    return listnum

def opsiter() :
    listops = [p for p in product(ops, repeat=3)]

    return listops

# Function main
def solve(a,b,c,d) :
    listnum = numiter(a,b,c,d)
    listops = opsiter()

    temp = []
    for i in listnum :
        for j in listops :
            temp.append(f"(({i[0]} {j[0]} {i[1]}) {j[1]} {i[2]}) {j[2]} {i[3]}")
            temp.append(f"({i[0]} {j[0]} ({i[1]} {j[1]} {i[2]})) {j[2]} {i[3]}")
            temp.append(f"{i[0]} {j[0]} ({i[1]} {j[1]} ({i[2]} {j[2]} {i[3]}))")
            temp.append(f"{i[0]} {j[0]} (({i[1]} {j[1]} {i[2]}) {j[2]} {i[3]})")
            temp.append(f"({i[0]} {j[0]} {i[1]}) {j[1]} ({i[2]} {j[2]} {i[3]})")
    
    res = set([])
    for i in temp :
        try :
            num = eval(i)
            if (abs(num-24) < 0.0000001) :
                res.add(i)
        except ZeroDivisionError :
            pass
    
    return res

# Main Function
if __name__ == "__main__":
    a,b,c,d = list(map(str,input().split(" ")))
    temp = solve(a,b,c,d)
    for i in temp :
        print(i)