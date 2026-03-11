"""
This is the Name Generator Microservice.
It takes an item color, and based on the color and series
the item is from, will generate a thematic name
for that collector's item.
"""

from flask import Flask, jsonify, request
import random

app = Flask(__name__)

themes_by_series = ["tamagotchi", "skullpanda", "labubu"]

tama_theme = ["pixel", "buzz", "beep"]

skull_theme = ["smirk", "rebel", "avril"]

labubu_theme = ["seymour", "chuck", "teddy"]

item_color_map = {
    "brown": ["teakwood", "toffee", "sesame bean"],
    "red": ["blossom", "strawberry pearl milk"],
    "blue": ["dew", "sea salt coconut", "melon soda", "water color glitter"],
    "green": ["pond", "green grape", "dubai choco matcha latte"],
    "purple": ["lightning"],
    "white": ["mist", "soymilk", "pearl flower", "white clover"],
    "orange": ["amber", "oj", "pearl milk tea"],
    "yellow": ["dawn", "24 Karat Gold"],
    "pink": ["windflower", "lychee berry", "pink glitter"]
}

color_names = {
    "brown": ["mulch", "tortilla", "peanut"],
    "red": ["juniper", "cherry", "pinch"],
    "blue": ["flipper", "sky", "ciel"],
    "green": ["hazel", "jade", "olive"],
    "purple": ["helen", "hugh", "shimmer"],
    "white": ["void", "egg", "pearl"],
    "orange": ["sour", "rusty", "coral"],
    "yellow": ["vanilla", "champagne", "sunny"],
    "pink": ["cotton", "melon", "taffy"]
}

@app.route("/generate/name", methods=["POST"])
def name_generator():
    """
    Accepts a series and an item color and returns
    a name based on those themes.
    :return: a dictionary with a key of theme name and value
    of a single string
    """
    data = request.get_json()
    series = data.get("series")
    req_item = data.get("item")
    prefix = "loading.."
    suffix = "loading.."
    found = False

    # prefixes
    for color, item_list in item_color_map.items():
        for item_name in item_list:
            if req_item == item_name:
                num = random.randint(0, 2)
                prefix = color_names.get(color)[num]
                found = True
    if not found:
        return jsonify({"error": "Invalid Color"}), 400

    # suffixes
    if series not in themes_by_series:
        return jsonify({"error": "Invalid Series"}), 400

    if series == "tamagotchi":
        num = random.randint(0, 2)
        suffix = tama_theme[num]
    if series == "skullpanda":
        num = random.randint(0, 2)
        suffix = skull_theme[num]
    if series == "labubu":
        num = random.randint(0, 2)
        suffix = labubu_theme[num]

    new_name = f"{prefix} {suffix}"

    return jsonify({
        "new_name": new_name
    })

if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("Thematic Name Generator Microservice is Running")
    print("http://localhost:5008")
    print("=" * 50 + "\n")

    app.run(port=5008, debug=True)