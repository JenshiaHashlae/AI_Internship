

import pandas as  pd
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
# data = {
#     'Product_id': [101,102,103,104,105],
#     'Product_name': ['Laptop', 'Smartphones', 'Tablet', 'Headphones', 'Camera'],
#     'Category' : ['Electronis','Electronis','Electronics','Accessories','Electronics'],
#     'Price': [1200,None, 300, 50, 600],
#     'Stock': [50, 100, 80, 200, 30]
# }
# print(data)
# df = pd.DataFrame(data)
# print(df)
# df['Price'].fillna(df['Price'].mean(), inplace=True)
# label_encoder = LabelEncoder()
# df['Product_name'] = label_encoder.fit_transform(df['Product_name'])
# df['Category'] = label_encoder.fit_transform(df['Category'])
# print(df)
# plt.scatter(df['Price'],df['Stock'])
# plt.title('Price vs Stock')
# plt.xlabel('Product price')
# plt.xlabel('Stock')
#plt.show()

data_with_missing = {
     'A': [1,2,None,4,5],
     'B': [None,2,3,None,5],
     'C':[1,None,3,4,None],
     'D': [None,None,None,None,None]
}
print(data_with_missing)
df = pd.DataFrame(data_with_missing)
print(df)
df['A'].fillna(df['A'].mean(), inplace=True)
df['B'].fillna(df['B'].mean(), inplace=True)
df['C'].fillna(df['C'].mean(), inplace=True)
df['A'].fillna(df['D'].mean(), inplace=True)
df['D'].fillna('1', inplace=True)

print(df)


