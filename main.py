from pyscript import display, document
from js import setTeamBackground

def intrams_checker(e=None):
    document.getElementById("output").innerHTML = ""
    document.getElementById("image").innerHTML = ""

    registration = document.querySelector('input[name="registration"]:checked')
    clearance = document.querySelector('input[name="clearance"]:checked')
    sports = document.querySelector('input[name="sports"]:checked')
    phil_games = document.querySelector('input[name="philGames"]:checked')

    grade = document.getElementById("level").value
    section = document.getElementById("section").value

    if not registration or not clearance:
        display("❌ You can’t play in Intrams.", target="output")
        return

    if registration.value != "registered" or clearance.value != "cleared":
        display("❌ You can’t play in Intrams.", target="output")
        return

    if not sports and not phil_games:
        display("❌ You can’t play in Intrams.", target="output")
        return

    if sports and sports.value == "no":
        if not phil_games or phil_games.value != "yes":
            display("❌ You can’t play in Intrams.", target="output")
            return

    if grade == "" or section == "":
        display("❌ Please select your grade and section.", target="output")
        return

    grade = int(grade)

    if section == "emerald":
        team = "Green Hornets" if grade in (7, 10) else "Red Bulldogs"

    elif section == "ruby":
        team = "Yellow Tigers" if grade in (7, 10) else "Blue Bears"

    elif section == "sapphire":
        team = "Red Bulldogs" if grade in (7, 10) else "Green Hornets"

    elif section == "topaz":
        team = "Blue Bears" if grade in (7, 10) else "Yellow Tigers"

    else:
        display("❌ You can’t play in Intrams.", target="output")
        return

    display(
        f"🎉 Congratulations! You are part of the {team} Team!",
        target="output"
    )

    team_color = team.split()[0]
    setTeamBackground(team_color)

    images = {
        "Green Hornets": "green hornets.jpg",
        "Red Bulldogs": "red bulldogs.jpg",
        "Blue Bears": "blue bears.jpg",
        "Yellow Tigers": "yellow tigers.jpg"
    }

    document.getElementById("image").innerHTML = (
        f"<img src='{images[team]}' class='img-fluid mt-3'>"
    )