// document.addEventListener('DOMContentLoaded', function() {
//   const projectList = document.getElementById('projectList');
//
//   projectList.addEventListener('click', function(e) {
//     if (e.target && e.target.classList.contains('read-more')) {
//       e.preventDefault();
//       const description = e.target.previousElementSibling;
//       description.classList.toggle('expanded');
//       e.target.textContent = description.classList.contains('expanded') ? 'Less' : 'Read more';
//     }
//   });
// });
document.addEventListener("DOMContentLoaded", function() {
  const descriptions = document.querySelectorAll('.project-item .description');

  descriptions.forEach(description => {
    const readMore = description.nextElementSibling; // The "Read more" link

    if (description.clientHeight < description.scrollHeight) {
      readMore.style.display = 'inline'; // Show the "Read more" link

      readMore.addEventListener('click', function(e) {
        e.preventDefault();
        if (description.classList.contains('expanded')) {
          description.classList.remove('expanded');
          readMore.textContent = 'Read more';
        } else {
          description.classList.add('expanded');
          readMore.textContent = 'Read less';
        }
      });
    }
  });
});
