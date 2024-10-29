#Criação da uma DATAFRAME em python com a biblioteca PYTHON
import pandas as pd

nomes = {
        'Nome': ['Eduardo','Louyse','Patrícia','Maria'],
        'Idade': ['18','6','25','54']
}

dt = pd.DataFrame(nomes)
colunm = dt["Nome"]

#Adiconando uma nova coluna
dt["Cidade"] = ["Alto Alegre do Pindaré", "São Luís", "Alto Alegre do Pindaré", "Santa Luzia"]

colunmTwo = dt["Cidade"]

print(dt)
print('==================')
print(colunm)
print('==================')
print(colunmTwo)
print('==================')
print(list(dt.columns))
print('==================')
print(list(dt.index))
print('==================')
print(list(dt.shape))
