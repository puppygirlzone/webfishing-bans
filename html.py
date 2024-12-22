import json
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

def get_steam_id_finder_html(steam_id: int | str) -> str:
    return (f"{{'https://www.steamidfinder.com/lookup/{steam_id}/'>"
            f"<img src='https://www.steamidfinder.com/signature/{steam_id}_png'>")

def gen_payload(ban_list: list[int | str]) -> str:
    return " ".join([get_steam_id_finder_html(steam_id) for steam_id in ban_list])
    
if __name__ == "__main__":
    with Path("LobbyLifeguard.json").open() as f:
        raw = json.load(f)
        ban_list = [int(ban_id.strip()) for ban_id in raw["banlist"].split(", ")]

    # Load template
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader, autoescape=select_autoescape(['html', 'xml']))
    template = env.get_template('shame.html')

    # Render template with data
    output = template.render(ban_list=ban_list)
    
    # Write to file
    with Path("build/shame.html").open("w") as f:
        f.write(output)
