from flask import Flask, render_template
import markdown
import frontmatter
import os
import shutil

from collections import defaultdict
from datetime import datetime

from markdown.extensions.codehilite import CodeHiliteExtension
from markdown.extensions.fenced_code import FencedCodeExtension


app = Flask(__name__)

# Helper Functions

POSTS_DIR = "posts"

def load_posts():
    posts = []
    for root, dirs, files in os.walk(POSTS_DIR):
        for filename in files:
            if filename.endswith(".md"):

                filepath = os.path.join(root, filename)

                post = frontmatter.load(filepath)
                rel_path = os.path.relpath(filepath, POSTS_DIR)  # e.g. "tech/first-post.md"
                slug = filename.replace(".md", "")
                posts.append({
                    "slug": slug,
                    "title": post.get("title", slug),
                    "date": post.get("date", ""),
                    "tags": post.get("tags", []),
                    "content": markdown.markdown(post.content)
                })
        
    posts.sort(key=lambda x: x['date'], reverse=True)
    return posts

def get_all_tags():
    tags = set()
    for filename in os.listdir(POSTS_DIR):
        if filename.endswith(".md"):
            post = frontmatter.load(os.path.join(POSTS_DIR, filename))
            for t in post.get("tags", []):
                tags.add(t)
    return sorted(tags)

def build_archive(posts):
    archive = defaultdict(lambda: {"months": defaultdict(int), "total": 0})

    for p in posts:
        if not p["date"]:
            continue

        dt = datetime.strptime(p["date"], "%Y-%m-%d")
        year = dt.year
        month = dt.month

        archive[year]["months"][month] += 1
        archive[year]["total"] += 1

    # Convert defaultdicts → normal dicts for Jinja safety
    clean = {}
    for year, data in archive.items():
        clean[year] = {
            "months": dict(data["months"]),
            "total": data["total"]
        }

    return dict(sorted(clean.items(), reverse=True))

def render_markdown(md_text):
    return markdown.markdown(
        md_text,
        # extensions=[
        #     FencedCodeExtension(),                    # ``` code fencing
        #     CodeHiliteExtension(noclasses=False),  # Add <code class="language-...">
        # ]
        extensions=["fenced_code", "codehilite", "tables"]
    )
        

# Flask App Routes


@app.route("/")
def home():
    return render_template("about.html", title="About", hide_sidebar=True)

@app.route("/blog")
def blog():
    posts = load_posts()
    return render_template(
        "blog.html",
        posts=posts,
        all_tags=get_all_tags(),
        archive=build_archive(posts))

@app.route("/post/<slug>")
def post(slug):
    posts = load_posts()
    path = os.path.join(POSTS_DIR, f"{slug}.md")
    if not os.path.exists(path):
        return "Post not found", 404
    
    post = frontmatter.load(path)

    return render_template(
        "post.html",
        title = post.get("title", slug),
        date =  post.get("date", ""),
        tags =  post.get("tags", []),
        content = render_markdown(post.content),
        all_tags=get_all_tags(),
        posts=posts,
        archive=build_archive(posts)
    )

@app.route("/about")
def about():
    return render_template("about.html", title="About", hide_sidebar=True)

@app.route("/resume")
def resume():
    return render_template("resume.html", all_tags=get_all_tags(), title="Resume")

@app.route("/tag/<tag>")
def tag_page(tag):
    posts = load_posts()
    filtered = [p for p in posts if tag in p["tags"]]

    return render_template(
        "tag.html",
        tag=tag,
        posts=filtered,
        all_tags=get_all_tags(),
        title=f"Posts tagged '{tag}'",
        archive=build_archive(posts)
    )

@app.route("/blog/<int:year>/<int:month>")
def blog_by_month(year, month):
    posts = [
        p for p in load_posts()
        if p["date"].startswith(f"{year}-{month:02d}")
    ]

    return render_template(
        "blog.html",
        posts=posts,
        all_tags=get_all_tags(),
        archive=build_archive(load_posts()),
        active_year=year,
        active_month=month
    )


@app.route("/blog/<int:year>")
def blog_by_year(year):
    posts = [
        p for p in load_posts()
        if p["date"].startswith(str(year))
    ]

    return render_template(
        "blog.html",
        posts=posts,
        all_tags=get_all_tags(),
        archive=build_archive(load_posts()),
        active_year=year,
        active_month=None
    )


if __name__ == "__main__":
    app.run(debug=True)
