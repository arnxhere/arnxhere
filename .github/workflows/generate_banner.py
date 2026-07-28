import datetime

# ASCII Art (Left Side) - Isko aap apni marzi ke ASCII art se replace kar sakte ho
ASCII_ART = """
  /\\_/\\  
 ( o.o ) 
  > ^ <  
"""

# Dynamic details calculate karna
username = "arnxhere"
today = datetime.date.today().strftime("%d %b %Y")

# Terminal-style output content
text_content = f"""
{username}@github
------------------
OS: GitHub Profile
Uptime: Active Today
Date: {today}

Languages: Python, HTML, CSS
Hobbies: Coding, Customizing
"""

# Dynamic SVG Image Generate Karna
svg_content = f"""<svg fill="none" width="800" height="300" xmlns="http://www.w3.org/2000/svg">
  <foreignObject width="100%" height="100%">
    <div xmlns="http://www.w3.org/1999/xhtml">
      <style>
        .terminal {{
          background-color: #0d1117;
          color: #c9d1d9;
          font-family: 'Courier New', Courier, monospace;
          padding: 20px;
          border-radius: 10px;
          border: 1px solid #30363d;
          display: flex;
          white-space: pre;
          font-size: 14px;
        }}
        .ascii {{ color: #58a6ff; margin-right: 30px; font-weight: bold; }}
        .info {{ color: #7ee787; }}
      </style>
      <div class="terminal">
        <div class="ascii">{ASCII_ART}</div>
        <div class="info">{text_content}</div>
      </div>
    </div>
  </foreignObject>
</svg>
"""

with open("terminal_banner.svg", "w", encoding="utf-8") as f:
    f.write(svg_content)
