import time, random

ARR = (7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2)
LAST = ('1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2')

number_list = ['1852181','1852182','1852183','1852184','1831703','1832127','1832136','1832137','1801778','1801779','1801780','1801781','1832196','1832197','1851210','1851211','1851212','1851213','1881653','1881654','1881655','1881656','1881657']
def makeNew():
    t = time.localtime()[0]
    x = '%02d%02d%02d%04d%02d%02d%03d' %(random.randint(10,99),
                                        random.randint(01,99),
                                        random.randint(01,99),
                                        random.randint(t - 23, t - 19),
                                        random.randint(1,12),
                                        random.randint(1,28),
                                        random.randint(1,999))
    y = 0
    for i in range(17):
        y += int(x[i]) * ARR[i]

    return '%s%s' %(x, LAST[y % 11])

def gen_qq():
    length = random.randrange(7,11)
    start = 1
    qq = []
    while start <= length:
        if start is 1:
            qq.append(str(random.randrange(1,10)))
        else:
            qq.append(str(random.randrange(0,10)))
        start+=1
    return "".join(qq)+"@qq.com"

def gen_phone():
	last = ""
	for i in xrange(4):
		last = last + str(random.randrange(0,10))
	phone = number_list[random.randrange(0,23)] + last
	return phone



with open("together.txt","w") as f:
	for i in xrange(300):
		f.write("ID: " + makeNew() + "\n")
		f.write("QQ: " + gen_qq() + "\n")
		f.write("Phone: " + gen_phone() + "\n\n")

with open("E-mail.txt","w") as f:
	for i in xrange(300):
		f.write(gen_qq() + "\n")

with open("Phone.txt","w") as f:
	for i in xrange(300):
		f.write(gen_phone() + "\n")

with open("ID.txt","w") as f:
	for i in xrange(300):
		f.write(makeNew() + "\n")
