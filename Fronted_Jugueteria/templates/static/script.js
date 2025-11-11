const API_URL = "http://127.0.0.1:8000/api";

document.getElementById("verificarBtn").addEventListener("click", async () => {
  const estado = document.getElementById("estadoConexion");
  estado.textContent = "Verificando...";
  try {
    const res = await fetch(`${API_URL}/verificar-conexion/`);
    const data = await res.json();
    if (data.status === "ok") {
      estado.textContent = `✅ Conectado a la base de datos: ${data.database}`;
      estado.style.color = "green";
    } else {
      estado.textContent = "❌ Error al conectar.";
      estado.style.color = "red";
    }
  } catch (err) {
    estado.textContent = "⚠️ No se pudo contactar al servidor.";
    estado.style.color = "red";
  }
});

document.getElementById("cargarBtn").addEventListener("click", async () => {
  const contenedor = document.getElementById("listaProductos");
  contenedor.innerHTML = "<p>Cargando productos...</p>";

  try {
    const res = await fetch(`${API_URL}/productos/`);
    const data = await res.json();
    if (data.count > 0) {
      contenedor.innerHTML = "";
      data.productos.forEach(p => {
        contenedor.innerHTML += `
          <div class="producto">
            <h3>${p.nombre}</h3>
            <p><b>Código:</b> ${p.codigo}</p>
            <p><b>Precio:</b> $${p.precio}</p>
            <p><b>Stock:</b> ${p.stock}</p>
          </div>
        `;
      });
    } else {
      contenedor.innerHTML = "<p>No hay productos disponibles.</p>";
    }
  } catch (err) {
    contenedor.innerHTML = "<p style='color:red;'>Error al cargar productos.</p>";
  }
});
