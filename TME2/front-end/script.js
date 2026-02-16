/**
 * Donn&eacute;es "cod&eacute;es en dur" (locales) pour tester l'affichage.
 * IMPORTANT :
 * - Remplacez les champs "image" par les vrais noms de fichiers plac&eacute;s dans /images
 * - Exemple : images/inception.jpg
 */

async function loadMovies() {
  //on peut faire un try catch ici pour gérer les erreurs
  const res = await fetch(`http://127.0.0.1:8000/movies`);
  if (!res.ok) {
      console.error("Erreur serveur:", res.status);
      return [];
  }
  const movies = await res.json()
  return movies
}

// URL de base de l'API, pour construire les liens vers les images
const API_BASE = "http://127.0.0.1:8000";
// Récupération du conteneur où les cartes de films seront insérées
const container = document.getElementById("movies");

/**
 * G&eacute;n&egrave;re les cartes de films dans la page.
 */
loadMovies().then(moviesList => {
  // On utilise forEach pour créer une carte pour CHAQUE film
  moviesList.forEach(movie => {
    const card = document.createElement("article");
    card.className = "card";
    card.innerHTML = `
      <img src="${API_BASE}${movie.image_url}" alt="${movie.title}">
      <div class="card-content">
        <h2>${movie.title}</h2>
        <p class="meta"><strong>Réalisateur :</strong> ${movie.director}</p>
        <p class="desc">${movie.genre}</p>
      </div>
    `;
    container.appendChild(card);
  });
});