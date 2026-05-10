#-----------------------------------------------------------------------------------------------------------------------------------------
from scapy.all import sniff # import all modules 
from engine.analyzer import analyze_packet # import the analyze_packet function from the analyzer module
import pandas as pd # to store the data in a structured format
import os           # for check the File 
from engine.ai_model import run_analysis # import the Aipro and getdata functions from the ai_model module

#---------------------------------------------------------------------------------------------------------------------------------------
CSV_FILE = "logs/network_traffic.csv" # define the name of the CSV file to store packet data
buffer = [] # create an empty list to store pocket data before writing to the csv file 

def save_data():
    global buffer
    # check if Packets are catched and stored in the buffer, if yes then save the data to the CSV file
    if buffer:
        #formet the data in the buffer as a DataFrame and save it to the CSV file
        df = pd.DataFrame(buffer)
        if  not os.path.exists(CSV_FILE):
            df.to_csv(CSV_FILE , index=False) # if the CSV file does not exist, create a new one and write the data to it
        else:
            df.to_csv(CSV_FILE, mode = 'a', header=False , index= False ) # if the CSV file already exists, append the new data to it without writing the header 
            #mode a mains append mode, header false means do not write the header again, index false means do not write the index column
        print(f"--- [OK] {len(buffer)} packets saved to logs/ ---")
        buffer = [] # List ko khali karo taaki naye packets aa sakein


def paket_cllBack(packet):
    global buffer
    #this function is called for each captured packet
    data = analyze_packet(packet)
    if data:
        buffer.append(data) # add the collected information about the packet to the buffer list
        print(f" packet detected: {data}")
        if len(buffer) >= 20:
            save_data()
    

print("--- Nexa IDS: Logging Started ---")
try:
    print("--- Nexa IDS: Logging Started ---")
    sniff(prn=paket_cllBack, store=0)
except KeyboardInterrupt:
    print("\n--- Logging Stopped by User ---")
finally:
    # 1. Sabse pehle buffer mein bacha hua data file mein daalo
    if buffer:
        print(f"[+] Recovering {len(buffer)} packets from buffer...")
        save_data() 
    
    # 2. Jab file mein data save ho jaye, TAB analysis chalao
    print("[*] Launching Final Analysis...")
    run_analysis() 
    
    print("--- Goodbye ---")

