/* ------------------------------------------------------------------
   DATOS DE CONTACTO — rellena aquí y se actualiza toda la web.
   whatsapp: número con prefijo de país, solo dígitos (ej. "34600000000")
   phone:    tal como quieres que se vea (ej. "+34 600 00 00 00")
   email:    dirección de correo
   ------------------------------------------------------------------ */
const CONTACT = {
  whatsapp: "",
  phone: "",
  email: ""
};

const KEYWORD = "EMPRENDER";

function waLink(text) {
  const base = CONTACT.whatsapp ? `https://wa.me/${CONTACT.whatsapp}` : "https://wa.me/";
  return `${base}?text=${encodeURIComponent(text)}`;
}

function applyContact() {
  document.querySelectorAll("[data-wa]").forEach((el) => {
    el.href = waLink(el.dataset.wa || KEYWORD);
    el.target = "_blank";
    el.rel = "noopener";
  });
  document.querySelectorAll("[data-phone]").forEach((el) => {
    if (CONTACT.phone) {
      el.href = `tel:${CONTACT.phone.replace(/[^\d+]/g, "")}`;
      el.textContent = CONTACT.phone;
    } else {
      el.closest(".channel")?.setAttribute("hidden", "");
    }
  });
  document.querySelectorAll("[data-email]").forEach((el) => {
    if (CONTACT.email) {
      el.href = `mailto:${CONTACT.email}`;
      el.textContent = CONTACT.email;
    } else {
      el.closest(".channel")?.setAttribute("hidden", "");
    }
  });
  document.querySelectorAll("[data-wa-text]").forEach((el) => {
    if (CONTACT.whatsapp) el.textContent = `+${CONTACT.whatsapp}`;
  });
}

function setupHeader() {
  const header = document.querySelector(".site-header");
  const toggle = document.querySelector(".menu-toggle");
  const nav = document.querySelector(".nav");
  const onScroll = () => header?.classList.toggle("is-scrolled", window.scrollY > 8);
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });
  toggle?.addEventListener("click", () => {
    const open = nav.classList.toggle("is-open");
    toggle.setAttribute("aria-expanded", String(open));
    toggle.textContent = open ? "CERRAR" : "MENÚ";
  });
  nav?.querySelectorAll("a").forEach((a) =>
    a.addEventListener("click", () => {
      nav.classList.remove("is-open");
      toggle?.setAttribute("aria-expanded", "false");
      if (toggle) toggle.textContent = "MENÚ";
    })
  );
}

function setupForm() {
  const form = document.getElementById("contact-form");
  if (!form) return;
  const status = form.querySelector(".form-status");
  form.addEventListener("submit", (e) => {
    e.preventDefault();
    const data = new FormData(form);
    const name = (data.get("nombre") || "").toString().trim();
    const interest = (data.get("interes") || "").toString();
    const msg = (data.get("mensaje") || "").toString().trim();
    if (!name || !msg) {
      status.textContent = "Escribe tu nombre y un mensaje para que pueda responderte.";
      return;
    }
    const text = `Hola Juan Antonio, soy ${name}.${interest ? ` Me interesa: ${interest}.` : ""}\n\n${msg}`;
    if (CONTACT.whatsapp) {
      window.open(waLink(text), "_blank", "noopener");
      status.textContent = "Se ha abierto WhatsApp con tu mensaje. Solo falta pulsar enviar.";
    } else if (CONTACT.email) {
      window.location.href = `mailto:${CONTACT.email}?subject=${encodeURIComponent("Contacto web — " + name)}&body=${encodeURIComponent(text)}`;
      status.textContent = "Se ha abierto tu correo con el mensaje preparado.";
    } else {
      status.textContent = "El formulario aún no tiene un canal configurado.";
    }
  });
}

document.addEventListener("DOMContentLoaded", () => {
  applyContact();
  setupHeader();
  setupForm();
  const y = document.getElementById("year");
  if (y) y.textContent = new Date().getFullYear();
});
