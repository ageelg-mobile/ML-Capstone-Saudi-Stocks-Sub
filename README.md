# ML-Capstone-Saudi-Stocks-Sub
ML Engineer Capstone Project - Saudi Stocks
Machine Learning Nanodegree - Capstone Proposal
Using Machine Learning to Predict Saudi Stock Performance
1st December 2019
Proposal review URL https://review.udacity.com/#!/reviews/2044772

Code Instructions
The code is two parts,
- A mixer.py file that merges all the data files and dose the needed processing to generate
  combined.csv file 
- The iPython Notebook ML-Capstone-Saudi-Stocks.ipynb, which has the rest of the code
- an index of the data is provided in dataindex.txt

Index of 25 data files

Description                  Date Range                 File                Source
---------------              ------------               -------------       --------------------------------------------------------------   
Saudi Stock Index (TASI)     1/1/2006 - 11/28/2019      TASI.CSV            https://www.investing.com/indices/tasi-historical-data
Saudi SABIC                  1/1/2006 - 11/29/2019      SABIC.CSV           https://www.investing.com/equities/sa-basic-ind-historical-data
Saudi AlAhly Bank            11/13/2014 - 12/01/2019    ALAHLY.CSV          https://www.investing.com/equities/national-com-bnk-historical-data
Saudi AlRajhi Bank           1/1/2006 - 12/01/2019      ALRAJHI.CSV         https://www.investing.com/equities/al-rajhi-bank-historical-data
Saudi Telecom STC            1/1/2006 - 12/01/2019      STC.CSV             https://www.investing.com/equities/saudi-telecom-historical-data
Saudi Electric SCECO         1/1/2006 - 12/01/2019      SCECO.CSV           https://www.investing.com/equities/saudi-electric-historical-data
Oil	                         1/2/2003 - 11/28/2019      OIL.CSV             https://www.quandl.com/data/OPEC/ORB-OPEC-Crude-Oil-Price 
Gold                         1/2/2006 - 11/29/2019      GOLD.CSV            https://www.investing.com/commodities/gold-historical-data
Shanghai SSEC                1/4/2006 - 11/29/2019      SSEC.CSV            https://www.investing.com/indices/shanghai-composite-historical-data
Dow Jones                    1/3/2006 - 11/29/2019      DJI.CSV             https://finance.yahoo.com/quote/%5EDJI/history?p=%5EDJI
Dollar                       1/3/2006 - 11/29/2019      DOLLAR.CSV          https://www.investing.com/currencies/us-dollar-index-historical-data
NYSE                         1/3/2006 - 11/29/2019      NYSE.CSV            https://finance.yahoo.com/quote/%5ENYA/history?p=^NYA&.tsrc=fin-srch  
NASDAQ                       1/3/2006 - 11/29/2019      IXIC.CSV            https://finance.yahoo.com/quote/%5EIXIC/history?p=%5EIXIC
Nikkei                       1/4/2006 - 11/29/2019      N225.CSV            https://www.investing.com/indices/japan-ni225-historical-data
SAR vs Dollar                1/2/2006 - 11/29/2019      USDSAR.CSV          https://www.investing.com/currencies/usd-sar-historical-data
Karachi                      1/2/2006 - 11/29/2019      KARACHI.CSV         https://www.investing.com/indices/karachi-100-historical-data
Tel Aviv                     1/1/2006 - 11/29/2019      TA.CSV              https://www.investing.com/indices/ta25-historical-data
FTSE                         1/3/2006 - 11/29/2019      FTSE.CSV            https://www.investing.com/indices/uk-100-historical-data   
German DAX                   1/2/2006 - 11/29/2019      DAX.CSV             https://www.investing.com/indices/germany-30  
EURO vs Dollar               1/2/2006 - 11/29/2019      EURUSD.CSV          https://www.investing.com/currencies/eur-usd-historical-data
Dubai Fi Market DFM          8/3/2007 - 11/28/2019      DFM.CSV             https://www.investing.com/equities/dfm-historical-data
Gulf bank of Kuwait          1/2/2006 - 11/29/2019      GBKK.CSV            https://www.investing.com/equities/gulf-bank-historical-data
Egypt  EGX                   1/3/2006 - 12/01/2019      EGX.CSV             https://www.investing.com/indices/egx-100-historical-data
Russia RTS                   1/10/2006 - 11/29/2019     MOEX.CSV            https://www.investing.com/indices/mcx10-historical-data
Turky  BIST                  1/2/2006 - 11/29/2019      BIST.CSV            https://www.investing.com/indices/ise-100-historical-data
