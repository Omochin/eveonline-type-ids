import os
import zipfile
import shutil
import csv
import yaml

def generate_html(type_ids):
    csv_list = []
    html = '<!DOCTYPE html><html><head><title>Type IDs</title>'
    html += '<meta charset="UTF-8"><link rel="stylesheet" type="text/css" href="./type_ids.css"></head><body>'
    html += '<p><a href="./Type IDs.csv" download>Download Type IDs.csv</a></p>'
    html += '<table><tr><th>ID</th><th>Name</th></tr>'
    for i, items in type_ids.items():
        type_id = str(i)
        try:
            type_name = str(items['name']['en'])
        except KeyError:
            type_name = ''

        csv_list.append([type_id, type_name])
        html += '<tr><td>' + type_id + '</td>'
        html += '<td>' + type_name + '</td></tr>'
    html += '</table></body></html>'

    with open('./docs/Type IDs.csv', 'w', encoding='utf-8') as file:
        csv.writer(file, lineterminator='\n').writerows(csv_list)

    with open('./docs/index.html', 'w', encoding='utf-8') as file:
        file.write(html)

def main():
    if not os.path.isdir('./docs/'):
        os.mkdir('./docs/')

    shutil.copy('./type_ids.css', './docs/type_ids.css')
    for filename in os.listdir():
        base, ext = os.path.splitext(filename)
        if ext == '.zip' and 'sde-' in base and '-TRANQUILITY' in base:
            with zipfile.ZipFile(filename) as zfile:
                with zfile.open('sde/fsd/typeIDs.yaml') as type_ids_yaml:
                    generate_html(yaml.load(type_ids_yaml))
            break

if __name__ == '__main__':
    main()
