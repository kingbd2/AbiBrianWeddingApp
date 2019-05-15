<template>
    <nav class="navbar is-fixed-top" role="navigation" aria-label="main navigation">
        <div class="navbar-brand">
            <a class="navbar-item" href="https://bulma.io">
                <!-- <img src="https://bulma.io/images/bulma-logo.png" width="112" height="28"> -->
            </a>

            <a role="button" class="navbar-burger burger" aria-label="menu" aria-expanded="false"
                data-target="navbarBasicExample">
                <span aria-hidden="true"></span>
                <span aria-hidden="true"></span>
                <span aria-hidden="true"></span>
            </a>
        </div>

        <div id="navbarBasicExample" class="navbar-menu">
            <div class="navbar-start is-uppercase" style="flex-grow: 1; justify-content: center;">
                <a class="navbar-item">
                    <nuxt-link to="/">
                    Our Wedding
                    </nuxt-link>
                </a>
                
                    <a class="navbar-item">
                        <nuxt-link to="/accomodations">
                        Guest Accomodations
                        </nuxt-link>
                    </a>
                
                <a class="navbar-item has-text-primary">
                    RSVP
                </a>

                <div class="navbar-item has-dropdown is-hoverable">
                    <a class="navbar-link">
                        Photos
                    </a>

                    <div class="navbar-dropdown">
                        <a class="navbar-item">
                            About
                        </a>
                        <a class="navbar-item">
                            Jobs
                        </a>
                        <a class="navbar-item">
                            Contact
                        </a>
                        <hr class="navbar-divider">
                        <a class="navbar-item">
                            Report an issue
                        </a>
                    </div>
                </div>
            </div>

            <!-- <div class="navbar-end">
                <div class="navbar-item">
                    <div class="buttons">
                        <a class="button is-primary">
                            <strong>Sign up</strong>
                        </a>
                        <a class="button is-light">
                            Log in
                        </a>
                    </div>
                </div>
            </div> -->
        </div>
    </nav>
</template>

<script>
    export default {
        data() {
            return {
                url: '',
                loading: false,
                party: null,
                error: null
            }
        },
        methods: {
            getParty() {
                this.error = this.party = null
                this.loading = true
                // this.url = this.$route.params.uuid
                // const url = this.$route.params.uuid
            //     console.log(url)
            //     return session.get(url)
            //         .then((res) => {
            //             if (res.data) {
            //                 this.loading = false
            //                 this.party = res.data
            //             } else {
            //                 context.error()
            //             }
            //         })
            //         .catch(error => {
            //             console.log(error)
            //             this.loading = false
            //             this.error = "Please go to your wedding invitation email and try again."
            //         })
            },
        }

    }
</script>

<style lang="scss">
    @import url('https://fonts.googleapis.com/css?family=Open+Sans:600|Source+Sans+Pro');

    .navbar-start {
        // font-family: 'Source Sans Pro', sans-serif;
        font-family: 'Open Sans', sans-serif;
    }
</style>