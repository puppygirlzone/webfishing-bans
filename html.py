import json
from pathlib import Path


def get_steam_id_finder_html(steam_id: int | str) -> str:
    return (f"<a href='https://www.steamidfinder.com/lookup/{steam_id}/'>"
            f"<img src='https://www.steamidfinder.com/signature/{steam_id}.png'>"
            "</a>")


def gen_payload(ban_list: list[int | str]) -> str:
    return "\n".join([get_steam_id_finder_html(steam_id) for steam_id in ban_list])
    

if __name__ == "__main__":
    with Path("LobbyLifeguard.json").open() as f:
        raw = json.load(f)
        ban_list = raw["banlist"].split(", ")

    # TODO - Change this so it has some actual CSS and other content. Maybe use jinja?
    with Path("build/shame.html").open("w") as f:
        payload = gen_payload(ban_list)
        f.write(payload)
