def user_info(**kwargs):
    return kwargs


# простой вариант решения без запроса у пользователя значений
print(user_info(name='Ivan', surname='Ivanov', birth_year='2000', town='Moscow',
                email='ivanov@mail.ru', phone='33-33-33'))
