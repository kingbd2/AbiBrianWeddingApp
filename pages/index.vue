<template>
  <div>

    <section class="hero is-primary">
      <div class="hero-body">
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

    <section class="container">
      <div>
        <figure>
          <img
            src="https://berqdg.bn.files.1drv.com/y4ml13TGhWP7VNsb9cqUVcto_Hhmb7uVQPhLI5fIwKd1Qf2NvqOZBdu6W65bMcTil5UGo3u9gVcT2XW6FO46skmjMn1yNxcgdQ7UjlHAUvn_PxUJZqd3m-qE97IhsPyYVup3n64PmvaRCmrMCqsflCUu7Mahd4nEdiD2fPbn1U0bifT_WHc8dGPRJBzaBMVbwDrPwYjwBRduvMAgOV0sjQE-w?width=2428&height=1366&cropmode=none"
            width="400" height="427" />
        </figure>

        <h1 class="title">
          We're getting married!
        </h1>
        <h2 class="subtitle">
          And we want to celebrate with you.
        </h2>

      </div>
    </section>
  </div>
</template>

<script>
  import Logo from '~/components/Logo.vue'

  export default {
    components: {
      Logo,
    },
    mounted() {
      console.log(this.$route.params.slug);
    }
  }
</script>

<style lang="scss" scoped>
  @import url('https://fonts.googleapis.com/css?family=Karla|Source+Serif+Pro');

  .title {
    font-family: 'Karla', sans-serif;
    // padding-top: 5%;
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
    background: linear-gradient(rgba(255, 255, 255, .8), rgba(255, 255, 255, .6)), url('../assets/images/front.png') no-repeat center center fixed;
    -webkit-background-size: cover;
    -moz-background-size: cover;
    -o-background-size: cover;
    background-size: cover;
  }
</style>