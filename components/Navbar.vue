<template>
    <nav class="navbar is-fixed-top" role="navigation" aria-label="main navigation">
        <div class="navbar-brand">
            <nuxt-link to="/">
            <a class="navbar-item">
                <img src="../assets/images/logo.svg" width="200" height="50">
            </a>
            </nuxt-link>
            <a class="navbar-burger" @click="showNav = !showNav" :class="{ 'is-active': showNav }">
                <span aria-hidden="true"></span>
                <span aria-hidden="true"></span>
                <span aria-hidden="true"></span>
            </a>
        </div>

        <div id="navbarBasicExample" class="navbar-menu" :class="{ 'is-active': showNav }">
            <div class="navbar-start is-uppercase" style="flex-grow: 1; justify-content: center;">
                <a class="navbar-item" @click="showNav = !showNav">
                    <nuxt-link to="/">
                        Our Wedding
                    </nuxt-link>
                </a>
                <a class="navbar-item" @click="showNav = !showNav">
                    <nuxt-link to="/accomodations">
                        Guest Accomodations
                    </nuxt-link>
                </a>
                <a class="navbar-item has-text-primary" @click="showNav = !showNav">
                    <nuxt-link to="/rsvp">
                        RSVP
                    </nuxt-link>
                </a>
                <a class="navbar-item" @click="showNav = !showNav">
                    <nuxt-link to="/photos">
                        Photos
                    </nuxt-link>
                </a>
            </div>
        </div>
    </nav>
</template>

<script>
    export default {
        data() {
            return {
                showNav: false
            }
        },
    }
</script>

<style lang="scss">
    @import url('https://fonts.googleapis.com/css?family=Open+Sans:600|Source+Sans+Pro');

    .navbar-start {
        // font-family: 'Source Sans Pro', sans-serif;
        font-family: 'Open Sans', sans-serif;
    }
</style>