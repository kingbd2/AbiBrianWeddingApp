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
                                If this doesn't work, <nuxt-link class="has-text-primary" to="/">check out the rest of
                                    our wedding site!</nuxt-link>
                            </h2>
                        </div>

                        <h1 class="title has-text-primary">Edit events</h1>
                        <div v-if="events" class="content">
                            <div class="card large">
                                <div class="card-content">
                                    <div class="media">
                                        <div class="media-content">
                                            <div class="columns has-text-primary">
                                                <div class="column is-1">
                                                    <div>ID</div>
                                                </div>
                                                <div class="column">
                                                    <div>Date</div>
                                                </div>
                                                <div class="column">
                                                    <div>Fancy Date</div>
                                                </div>
                                                <div class="column">
                                                    <div>Title</div>
                                                </div>
                                                <div class="column is-2">
                                                    <div>Details
                                                    </div>
                                                </div>
                                                <div class="column">
                                                    <div>Location ID</div>
                                                </div>
                                                <div class="column">
                                                    <div>Submit</div>
                                                </div>
                                                
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                    <div v-for="item in events" :key="item.id">
                                        <event-change-card :event="item"></event-change-card>
                                    </div>
                                
                            
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </div>

</template>

<script>
    import session from '../../../store/api/session';
    import EventChangeCard from '../../../components/EventChangeCard';
    export default {
        components: {
            EventChangeCard
        },
        validate({
            params
        }) {
            // Must be the password
            var pass = /2h0zPbD7PWNuQ0NTooi23CKkv5pG19tncVJLkcsld5DhstCer2P8rKqYbC3M/g;
            return pass.test(params.password)
        },
        data() {
            return {
                events: null,
                eventsurl: null,
                loading: false,
                error: null,

            }
        },
        created() {
            // fetch the data when the view is created and the data is
            // already being observed
            this.getEvents()
        },
        watch: {
            // call again the method if the route changes
            '$route': 'fetchData'
        },
        methods: {
            getEvents() {
                this.error = this.events = null
                this.loading = true
                this.eventsurl = 'events/'
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
            Submit(id) {
                this.error = this.response = null
                this.loading = true
                const events_url = '/events/' + id + '/'
                return session.put(events_url, {
                        event_name: this.events[id].event_name, // THIS IS THE WRONG ID
                        details: this.events[id].details, // THIS IS THE WRONG ID
                        end_time: this.events[id].end_time, // THIS IS THE WRONG ID
                        start_time: this.events[id].start_time, // THIS IS THE WRONG ID
                        date: this.events[id].date, // THIS IS THE WRONG ID

                    })
                    .then((res) => {
                        if (res.data) {
                            this.has_submitted = true
                            this.has_changed = false
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
        },
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

    $gl-ms : "screen and (max-width: 23.5em)"; // up to 360px
    $gl-xs : "screen and (max-width: 35.5em)"; // up to 568px
    $gl-sm : "screen and (max-width: 48em)"; // max 768px
    $gl-md : "screen and (max-width: 64em)"; // max 1024px
    $gl-lg : "screen and (max-width: 80em)"; // max 1280px

    table {
        border-spacing: 1;
        border-collapse: collapse;
        background: white;
        border-radius: 6px;
        overflow: hidden;
        max-width: 800px;
        width: 100%;
        margin: 0 auto;
        position: relative;

        * {
            position: relative
        }

        td,
        th {
            padding-left: 8px
        }

        thead tr {
            height: 60px;
            // background: #FFED86;
            font-size: 16px;
        }

        tbody tr {
            height: 48px;
            border-bottom: 1px solid #E3F1D5;

            &:last-child {
                border: 0;
            }
        }

        td,
        th {
            text-align: left;

            &.l {
                text-align: right
            }

            &.c {
                text-align: center
            }

            &.r {
                text-align: center
            }
        }
    }

    @media #{$gl-xs} {

        table {
            display: block;

            >*,
            tr,
            td,
            th {
                display: block
            }

            thead {
                display: none
            }

            tbody tr {
                height: auto;
                padding: 8px 0;

                td {
                    padding-left: 45%;
                    margin-bottom: 12px;

                    &:last-child {
                        margin-bottom: 0
                    }

                    &:before {
                        position: absolute;
                        font-weight: 700;
                        width: 40%;
                        left: 10px;
                        top: 0
                    }

                    &:nth-child(2):before {
                        content: "Name";
                    }

                    &:nth-child(3):before {
                        content: "Party";
                    }


                    &:nth-child(4):before {
                        content: "Attending?";
                    }

                    &:nth-child(5):before {
                        content: "Dietary";
                    }

                    &:nth-child(6):before {
                        content: "Kid?";
                    }
                }
            }
        }
    }
</style>