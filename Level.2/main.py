def answer(lambs):
    totals = [generous(lambs), stingy(lambs)]
    difference = max(totals) - min(totals)
    return difference

def generous(lambs):
    num = 1
    while True:
        total = 2**(num) - 1
        if total <= lambs:
            num += 1
        else:
            num -= 1
            break
    return num

def stingy(lambs):
    num = 1
    last = 0
    cur = 1
    lambs -= 1
    while lambs > 0:
        if lambs < last + cur:
            break
        num += 1
        cur,last = cur + last , cur
        lambs -= cur

    return num
