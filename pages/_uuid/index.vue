<template>
    <div>
        <section class="hero is-primary is-fullheight is-background">
            <div class="hero-body">
                <div class="container">
                    <div class="party">
                        <div class="loading" v-if="loading">
                            <h1 class="title has-text-info"> Loading...</h1>
                        </div>

                        <div v-if="error" class="error">
                            <h1 class="title has-text-info"> {{ error }}</h1>
                            <h2 class="subtitle has-text-info">
                                If this doesn't work, <nuxt-link class="has-text-primary" to="/">check out the rest of our wedding site!</nuxt-link>
                            </h2>

                        </div>

                        <div v-if="party" class="content">
                            <div class="columns">
                                <div class="column is-5">
                                    <h1 class="title has-text-info">Hi, {{ partytext }}!</h1>
                                    <p class="is-size-4 has-text-info">You have been invited to our wedding, and we are
                                        very excited to celebrate with you. </p>
                                    <div>
                                        <nuxt-link :to="{name: 'uuid-guests', params: { uuid:guesturl } }">
                                            <div class="button is-primary rsvp">
                                                RSVP for your guests</div>
                                        </nuxt-link>
                                    </div>
                                </div>
                                <div class="column is-5 is-offset-2">
                                    <h1 class="title has-text-info">Wedding details</h1>
                                    <p class="is-size-4 has-text-info">Date: September 1st, 2019</p>
                                    <p class="is-size-4 has-text-info">Ceremony starts at 4:00 pm</p>
                                    </br>
                                    <h1 class="title has-text-info">Location</h1>
                                    <a href="https://wildflowers.farm/weddings">
                                        <div class="button is-info">Wildflowers Farm</div>
                                    </a>
                                    <p class="is-size-4 has-text-info">42338 Fruit Ridge Line, St Thomas, Ontario,
                                        Canada N5P 3S9
                                    </p>
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
                return session.get(partyurl, {
                        crossdomain: true
                    })
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
                            for (i = 0; i < this.guests.length; i++) {
                                if (this.guests[i].is_primarycontact === true) {
                                    this.partytext = this.guests[i].first_name;
                                } else {
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

    .hero.is-primary.is-background {
        background: linear-gradient(rgba(255, 255, 255, .6), rgba(255, 255, 255, .8)), url('https://b0rtdg.bn.files.1drv.com/y4mUKhWv84jRu2sffpC_unLOD1mj7KsVbvKBnvKcXsgvHA54Vf4f1An1wG31t6yJnqKDYP3aUclf-b4s3bbD8JpmKMVY73vGJesWbp09zpMh96z1JPEb_1nS8jpCuXWn8uIArzw3I6iTShKuhnqcx9sxmfCogjKxNQI7fmzmnzVB_fKT_3L-7wwN4IpSBsJLJPkM_OwVjGIfbJJPnz4W4ahEg?width=1500&height=2000&cropmode=none') no-repeat center center fixed;
        -webkit-background-size: cover;
        -moz-background-size: cover;
        -o-background-size: cover;
        background-size: cover;
        image-rendering: -webkit-optimize-contrast;
        // -webkit-filter: grayscale(100%);
        /* Chrome, Safari, Opera */
        // filter: grayscale(100%);
    }

    .button.rsvp {
        margin-bottom: 15%;
    }
</style>