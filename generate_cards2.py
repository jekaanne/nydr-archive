import os

dir_path = "/Users/jessicamurray/Documents/nydr-archive/nydr-archive/content/topics/disability-independence-day"
subdirs = [d for d in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, d))]
subdirs.sort()

cards = []
for sd in subdirs:
    # Get title from _index.md
    title = sd
    index_path = os.path.join(dir_path, sd, "_index.md")
    if os.path.exists(index_path):
        with open(index_path, 'r') as f:
            for line in f:
                if line.startswith("title: "):
                    title = line.split("title: ")[1].strip().strip('"').strip("'")
                    break
    
    # Try to find the first image in the subtopic
    img = ""
    alt = ""
    for file in os.listdir(os.path.join(dir_path, sd)):
        if file.endswith(".md") and file != "_index.md":
            with open(os.path.join(dir_path, sd, file), 'r') as f:
                for line in f:
                    if line.startswith("featured: "):
                        img = line.split("featured: ")[1].strip().strip('"').strip("'")
                    elif line.startswith("featuredAlt: "):
                        alt = line.split("featuredAlt: ")[1].strip().strip('"').strip("'")
            if img:
                break
                
    cards.append({
        'title': title,
        'img': img,
        'alt': alt,
        'text': '',
        'url': f'/topics/disability-independence-day/{sd}'
    })

yaml_str = "cards:\n"
for c in cards:
    yaml_str += f"- title: \"{c['title']}\"\n"
    yaml_str += f"  img: \"{c['img']}\"\n"
    yaml_str += f"  alt: \"{c['alt']}\"\n"
    yaml_str += f"  text: \"\"\n"
    yaml_str += f"  btn:\n"
    yaml_str += f"    text: \"View gallery\"\n"
    yaml_str += f"    url: \"{c['url']}\"\n"

with open("cards.yaml", "w") as f:
    f.write(yaml_str)

print("Generated cards.yaml")
