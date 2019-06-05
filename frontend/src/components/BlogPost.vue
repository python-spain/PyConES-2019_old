<template>
    <div id="blog-post" class="container">
        <img :src="post.image" alt="Post image" />
        <div class="left-text">
            <h2 class="title">{{post.title}}</h2>
            <p class="author">{{post.created_on}} por {{post.author}}.</p>
            <hr>
            <div v-html="post.body" class="post-content"></div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: "BlogPost",
    components: {},
    data(){
        return {
            post: {}
        }
    },
    methods: {
        set_post(){
            axios.get('http://localhost:8000/backend/post/' + this.$route.params.id)
                .then(response => {
                    this.post = response.data
                })
                .catch(error => console.log(error))
        }
    },
    created(){
        this.$eventBus.$on('locale-change', (data) => {
            this.set_post()
        });
        this.set_post()
    },
}
</script>
<style>
.title{
    margin-top:1em;
}

.author{
    font-size: 80%;
    color: grey;
}

.left-text {
    text-align: left;
}
#blog-post > img{
    max-width: 80%;
    margin-left: 10%;
    max-height: 500px;
}
#blog-post a{
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
