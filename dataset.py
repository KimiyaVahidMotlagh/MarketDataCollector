import yfinance as yf
import pandas as pd
from datetime import datetime

# تابعی برای دریافت داده‌های قیمتی از yfinance
def get_financial_data(symbol, start_date, end_date):
    data = yf.download(symbol, start=start_date, end=end_date)
    return data[['Open', 'High', 'Low', 'Close', 'Volume']]

# تعیین تاریخ شروع و پایان (تاریخ پایان به زمان کنونی تغییر یافته است)
start_date = '2021-01-01'
end_date = datetime.now().strftime('%Y-%m-%d')

# دریافت داده‌های مالی
gold_data = get_financial_data('GC=F', start_date, end_date)
crude_oil_data = get_financial_data('CL=F', start_date, end_date)
dollar_index_data = get_financial_data('DX=F', start_date, end_date)

# تغییر نام ستون‌ها برای تمایز بین شاخص‌ها
gold_data = gold_data.reset_index()
gold_data.columns = ['Date'] + [f"Gold_{col}" for col in gold_data.columns[1:]]

crude_oil_data = crude_oil_data.reset_index()
crude_oil_data.columns = ['Date'] + [f"CrudeOil_{col}" for col in crude_oil_data.columns[1:]]

dollar_index_data = dollar_index_data.reset_index()
dollar_index_data.columns = ['Date'] + [f"DollarIndex_{col}" for col in dollar_index_data.columns[1:]]

# ترکیب داده‌ها به یک دیتاست واحد با استفاده از merge و how='outer'
combined_dataset = pd.merge(gold_data, crude_oil_data, on='Date', how='outer')
combined_dataset = pd.merge(combined_dataset, dollar_index_data, on='Date', how='outer')
combined_dataset.set_index('Date', inplace=True)
print(combined_dataset.head(10))
