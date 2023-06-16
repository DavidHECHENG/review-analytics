data = []
count = 0
with open ("reviews.txt","r") as f :
    for line in f :
        data.append(line)
        count = count + 1 #count += 1
        if count % 1000 == 0 :
            print(len(data))

sum_len = 0
with open ("reviews.txt","r") as f :
    for line in f :
        data.append(line)
        sum_len = sum_len + len(line)
print('平均留言長度為：', sum_len / len(data) )