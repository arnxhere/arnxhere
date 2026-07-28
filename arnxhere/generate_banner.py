import datetime

ASCII_ART = r"""
  /\_/\  
 ( o.o ) 
  > ^ <  
"""

username = "arnxhere"
today = datetime.date.today().strftime("%d %b %Y")

banner_content = f"""```text
{ASCII_ART}
{username}@github
-------------------
OS: GitHub Profile
Uptime: Active Today
Date: [today]
with open("README.md", "w") as f:
    f.write(banner_content)
