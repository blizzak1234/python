from model.contact import Contact
import random
import string



# #случайные строки для имени
# def random_string(prefix, maxlen):
#     symbols = string.ascii_letters + " "*10
#     return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
#
# #случайные строки для имейла
# def random_string_email(prefix, maxlen):
#     symbols = string.ascii_letters + string.digits
#     return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + "@" + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + "." + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
#
# #случайные строки для телефона
# def random_string_phone(prefix, maxlen):
#     symbols = string.digits
#     return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
#
# #случайные строки для адреса
# def random_string_add(prefix, maxlen):
#     symbols = string.ascii_letters + string.digits + " "*10
#     return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


# testdata = [Contact(F_name=random_string("fn_", 5), L_name=random_string("ln_", 5),
#                     C_address=random_string_add("addr", 5), H_phone=random_string_phone("hom_", 7),
#                     M_phone=random_string_phone("mob_", 10), W_phone=random_string_phone("wor_", 8),
#                     S_phone=random_string_phone("sec_", 9), C_email=random_string_email("email_", 4))]



# testdata = [Group(name="", header="", footer="")] + [
#     Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20))
#     for i in range(n) #цикл для генерации случайных данных. 5 раз. то есть все данные для теста будут состоять из одной пустой группы и 5 групп со случ. данными
#]

testdata = [Contact(F_name="fn_", L_name="ln_",
                    C_address="addr", H_phone="562456",
                    M_phone="235423543", W_phone="25462456",
                    S_phone="2352354", C_email="email@fake.rt")]
