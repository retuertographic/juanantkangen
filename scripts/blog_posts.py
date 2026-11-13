# Contenido del blog. Cada artículo se publica en /blog/<seccion>/<slug>/.
# Reglas de la marca: tuteo, frases cortas, sin promesas de salud ni de
# ingresos y sin anécdotas que Juan Antonio no haya contado.
# Fotos: banco de imágenes de Magnific (Freepik), en assets/blog/<slug>.jpg.
# Cuerpo en HTML sencillo: <p>, <h2>, <ul class="yes|no">, <blockquote>.

SECTIONS = [
    {
        "slug": "emprender-con-cabeza",
        "image": "assets/photos/emprender-con-cabeza.jpg",
        "image_alt": "Profesional organizando ideas con notas adhesivas en una pared",
        "name": "Emprender con cabeza",
        "intro": "Preguntas antes de empezar, cómo elegir un proyecto y errores comunes que se pueden evitar.",
    },
    {
        "slug": "desarrollo-personal",
        "image": "assets/photos/desarrollo-personal.jpg",
        "image_alt": "Hombre leyendo y tomando notas en una biblioteca",
        "name": "Desarrollo personal",
        "intro": "Hábitos, constancia y cómo gestionar las dudas mientras construyes algo propio.",
    },
    {
        "slug": "bienestar",
        "image": "assets/photos/bienestar.jpg",
        "image_alt": "Tres amigos paseando por la orilla del mar",
        "name": "Bienestar",
        "intro": "Equilibrio entre trabajo y vida. Porque tu negocio no puede ir mejor que tú.",
    },
    {
        "slug": "la-oportunidad",
        "image": "assets/photos/la-oportunidad.jpg",
        "image_alt": "Jarra y vaso de agua junto a una planta",
        "name": "La oportunidad",
        "intro": "Cómo funciona el proyecto con el que trabajo, para quién encaja y para quién no.",
    },
    {
        "slug": "vendehumo",
        "image": "assets/photos/vendehumo.jpg",
        "image_alt": "Pompas de jabón flotando en un cielo azul",
        "name": "Desmontando el vendehumo",
        "intro": "Humor amable sobre gurús, atajos y promesas fáciles.",
    },
]

POSTS = [
    {
        "section": "emprender-con-cabeza",
        "slug": "esto-encaja-conmigo",
        "image": "assets/blog/esto-encaja-conmigo.jpg",
        "image_alt": "Hombre pensativo tomando notas en un cuaderno junto a un café",
        "title": "¿Esto encaja conmigo? La pregunta que va antes del dinero",
        "card_title": "¿Esto encaja conmigo?",
        "excerpt": "Antes de preguntarte «¿cuánto se gana?», pregúntate «¿esto encaja conmigo?». Es la pregunta que de verdad importa.",
        "body": """
<p>Antes de preguntarte «¿cuánto se gana?», pregúntate «¿esto encaja conmigo?».</p>
<p>Acompañando a otras personas en su camino como emprendedores, he aprendido que la segunda pregunta es la que de verdad importa.</p>
<h2>Cuatro preguntas que conviene hacerse</h2>
<ul class="yes">
  <li><strong>¿Cuánto tiempo real puedo dedicarle?</strong> No el que te gustaría tener. El que tienes de verdad, con tu trabajo y tu familia.</li>
  <li><strong>¿Me gusta trabajar con personas?</strong> Casi todos los proyectos van de eso: escuchar, explicar, acompañar.</li>
  <li><strong>¿Creo en lo que voy a ofrecer?</strong> Si no te convence a ti, difícilmente convencerá a nadie.</li>
  <li><strong>¿Tengo con quién aprender?</strong> Empezar solo es posible. Empezar acompañado es mucho más llevadero.</li>
</ul>
<h2>No todo vale para todos</h2>
<p>Cada persona parte de un lugar distinto. Unas quieren empezar una nueva etapa profesional, otras exploran un negocio propio y otras buscan ampliar su actividad.</p>
<blockquote>Ningún proyecto es bueno para todo el mundo. El bueno es el que encaja contigo.</blockquote>
<p>💬 ¿Qué pregunta añadirías tú? Cuéntamelo por WhatsApp.</p>
""",
    },
    {
        "section": "vendehumo",
        "slug": "rico-en-90-dias",
        "image": "assets/blog/rico-en-90-dias.jpg",
        "image_alt": "Reloj de arena de madera sobre una mesa",
        "title": "Si te prometen hacerte rico en 90 días, el negocio es el curso",
        "card_title": "Rico en 90 días",
        "excerpt": "Si alguien te promete hacerte rico en 90 días, el único que se va a hacer rico es él. Con tu curso.",
        "body": """
<p>Si alguien te promete hacerte rico en 90 días, el único que se va a hacer rico es él. Con tu curso.</p>
<p>Seguro que los has visto: música épica, coches de alquiler en las fotos y frases motivacionales de taza.</p>
<h2>Emprender no va de atajos</h2>
<p>Va de encontrar un proyecto que encaje contigo, aprender y construir relaciones sin prisa.</p>
<ul class="no">
  <li>Cifras de ganancias que no son tuyas.</li>
  <li>«Últimas plazas» y «solo hoy».</li>
  <li>«Deja tu trabajo ya».</li>
  <li>«Sin esfuerzo y sin riesgo».</li>
</ul>
<h2>Por dónde empiezo yo</h2>
<p>Por eso, cuando alguien me pregunta por una oportunidad, no empiezo hablando de dinero. Empiezo preguntando qué busca.</p>
<p>💬 ¿Qué es lo más curioso que te han prometido para «emprender sin esfuerzo»? Cuéntamelo, que nos reímos juntos.</p>
""",
    },
    {
        "section": "desarrollo-personal",
        "slug": "la-motivacion-dura-una-semana",
        "image": "assets/blog/la-motivacion-dura-una-semana.jpg",
        "image_alt": "Planificador semanal en una tablilla junto a una taza de café",
        "title": "La motivación dura una semana. Los hábitos, años",
        "card_title": "La motivación dura una semana. Los hábitos, años",
        "excerpt": "La motivación es como el gimnasio en enero: llena el primer día y medio vacía en febrero.",
        "body": """
<p>La motivación es como el gimnasio en enero: llena el primer día y medio vacía en febrero.</p>
<p>Lo que sostiene un proyecto no es la motivación, son los hábitos. Pequeños, aburridos y constantes.</p>
<h2>Tres hábitos pequeños</h2>
<ul class="yes">
  <li><strong>Una llamada al día.</strong> Una conversación de verdad, con calma.</li>
  <li><strong>Una cosa nueva aprendida por semana.</strong> Poco a poco se nota.</li>
  <li><strong>Un rato para ti, también.</strong> Sin él, lo demás no aguanta.</li>
</ul>
<h2>Constancia antes que intensidad</h2>
<p>Los días con ganas son fáciles. Los hábitos sirven para los otros días, los que no apetece.</p>
<p>🌿 ¿Qué hábito te está ayudando a avanzar este año?</p>
""",
    },
    {
        "section": "bienestar",
        "slug": "tu-negocio-no-puede-ir-mejor-que-tu",
        "image": "assets/blog/tu-negocio-no-puede-ir-mejor-que-tu.jpg",
        "image_alt": "Hombre estirándose junto a un lago",
        "title": "Tu negocio no puede ir mejor que tú",
        "card_title": "Tu negocio no puede ir mejor que tú",
        "excerpt": "Emprender ilusiona, pero también cansa. Por eso el bienestar no es un extra: es parte del plan.",
        "body": """
<p>Emprender ilusiona, pero también cansa. Por eso el bienestar no es un extra: es parte del plan.</p>
<p>Los domingos revisando cuentas, el Excel con más pestañas que clientes… Todo eso pesa si no te cuidas.</p>
<h2>Nada nuevo, pero todo importa</h2>
<ul class="yes">
  <li>Dormir.</li>
  <li>Moverte.</li>
  <li>Beber agua.</li>
  <li>Desconectar un rato.</li>
</ul>
<p>No son trucos. Son hábitos. Y un proyecto sostenido en el tiempo necesita a alguien que también se sostenga.</p>
<p>🌿 ¿Qué haces tú para cuidarte cuando el trabajo aprieta?</p>
""",
    },
    {
        "section": "la-oportunidad",
        "slug": "la-oportunidad-sin-humo",
        "image": "assets/blog/la-oportunidad-sin-humo.jpg",
        "image_alt": "Dos hombres sonrientes conversando con un café",
        "title": "La oportunidad con la que trabajo, contada sin humo",
        "card_title": "La oportunidad, sin humo",
        "excerpt": "Sin música épica ni coches de alquiler: qué es Kangen, quién está detrás y cómo se cobra.",
        "body": """
<p>Hoy te cuento la oportunidad con la que trabajo. Sin música épica ni coches de alquiler.</p>
<h2>Qué es y quién está detrás</h2>
<p>Kangen es la tecnología de agua de Enagic, una empresa japonesa fundada en 1974 y presente en 29 países (<a href="https://www.enagic.com/es/oportunidad-de-negocio" target="_blank" rel="noopener">fuente: Enagic</a>).</p>
<h2>Cómo funciona</h2>
<ul class="yes">
  <li>Como distribuidor independiente, se cobra por la venta de producto, no por apuntar gente.</li>
  <li>Sin compra inicial obligatoria, sin stock y sin envíos.</li>
  <li>Tú decides tu ritmo.</li>
  <li>Cuentas con formación y acompañamiento.</li>
</ul>
<h2>No es para todo el mundo</h2>
<p>Si buscas dinero rápido, no encaja. Si te gusta trabajar con personas y avanzar paso a paso, puede que sí.</p>
<p>🤝 ¿Quieres verlo con calma? Escríbeme «EMPRENDER».</p>
<p class="note">Distribuidor independiente de Enagic. Los resultados dependen del trabajo de cada persona; no se garantizan ingresos.</p>
""",
    },
    {
        "section": "la-oportunidad",
        "slug": "para-quien-no-es-este-proyecto",
        "image": "assets/blog/para-quien-no-es-este-proyecto.jpg",
        "image_alt": "Poste indicador con flechas en varias direcciones en un parque",
        "title": "Para quién NO es este proyecto",
        "card_title": "Para quién NO es este proyecto",
        "excerpt": "Saber para quién no es un proyecto ahorra tiempo a todos. Empezando por ti.",
        "body": """
<p>Saber para quién no es un proyecto ahorra tiempo a todos. Empezando por ti.</p>
<h2>Mejor no, si…</h2>
<ul class="no">
  <li>Buscas dinero rápido.</li>
  <li>Quieres resultados sin dedicarle tiempo.</li>
  <li>No te apetece tratar con personas.</li>
  <li>No crees en lo que vas a ofrecer.</li>
  <li>Esperas que alguien te garantice ingresos.</li>
</ul>
<h2>Puede encajar, si…</h2>
<ul class="yes">
  <li>Buscas una nueva etapa profesional.</li>
  <li>Estás explorando tener un negocio propio.</li>
  <li>Eres profesional o autónomo y quieres ampliar tu actividad.</li>
  <li>Prefieres avanzar paso a paso, con alguien a tu lado.</li>
</ul>
<p>No hace falta dejar tu trabajo: cada persona parte de un lugar distinto y muchas empiezan compaginándolo.</p>
<p>💬 ¿Te reconoces en la segunda lista? Hablamos con un café.</p>
""",
    },
]
