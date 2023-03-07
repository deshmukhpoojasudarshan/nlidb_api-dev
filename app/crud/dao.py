from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

class DAO():
  
    def execute_query(self, db: Session, sql: str) :
        results = []
        cursor = db.execute(sql)
        results.append(jsonable_encoder([ row for row in cursor.fetchall() ]))
        return results
dao = DAO()        