import json
import data_fetcher
    

def serialize_animal(animal):
    """
    Converts a single animal dictionary into an HTML <li> element
    using the predefined CSS classes and formatting.
    """
    name = animal.get("name")
    diet = animal.get("characteristics", {}).get("diet")
    locations = animal.get("locations", [])
    location = locations[0] if locations else None
    type = animal.get("characteristics", {}).get("type")

    html = '<li class="cards__item">\n'

    if name:
        html += f'<div class="card__title">{name}</div>\n'

    html += '<p class="card__text">\n'

    if diet:
        html += f"<strong>Diet:</strong> {diet}<br>\n"
    if location:
        html += f"<strong>Location:</strong> {location}<br>\n"
    if type:
        html += f"<strong>Type:</strong> {type}<br>\n"

    html += '</p>\n</li>\n'

    return html


def get_data_from_file(animals_data):
    """
    Loops through all animals and returns a complete HTML <ul> list
    with each animal rendered as an HTML card.
    """
    html_content = ""

    for animal in animals_data:
        html_content += serialize_animal(animal)

    return f'<ul class="cards">\n{html_content}</ul>'


def create_html(html_content):
    """
    Loads the HTML template, replaces the placeholder,
    and writes the final HTML file to disk.
    """
    with open('animals_template.html', "r") as template_file:
        template = template_file.read()

    final_html = template.replace("__REPLACE_ANIMALS_INFO__", html_content)

    with open('animals_page.html', "w") as output_file:
        output_file.write(final_html)


def main():

    choosen_animal = input("What animal you want?: ")

    # Load animal data from API
    animals_data = data_fetcher.load_data_from_api(choosen_animal)

    if not animals_data:
        html_content = f"<h2> The animal *{choosen_animal}* doesn't exist.</h2>"
    else:
        # Generate HTML content
        html_content = get_data_from_file(animals_data)

    # Create and save final HTML file
    create_html(html_content)


if __name__ == "__main__":
    main()