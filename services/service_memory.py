import json
from datetime import date
            

def retrieve_memories(messages):
       if messages is not None and len(messages)>0:
              __create_daily_history(messages)
       else:
              messages = __read_daily_history()
       return messages

def __generate_file_name():
       today = str(date.today())
       file_name=f"chat_history//chat-{today}.json"
       return file_name     

def __create_daily_history(messages):
       with open(__generate_file_name(), "w", encoding='utf8') as outfile:
              json.dump(messages, outfile,indent=4, ensure_ascii=False)

def __read_daily_history():
       try:
              with open(__generate_file_name(), 'r') as openfile:
                     messages = json.load(openfile)
                     return messages     
       except FileNotFoundError:
              print("Log chat diario náo encontrado. Criando novo...")
              __create_daily_history([])  