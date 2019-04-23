<template>
  <div>
    <b-carousel
      id="carousel-1"
      v-model="slide"
      :interval="4000"
      background="#ababab"
      img-width="1024"
      img-height="480"
      style="text-shadow: 1px 1px 2px #333;overflow: hidden;"
      @sliding-start="onSlideStart"
      @sliding-end="onSlideEnd"
    >
      <!-- Text slides with image -->
      <b-carousel-slide
        caption="PyConES 2019"
        text="Alicante, España. Octubre 04-06 2019"
        img-src="static/UAs.jpg"
        >
      </b-carousel-slide>

      <!-- Slides with custom text -->
      <b-carousel-slide 
        caption="PyConES 2019"
        text="Alicante, España. Octubre 04-06 2019"
        img-src="static/Alicante_vista.jpg"
      >
      </b-carousel-slide>

      <!-- Slides with image only -->
      <b-carousel-slide 
        caption="PyConES 2019"
        text="Alicante, España. Octubre 04-06 2019"
        img-src="static/alicante_prom.jpg"
      ></b-carousel-slide>

    </b-carousel>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        slide: 0,
        sliding: null
      }
    },
    methods: {
      onSlideStart(slide) {
        this.sliding = true
      },
      onSlideEnd(slide) {
        this.sliding = false
      }
    }
  }
</script>

