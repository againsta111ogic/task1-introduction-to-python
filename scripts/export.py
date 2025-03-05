import json
import os
import xml.etree.ElementTree as ET
from db.db_connector import connect_to_db

def export_data(format: str):

    if not os.path.exists('output'):
        os.makedirs('output')
        
    db = connect_to_db()
    mycursor = db.cursor(dictionary=True)

    with open('db/queries.sql', 'r') as f:
        queries = f.read().split(';')
        results = []
        for query in queries:
            query = query.strip()
            if query:
                try:
                    mycursor.execute(query)
                    results.append(mycursor.fetchall())
                except Exception as e:
                    print(f'Error occured during execution; {e}')
                    continue

    if format == 'json':
        structured_results = {
            f"query_{i+1}": result for i, result in enumerate(results)
        }
        with open('output/output.json', 'w') as f:
            json.dump(structured_results, f, indent=4, sort_keys=True)
            
    elif format == 'xml':
        root = ET.Element('query_results')
        for i, result in enumerate(results):
            query_element = ET.SubElement(root, f'query_{i+1}')
            for row in result:
                item = ET.SubElement(query_element, 'item')
                for key, value in row.items():
                    ET.SubElement(item, key).text = str(value)

        tree = ET.ElementTree(root)
        ET.indent(root, space='     ', level=0)
        tree.write('output/output.xml', encoding='utf-8', xml_declaration=True)
                
    mycursor.close()
    db.close()
