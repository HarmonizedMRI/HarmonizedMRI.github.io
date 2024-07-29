---
layout: page
title: Projects
permalink: /projects/
---

<div id="filterContainer">
  <input type="text" id="searchBox" placeholder="Search projects...">
  <select id="categoryFilter">
    <option value="all">All Categories</option>
    <option value="Sequence programming">Sequence programming</option>
    <option value="Image reconstruction">Image reconstruction</option>
    <option value="Image processing">Image processing</option>
    <option value="Simulations">Simulations</option>
    <option value="Protocol workflow">Protocol workflow</option>
    <option value="Pulseq interpreter">Pulseq interpreter</option>
    <option value="fMRI">fMRI</option>
    <option value="Diffusion">Diffusion</option>
    <option value="Quantitative MRI">Quantitative MRI</option>
    <option value="13C/MNS">13C/MNS</option>
  </select>
</div>

<div id="projectList">
  {% for project in site.data.projects %}
    {% include project.html %}
  {% endfor %}
</div>

<script src="{{ site.baseurl }}/assets/js/search.js"></script>
