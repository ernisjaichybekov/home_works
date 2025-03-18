# def season(month):
#     if month in [12, 1, 2]:
#         return "Winter"
#     elif month in [3, 4, 5]:
#         return "Spring"
#     elif month in [6, 7, 8]:
#         return "Summer"
#     elif month in [9, 10, 11]:
#         return "Autumn"
#     else:
#         return "Error"


# print(season(1))
# print(season(3))
# print(season(6))
# print(season(9))
# print(season(13))



def is_date(day,month,year):
    from datetime import date
    return date(year,month,day)
print(is_date(18,3,2025))
print(is_date(29,2,2025))


def func(a,b,c):
    pass
func(1,2,3)