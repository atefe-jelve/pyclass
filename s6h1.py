#ATEFE-JELVE__THURSDAY14-18
#SUM-NUMBERS-IN-RANGE-1_1000-DIV-BY-3
# sum_ = 0
# div3 = list()
# for i in range(0,1001):
#     div_ = i % 3
#     if div_ == 0:
#         sum_ = sum_ + i
#         div3.append(i)
# print(div3)
# print(f' sum of numbers that is div by 3 is: {sum_} ')

sum_ = 0
div3 = list()
i = 0
while i < 1001:
    div_ = i % 3
    if div_ == 0:
        sum_ = sum_ + i
        div3.append(i)
    i = i + 1
print(div3)
print(f' sum of numbers that is div by 3 is: {sum_} ')
