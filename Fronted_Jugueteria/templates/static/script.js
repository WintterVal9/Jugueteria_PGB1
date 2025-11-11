document.addEventListener("DOMContentLoaded", () => {
  const estadoConexion = document.getElementById("estadoConexion");
  const listaProductos = document.getElementById("listaProductos");
  const verificarBtn = document.getElementById("verificarBtn");
  const cargarBtn = document.getElementById("cargarBtn");

  // Verificar conexión
  verificarBtn.addEventListener("click", async () => {
    estadoConexion.textContent = "Verificando...";
    try {
      const res = await fetch("http://127.0.0.1:8000/api/verificar-conexion/");
      const data = await res.json();
      if (data.status === "ok") {
        estadoConexion.textContent = `✅ Conectado a la base de datos: ${data.database}`;
        estadoConexion.style.color = "green";
      } else {
        estadoConexion.textContent = "❌ Error en la conexión.";
        estadoConexion.style.color = "red";
      }
    } catch (error) {
      estadoConexion.textContent = "⚠️ No se pudo conectar con el servidor.";
      estadoConexion.style.color = "red";
    }
  });

  // Cargar productos
  cargarBtn.addEventListener("click", async () => {
    listaProductos.innerHTML = "Cargando productos...";
    try {
      const res = await fetch("http://127.0.0.1:8000/api/productos/");
      const data = await res.json();

      if (data.productos && data.productos.length > 0) {
        listaProductos.innerHTML = "";
        data.productos.forEach(p => {
          const card = document.createElement("div");
          card.className = "producto";
          card.innerHTML = `
            <h3>${p.nombre}</h3>
            <p><b>Código:</b> ${p.codigo}</p>
            <p><b>Precio:</b> $${p.precio}</p>
            <p><b>Stock:</b> ${p.stock}</p>
          `;
          listaProductos.appendChild(card);
        });
      } else {
        listaProductos.innerHTML = "<p>No hay productos registrados.</p>";
      }
    } catch (error) {
      listaProductos.innerHTML = "<p style='color:red;'>Error al cargar productos.</p>";
    }
  });
});
