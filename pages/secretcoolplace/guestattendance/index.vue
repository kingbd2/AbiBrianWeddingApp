<template>
    <div>
        <section class="hero is-fullheight is-primary is-background">
            <div class="hero-body">
                <div class="container has-text-centered">
                    <div class="columns is-vcentered">
                        <div class="column is-5">
                            <figure class="image">
                                <img src="https://axisya.bn.files.1drv.com/y4mTNWo6kutfQ1dEuy9Oc-kCFAVYl9dj3rUly1lPI7CE3WS37cqyzTRq-U_HKDGWbcXD-BHvQ5jtVjKX830Y2vU95IT8x733X77mMqkDQ1XIQ7Km9Jd-ifGAOh2MaRfrxorEbkDVbw-5b1X9ezAfANEXThStzIXUFdbpKslo8tq8acQ2UItkVuJFq3PBBlILNXWmUdLf2x7LeyiUkeTEynh7Q?width=640&height=427&cropmode=none"
                                    alt="Description">
                            </figure>
                        </div>
                        <div class="column is-6 is-offset-1">
                            <h1 class="title is-4 has-text-info">
                                Are you supposed to be here?
                            </h1>
                            <br>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </div>
</template>

<script>
    export default {

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

    img {
        -webkit-filter: grayscale(100%);
        /* Chrome, Safari, Opera */
        filter: grayscale(100%);
    }

    .hero.is-primary.is-background {
        background: linear-gradient(rgba(255, 255, 255, .6), rgba(255, 255, 255, .99)), url('https://b0rtdg.bn.files.1drv.com/y4mUKhWv84jRu2sffpC_unLOD1mj7KsVbvKBnvKcXsgvHA54Vf4f1An1wG31t6yJnqKDYP3aUclf-b4s3bbD8JpmKMVY73vGJesWbp09zpMh96z1JPEb_1nS8jpCuXWn8uIArzw3I6iTShKuhnqcx9sxmfCogjKxNQI7fmzmnzVB_fKT_3L-7wwN4IpSBsJLJPkM_OwVjGIfbJJPnz4W4ahEg?width=1500&height=2000&cropmode=none') no-repeat center center fixed;
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