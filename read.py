data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 10000 == 0:
			print(len(data))

print('讀取完成，共有', len(data), '筆資料')

sum_length = 0
for d in data:
	sum_length = sum_length + len(d)

print('每一筆的平均長度為', sum_length/len(data), '個字')

wc = {}
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1

for word in wc:
	if wc[word] > 1000:
		print(word, wc[word])

print(len(wc))
print(wc['Allen'])

while True:
	word = input ('請問你查什麼字？')
	if word == 'q':
		break
	if word in wc:
	    print(word, '出現的次數：', wc[word])
	else:
		print('沒有出現過喔！')  


print('感謝查詢')
