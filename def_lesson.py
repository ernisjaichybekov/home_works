# def main(name,age):
#     return f'pribet {name},mne {age} let'
# print(main(name='ernis',))
#
# '''
# main(name='aman') - aaaa
# main(ernis) - eeee
# def main(name= ernis) - dddddd
# # '''
# def custom_sum(*args):
#     return sum(args)
# print(custom_sum(2,4,5,6,6,7,7,2,4,5))


# def info(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key}: {value}")
#
# info(name="anna", age=25, city="mockva")
# info(width=20, hight=20)
#
# def create_profile()
# create_profile("чтение", "спорт", name="Иван", age=30)
# create_profile("программирование", "музыка", city="Москва", job="Разработчик")

def create_profile(*hobbies, **info):
    if hobbies:
        print(f"Хобби: {', '.join(hobbies)}")
    for key, value in info.items():
        print(f"{key}: {value}")
    print()

create_profile("чтение", "спорт", name="Иван", age=30)
create_profile("программирование", "музыка", city="Москва", job="Разработчик")