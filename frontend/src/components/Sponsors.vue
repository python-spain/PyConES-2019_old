<template>
    <div>
        <SectionHeader title="Sponsors" image="Diamantes o algo de dinero"/>
        <div>
            <ImageList title="Cornerstone" source=""/>
            <ImageList title="Diamond" source=""/>
            <ImageList title="Gold" source=""/>
        </div>
    </div>
</template>

<script>
import SectionHeader from './SectionHeader.vue'
import ImageList from './ImageList.vue'

export default {
    name: "PageSection",
    props: ['title', 'content'],
    components: {
        SectionHeader,
        ImageList
    }
}
</script>

<style>
</style>
