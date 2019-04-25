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
                title="Coming soon"
                image_src="https://img.icons8.com/ios/420/user-female-filled.png"
                :description="$t('speakers.soon.desc')"
            />
            <InfoCard
                class="col-sm-10 offset-sm-1 col-md-5 offset-md-0 col-lg-3"
                title="Coming soon"
                image_src="https://img.icons8.com/ios/420/user-male-filled.png"
                :description="$t('speakers.soon.desc')"
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
