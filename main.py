import os

ROAST = "I asked my agent for one roast \u2014 it wrote a plan, a skill, and a cron job to remind me to laugh later."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ROAST)
