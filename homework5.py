immutable_var = (10, 15, "Q", "r", False)
print("Неизменяемый кортеж:",immutable_var)
# immutable_var[2] = "W" TypeError: 'tuple' object does not support item assignment
# Кортеж не поддерживает замену элементов
mutable_list=[12, 34, True, "T", "union"]
print("Список:", mutable_list)
mutable_list[2]= False
print("Изменённый список:", mutable_list)
