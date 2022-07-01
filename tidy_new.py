import pandas as pd
info_ = pd.read_excel('sales_data.xlsx')
df = pd.DataFrame(info_)

print(df.isna().any())

df['FREQUENCY BY ACTIVITY'] = df.iloc[:,8:10].sum(axis=1)
df['RFM_TOTAL_VALUE_TESTING'] = df['REVENUE'] + df['FREQUENCY BY ACTIVITY']
df['RFM_VALUE_ACTUAL'] = df['RFM_TOTAL_VALUE_TESTING'] - df['REVENUE']
df['MONDAY ACTIVITY'] = df['MONDAY_ORDERS'] + df['MONDAY_REVENUE']
df['TUESDAY_ACTIVITY'] = df['TUESDAY_ORDERS'] + df['TUESDAY_REVENUE']
df['WEDNESDAY_ACTIVITY'] = df['WEDNESDAY_ORDERS'] + df['WEDNESDAY_REVENUE']
df['THURSDAY_ACTIVITY'] = df['THURSDAY_ORDERS'] + df['THURSDAY_REVENUE']
df['FRIDAY_ACTIVITY'] = df['FRIDAY_ORDERS'] + df['FRIDAY_REVENUE']
df['SATURDAY_ACTIVITY'] = df['SATURDAY_ORDERS'] + df['SATURDAY_REVENUE']
df['SUNDAY_ACTIVITY'] = df['SUNDAY_ORDERS'] + df['SUNDAY_REVENUE']
df['WEEK1_ACTIVITY'] = df['WEEK1_DAY01_DAY07_ORDERS'] + df['WEEK1_DAY01_DAY07_REVENUE']
df['WEEK2_ACTIVITY'] = df['WEEK2_DAY08_DAY15_ORDERS'] + df['WEEK2_DAY08_DAY15_REVENUE']
df['WEEK3_ACTIVITY'] = df['WEEK3_DAY16_DAY23_ORDERS'] + df['WEEK3_DAY16_DAY23_ORDERS']
df['WEEK4_ACTIVITY'] = df['WEEK4_DAY24_DAY31_ORDERS'] + df['WEEK4_DAY24_DAY31_REVENUE']

print(df.columns)
print(df.head())

excel_file = pd.ExcelWriter('New_Sales_DF.xlsx')
df.to_excel(excel_file)
excel_file.save()

