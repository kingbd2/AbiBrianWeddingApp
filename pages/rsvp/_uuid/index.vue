<template>
    <section class="container">
        <div>
            <figure>
                <img src="https://berqdg.bn.files.1drv.com/y4ml13TGhWP7VNsb9cqUVcto_Hhmb7uVQPhLI5fIwKd1Qf2NvqOZBdu6W65bMcTil5UGo3u9gVcT2XW6FO46skmjMn1yNxcgdQ7UjlHAUvn_PxUJZqd3m-qE97IhsPyYVup3n64PmvaRCmrMCqsflCUu7Mahd4nEdiD2fPbn1U0bifT_WHc8dGPRJBzaBMVbwDrPwYjwBRduvMAgOV0sjQE-w?width=2428&height=1366&cropmode=none"
                    width="400" height="427" />
            </figure>
            <h1 class="title">
                We're getting married!
            </h1>
            <h2 class="subtitle">
                And we want to celebrate with you.
            </h2>
            <div class="party">
                <div class="loading" v-if="loading">
                    Loading...
                </div>

                <div v-if="error" class="error">
                    {{ error }}
                </div>

                <div v-if="party" class="content">
                    <h2>{{ party.name }}</h2>
                    <p>{{ party.email }}</p>
                </div>
                <div>
                    <nuxt-link to="rsvp-uuid-guests">RSVP for your guests</nuxt-link>
                    <!-- <div class="button"></div> -->
                </div>
            </div>
            <!-- <section class="hero is-primary">
        <div class="hero-body">
          <div class="container">
            <h1 class="title">
              Primary title
            </h1>
            <h2 class="subtitle">
              Primary subtitle
            </h2>
          </div>
        </div>
      </section> -->
        </div>
    </section>
</template>

<script>
    // export default {
    //   async asyncData ({ params }) {
    //     let { data } = await axios.get(`https://my-api/posts/${params.id}`)
    //     return { title: data.title }
    //   }
    // }
    import session from '../../../store/api/session';
    export default {
        components: {},
        data() {
            return {
                loading: false,
                party: null,
                error: null
            }
        },
        created() {
            // fetch the data when the view is created and the data is
            // already being observed
            this.getParty()
        },
        watch: {
            // call again the method if the route changes
            '$route': 'fetchData'
        },
        methods: {
            getParty() {
                this.error = this.party = null
                this.loading = true
                const url = this.$route.params.uuid
                console.log(url)
                return session.get(url)
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
</style>