import os

dir_path = "/Users/jessicamurray/Documents/nydr-archive/nydr-archive/content/topics/disability-independence-day"
subdirs = [d for d in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, d))]
subdirs.sort()

cards = []
for sd in subdirs:
    index_path = os.path.join(dir_path, sd, "_index.md")
    if os.path.exists(index_path):
        with open(index_path, 'r') as f:
            content = f.read()
            if content.startswith("---"):
                parts = content.split("---")
                if len(parts) >= 3:
                    fm = parts[1]
                    title = ""
                    featured = ""
                    featuredAlt = ""
                    for line in fm.split("\n"):
                        if line.startswith("title: "):
                            title = line.split("title: ")[1].strip().strip('"').strip("'")
                        elif line.startswith("featured: "):
                            featured = line.split("featured: ")[1].strip().strip('"').strip("'")
                        elif line.startswith("featuredAlt: "):
                            featuredAlt = line.split("featuredAlt: ")[1].strip().strip('"').strip("'")
                    
                    cards.append({
                        'title': title or sd,
                        'img': featured,
                        'alt': featuredAlt,
                        'text': '',
                        'btn': {
                            'text': 'Learn more',
                            'url': f'/topics/disability-independence-day/{sd}'
                        }
                    })

print("cards:")
for c in cards:
    print(f"- title: \"{c['title']}\"")
    print(f"  img: \"{c.get('img', '')}\"")
    print(f"  alt: \"{c.get('alt', '')}\"")
    print(f"  text: \"{c.get('text', '')}\"")
    print(f"  btn:")
    print(f"    text: \"{c['btn']['text']}\"")
    print(f"    url: \"{c['btn']['url']}\"")

