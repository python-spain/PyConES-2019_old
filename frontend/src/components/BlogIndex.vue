<template>
    <div id="blog-index" class="container">
        <h2 class="title">
            BLOG
        </h2>
        <div class="last_post">
            <img src="https://sarcastickled.files.wordpress.com/2014/05/3545320-7140595685-hobbi.jpg" alt="Last post image" />
            <a :href="last_post.link">
                <h3>{{last_post.title}}</h3>
                <p>{{last_post.short_description}}</p>
            </a>
        </div>
        <div class="post_list">
            <h3>{{ $t("blog.prev_posts") }}</h3>
            <div v-for="post in posts">
                <a :href="post.link">
                    <p class="post_title">{{post.title}}</p>
                    <p>{{post.short_description}}</p>
                </a>
                <hr>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: "BlogIndex",
    components: {},
    data(){
        return {
            last_post: 'hola mundo',
            posts: []
        }
    },
    methods: {
        set_first_post(){
            axios.get('http://localhost:8000/backend/post')
                .then(response => {
                    this.last_post = response.data[response.data.length -1]
                    this.last_post.link = 'blog/' + this.last_post.external_id
                    this.posts = response.data.slice(0, -1)
                    this.posts.forEach(
                        (item) => {item.link = 'blog/' + item.external_id}
                    )
                })
                .catch(error => console.log(error))
        }
    },
    created(){
        this.$eventBus.$on('locale-change', (data) => {
            this.set_first_post()
        });
        this.set_first_post()
    },
}
</script>
<style>
.title{
    margin-top:1em;
}

.last_post{
    text-align: left;
}
.last_post > img{
    max-width: 80%;
    margin-left: 10%;
}
.last_post > a{
    color: #2c3e50;
}
.last_post > a:hover {
    text-decoration: none;
    color: blue;
}

.post_list{
    text-align: left;
}
.post_list .post_title{
    font-weight: bold;
}
.post_list > div > a {
    color: #2c3e50;
}
.post_list > div > a:hover{
    text-decoration: none;
    color: blue;
}

.blog_index > a{
    color: black;
    text-decoration: None;
}

</style>
