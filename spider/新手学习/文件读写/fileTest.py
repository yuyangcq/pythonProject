#写文件
with open('d:\\sample.txt', 'a+') as f:
    f.write('Hello, world!\n')

#读文件
with open('d:\\sample.txt', 'r') as f:
    print(f.read())
