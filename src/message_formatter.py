from collections import defaultdict

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
            html += f"""
                <li>
                    <b>{match.player1}</b> vs <b>{match.player2}</b><br>
                    Time: {match.time}
                </li>
            """

        html += "</ul>"

    html += """
        <p>Enjoy the matches!</p>
      </body>
    </html>
    """

    return html