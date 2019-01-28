<template>
  <div id="app">
    <nav class="navbar navbar-expand-sm bg-dark navbar-dark">
      <ul class="navbar-nav">
        <li class="nav-item active">
          <a class="nav-link" href="/">Inicio</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/asignar-pasajero">Asignar Pasajero</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/trayectos/">Trayectos</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/buses/">Buses</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/pasajeros/">Pasajeros</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/choferes/">Choferes</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/itinerarios/crear">Itinerarios</a>
        </li>
      </ul>
    </nav>
    <router-view/>
  </div>
</template>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}
#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
