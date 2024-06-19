---
layout: page
title: Projects
permalink: /projects/
---


<h3> <u> Pulseq interpreters </u> </h3>
<div class="container">
    {% for project in site.data.projects %}
        {% if project.category contains "Pulseq interpreter" %}
            {% include project.html %}
        {% endif%}
    {% endfor %}
</div>

<br>
<h3> <u> Pulse sequences and sequence development tools </u> </h3>
<div class="container">
    {% for project in site.data.projects %}
        {% if project.category contains "Sequence programming" %}
            {% include project.html %}
        {% endif%}
    {% endfor %}
</div>

<br>
<h3> <u> Image reconstruction </u> </h3>
<div class="container">
    {% for project in site.data.projects %}
        {% if project.category contains "Image reconstruction" %}
            {% include project.html %}
        {% endif%}
    {% endfor %}
</div>

<!--
<a href="https://lh3.googleusercontent.com/drive-viewer/AKGpihbeQVhsdXR-DR-NmH47bP7vMPda_eimgw8BsU0gKQaa0_LZHY88DFh1ZMXmKFDE1Zn4Af6MNmpAo0EpIG8ma5Lw-G5IxDyPwiU=s1600-rw-v1?source=screenshot.guru"> <img src="https://lh3.googleusercontent.com/drive-viewer/AKGpihbeQVhsdXR-DR-NmH47bP7vMPda_eimgw8BsU0gKQaa0_LZHY88DFh1ZMXmKFDE1Zn4Af6MNmpAo0EpIG8ma5Lw-G5IxDyPwiU=s1600-rw-v1" /> </a>
-->

<!--
<img src="https://lh3.googleusercontent.com/drive-viewer/AKGpihbeQVhsdXR-DR-NmH47bP7vMPda_eimgw8BsU0gKQaa0_LZHY88DFh1ZMXmKFDE1Zn4Af6MNmpAo0EpIG8ma5Lw-G5IxDyPwiU=s1600-rw-v1" />

<img src="https://drive.google.com/uc?id=1NXFqofC68pAttkQpm6i21V2PRj2JUJ01&export=view" />
<img src="https://drive.google.com/uc?id=1NXFqofC68pAttkQpm6i21V2PRj2JUJ01" />
<img src="https://drive.usercontent.google.com/download?id=1NXFqofC68pAttkQpm6i21V2PRj2JUJ01"/>
<img src="https://lh3.googleusercontent.com/drive-viewer/uc?id=1NXFqofC68pAttkQpm6i21V2PRj2JUJ01"/>
<img src="https://drive.google.com/file/d/1NXFqofC68pAttkQpm6i21V2PRj2JUJ01/view?usp=sharing"/>
-->
