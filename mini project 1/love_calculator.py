boy = input("Enter boy's name: ").lower()
girl = input("Enter girl's name: ").lower()
char_list1 = list(boy)
char_list2 = list(girl)

char_list = char_list1 + char_list2
score_true = (
char_list.count("t")+
char_list.count("r")+
char_list.count("u")+
char_list.count("e")
)

score_love = (
char_list.count("l")+
char_list.count("o")+
char_list.count("v")+
char_list.count("e")
)

print(f"{score_true}{score_love}")
