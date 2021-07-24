file = open(r'c:\Users\喻秋明\Desktop\test\score.txt','r',encoding='utf-8') 
file_lines = file.readlines()
file.close()
final_scores = [] 
print(file_lines)
for i in file_lines:
    data =i.split()    
    sum = 0                   
    for score in data[1:]:     
        sum = sum + int(score)     
    result = data[0]+str(sum)+'\n'    
    final_scores.append(result)
print(final_scores)
winner = open(r'c:\Users\喻秋明\Desktop\test\winner.txt','w',encoding='utf-8') 
winner.writelines(final_scores)
winner.close()