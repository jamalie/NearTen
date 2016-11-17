#Given a non-negative number "num", return True if num is within 2 of a multiple of 10. Note: (a % b) is the remainder of dividing a by b, so (7 % 5) is 2. See also: Introduction to Mod

#near_ten(12) -> True
#near_ten(17) -> False
#near_ten(19) -> True

def near_ten(num):
    result = 0
    mTen = 10

    if num == 0 or num == 1:
        return True

    if num < mTen:
        if num < 8:
            return False

    if num > mTen:
        result  = num%mTen
        if abs(result) < 3:
            return True

    while mTen < num:
        mTen +=10

    result = mTen%num
    if abs(result) < 3:
        return True

    return False


print 10%4
print near_ten(1)
print near_ten(2)
print near_ten(3)
print near_ten(4)
print near_ten(8)
print near_ten(9)
print near_ten(19)

