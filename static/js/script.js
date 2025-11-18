document.addEventListener("DOMContentLoaded", () => {
  const verificarBtn = document.getElementById("verificarBtn");
  const estadoConexion = document.getElementById("estadoConexion");
  const cargarBtn = document.getElementById("cargarBtn");
  const listaProductos = document.getElementById("listaProductos");

  const API_BASE = "http://127.0.0.1:8000";

  // 🔹 VERIFICAR CONEXIÓN - USANDO TU ENDPOINT
  verificarBtn.addEventListener("click", async () => {
    try {
      estadoConexion.textContent = "🔄 Conectando...";
      estadoConexion.style.color = "blue";

      const response = await fetch(`${API_BASE}/api/`);
      
      if (!response.ok) {
        throw new Error(`Error HTTP: ${response.status}`);
      }

      const data = await response.json();
      estadoConexion.textContent = `✅ ${data.mensaje || 'Conectado correctamente'}`;
      estadoConexion.style.color = "green";

    } catch (error) {
      estadoConexion.textContent = `❌ Error: ${error.message}`;
      estadoConexion.style.color = "red";
    }
  });

  // 🔹 CARGAR PRODUCTOS - VERSIÓN CORREGIDA
  cargarBtn.addEventListener("click", async () => {
    try {
      console.log("🔄 Cargando productos desde API...");
      listaProductos.innerHTML = "<p>🔄 Cargando productos...</p>";

      const response = await fetch(`${API_BASE}/api/productos/`);
      
      if (!response.ok) {
        throw new Error(`Error HTTP: ${response.status}`);
      }

      const productos = await response.json();
      console.log("📦 Productos recibidos:", productos);

      if (!productos.length) {
        listaProductos.innerHTML = "<p>⚠️ No hay productos registrados en la base de datos.</p>";
        return;
      }

      // 🔥 MOSTRAR EN TARJETAS BONITAS
      mostrarProductosEnTarjetas(productos);

    } catch (error) {
      console.error("❌ Error cargando productos:", error);
      listaProductos.innerHTML = `
        <div style="color: red; text-align: center;">
          <p>❌ Error al cargar productos</p>
          <p><small>${error.message}</small></p>
          <p><small>Verifica que /api/productos/ esté en tus URLs</small></p>
        </div>
      `;
    }
  });

  // 🔹 FUNCIÓN PARA MOSTRAR TARJETAS BONITAS
  function mostrarProductosEnTarjetas(productos) {
    listaProductos.innerHTML = "";
    
    productos.forEach((producto, index) => {
      const tarjeta = document.createElement("div");
      tarjeta.className = "card-producto fade-in";
      tarjeta.style.animationDelay = `${index * 0.1}s`;
      
      // Badge de stock con color dinámico
      const stockColor = producto.stock > 10 ? '#27ae60' : '#e74c3c';
      
      tarjeta.innerHTML = `
        ${producto.stock > 0 ? `<div class="stock-badge" style="background: linear-gradient(135deg, ${stockColor}, ${stockColor}dd)">Stock: ${producto.stock}</div>` : ''}
        <h3>${producto.nombre || 'Sin nombre'}</h3>
        <p><strong>Precio:</strong> $${producto.precio || '0.00'}</p>
        <p><strong>Código:</strong> ${producto.codigo || 'N/A'}</p>
        ${producto.descripcion ? `<p><strong>Descripción:</strong> ${producto.descripcion}</p>` : ''}
        ${producto.linea ? `<p><strong>Línea:</strong> ${producto.linea}</p>` : ''}
      `;
      
      listaProductos.appendChild(tarjeta);
    });
  }

  // 🔹 EFECTO CLICK PARA BOTONES
  document.addEventListener("click", e => {
    const target = e.target;
    if (target.classList.contains("btn")) {
      const rect = target.getBoundingClientRect();
      target.style.setProperty('--x', e.clientX - rect.left);
      target.style.setProperty('--y', e.clientY - rect.top);
    }
  });

  // 🔹 CREAR SPARKLES
  function crearSparkles() {
    const container = document.getElementById("sparkles-container");
    if (!container) return;
    
    for (let i = 0; i < 15; i++) {
      const sparkle = document.createElement("div");
      sparkle.className = "sparkle";
      sparkle.style.left = `${Math.random() * 100}%`;
      sparkle.style.top = `${Math.random() * 100}%`;
      sparkle.style.animationDelay = `${Math.random() * 5}s`;
      container.appendChild(sparkle);
    }
  }

  crearSparkles();
});