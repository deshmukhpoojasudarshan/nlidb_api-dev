
from app.crud.dao import dao
from sqlalchemy.orm import Session
from app.service.nl2sql_service import nl2sql_service


class QueryService():
    
    def execute_sql_query(self, sql:str, db:Session):
        return dao.execute_query(db,sql)
    
    def execute_nl_query(self,query:str, option:int, db:Session):
        sql = nl2sql_service.generate_sql(query,option)
        return dao.execute_query(db,sql)
        
   
    
            
queryservice = QueryService()