<template>
    <div>
        <h2 class="imagelist_title">{{title}}</h2>
        <p>Aquí van las imágenes con source {{source}}</p>
    </div>
</template>

<script>
export default {
    name: "ImageList",
    props: ['title', 'source'],
}
</script>

<style>
.imagelist_title{
    color: green
}
</style>
