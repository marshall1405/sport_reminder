from collections import defaultdict
from telly import check_telly

def format_matches_html(matches):

    grouped = defaultdict(list)

    for match in matches:
        grouped[match.league.name].append(match)

    html = """
    <html>
      <body>
        <h2>Tennis Match Alerts 🎾</h2>
    """

    for league_name, league_matches in grouped.items():
        html += f"<h3>{league_name}</h3><ul>"

        for match in league_matches:
            telly_channel = check_telly(match.channel)
            telly_info = f"📺 On telly: {telly_channel}" if telly_channel else "Not on telly"

            html += f"""
                <li>
                    <b>{match.player1}</b> vs <b>{match.player2}</b><br>
                    Time: {match.time} {telly_info}
                </li>
            """

        html += "</ul>"

    html += """
        <p>Enjoy the matches!</p>
      </body>
    </html>
    """

    return html