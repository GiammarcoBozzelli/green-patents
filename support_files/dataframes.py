#Import extreme weather events from EM-DAT
events = pd.read_excel("https://github.com/GiammarcoBozzelli/green-patents/raw/main/data/public_emdat_custom_request_2023-12-12_686c6667-5546-4cc0-a4b0-6062eb8d9e93.xlsx")
#Import Patents
patents = pd.read_csv("https://raw.githubusercontent.com/GiammarcoBozzelli/green-patents/main/data/PATS_IPC_13122023144148777.csv")
#Import GDP per Cap
GDPCap =  pd.read_excel("https://github.com/GiammarcoBozzelli/green-patents/raw/main/data/GDPperCAP_WB.xls")
#FDI from WB 266 coountries
FDI_WB = pd.read_csv("https://raw.githubusercontent.com/GiammarcoBozzelli/green-patents/main/data/API_BX.KLT.DINV.CD.WD_DS2_en_csv_v2_5995288(1).csv", header = 2)
#import climate worriness dataset (https://dataforgood.facebook.com/dfg/tools/climate-change-opinion-survey)
climate_worriness = pd.read_excel('https://github.com/GiammarcoBozzelli/green-patents/raw/main/data/climate_change_opinion_survey_2022_aggregated(1).xlsx',sheet_name = "climate_worry")
#import Education tertiary enrolmnet %
education = pd.read_csv('https://raw.githubusercontent.com/GiammarcoBozzelli/green-patents/main/data/b449f249-9a23-4840-b2cf-45c78ad26ef9_Data.csv')
#import pop
population = pd.read_excel("https://github.com/GiammarcoBozzelli/green-patents/raw/main/data/API_SP.POP.TOTL_DS.xls")
#final consumption ad % of GDP
consumption = pd.read_csv('https://raw.githubusercontent.com/GiammarcoBozzelli/green-patents/main/data/73da1b2c-1935-485e-af2c-b0b61b733993_Data.csv')
                                   
