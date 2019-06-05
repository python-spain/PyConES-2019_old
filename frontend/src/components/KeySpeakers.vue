<template>
    <div id="keyspeakers" class="container">
        <SectionHeader :title="$t('speakers.title')" image=""/>
        <div class="row">
            <InfoCard 
                class="col-sm-10 offset-sm-1 col-md-5 col-lg-3 offset-lg-0"
                title="Safia Abdalla"
                image_src="static/keynoters/safia.jpg"
                :description="$t('speakers.safia.desc')"
            />
            <InfoCard
                class="col-sm-10 offset-sm-1 col-md-5 offset-md-0 col-lg-3"
                title="Francisco Javier Ordoñez"
                image_src="static/keynoters/fj.jpg"
                :description="$t('speakers.fj.desc')"
            />
            <InfoCard
                class="col-sm-10 offset-sm-1 col-md-5 col-lg-3 offset-lg-0"
                title="Mabel Delgado"
                image_src="static/keynoters/mabel.jpg"
                :description="$t('speakers.mabel.desc')"
            />
            <InfoCard
                class="col-sm-10 offset-sm-1 col-md-5 offset-md-0 col-lg-3"
                title="Pablo Galindo"
                image_src="static/keynoters/galindo.jpg"
                :description="$t('speakers.galindo.desc')"
            />
        </div>
    </div>
</template>

<script>
import SectionHeader from './SectionHeader.vue'
import InfoCard from './InfoCard.vue'

export default {
    name: "KeySpeakers",
    components: {
        SectionHeader,
        InfoCard
    }
}
</script>
