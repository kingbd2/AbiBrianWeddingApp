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

                        <div v-if="party" class="content">
                            <!-- <div class="button" @click="createReport()">Generate Report</div>
                            <div class="has-text-info">Guests attending: {{ is_attending_count }} / {{ guestcount }}
                            </div>
                            <div class="has-text-info">Number of kids: {{ kids_attending_count }} / {{ guestcount }}
                            </div> -->
                            <h1 class="title has-text-primary">Here are all the comments!</h1>
                            <div v-for="item in party" :key="item.id">
                                <div v-if="item.comments">
                                    <p class="has-text-info">{{ item.name }}: "{{ item.comments }}"</p>
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
    import session from '../../../store/api/session';
    export default {
        components: {},
        // validate({
        //     params
        // }) {
        //     // Must be the password
        //     var pass = /EjCPkUFKe0ZLhr8GR2wMhNGoO3rIANpD3uqmyykWd9aBRvnwmGD456anu8yq/g;
        //     return pass.test(params.password)
        // },
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

            }
        },
        created() {
            // fetch the data when the view is created and the data is
            // already being observed
            // this.getGuests()
            this.getParties()
        },
        watch: {
            // call again the method if the route changes
            '$route': 'fetchData'
        },
        methods: {

            getParties() {
                this.error = this.party = null
                this.loading = true
                this.partylisturl = 'parties/'
                const partylisturl = 'parties/'
                return session.get(partylisturl, {
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