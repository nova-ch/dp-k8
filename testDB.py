
import pandas as pd
import json
import oracledb
from time import time

database_user = "atlas_pandaredwood_r"
database_password = "N4FFt*4n0McVj+"
dsn="adcr-s.cern.ch:10121/adcr_panda.cern.ch"

def main():
    try:
        # Establish a connection to Oracle
        print("Connecting to the database...")
        conn = oracledb.connect(user=database_user, password=database_password, dsn=dsn)
        print("Connection established successfully!")

        # Define SQL query
        query = """
        SELECT jeditaskid,
         json_value(taskparams,'$.cpuTime') as cpuTime ,
         json_value(taskparams,'$.ramCount') as ramCount,
         json_value(taskparams,'$.nEventsPerInputFile') as nEventsPerInputFile,
         json_value(taskparams,'$.nEventsPerJob') as nEventsPerJob,
         json_value(taskparams,'$.architecture') as architecture,
         json_value(taskparams, '$.ipConnectivity') as ipConnectivity,
         json_value(taskparams, '$.nFilesPerJob') as nFilesPerJob
        FROM atlas_panda.jedi_taskparams
        WHERE jeditaskid = 39891107
        """

        # Execute the query
        print("Executing query...")
        df = pd.read_sql(query, con=conn)

        # Output the DataFrame information
        print("Query executed successfully!")
        print(df.head())
        print("DataFrame shape:", df.shape)

    except oracledb.DatabaseError as e:
        # Handle database connection errors
        error, = e.args
        print("Database connection error:", error.message)

    finally:
        # Ensure the connection is closed
        if 'conn' in locals() and conn is not None:
            conn.close()
            print("Connection closed.")

if __name__ == "__main__":
    main()
