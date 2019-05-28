<template>
    <section class="container">
        <div>
            <!-- <figure>
                <img src="https://berqdg.bn.files.1drv.com/y4ml13TGhWP7VNsb9cqUVcto_Hhmb7uVQPhLI5fIwKd1Qf2NvqOZBdu6W65bMcTil5UGo3u9gVcT2XW6FO46skmjMn1yNxcgdQ7UjlHAUvn_PxUJZqd3m-qE97IhsPyYVup3n64PmvaRCmrMCqsflCUu7Mahd4nEdiD2fPbn1U0bifT_WHc8dGPRJBzaBMVbwDrPwYjwBRduvMAgOV0sjQE-w?width=2428&height=1366&cropmode=none"
                    width="400" height="427" />
            </figure>
            <h1 class="title">
                We're getting married!
            </h1>
            <h2 class="subtitle">
                And we want to celebrate with you.
            </h2> -->
            <div class="party">
                <div class="loading" v-if="loading">
                    Loading...
                </div>

                <div v-if="error" class="error">
                    {{ error }}
                </div>

                <div v-if="party" class="content">
                    <h2>Thanks for dropping by, {{ partytext }}! </h2>
                    <p>{{ party.email }}</p>
                    <p>{{ partytext }}</p>
                </div>
                <div>
                    <nuxt-link :to="{name: 'uuid-guests', params: { uuid:guesturl } }">
                    <div class="button is-primary">
                    RSVP for your guests</div></nuxt-link>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
    import session from '../../store/api/session';
    export default {
        components: {},
        validate({
            params
        }) {
            // Must be a uuid
            return /^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/i.test(params.uuid)
        },
        data() {
            return {
                guesturl: '',
                partyurl: '',
                loading: false,
                party: null,
                guests: [],
                error: null,
                partytext: ''
            }
        },
        created() {
            // fetch the data when the view is created and the data is
            // already being observed
            this.getParty()
            this.getGuests()
        },
        watch: {
            // call again the method if the route changes
            '$route': 'fetchData'
        },
        methods: {
            getParty() {
                this.error = this.party = null
                this.loading = true
                this.partyurl = this.$route.params.uuid + '/'
                const partyurl = this.$route.params.uuid + '/'
                return session.get(partyurl)
                    .then((res) => {
                        if (res.data) {
                            this.loading = false
                            this.party = res.data
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
            getGuests() {
                this.error = this.party = null
                this.loading = true
                this.guesturl = this.$route.params.uuid
                const guesturl = this.$route.params.uuid + '/guests/'
                return session.get(guesturl)
                    .then((res) => {
                        if (res.data) {
                            var i;
                            this.loading = false
                            this.guests = res.data
                            for (i = 0; i <this.guests.length; i++) {
                                if (this.guests[i].is_primarycontact === true) {
                                    this.partytext = this.guests[i].first_name;
                                }
                                else {
                                    continue
                                }
                            }
                        
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