import psycopg2
from psycopg2.extras import execute_values

def decorate_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f'Error: {e}')
    return wrapper

def insert_one(sql):
    try:
        conn = psycopg2.connect(f"dbname=try-postgis user=admin password=admin")
        cursor = conn.cursor()

        cursor.execute(sql)
        conn.commit()

    except Exception as e:
        print(f'Error: {e}')
    finally:
        conn.close()
        cursor.close()

def insert_multiple(sql, data):
    try:
        conn = psycopg2.connect(f"dbname=try-postgis user=admin password=admin")
        cursor = conn.cursor()

        execute_values(cursor, sql, data)
        conn.commit()

    except Exception as e:
        print(f'Error: {e}')
    finally:
        conn.close()
        cursor.close()

def run_query(sql):
    try:
        conn = psycopg2.connect(f"dbname=try-postgis user=admin password=admin")
        cursor = conn.cursor()

        cursor.execute(sql)
        result = cursor.fetchall()

        return result
    except Exception as e:
        print(f'Error: {e}')
    finally:
        conn.close()
        cursor.close()
    
