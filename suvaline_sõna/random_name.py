#from time import*
import string
import random
def id_generator(size = 8, chars = string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

siz = "6-Lk435h41P"
#print(id_generator())

print(id_generator(15, "679eYuIO-zxc-dF01"))

list1 = []
while False:
    check = id_generator(len(siz), siz)
    if not check in list1:
        list1.append(check)
        print(check)
    #sleep(0.05)

    if check == "312a":
        break
