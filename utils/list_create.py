import os

file_list = os.listdir('C:/Users/JEON_SANGEON/codestates/TIL/test')


file_name = []
for file in file_list:
    if file.count(".") == 1:
        name = file.split('.')[0]
        file.name.append(name)
    else:
        for k in range(len(file)-1,0,-1):
            if file[k]=='.':
                file_name.append(file[k])
                break

print(file_name)