# 載入panda模組
import pandas as pd 
# 建立 Series
data=pd.Series([20,10,15])
# 基本series操作
#print(data)
# print("Max", data.max())
# print("Median", data.median())
# data=data*2
# print(data)
# data=data==20
# print(data)


# 建立 DataFrame
data=pd.DataFrame({
    "name":["Amy","John","Bod"],
    "salary":[30000,50000,40000]

})
# 基本的 DataFrame操作
# print(data)
# 取得特地得欄位
# print(data["name"])
# print(data["salary"])
# 取的特定得列
print(data)
print("=============")
# print(data.iloc[0]) # 印出第一列
print(data.iloc[1]) # 印出第二列