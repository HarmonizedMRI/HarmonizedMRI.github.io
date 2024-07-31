document.addEventListener('DOMContentLoaded', function() {
  const projectList = document.getElementById('projectList');

  projectList.addEventListener('click', function(e) {
    if (e.target && e.target.classList.contains('read-more')) {
      e.preventDefault();
      const description = e.target.previousElementSibling;
      description.classList.toggle('expanded');
      e.target.textContent = description.classList.contains('expanded') ? 'Less' : 'Read more';
    }
  });
});
