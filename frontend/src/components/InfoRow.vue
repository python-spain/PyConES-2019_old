<template>
    <div id="info" class="container inforow">
        <div class="row">
            <InfoCard
                class="col-sm-10 offset-sm-1 col-lg-4 offset-lg-0"
                :title="$t('info.event.title')"
                image_src="/static/logo.png"
                :description="$t('info.event.desc')"
            />
            <InfoCard
                class="col-sm-10 offset-sm-1 col-lg-4 offset-lg-0"
                :title="$t('info.sponsors.title')"
                image_src="http://d36m266ykvepgv.cloudfront.net/uploads/media/HsFp1O2KHY/s-368-252/icon-sponsors2.png"
                :description="$t('info.sponsors.desc')"
                :link="$t('info.sponsors.file')"
                :button_text="$t('info.sponsors.button')"
                />
            <InfoCard
                class="col-sm-10 offset-sm-1 col-lg-4 offset-lg-0"
                :title="$t('info.call.title')"
                image_src="/static/cfp.png"
                :description="$t('info.call.desc')"
                link="https://easychair.org/cfp/pycones2019"
                :button_text="$t('info.call.button')"
            />
        </div>
    </div>
</template>

<script>
import InfoCard from './InfoCard.vue'

export default {
    name: "InfoRow",
    components: {
        InfoCard
    }
}
</script>

