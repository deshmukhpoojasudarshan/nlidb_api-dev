from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api import dependency
from app.service.query_service import queryservice
from app.service.nl2sql_service import nl2sql_service


router = APIRouter()

@router.get("/nl-query")
def query_result(query:str,option:int, db: Session = Depends(dependency.get_db)) -> Any:
    """
    Get SQL Query along with resultset.
    """
    return queryservice.execute_nl_query(query, option, db)

@router.get("/sql-query")
def sql_query(sql:str,db: Session = Depends(dependency.get_db)) -> Any:
    """
    Execute given SQL Query and return the result set.
    """ 
    return queryservice.execute_sql_query(sql,db)
    
@router.get("/nl-to-sql")
def nl_to_sql(query:str,option:int, db: Session = Depends(dependency.get_db)) -> Any:
    """
    Get SQL Query.
    """
    sql = nl2sql_service.generate_sql(query,option)
    return sql


    
