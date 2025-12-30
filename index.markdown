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
[this form](https://forms.gle/y6FwNjr2GR6E6Dg96)
and we will add the information to this site.

**We want your feedback!** 
We want to make the Pulseq framework even better, and your feedback will help us do that. 
How easy is it to use? Are there new features you’d like to see? 
What bottlenecks do you encounter in your current workflow with Pulseq?
Please let us know by filling out [this form](https://forms.gle/8c57r3MBmmv4FHxd7).

**New: Monthly Pulseq user group meeting!**
Anyone is welcome. Register [here](https://umich.zoom.us/meeting/register/DDHjJS_lTtS9ADGvekSKQw).
To volunteer to be a presenter in a future meeting, please fill out
[this form](https://docs.google.com/forms/d/e/1FAIpQLSf1R9NUyfXBFbpWf41XUk6P0UgFFzO6o4aJizxgrgTocL-17A/viewform?usp=header).
Recordings of past meetings are available at [https://www.youtube.com/@HarmonizedMRI](https://www.youtube.com/@HarmonizedMRI).
For more details, go [here](https://drive.google.com/drive/folders/1TBqcPHiFBNdjTZS_6Jb2JIfkquirwAGR?usp=sharing).

**New: Mailing list!** 
Email Address: <harmonizedmri@researchlist.partners.org>  
You can subscribe/unsubscribe by sending an email to:  
<subscribe-harmonizedmri@researchlist.partners.org>  
<unsubscribe-harmonizedmri@researchlist.partners.org>


We invite projects that support any part of an open, vendor-agnostic MRI workflow:

<br>
<img src="{{ site.baseurl }}/assets/images/hmri.png" alt="HarmonizedMRI"/> <!-- width="800"/> -->

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
            <img src="{{ site.baseurl }}{{ featured_project.logo }}" alt="{{ featured_project.title }} Logo" />
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
