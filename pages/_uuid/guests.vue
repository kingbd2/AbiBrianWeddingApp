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

                                    <div v-if="guests" class="content">
                                        <p class="is-size-3 has-text-success has-text-left has-text-weight-bold">Please
                                            RSVP for your guests below, and
                                            don't forget to leave a comment below!</p>
                                        <div class="container" v-for="guest in guests" :key="guest.id">
                                            <guestrsvp v-bind:guest="guest" v-on:childToParent="onChildClick">
                                            </guestrsvp>
                                        </div>


                                        <div class="container" v-if="commentSubmitted === false">
                                            <div class="card large has-background-link">
                                                <div class="card-content">
                                                    <div class="media">
                                                        <div class="media-content">
                                                            <p class="is-size-4 has-text-info">We would love to hear
                                                                from you.
                                                            </p>
                                                            <div class="columns">
                                                                <div class="column">
                                                                    <textarea class="textarea"
                                                                        placeholder="Please leave a message for the bride and groom!"
                                                                        v-model="party_comment"></textarea>
                                                                    <div class="column">
                                                                        <div class="button is-primary"
                                                                            @click='SubmitComment()'>
                                                                            Submit Comment</div>
                                                                    </div>
                                                                </div>

                                                            </div>
                                                        </div>

                                                    </div>
                                                </div>
                                            </div>
                                        </div>

                                        <div class="container" v-else>
                                            <div class="card large has-background-primary">
                                                <div class="card-content">
                                                    <div class="media">
                                                        <div class="media-content">
                                                            <div class="columns">
                                                                <div class="column">
                                                                    <p class="title is-size-4 has-text-white">Thanks, we
                                                                        will see you soon!
                                                                    </p>

                                                                    <p class="is-size-4 has-text-white">Love, Abiella
                                                                        and Brian :)</p>
                                                                </div>
                                                                <div class="column is-8">
                                                                    <div class="box has-background-light">
                                                                        <p class="is-size-5 has-text-danger">If you need
                                                                            to change your responses, please go back to
                                                                            your emailed invitation and click on the
                                                                            link provided. Please RSVP by July 15th, 2019. 
                                                                        </p>
                                                                        <p class="is-size-5">Check out other parts of
                                                                            our site!</p>
                                                                        <ul>
                                                                            <nuxt-link to="/">
                                                                                <a class="button navbar-item has-text-primary"
                                                                                    @click="showNav = !showNav">

                                                                                    Our Wedding

                                                                                </a>
                                                                            </nuxt-link>
                                                                            <nuxt-link to="/accomodations">
                                                                                <a class="button navbar-item"
                                                                                    @click="showNav = !showNav">

                                                                                    Guest Accomodations

                                                                                </a>
                                                                            </nuxt-link>

                                                                            <nuxt-link to="/registry">
                                                                                <a class="button navbar-item has-text-info"
                                                                                    @click="showNav = !showNav">

                                                                                    Registry

                                                                                </a>
                                                                            </nuxt-link>
                                                                            <nuxt-link to="/photos">
                                                                                <a class="button navbar-item has-text-info"
                                                                                    @click="showNav = !showNav">

                                                                                    Photos

                                                                                </a>
                                                                            </nuxt-link>
                                                                        </ul>

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
                commentSubmitted: false,
                loading: false,
                guests: null,
                error: null,
                party_id: this.$route.params.uuid,
                party_comment: '',
                IDfromChild: '',
                party: null,
            }
        },
        created() {
            // fetch the data when the view is created and the data is
            // already being observed
            this.getGuests()
            this.getParty()
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
            onChildClick(value) {
                this.fromChild = value
            },
            SubmitComment() {
                this.loading = true
                const COMMENT_URL = this.$route.params.uuid + '/'
                return session.put(COMMENT_URL, {
                        comments: this.party_comment,
                        email: this.party.email,
                        name: this.party.name      

                    })
                    .then((res) => {
                        if (res.data) {
                            this.commentSubmitted = true
                            this.loading = false
                        } else {
                            context.error()
                        }
                    })
                    .catch(error => {
                        console.log(error)
                        this.loading = false
                        this.error = "Please go to your wedding invitation email and try again."
                    })
            }
        },
        computed: {
            yes_no_is_attending: function () {
                if (this.is_attending === true) {
                    return "Yes"
                } else {
                    return "No"
                }
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