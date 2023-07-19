#Sean Rooney
#Using selenium to grab the price element from a web browser
#Exporting to a CSV

import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from datetime import datetime
from pathlib import Path

def describe_df_csv(dataframe, absolute_path, relative_path ):
    #Trying to print anothe csv file with aggregate math functions created from pandas  dataframe.describe
    df = dataframe.describe(exclude=['O'])
    rp = Path(relative_path)
    date_time={'Date': [datetime.now()]}
    date_df = pd.DataFrame(date_time)
    try:
        absolute_path = rp.resolve(strict=True)
    except FileNotFoundError:

        df.to_csv(absolute_path, index=True, header=True)
        date_df.to_csv(absolute_path, mode='a',header=True,index=False)           
        print('Pandas Math description file created')
        
    else:
        df.to_csv(absolute_path,mode='a',index=True,header=False)    
        date_df.to_csv(absolute_path, mode='a',header=True,index=False) 
        print('Pandas Math description file updated') 
    



def main():
    if __name__ == "__main__":
        descriptionlist = []
        pricelists = []
        price_floats =[]
        date_time = []
        max_len = 0
        my_file = Path('Graphic_data.CSV')
        my_abs_path = 'C:/Users/Sean/Desktop/PythonProjects/webScrapperGraphicsCards/Graphic_data.CSV'
        



        options=Options()
        options.add_argument('--headless')
        options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
        driver = webdriver.Firefox( options = options, executable_path= r"D:\PythonProjects\webScrapperGraphicsCards\geckodriver.exe")
        driver.get('https://www.newegg.com/p/pl?d=3080')
        list_wrap = driver.find_element(By.CLASS_NAME,'list-wrap')
        page_length = list_wrap.find_element(By.CLASS_NAME, 'list-tool-pagination-text')
        length_num = page_length.find_elements(By.TAG_NAME, 'Strong')

        #getting the max number of pages to iterate thorugh all postings on the website
        for i in length_num[len(length_num)-1::-1]:
            page_range = i.text
            max_len = int(page_range.split('/',1)[1]) #split based on '/' repeating once keeping the second half of the split    

            

        #iteration and data cleaning for the price and description data from (website)
        for i in range(1,max_len):
            driver.get('https://www.newegg.com/p/pl?d=3080&page='+ str(i))
            list_wrap = driver.find_element(By.CLASS_NAME,'list-wrap')
            item_price = list_wrap.find_elements(By.CLASS_NAME, 'price-current')
            item_desc = list_wrap.find_elements(By.CLASS_NAME,'item-title')
            page_length = list_wrap.find_elements(By.CLASS_NAME, 'list-tool-pagination-text')
            #some data cleaning and then adding it to a dictionary to use with pandas DataFrame
            for i, p in enumerate(item_price):
                price = p.text
                stipped = price.split('(',1)[0].strip()
                float_number = stipped.replace('$','').strip()
                if float_number != '':
                    pricelists.append(float(float_number.replace(',','')))
                else:
                    pricelists.append(float_number)          
                
            for i, d in enumerate(item_desc):
                description = d.text
                descriptionlist.append(description) 

            for i in range(len(item_price)):
                current_date_time = datetime.now()
                date_time.append(current_date_time)           
            
        
        graphics_card_data = {'Description':descriptionlist,
                                'Price':pricelists,
                                'Date and Time':date_time}

        df = pd.DataFrame(graphics_card_data)

        try:
            my_abs_path = my_file.resolve(strict=True)
        except FileNotFoundError:
            # doesn't exist
            df.to_csv('C:/Users/Sean/Desktop/PythonProjects/webScrapperGraphicsCards/Graphic_data.CSV', index=False, header=True)
            #print(df)
            print('file created')
        else:
            # exists
            df.to_csv('C:/Users/Sean/Desktop/PythonProjects/webScrapperGraphicsCards/Graphic_data.CSV',mode='a',index=False,header=False)
            print('file updated')

        #calling this funiton to wrtie aggregate fucntions from Pandas and saving to a csv file user defined
        #describe_df_csv(df ,'C:/Users/Sean/Desktop/PythonProjects/webScrapperGraphicsCards/graphic_card_math.csv', 'graphic_card_math.csv')






start_time = datetime.now()
main()
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))

















        

