<template>
    <div>
        <section class="hero is-white is-fullheight">
            <div class="hero-body">
                <div class="container">
                    <div>
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

                                    <div class="loading" v-if="guests">
                                        <div class="box has-background-light">
                                            <p class="is-size-4">To RSVP to the wedding, go here: <nuxt-link :to="{name: 'uuid-guests', params: { uuid:guesturl } }">
                                                    <div class="button is-primary rsvp">
                                                        RSVP for the wedding</div>
                                                </nuxt-link></p>
                                        </div>

                                        <div class="content">
                                            <div class="card large">
                                                <div class="card-content">

                                                    <p
                                                        class="is-size-3 has-text-success has-text-left has-text-weight-bold">
                                                        We
                                                        hope
                                                        to see you at the following wedding weekend events:</p>
                                                    <div v-if="guests[0].shabbat === true">
                                                        <div class="box has-background-light">
                                                            <h2 class="has-text-primary">
                                                                {{ events[0].event_name }}</h2>
                                                            <p class="has-text-info has-text-weight-bold">
                                                                {{ events[0].fancy_date }}
                                                            </p>
                                                            <p>{{ events[0].details }}</p>
                                                            <div class="columns">
                                                                <div class="column">
                                                                    <div class="box">

                                                                        <div v-for="location in locations"
                                                                            :key="location.id">
                                                                            <div
                                                                                v-if="events[0].location_id===location.id">
                                                                                <p class="has-text-primary">
                                                                                    {{ location.location_name }}
                                                                                </p>
                                                                                <p class="has-text-info">
                                                                                    {{ location.street_num }}
                                                                                    {{ location.street_name}}
                                                                                </p>
                                                                                <p class="has-text-info">
                                                                                    {{ location.city }},
                                                                                    {{ location.province }}
                                                                                </p>
                                                                                <p class="has-text-info">
                                                                                    {{ location.postal_code }}
                                                                                </p>

                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                                <div class="column">
                                                                    <eventrsvp :guest="guests" :eventType="shabbat">
                                                                    </eventrsvp>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>

                                                    <div v-if="guests[0].wedding_rehearsal === true">
                                                        <div class="box has-background-light">
                                                            <h2 class="has-text-primary">
                                                                {{ events[1].event_name }}</h2>
                                                            <p class="has-text-info has-text-weight-bold">
                                                                {{ events[1].fancy_date }}
                                                            </p>
                                                            <p>{{ events[1].details }}</p>
                                                            <div class="columns">
                                                                <div class="column">
                                                                    <div class="box">

                                                                        <div v-for="location in locations"
                                                                            :key="location.id">
                                                                            <div
                                                                                v-if="events[1].location_id===location.id">
                                                                                <p class="has-text-primary">
                                                                                    {{ location.location_name }}
                                                                                </p>
                                                                                <p class="has-text-info">
                                                                                    {{ location.street_num }}
                                                                                    {{ location.street_name}}
                                                                                </p>
                                                                                <p class="has-text-info">
                                                                                    {{ location.city }},
                                                                                    {{ location.province }}
                                                                                </p>
                                                                                <p class="has-text-info">
                                                                                    {{ location.postal_code }}
                                                                                </p>

                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                                <div class="column">
                                                                    <eventrsvp :guest="guests"
                                                                        :eventType="wedding_rehearsal">
                                                                    </eventrsvp>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>

                                                    <div v-if="guests[0].rehearsal_dinner === true">
                                                        <div class="box has-background-light">
                                                            <h2 class="has-text-primary">
                                                                {{ events[2].event_name }}</h2>
                                                            <p class="has-text-info has-text-weight-bold">
                                                                {{ events[2].fancy_date }}
                                                            </p>
                                                            <p>{{ events[2].details }}</p>
                                                            <div class="columns">
                                                                <div class="column">
                                                                    <div class="box">
                                                                        <div v-for="location in locations"
                                                                            :key="location.id">
                                                                            <div
                                                                                v-if="events[2].location_id===location.id">
                                                                                <p class="has-text-primary">
                                                                                    {{ location.location_name }}
                                                                                </p>
                                                                                <p class="has-text-info">
                                                                                    {{ location.street_num }}
                                                                                    {{ location.street_name}}
                                                                                </p>
                                                                                <p class="has-text-info">
                                                                                    {{ location.city }},
                                                                                    {{ location.province }}
                                                                                </p>
                                                                                <p class="has-text-info">
                                                                                    {{ location.postal_code }}
                                                                                </p>

                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                                <div class="column">
                                                                    <eventrsvp :guest="guests"
                                                                        :eventType="rehearsal_dinner">
                                                                    </eventrsvp>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>

                                                    <div v-if="guests[0].brunch === true">
                                                        <div class="box has-background-light">
                                                            <h2 class="has-text-primary">
                                                                {{ events[4].event_name }}</h2>
                                                            <p class="has-text-info has-text-weight-bold">
                                                                {{ events[4].fancy_date }}
                                                            </p>
                                                            <p>{{ events[4].details }}</p>
                                                            <div class="columns">
                                                                <div class="column">
                                                                    <div class="box">
                                                                        <div v-for="location in locations"
                                                                            :key="location.id">
                                                                            <div
                                                                                v-if="events[4].location_id===location.id">
                                                                                <p class="has-text-primary">
                                                                                    {{ location.location_name }}
                                                                                </p>
                                                                                <p class="has-text-info">
                                                                                    {{ location.street_num }}
                                                                                    {{ location.street_name}}
                                                                                </p>
                                                                                <p class="has-text-info">
                                                                                    {{ location.city }},
                                                                                    {{ location.province }}
                                                                                </p>
                                                                                <p class="has-text-info">
                                                                                    {{ location.postal_code }}
                                                                                </p>

                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                                <div class="column">
                                                                    <eventrsvp :guest="guests" :eventType="brunch">
                                                                    </eventrsvp>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
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
    import Eventrsvp from '../../components/Eventrsvp'
    // import LocationMap from '../../components/LocationMap'
    export default {
        components: {
            Eventrsvp
            // LocationMap
        },
        data() {
            return {
                guesturl: '',
                partyurl: '',
                loading: false,
                party: null,
                guestcount: 0,
                guests: null,
                error: null,
                partytext: '',
                is_attending_count: 0,
                kids_attending_count: 0,
                events: null,
                locations: null,
                showMap: 'false',
                shabbat: 'shabbat',
                wedding_rehearsal: 'wedding_rehearsal',
                rehearsal_dinner: 'rehearsal_dinner',
                brunch: 'brunch',
            }
        },
        created() {
            // fetch the data when the view is created and the data is
            // already being observed
            this.getGuests()
            this.getEvents()
            this.getLocations()
        },
        // mounted: function () {
        //     if (!mapboxgl.supported()) {
        //         this.showMap = false;
        //     } else {
        //         this.showMap = true;
        //     }
        // },
        methods: {
            getGuests() {
                this.error = this.party = null
                this.loading = true
                this.guesturl = this.$route.params.uuid
                const url = this.$route.params.uuid + '/guests/'
                console.log(url)
                return session.get(url, {
                        crossdomain: true
                    })
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
            getEvents() {
                this.error = this.events = null
                this.loading = true
                this.events = 'events/'
                const eventsurl = 'events/'
                return session.get(eventsurl, {
                        crossdomain: true
                    })
                    .then((res) => {
                        if (res.data) {
                            this.loading = false
                            this.events = res.data
                            // this.guestcount = res.data.length
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
            getLocations() {
                this.error = this.locations = null
                this.loading = true
                this.locationurl = 'locations/'
                const locationurl = 'locations/'
                return session.get(locationurl, {
                        crossdomain: true
                    })
                    .then((res) => {
                        if (res.data) {
                            this.loading = false
                            this.locations = res.data
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
        },

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

    .box {
        margin-top: 5%;
    }
</style>