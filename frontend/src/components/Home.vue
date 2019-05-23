<template>
    <div>
        <Header />
        <Tickets />
        <InfoRow/>
        <KeySpeakers/>
    </div>
</template>

<script>
//import axios from 'axios'
import Sponsors from './Sponsors.vue'
import KeySpeakers from './KeySpeakers.vue'
import InfoRow from './InfoRow.vue'
import Header from './Header.vue'
import Tickets from './Tickets.vue'

export default {
    components: {
        Header,
        Sponsors,
        KeySpeakers,
        InfoRow,
        Tickets
    },
}
</script>
