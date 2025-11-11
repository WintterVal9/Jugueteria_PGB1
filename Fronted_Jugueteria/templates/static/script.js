document.addEventListener("DOMContentLoaded", () => {
  const verificarBtn = document.getElementById("verificarBtn");
  const estadoConexion = document.getElementById("estadoConexion");
  const cargarBtn = document.getElementById("cargarBtn");
  const listaProductos = document.getElementById("listaProductos");

  // 🧩 Verificar conexión con el backend
  verificarBtn.addEventListener("click", async () => {
    try {
      const response = await fetch("http://127.0.0.1:8000/verificar-conexion/");
      if (!response.ok) throw new Error("No se pudo conectar con el servidor");
      const data = await response.json();
      estadoConexion.textContent = `✅ Conectado: ${data.mensaje}`;
    } catch (error) {
      console.error(error);
      estadoConexion.textContent = "⚠️ No se pudo conectar con el servidor.";
    }
  });

  // 🧸 Cargar lista de productos
  cargarBtn.addEventListener("click", async () => {
    try {
      const response = await fetch("http://127.0.0.1:8000/productos/");
      if (!response.ok) throw new Error("Error al cargar productos");
      const productos = await response.json();

      listaProductos.innerHTML = "";
      productos.forEach(p => {
        const item = document.createElement("div");
        item.classList.add("producto");
        item.innerHTML = `
          <h3>${p.nombre}</h3>
          <p>Precio: $${p.precio}</p>
          <p>Categoría: ${p.categoria}</p>
        `;
        listaProductos.appendChild(item);
      });
    } catch (error) {
      console.error(error);
      listaProductos.innerHTML = "Error al cargar productos.";
    }
  });
});
