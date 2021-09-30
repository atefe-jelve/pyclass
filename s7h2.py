#ATEFE-JELVE__THURSDAY14-18
#SORT-NAME

name = ['atefe', 'ali' , 'mehdi' , 'tahere' ,'x']
print(name)
end = len(name)
for i in range(end):  # az 0 ta end va baes misge ke chand bar tekrar beshe halghe vagar na yeba nmire ta akhar charkhe
    for j in range(end-1-i): # -1 chon darim ezafe mikonim va az rage bishtar mishe  yeki "va" -i ham bekhatere inke akhari moratab shode dige niaz nist ezafe shemorde beshe
        if name[j]>name[j+1]:
            name[j],name[j+1]=name[j+1],name[j]
    # print(name)
print(name)
print(sorted(name))
###############################################################################
# def sort_isrt(name):
#     for i in range(1,len(name)):  #chon hamishe ba onsore 2 moghayese mishe 1 mizarim start ro
#         if name[i] < name[i - 1]:
#             j = i
#             while name[j] < name[j-1] and j > 0 :
#                 name[j] , name[j - 1] = name[j - 1] , name[j]  # har onsor ba onsore ghabli moghayese mishe
#                 print(j)
#                 j = j - 1
#                 print(name)
#     return name
#
# result = sort_isrt(name)
# print(result)
#
#
################################################################################


# def sort_slct(name):
#     for i in range(0, len(name)):
#         minn = 'xxxxxxxxxx'
#         index = 0
#         for j in range(i, len(name)):
#             if (name[j] < minn):
#                 minn = name[j]
#                 index = j
#                 name[index],name[i]=name[i],name[index]
#     return name
# result = sort_slct(name)
#
# print(result)
