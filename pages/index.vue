<template>
  <section class="container">
    <div>
      <!-- <logo /> -->
      <!-- <div class="columns is-centered is-vcentered">
        <div class="column has-text-centered is-one-third">
          <div class="textcontainer">
            <h1 class="title has-text-primary">Shmells and Marty</h1>
            <h2 class="subtitle has-text-info">The queen and king of cheesy</h2>
          </div>
        </div>
        <div class="column is-one-third is-offset-2 has-text-centered">
          <figure class="image is-256x256">
            <img class="is-rounded" src="../../assets/images/brianandabi/brianandabi4.jpg" alt="Shmells and Marty">
          </figure>
        </div>
      </div> -->
      <!-- <figure class="image is-128x128">
        <img src="../assets/images/front.png">
      </figure> -->
      <figure>
        <img src="https://berqdg.bn.files.1drv.com/y4ml13TGhWP7VNsb9cqUVcto_Hhmb7uVQPhLI5fIwKd1Qf2NvqOZBdu6W65bMcTil5UGo3u9gVcT2XW6FO46skmjMn1yNxcgdQ7UjlHAUvn_PxUJZqd3m-qE97IhsPyYVup3n64PmvaRCmrMCqsflCUu7Mahd4nEdiD2fPbn1U0bifT_WHc8dGPRJBzaBMVbwDrPwYjwBRduvMAgOV0sjQE-w?width=2428&height=1366&cropmode=none" 
        width="400" height="427" />
      </figure>

      <h1 class="title">
        We're getting married!
      </h1>
      <h2 class="subtitle">
        And we want to celebrate with you.
      </h2>
      <!-- <section class="hero is-primary">
        <div class="hero-body">
          <div class="container">
            <h1 class="title">
              Primary title
            </h1>
            <h2 class="subtitle">
              Primary subtitle
            </h2>
          </div>
        </div>
      </section> -->
    </div>
  </section>
</template>

<script>
  import Logo from '~/components/Logo.vue'

  export default {
    components: {
      Logo
    }
  }
</script>

<style lang="scss">
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
</style>