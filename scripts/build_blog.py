#!/usr/bin/env python3
"""Genera el blog estático a partir de scripts/blog_posts.py.

    python3 scripts/build_blog.py

Crea:
  blog/index.html                      listado con todas las secciones
  blog/<seccion>/index.html            listado de una sección
  blog/<seccion>/<slug>/index.html     artículo
y actualiza el bloque «Lo último en el blog» de index.html
(entre <!-- BLOG:START --> y <!-- BLOG:END -->).
"""
import html
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from blog_posts import POSTS, SECTIONS  # noqa: E402

SITE = "https://juanantonio.retuertographicdesign.com"
SECTION_BY_SLUG = {s["slug"]: s for s in SECTIONS}
HOME_CARDS = 6
DISCLAIMER = ("Distribuidor independiente de Enagic. Los resultados dependen del trabajo de cada persona; "
              "no se garantizan ingresos. Los productos no están destinados a diagnosticar, tratar ni prevenir enfermedades.")
FONTS = ("https://fonts.googleapis.com/css2?family=Jost:wght@300;400;500;600"
         "&family=Libre+Caslon+Text:ital,wght@0,400;0,700;1,400&display=swap")
FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='8' fill='%23102250'/%3E"
           "%3Ctext x='32' y='44' font-family='Georgia,serif' font-weight='700' font-size='34' fill='%23ccdef6' text-anchor='middle'%3EJA%3C/text%3E%3C/svg%3E")
ARROW = '<svg class="arrow" viewBox="0 0 16 16" width="14" height="14" aria-hidden="true"><path d="M2 8h11M9 4l4 4-4 4" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'

e = html.escape


def img_size(rel):
    from PIL import Image
    with Image.open(ROOT / rel) as im:
        return im.size


def post_path(p):
    return f"blog/{p['section']}/{p['slug']}/"


def head(title, description, prefix, canonical, og_image="assets/og.jpg"):
    return f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(title)}</title>
<meta name="description" content="{e(description)}">
<link rel="canonical" href="{SITE}/{canonical}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(description)}">
<meta property="og:image" content="{SITE}/{og_image}">
<meta property="og:url" content="{SITE}/{canonical}">
<meta property="og:locale" content="es_ES">
<meta name="theme-color" content="#ccdef6">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}">
<link rel="stylesheet" href="{prefix}assets/styles.css">
<link rel="icon" href="{FAVICON}">
</head>
<body>
"""


def header(prefix):
    return f"""
<header class="site-header">
  <div class="wrap">
    <a class="logo" href="{prefix}index.html" aria-label="Juan Antonio Emprende, inicio"><b>Juan Antonio</b><span>Emprende</span></a>
    <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="nav">MENÚ</button>
    <nav class="nav" id="nav" aria-label="Principal">
      <a href="{prefix}index.html#sobre-mi">Sobre mí</a>
      <a href="{prefix}index.html#emprender">Emprender</a>
      <a href="{prefix}index.html#bienestar">Bienestar</a>
      <a href="{prefix}oportunidad.html">La oportunidad</a>
      <a href="{prefix}blog/" aria-current="page">Blog</a>
      <a class="btn" href="{prefix}index.html#contacto">Contacto</a>
    </nav>
  </div>
</header>
"""


def footer(prefix):
    return f"""
<footer class="site-footer">
  <div class="wrap">
    <div class="footer-top">
      <a class="logo" href="{prefix}index.html"><b>Juan Antonio</b><span>Emprende</span></a>
      <nav class="footer-nav" aria-label="Pie">
        <a href="{prefix}index.html#sobre-mi">Sobre mí</a>
        <a href="{prefix}index.html#emprender">Emprender</a>
        <a href="{prefix}index.html#bienestar">Bienestar</a>
        <a href="{prefix}oportunidad.html">La oportunidad</a>
        <a href="{prefix}blog/">Blog</a>
        <a href="{prefix}index.html#contacto">Contacto</a>
      </nav>
    </div>
    <p class="disclaimer">{DISCLAIMER}<br>© <span id="year">2026</span> Juan Antonio Emprende</p>
  </div>
</footer>

<script src="{prefix}assets/main.js"></script>
</body>
</html>
"""


def cta(prefix):
    return f"""
  <section class="blog-cta">
    <div class="wrap">
      <div class="guide">
        <div>
          <span class="eyebrow" style="color:#9fb2d6">Conversación con Juan Antonio</span>
          <h2>¿Lo hablamos con un café?</h2>
          <p>Si estás explorando una oportunidad o una nueva etapa, me gustaría conocerte. Cuando quieras, hablamos.</p>
        </div>
        <div class="cta-actions">
          <a class="btn" data-wa="EMPRENDER" href="{prefix}index.html#contacto">Escríbeme «EMPRENDER»</a>
          <a class="btn btn--line" href="{prefix}index.html#contacto">Ir a contacto</a>
        </div>
      </div>
    </div>
  </section>
"""


def card(p, prefix, excerpt=True, image=True):
    sec = SECTION_BY_SLUG[p["section"]]
    img = ""
    if image and p.get("image"):
        w, h = img_size(p["image"])
        img = f'<div class="bcard-img"><img src="{prefix}{p["image"]}" alt="{e(p.get("image_alt", ""))}" loading="lazy" width="{w}" height="{h}"></div>'
    exc = f'<p>{e(p["excerpt"])}</p>' if excerpt else ""
    cls = "bcard bcard--img" if img else "bcard"
    return f"""<article class="{cls}">
          <a href="{prefix}{post_path(p)}">
            {img}<div class="bcard-body">
              <span class="bcard-cat">{e(sec["name"])}</span>
              <h3>{e(p["card_title"])}</h3>
              {exc}
              <span class="bcard-more">Leer {ARROW}</span>
            </div>
          </a>
        </article>"""


def breadcrumb(items):
    parts = []
    for label, href in items:
        parts.append(f'<a href="{href}">{e(label)}</a>' if href else f'<span aria-current="page">{e(label)}</span>')
    return '<nav class="crumbs" aria-label="Migas de pan">' + '<span class="sep">/</span>'.join(parts) + "</nav>"


def write(rel, content):
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def build_listing():
    prefix = "../"
    nav = "".join(f'<a href="#{s["slug"]}">{e(s["name"])}</a>' for s in SECTIONS
                  if any(p["section"] == s["slug"] for p in POSTS))
    sections = []
    for s in SECTIONS:
        posts = [p for p in POSTS if p["section"] == s["slug"]]
        if not posts:
            continue
        cards = "\n        ".join(card(p, prefix) for p in posts)
        sections.append(f"""
    <div class="blog-group" id="{s['slug']}">
      <div class="blog-group-head">
        <h2><a href="{s['slug']}/">{e(s['name'])}</a></h2>
        <p>{e(s['intro'])}</p>
      </div>
      <div class="bcards">
        {cards}
      </div>
    </div>""")
    body = f"""{header(prefix)}
<main>
  <section class="page-hero">
    <div class="wrap">
      {breadcrumb([("Inicio", "../index.html"), ("Blog", None)])}
      <h1>Blog</h1>
      <p class="lead">Ideas para emprender con cabeza: preguntas que conviene hacerse, hábitos, bienestar y la oportunidad con la que trabajo, contada sin humo.</p>
      <nav class="blog-nav" aria-label="Secciones del blog">{nav}</nav>
    </div>
  </section>
  <section class="blog-list">
    <div class="wrap">{''.join(sections)}
    </div>
  </section>
{cta(prefix)}
</main>
{footer(prefix)}"""
    write("blog/index.html", head("Blog · Juan Antonio Emprende",
                                  "Ideas para emprender con cabeza: preguntas, hábitos, bienestar y la oportunidad sin humo.",
                                  prefix, "blog/") + body)


def build_section(s):
    prefix = "../../"
    posts = [p for p in POSTS if p["section"] == s["slug"]]
    if not posts:
        return
    cards = "\n        ".join(card(p, prefix) for p in posts)
    body = f"""{header(prefix)}
<main>
  <section class="page-hero">
    <div class="wrap">
      {breadcrumb([("Inicio", "../../index.html"), ("Blog", "../"), (s["name"], None)])}
      <h1>{e(s["name"])}</h1>
      <p class="lead">{e(s["intro"])}</p>
    </div>
  </section>
  <section class="blog-list">
    <div class="wrap">
      <div class="bcards">
        {cards}
      </div>
      <a class="back-link" href="../">← Volver al blog</a>
    </div>
  </section>
{cta(prefix)}
</main>
{footer(prefix)}"""
    write(f"blog/{s['slug']}/index.html",
          head(f"{s['name']} · Blog · Juan Antonio Emprende", s["intro"], prefix, f"blog/{s['slug']}/") + body)


def build_post(p):
    prefix = "../../../"
    sec = SECTION_BY_SLUG[p["section"]]
    url = f"{SITE}/{post_path(p)}"
    share_text = f"{p['title']} {url}"
    from urllib.parse import quote
    figure = ""
    if p.get("image"):
        w, h = img_size(p["image"])
        figure = f'<figure class="post-figure"><img src="{prefix}{p["image"]}" alt="{e(p.get("image_alt", ""))}" width="{w}" height="{h}"></figure>'
    body = f"""{header(prefix)}
<main>
  <section class="page-hero post-hero">
    <div class="wrap">
      {breadcrumb([("Inicio", prefix + "index.html"), ("Blog", "../../"), (sec["name"], "../"), (p["card_title"], None)])}
      <span class="bcard-cat">{e(sec["name"])}</span>
      <h1>{e(p["title"])}</h1>
    </div>
  </section>
  <article class="post">
    <div class="wrap post-wrap">
      {figure}
      <div class="post-body">
{p["body"].strip()}
      </div>
      <div class="share" aria-label="Compartir">
        <span>Compartir</span>
        <a href="https://wa.me/?text={quote(share_text)}" target="_blank" rel="noopener">WhatsApp</a>
        <a href="https://www.linkedin.com/sharing/share-offsite/?url={quote(url, safe='')}" target="_blank" rel="noopener">LinkedIn</a>
        <a href="https://www.facebook.com/sharer/sharer.php?u={quote(url, safe='')}" target="_blank" rel="noopener">Facebook</a>
        <a href="mailto:?subject={quote(p['title'])}&amp;body={quote(url)}">Correo</a>
        <button type="button" class="copy-link" data-url="{url}">Copiar enlace</button>
        <span class="copy-status" role="status" aria-live="polite"></span>
      </div>
      <a class="back-link" href="../">← Volver a {e(sec["name"])}</a>
    </div>
  </article>
{cta(prefix)}
</main>
{footer(prefix)}"""
    og = p.get("image", "assets/og.jpg")
    write(post_path(p) + "index.html", head(f"{p['title']} · Juan Antonio Emprende", p["excerpt"], prefix, post_path(p), og) + body)


def build_home_block():
    posts = POSTS[:HOME_CARDS]
    cards = "\n        ".join(card(p, "", excerpt=(i == 0)) for i, p in enumerate(posts))
    block = f"""<!-- BLOG:START (generado por scripts/build_blog.py) -->
  <section id="blog" class="home-blog">
    <div class="wrap">
      <div class="section-head">
        <h2 class="section-title">Lo último en el blog</h2>
        <p>Ideas prácticas para emprender con cabeza: lo que conviene preguntarse antes de empezar y lo que ayuda a seguir.</p>
      </div>
      <div class="bcards">
        {cards}
      </div>
      <a class="bcard-all" href="blog/">Ver todos los artículos {ARROW}</a>
    </div>
  </section>
  <!-- BLOG:END -->"""
    index = ROOT / "index.html"
    src = index.read_text(encoding="utf-8")
    new, n = re.subn(r"<!-- BLOG:START.*?<!-- BLOG:END -->", block, src, flags=re.S)
    if n != 1:
        sys.exit("index.html: no encuentro el bloque <!-- BLOG:START --> … <!-- BLOG:END -->")
    index.write_text(new, encoding="utf-8")


def main():
    shutil.rmtree(ROOT / "blog", ignore_errors=True)
    build_listing()
    for s in SECTIONS:
        build_section(s)
    for p in POSTS:
        build_post(p)
    build_home_block()
    print(f"Blog generado: {len(POSTS)} artículos")


if __name__ == "__main__":
    main()
