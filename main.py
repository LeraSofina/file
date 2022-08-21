with open ('1.txt', 'r', encoding='utf-8') as file1:
    file_1 = file1.read()
    lines = str(file_1.count('\n') + 1)
    name1 = '1.txt'
    content1_info = [name1, lines, file_1]
    content1 = '\n'.join(content1_info)


with open ('2.txt', 'r', encoding='utf-8') as file2:
    file_2 = file2.read()
    lines = str(file_2.count('\n') + 1)
    name2 = '2.txt'
    content2_info = [name2, lines, file_2]
    content2 = '\n'.join(content2_info)


with open ('3.txt', 'r', encoding='utf-8') as file3:
    file_3 = file3.read()
    lines = str(file_3.count('\n') + 1)
    name3 = '3.txt'
    content3_info = [name3, lines, file_3]
    content3 = '\n'.join(content3_info)


new_file_content = [content1, content2, content3]
new_file_content.sort(key=len)
new_file = '\n'.join(new_file_content)


with open ('4.txt', 'x', encoding='utf-8') as file4:
    file4.write(new_file)










