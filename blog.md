---
layout: default
title: Blog
permalink: /blog/
---

<h2>Lab Notes</h2>

<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ site.baseurl }}{{ post.url}}">{{ post.title }}</a> – <small>{{ post.date | date: "%B %d, %Y" }}</small>
    </li>
  {% endfor %}
</ul>