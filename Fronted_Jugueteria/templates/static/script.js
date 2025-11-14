document.addEventListener("DOMContentLoaded", () => {
  const verificarBtn = document.getElementById("verificarBtn");
  const estadoConexion = document.getElementById("estadoConexion");
  const cargarBtn = document.getElementById("cargarBtn");
  const listaProductos = document.getElementById("listaProductos");
  document.addEventListener("click", e => {
    const target = e.target;

    // Solo aplica a botones o elementos con clase .btn
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
      console.log("🔍 Probando conexión con el servidor...");
      estadoConexion.textContent = "🔄 Conectando...";
      estadoConexion.style.color = "blue";

      const response = await fetch(`${API_BASE}/api/`);
      
      if (!response.ok) {
        throw new Error(`Error HTTP: ${response.status}`);
      }

      const data = await response.json();
      console.log("✅ Respuesta del servidor:", data);
      
      estadoConexion.textContent = `✅ Conectado correctamente: ${data.mensaje || data.estado || 'Servidor activo'}`;
      estadoConexion.style.color = "green";
    } catch (error) {
      console.error("❌ Error de conexión:", error);
      estadoConexion.textContent = `❌ Error de conexión: ${error.message}`;
      estadoConexion.style.color = "red";
    }
  });

  // 🔹 Cargar lista de productos
  cargarBtn.addEventListener("click", async () => {
    try {
      console.log("🔄 Cargando productos...");
      listaProductos.innerHTML = "<p>🔄 Cargando productos...</p>";

      const response = await fetch(`${API_BASE}/api/productos/`);
      
      if (!response.ok) {
        throw new Error(`Error HTTP: ${response.status}`);
      }

      const data = await response.json();
      console.log("📦 Productos recibidos:", data);

      // Manejar diferentes estructuras de respuesta
      let productos = [];
      if (Array.isArray(data)) {
        productos = data; // Si la respuesta es directamente un array
      } else if (data.productos && Array.isArray(data.productos)) {
        productos = data.productos; // Si la respuesta tiene propiedad "productos"
      } else if (data.data && Array.isArray(data.data)) {
        productos = data.data; // Si la respuesta tiene propiedad "data"
      }

      if (!productos.length) {
        listaProductos.innerHTML = "<p>⚠️ No hay productos registrados.</p>";
        return;
      }

      // Mostrar productos
      listaProductos.innerHTML = "";
      productos.forEach((producto) => {
        const item = document.createElement("div");
        item.classList.add("producto");
        item.innerHTML = `
          <h3>${producto.nombre || 'Sin nombre'}</h3>
          <p>💲 Precio: $${producto.precio || '0.00'}</p>
          <p>🏷️ Código: ${producto.codigo || 'N/A'}</p>
          <p>📦 Stock: ${producto.stock || '0'}</p>
          ${producto.descripcion ? `<p>📝 ${producto.descripcion}</p>` : ''}
          ${producto.linea ? `<p>📋 Línea: ${producto.linea}</p>` : ''}
        `;
        listaProductos.appendChild(item);
      });

    } catch (error) {
      console.error("❌ Error cargando productos:", error);
      listaProductos.innerHTML = `
        <div style="color: red; text-align: center;">
          <p>❌ Error al cargar productos</p>
          <p><small>${error.message}</small></p>
          <p><small>Verifica que el endpoint /api/productos/ exista</small></p>
        </div>
      `;
    }
  });

  // 🔹 Función adicional para probar la base de datos
  const probarBaseDatos = async () => {
    try {
      console.log("🗄️ Probando conexión a base de datos...");
      const response = await fetch(`${API_BASE}/api/verificar-conexion/`);
      
      if (response.ok) {
        const data = await response.json();
        console.log("✅ Conexión BD:", data);
        return data;
      }
    } catch (error) {
      console.log("ℹ️ Endpoint de BD no disponible, pero el servidor funciona");
    }
  };

  // 🔹 Probar automáticamente la conexión al cargar la página
  console.log("🚀 Inicializando aplicación...");
  
  // Probar conexión básica al cargar
  setTimeout(() => {
    fetch(`${API_BASE}/api/`)
      .then(response => {
        if (response.ok) {
          console.log("🌐 Servidor conectado al cargar la página");
          estadoConexion.textContent = "✅ Servidor conectado (auto-detectado)";
          estadoConexion.style.color = "green";
        }
      })
      .catch(error => {
        console.log("ℹ️ Esperando verificación manual del servidor");
      });
  }, 1000);
});