def build_comic_layout(outline, story, images):
    layout = []
    for i, panel in enumerate(outline):
        layout.append({
            "panel": panel["panel"],
            "title": panel["title"],
            "desc": panel["desc"],
            "image": images[i],
            "story": story
        })
    return layout
