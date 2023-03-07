
from app.db.session import engine
from sqlalchemy import inspect

class DBUtil():
    
    
    def get_schema_details(self):
        # [sales('sales_nr', 'customer_nr', 'staff_nr', 'shop_nr', 'date', 'sum_total'), sales_details('product_code','sales_nr','quantity')] 
        schema=[]
        tables = inspect(engine).get_table_names()
        for table in tables:
            table_schema = f'''{table}('''
            columns = self.get_columns(table)
            for column in columns:
                table_schema += f"""'{column}',"""

            table_schema += ")"
            schema.append(table_schema)
        print(schema)
        return schema
       
    
    
    def get_tables(self):
        tables = inspect(engine).get_table_names()
        # print(tables)
        return tables
    
    
    def get_columns(self, table:str):
        column_names = []
        columns = inspect(engine).get_columns(table)
        for column in columns:
            column_names.append(column["name"])
        # print(column_names)
        return column_names

db_util = DBUtil()