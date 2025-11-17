document.addEventListener("DOMContentLoaded", () => {
  const verificarBtn = document.getElementById("verificarBtn");
  const estadoConexion = document.getElementById("estadoConexion");
  const cargarBtn = document.getElementById("cargarBtn");
  const listaProductos = document.getElementById("listaProductos");

  document.addEventListener("click", e => {
    const target = e.target;

    if (target.classList.contains("btn") ||
        target.classList.contains("btn-edit") ||
        target.classList.contains("btn-delete") ||
        target.classList.contains("new-product-btn")) {

        const rect = target.getBoundingClientRect();
        target.style.setProperty('--x', e.clientX - rect.left);
        target.style.setProperty('--y', e.clientY - rect.top);
    }
  });

  const API_BASE = "http://127.0.0.1:8000";

  // 🔹 Verificar conexión con el backend
  verificarBtn.addEventListener("click", async () => {
    try {
      estadoConexion.textContent = "🔄 Conectando...";
      estadoConexion.style.color = "blue";

      const response = await fetch(`${API_BASE}/api/`);
      if (!response.ok) throw new Error(`Error HTTP: ${response.status}`);

      const data = await response.json();
      estadoConexion.textContent = `✅ Conectado: ${data.mensaje || data.estado}`;
      estadoConexion.style.color = "green";

    } catch (error) {
      estadoConexion.textContent = `❌ Error: ${error.message}`;
      estadoConexion.style.color = "red";
    }
  });

  // 🔹 Cargar lista de productos
  cargarBtn.addEventListener("click", async () => {
    try {
      listaProductos.innerHTML = "<p>🔄 Cargando productos...</p>";

      const response = await fetch(`${API_BASE}/api/productos/`);
      if (!response.ok) throw new Error(`Error HTTP: ${response.status}`);

      const data = await response.json();

      let productos = [];
      if (Array.isArray(data)) productos = data;
      else if (data.productos) productos = data.productos;
      else if (data.data) productos = data.data;

      if (!productos.length) {
        listaProductos.innerHTML = "<p>⚠️ No hay productos registrados.</p>";
        return;
      }

      // ✨ MOSTRAR PRODUCTOS BONITOS (solo esto fue mejorado visualmente)
      listaProductos.innerHTML = "";
      productos.forEach((producto, index) => {
        const item = document.createElement("div");
        item.classList.add("card-producto", "fade-in", "mb-3");
        item.style.animationDelay = `${index * 0.12}s`;

        item.innerHTML = `
          <h3>${producto.nombre || 'Sin nombre'}</h3>
          <p>💲 <strong>Precio:</strong> $${producto.precio || '0.00'}</p>
          <p>🏷️ <strong>Código:</strong> ${producto.codigo || 'N/A'}</p>
          <p>📦 <strong>Stock:</strong> ${producto.stock || '0'}</p>
          ${producto.descripcion ? `<p>📝 <strong>Descripción:</strong> ${producto.descripcion}</p>` : ''}
          ${producto.linea ? `<p>📋 <strong>Línea:</strong> ${producto.linea}</p>` : ''}
        `;

        listaProductos.appendChild(item);
      });

    } catch (error) {
      listaProductos.innerHTML = `
        <div style="color: red; text-align: center;">
          <p>❌ Error al cargar productos</p>
          <p><small>${error.message}</small></p>
        </div>
      `;
    }
  });

  // 🔹 Probar automáticamente la conexión al cargar la página
  setTimeout(() => {
    fetch(`${API_BASE}/api/`)
      .then(response => {
        if (response.ok) {
          estadoConexion.textContent = "✅ Servidor conectado";
          estadoConexion.style.color = "green";
        }
      })
      .catch(() => {});
  }, 1000);
});
