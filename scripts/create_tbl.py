
from sqlalchemy import (
    create_engine,
    text
)
import yaml
import os
from dotenv import load_dotenv
import click

load_dotenv(".env",override=True)

@click.command()
@click.option('-t', '--table', required=True, help="The name of the table key in the config to create.")
def main(table: str):

    # Open and read the YAML file
    with open("config/config.yaml", "r") as file:
        config = yaml.safe_load(file)

    sql_location = config['sql']['ddl'][table]

    db_uri = os.environ.get('DB_URI')

    with open(sql_location) as file:
        query = file.read()
        file.close()
    queries = query.split(';')

    engine = create_engine(db_uri,echo=True)

    with engine.connect() as conn:
        # Execute the SQL query to create the table
        with engine.connect() as conn:
            for q in queries:
                q = q.strip()
                if q:  # Make sure not to execute empty statements
                    conn.execute(text(q))
        
    print(f"Table {table} created successfully!")

if __name__=='__main__':
    main()