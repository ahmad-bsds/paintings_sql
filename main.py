import psycopg2
import pandas as pd
from sqlalchemy import create_engine


try:
    # Create the connection string
    conn_string = "postgresql://postgres:0177756@localhost/paintings"

    # Create the SQLAlchemy engine
    db = create_engine(conn_string)

    # Connect to the database
    conn = db.connect()

    # List of CSV files to import
    files = ['artist', 'canvas_size', 'image_link', 'museum_hours', 'museum', 'product_size', 'subject', 'work']

    # Import each CSV file into the database
    for file in files:
        df = pd.read_csv(f'{file}.csv')
        df.to_sql(file, con=conn, if_exists='replace', index=False)

    # Close the connection
    conn.close()
    print("Success!")

except:
    print("Little more efforts needed!")