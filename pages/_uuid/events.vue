<template>
    <div>
        <section class="hero is-white is-fullheight">
            <div class="hero-body">
                <div class="container">
                    <div>
                        <!-- <h1 class="title has-text-info"> {{ error }}</h1> -->

                        <div class="tile is-ancestor">
                            <div class="tile is-vertical is-8">
                                <div class="party">
                                    <div class="loading" v-if="loading">
                                        <h1 class="title has-text-info"> Loading...</h1>
                                    </div>

                                    <div v-if="error" class="error">
                                        <h1 class="title has-text-info"> {{ error }}</h1>
                                        <h2 class="subtitle has-text-info">
                                            If this doesn't work, <nuxt-link class="has-text-primary" to="/">check out
                                                the rest of our wedding site!</nuxt-link>
                                        </h2>
                                    </div>

                                    <div class="content">
                                        <p class="is-size-3 has-text-success has-text-left has-text-weight-bold">We hope to see you at the following wedding weekend events:</p>
                                    </div>
                                </div>
                            </div>
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
        // padding-top: 5%;
    }

    .is-size-3 {
        padding-top: 5%;
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

    .hero.is-white {
        background: linear-gradient(rgba(255, 255, 255, .8), rgba(255, 255, 255, .6)), url('https://b0rtdg.bn.files.1drv.com/y4mUKhWv84jRu2sffpC_unLOD1mj7KsVbvKBnvKcXsgvHA54Vf4f1An1wG31t6yJnqKDYP3aUclf-b4s3bbD8JpmKMVY73vGJesWbp09zpMh96z1JPEb_1nS8jpCuXWn8uIArzw3I6iTShKuhnqcx9sxmfCogjKxNQI7fmzmnzVB_fKT_3L-7wwN4IpSBsJLJPkM_OwVjGIfbJJPnz4W4ahEg?width=1500&height=2000&cropmode=none') no-repeat center center fixed;
        -webkit-background-size: cover;
        -moz-background-size: cover;
        -o-background-size: cover;
        background-size: cover;
    }
</style>