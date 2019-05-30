<template>
    <div>
        <section class="hero is-white is-fullheight">
            <div class="hero-body">
                <div class="container">
                    <div>
                        <h1 class="title">
                                    Please RSVP for your guests.
                                </h1>
                        <div class="tile is-ancestor">
                            <div class="tile is-vertical is-8">
                                <!-- <figure>
                <img src="https://berqdg.bn.files.1drv.com/y4ml13TGhWP7VNsb9cqUVcto_Hhmb7uVQPhLI5fIwKd1Qf2NvqOZBdu6W65bMcTil5UGo3u9gVcT2XW6FO46skmjMn1yNxcgdQ7UjlHAUvn_PxUJZqd3m-qE97IhsPyYVup3n64PmvaRCmrMCqsflCUu7Mahd4nEdiD2fPbn1U0bifT_WHc8dGPRJBzaBMVbwDrPwYjwBRduvMAgOV0sjQE-w?width=2428&height=1366&cropmode=none"
                    width="400" height="427" />
            </figure> -->
                                
                                <div class="party">
                                    <div class="loading" v-if="loading">
                                        Loading...
                                    </div>

                                    <div v-if="error" class="error">
                                        {{ error }}
                                    </div>

                                    <div v-if="guests" class="content">
                                        <div class="container" v-for="guest in guests" :key="guest.id">
                                            <guestrsvp v-bind:guest="guest"></guestrsvp>
                                            <!-- <div class="button is-primary" @click='Rsvp(guest.id)'>Submit</div> -->
                                        </div>
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
    import session from '../../store/api/session';
    import Guestrsvp from '~/components/Guestrsvp';
    export default {
        components: {
            Guestrsvp
        },
        data() {
            return {
                loading: false,
                guests: null,
                error: null
            }
        },
        created() {
            // fetch the data when the view is created and the data is
            // already being observed
            this.getGuests()
        },
        watch: {
            // call again the method if the route changes
            '$route': 'fetchData'
        },
        methods: {
            getGuests() {
                this.error = this.party = null
                this.loading = true
                const url = this.$route.params.uuid + '/guests/'
                console.log(url)
                return session.get(url)
                    .then((res) => {
                        if (res.data) {
                            this.loading = false
                            this.guests = res.data
                        } else {
                            context.error()
                        }
                    })
                    .catch(error => {
                        console.log(error)
                        this.loading = false
                        this.error = "Please go to your wedding invitation email and try again."
                    })
            },
        }
        // 

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

    .hero.is-white {
        background: linear-gradient(rgba(255, 255, 255, .8), rgba(255, 255, 255, .6)), url('https://ap2dba.bl.files.1drv.com/y4mCaD1MuSDy_QEpztDrD1OV-Ix3DJj-iENy6Nbufw5pzmC2jN28YSBwP7e6PXA-QJFIyuarcsMlySB4hka2Eldob4nFQ9BA0FAWONr9cG6IxQ9VCj8B79Q1xhWV0e81c6-2GWX878J6NZ4wOVQCPilMy8kDe6Ui97mzvfJY1DqBZWiRY5bS1I5icJ-6Xbi3L3r0A0gjEUFfuNQ8SqX5PhR6w?width=5184&height=3456&cropmode=none') no-repeat center center fixed;
        -webkit-background-size: cover;
        -moz-background-size: cover;
        -o-background-size: cover;
        background-size: cover;
    }
</style>