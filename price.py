
from jugaad_data.nse import NSELive
import numpy as np
import pandas as pd
import schedule
import time
def live_price():
  n = NSELive()
  nifty_data = n.live_index('NIFTY 50')
  price=(nifty_data['name'], nifty_data['timestamp'], nifty_data['data'][0]['lastPrice'])
  print(price)
  print(nifty_data['advance']['advances'])
live_price()
'''('NIFTY 50', '17-Aug-2023 13:32:57', 19350.6)
dict_keys(['name', 'advance', 'timestamp', 'data', 'metadata', 'marketStatus', 'date30dAgo', 'date365dAgo'])'''

def start_scheduler():
    def job():
        live_price()

    # Schedule the job to run at midnight
    schedule.every().day.at("00:00").do(job)

    # Start the scheduler loop
    while True:
        schedule.run_pending()
        time.sleep(1)

#start_scheduler()

#zip two list together to make one dictionary
def lists_to_dict(keys, values):
    if len(keys) != len(values):
        raise ValueError("Length of keys and values lists must be equal")
    return dict(zip(keys, values))


    
 
def list_nifty_stock():
  p = NSELive()
  q = p.live_index("NIFTY 50")
  comp=[]
  price=[]
  for idx in q['data']:
    comp.append(idx['identifier'])
    price.append(idx['lastPrice'])
# print (len(idx.keys()))"""this print shows the number ofcompanies"""
# print ('the company name is',idx['identifier'],'and the price is it',idx['lastPrice'])
  result_dict = lists_to_dict(comp,price) #zip two list together to make one dictionary
  #print (result_dict)
  result_dict = {k: [v] for k, v in result_dict.items()} # Output: Dictionary with lists as values: {'a': [1], 'b': [2], 'c': [3]}
  #print("Dictionary with lists as values:", result_dict)
  try:
    data = pd.DataFrame(result_dict)  # Create DataFrame from dictionary
    print("DataFrame:\n", data)
    #data.to_excel("result.xlsx", index=False)  """ Save DataFrame to Excel file without row indices"""
    #print("DataFrame successfully exported to 'output.xlsx'")
  except Exception as e:
    print(f"Error: {e}")
  
list_nifty_stock()

