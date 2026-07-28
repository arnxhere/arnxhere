import datetime
from PIL import Image

# 1. Image ko ASCII mein convert karne ka logic
def image_to_ascii(image_path, new_width=45):
    try:
        img = Image.open(image_path)
    except Exception as e:
        return f"Image load nahi ho paaye: {e}"

    # Aspect ratio maintain karke resize
    width, height = img.size
    aspect_ratio = height / width
    new_height = int(new_width * aspect_ratio * 0.55)
    img = img.resize((new_width, new_height))
    img = img.convert('L') # Grayscale

    # Light to dark ASCII characters
    chars = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]
    
    pixels = img.getdata()
    ascii_str = ""
    for pixel in pixels:
        ascii_str += chars[pixel // 25]
    
    # Lines mein break karna
    ascii_lines = [ascii_str[i:i+new_width] for i in range(0, len(ascii_str), new_width)]
    return "\n".join(ascii_lines)

# Image path (jo photo tumne upload ki hai)
ascii_face = image_to_ascii("avatar.jpg", new_width=40)

# 2. Dynamic Uptime Calculate karna
START_DATE = datetime.datetime(2007, 4, 1) # Tumhari DOB ya start date
now = datetime.datetime.now()
diff = now - START_DATE

years = diff.days // 365
months = (diff.days % 365) // 30
days = (diff.days % 365) % 30
uptime_str = f"{years} years, {months} months, {days} days"

# 3. Final Content Design
details_text = f"""arnxhere@github
--------------------------------------------------
OS................... Linux, Windows 11
Uptime............... {uptime_str}
Host................. Code & Edits
Kernel............... Developer
IDE.................. VSCode, KineMaster

Languages.Prog....... Python, HTML, CSS, JavaScript
Languages.Real....... Hindi, English

Hobbies.............. Video Editing, Tech, Gaming

- Contact ----------------------------------------
Email................ arnxhere@gmail.com
GitHub............... github.com/arnxhere

- Stats ------------------------------------------
Last Updated......... {now.strftime('%d %b %Y %H:%M UTC')}
--------------------------------------------------"""

# Layout Markdown
content = f"""```text
[ascii_face]
