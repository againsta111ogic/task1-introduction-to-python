import json
import os
import xml.etree.ElementTree as ET
from db.db_connector import connect_to_db

def export_data(format: str):

    if not os.path.exists('output'):
        os.makedirs('output')
        
    db = connect_to_db()
    mycursor = db.cursor()

    with open('db/queries.sql', 'r') as f:
        queries = f.read().split(';')
        results = []
        for query in queries:
            mycursor.execute(query)
            results.append(mycursor.fetchall())

    if format == 'json':
        with open('output/output.json', 'w') as f:
            json.dump(results, f)
    elif format == 'xml':
        root = ET.Element('query_results')
        for result in results:
            for row in result:
                item = ET.SubElement(root, 'item')
                for key, value in row.items():
                    ET.SubElement(item, key).text = str(value)
        tree = ET.ElementTree('root')
        tree.write('output/output.xml')
                
    mycursor.close()
    db.close()
