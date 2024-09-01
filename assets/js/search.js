document.addEventListener("DOMContentLoaded", function() {
  const searchBox = document.getElementById("searchBox");
  const categoryFilter = document.getElementById("categoryFilter");
  const projectItems = document.querySelectorAll(".project-item");

  searchBox.addEventListener("input", filterProjects);
  categoryFilter.addEventListener("change", filterProjects);

  function filterProjects() {
    const searchQuery = searchBox.value.toLowerCase();
    const selectedCategory = categoryFilter.value;

    projectItems.forEach(function(item) {
      const title = item.querySelector("h3").textContent.toLowerCase();
      const categories = item.getAttribute("data-category").split(',').map(cat => cat.trim());

      const matchesSearch = title.includes(searchQuery);
      const matchesCategory = selectedCategory === "all" || categories.includes(selectedCategory);

      if (matchesSearch && matchesCategory) {
        item.style.display = "";
      } else {
        item.style.display = "none";
      }
    });
  }
});
