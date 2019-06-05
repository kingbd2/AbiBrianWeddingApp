<template>
  <div>
    <!-- <div class="container"> -->
    <section class="hero is-primary is-fullheight is-background">
      <div class="hero-head">
        <header>
          <div class="container">
            <div class="section">
              <div class="has-text-centered">
                <h1 class="title is-1 is-spaced has-text-info">Abiella & Brian are getting married!</h1>
                <h4 class="subtitle is-4 has-text-info">September 1st, 2019</h4>
                <h4 class="p is-4 has-text-info">Wildflowers Farm</h4>
                <h4 class="p is-4 has-text-info">42338 Fruit Ridge Line, St. Thomas, ON</h4>

              </div>
            </div>
          </div>
        </header>
      </div>
    </section>

    <section class="hero is-info is-fullheight is-background">
      <div class="hero-head">
        <div class="container">
          <div class="section">
            <div class="has-text-centered">
              <h1 class="title is-1 is-spaced has-text-info">We are very excited to celebrate with you!</h1>
              <h4 class="p is-4 has-text-info">Time until marriage:</h4>
              <h4 class="subtitle is-3 has-text-info">
                <Countdown class="has-text-info" deadline="September 1, 2019"></Countdown>
              </h4>
              <!-- <h4 class="p is-4 has-text-info">Wildflowers Farm</h4>
              <h4 class="p is-4 has-text-info">42338 Fruit Ridge Line, St. Thomas, ON</h4> -->
            </div>
          </div>
        </div>
      </div>
    </section>

  </div>
</template>

<script>
  import Countdown from '../components/Countdown'
  export default {
    components: {
      Countdown
    },
  }
</script>

<style lang="scss" scoped>
  @import url('https://fonts.googleapis.com/css?family=Karla|Source+Serif+Pro');

  .title {
    font-family: 'Source Serif Pro', serif;
    padding-top: 10%;
    padding-bottom: 2%;
  }

  .subtitle {
    font-family: 'Karla', sans-serif;
    padding-bottom: 10%;
  }

  p {
    font-family: 'Karla', sans-serif;
  }

  .subtitle.quote {
    padding-top: 2%;
  }

  .articles {
    padding-bottom: 5%;
    padding-top: 5%;
  }

  .container {
    margin-top: 5%;
  }

  .hero.is-primary.is-background {
    background: linear-gradient(rgba(255, 255, 255, .5), rgba(255, 255, 255, .99)), url('../assets/images/background-grey.png') no-repeat center center fixed;
    -webkit-background-size: cover;
    -moz-background-size: cover;
    -o-background-size: cover;
    background-size: cover;
    image-rendering: -webkit-optimize-contrast;
    // -webkit-filter: grayscale(100%);
    /* Chrome, Safari, Opera */
    // filter: grayscale(100%);
  }

  .hero.is-info.is-background {
    background: linear-gradient(rgba(255, 255, 255, .9), rgba(255, 255, 255, .1)), url('../assets/images/front.png') no-repeat center center fixed;
    -webkit-background-size: cover;
    -moz-background-size: cover;
    -o-background-size: cover;
    background-size: cover;
    image-rendering: -webkit-optimize-contrast;
    // -webkit-filter: grayscale(100%);
    /* Chrome, Safari, Opera */
    // filter: grayscale(100%);
  }
</style>