# Juan Antonio Emprende — web

Web estática (HTML + CSS + JS, sin dependencias) de la marca personal de Juan Antonio.

- `index.html` — portada: cabecera, sobre mí, tres puertas (negocio, bienestar, desarrollo personal), la oportunidad, blog, guía y contacto.
- `oportunidad.html` — la oportunidad Kangen, sin humo: para quién encaja, quién está detrás, cómo funciona, preguntas incómodas.
- `assets/` — estilos, script, foto y imagen para redes.

## Datos de contacto

Rellena el bloque `CONTACT` al principio de `assets/main.js` (WhatsApp, teléfono y correo). Los botones «Escríbeme EMPRENDER» y el formulario usan ese WhatsApp.

## Despliegue

Cada push a `main` o a la rama de trabajo publica la web en GitHub Pages mediante `.github/workflows/pages.yml`.
Si es la primera vez, en *Settings → Pages* elige **Source: GitHub Actions**.

## Líneas rojas de contenido

Nada de promesas de salud ni de ingresos, ni datos inventados. El aviso legal del pie es obligatorio.

## Dominio

La web se sirve en https://juanantonio.retuertographicdesign.com (registro CNAME `juanantonio` → `retuertographic.github.io.` en el DNS de SiteGround).
En *Settings → Pages → Custom domain* debe figurar ese mismo dominio, con *Enforce HTTPS* activado.

## Blog

Los artículos se escriben en `scripts/blog_posts.py` y se generan con:

    python3 scripts/build_blog.py

Crea `blog/` (listado, una página por sección y una por artículo, en `/blog/<seccion>/<slug>/`) y actualiza el bloque «Lo último en el blog» de la portada. Sube también la carpeta `blog/` generada.

## Fotografías

Las fotos son del banco de imágenes de Magnific (Freepik):
- `assets/photos/` — cabeceras de páginas interiores, secciones del blog y bloques de la portada.
- `assets/blog/<slug>.jpg` — una por artículo (tarjeta y cabecera del artículo).
