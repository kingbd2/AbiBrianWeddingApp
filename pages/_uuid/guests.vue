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
                                        <div class="container" v-for="guest in guests" :key="guest.id">
                                            <guestrsvp v-bind:guest="guest"></guestrsvp>
                                            <!-- <div class="button is-primary" @click='Rsvp(guest.id)'>Submit</div> -->
                                        </div>
                                        <input class="input" type="text"
                                            placeholder="Please leave a message for the bride and groom!"
                                            v-model="party_comment">
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
                error: null,
                party_id: this.$route.params.uuid,
                party_comment: '',
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
        background: linear-gradient(rgba(255, 255, 255, .8), rgba(255, 255, 255, .6)), url('https://b0rtdg.bn.files.1drv.com/y4mUKhWv84jRu2sffpC_unLOD1mj7KsVbvKBnvKcXsgvHA54Vf4f1An1wG31t6yJnqKDYP3aUclf-b4s3bbD8JpmKMVY73vGJesWbp09zpMh96z1JPEb_1nS8jpCuXWn8uIArzw3I6iTShKuhnqcx9sxmfCogjKxNQI7fmzmnzVB_fKT_3L-7wwN4IpSBsJLJPkM_OwVjGIfbJJPnz4W4ahEg?width=1500&height=2000&cropmode=none') no-repeat center center fixed;
        -webkit-background-size: cover;
        -moz-background-size: cover;
        -o-background-size: cover;
        background-size: cover;
    }
</style>