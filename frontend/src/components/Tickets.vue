<template>
    <div id="tickets" class="container inforow">
        <p class="tickets-msg">{{$t('info.tickets.intro')}}</p>
        <a href="https://www.eventbrite.es/e/entradas-pycones-2019-61864318843">
            <button class="btn btn-primary">{{$t('info.tickets.button')}}</button>
        </a>
    </div>
</template>

<script>

export default {
    name: "Tickets",
    components: {
    },
}
</script>

<style>
.tickets-msg{
    font-size: 200%;
    font-weight: bold;
}
</style>
