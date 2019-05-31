<template>
    <div>
        <section class="hero is-fullheight is-primary is-background">
            <div class="hero-body">
                <div class="container has-text-centered">
        <div class="columns is-multiline">
            <div class="column is-one-quarter-desktop is-half-tablet">
                <div class="card">
                    <div class="card-image">
                        <figure class="image is-3by2">
                            <img src="https://unsplash.it/300/200/?random&pic=1" alt="">
                        </figure>
                        <div class="card-content is-overlay is-clipped">
                            <span class="tag is-info">
                                Photo Title That is really long to show the clipping
                            </span>
                        </div>
                    </div>
                    <footer class="card-footer">
                        <a class="card-footer-item">
                            BUY
                        </a>
                    </footer>
                </div>
            </div>
            <div class="column is-one-quarter-desktop is-half-tablet">
                <div class="card">
                    <div class="card-image">
                        <figure class="image is-3by2">
                            <img src="https://unsplash.it/300/200/?random&pic=2" alt="">
                        </figure>
                        <div class="card-content is-overlay is-clipped">
                            <span class="tag is-info">
                                Photo Title
                            </span>
                        </div>
                    </div>
                    <footer class="card-footer">
                        <a class="card-footer-item">
                            BUY
                        </a>
                    </footer>
                </div>
            </div>
            <div class="column is-one-quarter-desktop is-half-tablet">
                <div class="card">
                    <div class="card-image">
                        <figure class="image is-3by2">
                            <img src="https://unsplash.it/300/200/?random&pic=3" alt="">
                        </figure>
                        <div class="card-content is-overlay is-clipped">
                            <span class="tag is-info">
                                Photo Title
                            </span>
                        </div>
                    </div>
                    <footer class="card-footer">
                        <a class="card-footer-item">
                            BUY
                        </a>
                    </footer>
                </div>
            </div>
            <div class="column is-one-quarter-desktop is-half-tablet">
                <div class="card">
                    <div class="card-image">
                        <figure class="image is-3by2">
                            <img src="https://unsplash.it/300/200/?random&pic=4" alt="">
                        </figure>
                        <div class="card-content is-overlay is-clipped">
                            <span class="tag is-info">
                                Photo Title
                            </span>
                        </div>
                    </div>
                    <footer class="card-footer">
                        <a class="card-footer-item">
                            BUY
                        </a>
                    </footer>
                </div>
            </div>
            <div class="column is-one-quarter-desktop is-half-tablet">
                <div class="card">
                    <div class="card-image">
                        <figure class="image is-3by2">
                            <img src="https://unsplash.it/300/200/?random&pic=5" alt="">
                        </figure>
                        <div class="card-content is-overlay is-clipped">
                            <span class="tag is-info">
                                Photo Title
                            </span>
                        </div>
                    </div>
                    <footer class="card-footer">
                        <a class="card-footer-item">
                            BUY
                        </a>
                    </footer>
                </div>
            </div>
            <div class="column is-one-quarter-desktop is-half-tablet">
                <div class="card">
                    <div class="card-image">
                        <figure class="image is-3by2">
                            <img src="https://unsplash.it/300/200/?random&pic=6" alt="">
                        </figure>
                        <div class="card-content is-overlay is-clipped">
                            <span class="tag is-info">
                                Photo Title
                            </span>
                        </div>
                    </div>
                    <footer class="card-footer">
                        <a class="card-footer-item">
                            BUY
                        </a>
                    </footer>
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
        background: linear-gradient(rgba(255, 255, 255, .6), rgba(255, 255, 255, .99)), url('../../assets/images/background-grey.png') no-repeat center center fixed;
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