---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: home
---

<h1> Welcome to the Pulseq project list! </h1>

This site provides a list of
community-developed MRI pulse sequence and development tools
based on the Pulseq file format for vendor-agnostic MRI.
It is meant to supplement the official Pulseq site and repository,
[https://pulseq.github.io/](https://pulseq.github.io/).

We would love for you to **contribute your own project to this site**!
To do so, fill out

[//]: # ([this Google form]&#40;https://forms.gle/y6FwNjr2GR6E6Dg96&#41;)
[this Google form](https://forms.gle/qVAzKdGqwghET7dB7)
and we will add the information to this site.

We invite projects that support any part of an open, vendor-agnostic MRI workflow:

<br>
<img src="{{ site.baseurl }}/assets/hmri.png" alt="HarmonizedMRI"/> <!-- width="800"/> -->

<!--
{% for post in site.pages %}
<li> <a href="{{ post.url }}">{{ post.title }}</a></li>
{% endfor %}
-->

<!-- Featured Project Section -->
<br>
<h2>Featured Project</h2>
<div id="featuredProject">
  {% assign featured_project = site.data.projects | where_exp: "item", "item.featured == 'true' or item.featured == 'True'" | first %}
  {% if featured_project %}
    <div class="project-item" data-category="{{ featured_project.category | join: ', ' }}">
      <div class="project-logo">
        {% if featured_project.logo %}
          <a href="{{ featured_project.url }}" target="_blank">
            <img src="{{ site.baseurl }}/{{ featured_project.logo }}" alt="{{ featured_project.title }} Logo" />
          </a>
        {% else %}
          <a href="{{ featured_project.url }}" target="_blank">{{ featured_project.title }}</a>
        {% endif %}
      </div>
      <div class="project-content">
        <p class="categories">{{ featured_project.category | join: ', ' }}</p>
        <h3>{{ featured_project.title }}</h3>
        <p>{{ featured_project.description }}</p>
      </div>
    </div>
  {% else %}
    <p>No featured project at this time.</p>
  {% endif %}
</div>
