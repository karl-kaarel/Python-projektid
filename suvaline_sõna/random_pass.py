import string
import random
def id_generator(size = 20, chars = string.ascii_uppercase + string.digits):
    #return ''.join(random.choice(chars) for _ in range(size)
    code = ""
    for _ in range(size):
        code += "".join(random.choice(chars))
    return code
        
def id_generator1(size=20, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

#print(id_generator())
print(id_generator1())

#print(id_generator(4, "acdef"))
