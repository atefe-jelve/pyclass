#ATEFE-JELVE__THURSDAY14-18
#SUM-NUMBERS-BETWEEN-1000_2000-BY-FOR
list_ = list()
sum_ = 0
for i in range(1000,2000):
    if i % 2 != 0:
        list_.append(i)
        sum_ = sum_ + i
print(list_)
print(sum_)
