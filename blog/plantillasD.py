  <div>
        <h1><a href="/">Django Girls Blog</a></h1>
    </div>

    {% for post in posts %}
        <div>
            <p>Campo: {{ post.autor }}</p>
            <p>Campo: {{ post.titulo }}</p>
            <p>Campo: {{ post.texto }}</p>
            <p>Campo: {{ post.fecha }}</p>
            <p>Campo: {{ post.fecha }}</p>
            <p>Campo: {{ post.fecha_creacion }}</p>
            <p>Campo: {{ post.fecha_publicacion }}</p>
            <h1><a href="">{{ post.title }}</a></h1>
            <p>{{ post.text|linebreaks }}</p>
        </div>
    {% endfor %}
