<template>
  <section class="container">
    <div>
      <!-- <logo /> -->
      <figure class="image is-128x128">
        <img src="../../assets/images/front.png">
      </figure>
      <figure class="image is-128x128">
        <img src="https://b0rldg.bn.files.1drv.com/y4mjEgv7U-YShZxhuJGHcJq570FGnpqtH_jbTDJc2YkIw5HzIp2Oc_uHBR2HqfA-H_KXitQQHgXmWp5jH9GfwMIEg3Fn0U55lS8ZUxGSdZ-Nv3UQjnnbyZgCHTMGgpqayG045cevXad1xeSDcTFVupt1aYowxr9sKCPN2yKbthO-lmdUiyR25tO1tsTLhF4aC-W7g2fqZMdNUat-4D4ZOyc9A?width=640&height=427&cropmode=none" width="640" height="427" />
      </figure>
      <h1 class="title">
        We're getting married!
      </h1>
      <h2 class="subtitle">
        Abi and Brian wedding app
      </h2>
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

<style>
  .container {
    margin: 0 auto;
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
  }

  .title {
    font-family: 'Quicksand', 'Source Sans Pro', -apple-system, BlinkMacSystemFont,
      'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
    display: block;
    font-weight: 300;
    font-size: 100px;
    color: #35495e;
    letter-spacing: 1px;
  }

  .subtitle {
    font-weight: 300;
    font-size: 42px;
    color: #526488;
    word-spacing: 5px;
    padding-bottom: 15px;
  }

  .links {
    padding-top: 15px;
  }
</style>