id_list = [12364, 1535, 112, 1425]
id_income_dict = {12364: 25000, 1535: 16000, 1425: 10000, 112: 14500}
premium_set = set({})

for id_surname in id_list:
   if id_surname % 5 == 0:
      premium_set.add(id_surname)

print(f"premium_set = {premium_set}")
print(f"BEFORE: id_income_dict = {id_income_dict}")

for id_income in id_income_dict:
   if id_income in premium_set:
      id_income_dict[id_income] *= float(1.2)
      id_income_dict[id_income] = int(id_income_dict[id_income])
   else:
      id_income_dict[id_income] *= float(1.1)
      id_income_dict[id_income] = int(id_income_dict[id_income])

print(f"AFTER:  id_income_dict = {id_income_dict}")

# RESULT:
# premium_set = {1425, 1535}
# BEFORE: id_income_dict = {12364: 25000, 1535: 16000, 1425: 10000, 112: 14500}
# AFTER:  id_income_dict = {12364: 27500, 1535: 19200, 1425: 12000, 112: 15950}

