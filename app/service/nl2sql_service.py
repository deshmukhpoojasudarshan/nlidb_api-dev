import openai
from app.core.config import settings
from app.util.db_util import db_util
from app.util import query_util
from app.service.gpt_service import gpt_service

class NL2SQLService():
    
 
    def generate_sql(self,query:str, option:int):
        
        if (option==1):
            schema = db_util.get_schema_details()
            gpt_query = (f'''Prompt: {query} \n Table: {schema} \n —- SQL Code:\n''')
            print(gpt_query)
            sql = gpt_service.get_response(gpt_query)
            return query_util.format_sql(sql)
        
        else:
            # call to BART Based model
            pass
    
            
nl2sql_service = NL2SQLService()