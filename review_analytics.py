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

new = []
for d in data :
    if len(d) < 100 :
        new.append(d)
print('一共有',len(new),'筆留言長度小於100')
print(new[0])
print(new[1])


wc = {}
for d in data :
    words = d.split(' ')
    for word in words :
        if word in wc :
            wc[word] += 1

        else :
            wc[word] = 1

while True :
    word = input('請輸入您想查找的關鍵字：')
    if word == 'q' :
        print('感謝您使用本查詢功能！')
        break
    if word in wc :    
        print(word,'出現過的次數為：',wc[word])
    else :
        print('此單字不曾出現出現在留言之中！')