<template>
    <div class="sectionheader_background">
        <h2 class="sectionheader_title">{{title}}</h2>
    </div>
</template>

<script>
export default {
    name: "SectionHeader",
    props: ['title', 'image'],
}
</script>

<style>
.sectionheader_title{
    color: black 
}
.sectionheader_background{
    /*background-image = url("")*/
    width:100%;
    margin: 0px;
    padding: 0px;
    margin-top: 1em;
    margin-bottom: 1em;
}
</style>
