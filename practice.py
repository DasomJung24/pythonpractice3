# writedata.py
"""
f = open("/Users/apple/Desktop/python2/새파일.txt", "w")
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()
"""
# readline.py
"""
f = open("/Users/apple/Desktop/python2/새파일.txt", 'r')
line = f.readline()
print(line)
f.close()
"""
# readline_all.py
'''
f = open("/Users/apple/Desktop/python2/새파일.txt", 'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()
'''
"""
f = open("/Users/apple/Desktop/python2/새파일.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()
"""
'''
f = open("/Users/apple/Desktop/python2/새파일.txt", 'r')
data = f.read()
print(data)
f.close()
'''
# adddata.py
f = open("/Users/apple/Desktop/python2/새파일.txt", 'a')
for i in range(11, 20):
    data = "%d 번째 줄입니다.\n" % i
    f.write(data)
f.close()