{% assign sequences = site.data.projects | where: "type", "sequence" %}

<div class="container">
    {% for project in sequences %}
        {% include project.html %}
    {% endfor %}
</div>

