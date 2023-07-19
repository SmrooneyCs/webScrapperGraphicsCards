from GraphicsCardPrices import describe_df_csv
import pandas as pd

df = pd.read_csv(r'C:/Users/Sean/Desktop\PythonProjects/webScrapperGraphicsCards/Graphic_data.CSV')
describe_df_csv(df ,'C:/Users/Sean/Desktop/PythonProjects/webScrapperGraphicsCards/graphic_card_math.csv', 'graphic_card_math.csv')
