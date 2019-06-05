<template>
  <div>
    <!-- <div class="container"> -->
    <section class="hero is-primary is-fullheight is-background">
      <div class="hero-head">
        <header>
          <div class="container">
            <div class="section">
              <div class="has-text-centered">
                <h1 class="title is-1 is-spaced has-text-info">Abiella & Brian</h1>
                <h4 class="subtitle is-4 has-text-info">September 1st, 2019</h4>
                <h4 class="p is-4 has-text-info">Wildflowers Farm</h4>
                <h4 class="p is-4 has-text-info">42338 Fruit Ridge Line, St. Thomas, ON</h4>
              </div>
            </div>
            <!-- <div class="section has-text-info">
              <div class="tabs is-centered">
                <ul>
                  <li class="is-active"><a href="index.html">Home</a></li>
                  <li><a href="post.html">Static Post</a></li>
                  <li><a href="">Portfolio</a></li>
                  <li><a href="">Search</a></li>
                  <li><a href="contact.html">Contact</a></li>
                  <li><a href="about.html">About</a></li>
                </ul>
              </div>
            </div> -->
          </div>
        </header>
      </div>
    </section>

    <section class="hero is-info is-fullheight is-background">
      <div class="hero-head">
    <div class="container">
      <h1 class="title has-text-info">
        Abiella & Brian
      </h1>
      <h2 class="subtitle has-text-info">
        August 24, 2019 • 5850 Rokeby Line, Petrolia, ON
      </h2>
    </div>
      </div>
    </section>

  </div>
</template>

<script>
  export default {
    components: {

    },
  }
</script>

<style lang="scss" scoped>
  @import url('https://fonts.googleapis.com/css?family=Karla|Source+Serif+Pro');

  .title {
    font-family: 'Karla', sans-serif;
    padding-top: 10%;
    padding-bottom: 2%;
  }

  .subtitle {
    font-family: 'Source Serif Pro', serif;
    padding-bottom: 10%;
  }

  p {
    font-family: 'Source Serif Pro', serif;
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

  .hero.is-primary {
    background: linear-gradient(rgba(255, 255, 255, .8), rgba(255, 255, 255, .6)), url('https://axisya.bn.files.1drv.com/y4mTNWo6kutfQ1dEuy9Oc-kCFAVYl9dj3rUly1lPI7CE3WS37cqyzTRq-U_HKDGWbcXD-BHvQ5jtVjKX830Y2vU95IT8x733X77mMqkDQ1XIQ7Km9Jd-ifGAOh2MaRfrxorEbkDVbw-5b1X9ezAfANEXThStzIXUFdbpKslo8tq8acQ2UItkVuJFq3PBBlILNXWmUdLf2x7LeyiUkeTEynh7Q?width=640&height=427&cropmode=none') no-repeat center center fixed;
    -webkit-background-size: cover;
    -moz-background-size: cover;
    -o-background-size: cover;
    background-size: 300 300;
    background-position: 50% 50%;
    image-rendering: -webkit-optimize-contrast;
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
    background: linear-gradient(rgba(255, 255, 255, .9), rgba(255, 255, 255, .5)), url('../assets/images/front.png') no-repeat center center fixed;
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