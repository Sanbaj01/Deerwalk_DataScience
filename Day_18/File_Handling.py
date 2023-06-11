# try:
#     f = open('abc.txt', 'r')
# except FileNotFoundError:
#     print('file does not exist.')
# # print(f.read())

# # print(f.readline(1))
# # print(f.readlines())

# # for line in f.readlines():
# #     print(line.strip())

# f = open('abc.txt', 'w')
# f.write('a sathi timi kaha chau vana na \nlamo din kasari bitaune')

###NOTE- File opened in write mode cannot be read
###NOTE- Append mode : we can add file content, whereas in write mode it replaces old file content with new file content
#---APPEND----

# f = open('abc.txt', 'a')
# f.write('\ntyo galli ma chimeki karauthe saro')
# print(f.closed)
# f.close()
# print(f.closed)

# with open('abc.txt', 'r') as f:
#     print(f.read())

# print(f.read())

with open('myfile.txt','w') as f:
    f.write('This is my file.')
    
    