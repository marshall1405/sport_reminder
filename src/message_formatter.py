def format_matches_html(matches):
    html = """
    <html>
      <body>
        <h2>Tennis Match Alerts 🎾</h2>
        <ul>
    """

    for match in matches:
        tournament_info = f" ({match.league.name})"
        html += f"""
            <li>
                <b>{match.team1}</b> vs <b>{match.team2}</b>{tournament_info} <br>
                Time: {match.time}
            </li>
        """

    html += """
        </ul>
        <p>Get ready to watch!</p>
      </body>
    </html>
    """
    return html
