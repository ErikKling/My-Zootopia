import json

def load_data(file_path):
    """ Loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)

animals_data = load_data('animals_data.json')

def get_data_from_file():
    html_content = ""

    for animal in animals_data:
        name = animal.get("name")
        diet = animal.get("characteristics", {}).get("diet")
        locations = animal.get("locations", [])
        location = locations[0] if locations else None
        type = animal.get("characteristics", {}).get("type")


        html = '<li class="cards__item">\n'

        if name:
            html += f"Name: {name}<br>\n"
        if diet:
            html += f"Diet: {diet}<br>\n"
        if location:
            html += f"Location: {location}<br>\n"
        if type:
            html += f"Type: {type}<br>\n"
        
        html += '</li>\n'

        html_content += html
    
    return f'<ul class="cards">{html_content}</ul>'

html_content = get_data_from_file()

with open('animals_template.html', "r") as template_file:
    template = template_file.read()

final_html = template.replace("__REPLACE_ANIMALS_INFO__", html_content)

with open('animals_page.html', "w") as output_file:
    output = output_file.write(final_html)