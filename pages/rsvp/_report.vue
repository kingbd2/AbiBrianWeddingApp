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

                        <div v-if="guests" class="content">
                            <div class="button" @click="createReport()">Generate Report</div>
                            <div class="has-text-info">Guests attending: {{ is_attending_count }} / {{ guestcount }}
                            </div>
                            <div class="has-text-info">Number of kids: {{ kids_attending_count }} / {{ guestcount }}
                            </div>
                            <div v-for="item in party" :key="item.id">
                                <p class="has-text-info">{{ item.comments }}</p>
                            </div> 
                            <table class="table is-striped is-hoverable is-fullwidth">
                                <thead>
                                    <tr>
                                        <th>Number</th>
                                        <th>Name</th>
                                        <th>Party</th>
                                        <th>Group</th>
                                        <th>Attending?</th>
                                        <th>Dietary Restrictions?</th>
                                        <th>Kid?</th>
                                        <th>Make changes</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr v-for="item in guests" :key="item.id">
                                        <th>{{ item.id }}</th>
                                        <td>{{ item.first_name }} {{ item.last_name }}</td>
                                        <td>{{ item.party }}</td>
                                        <td><input class="input" type="text" placeholder="Group"
                                v-model="item.group"></td>
                                        <td>{{ item.is_attending }}</td>
                                        <td>{{ item.has_dietary_restrictions }} {{ item.dietary_restrictions }}</td>
                                        <td>{{ item.iskid }}</td>
                                        <td><div class="button is-primary" @click="createReport()">Submit changes</div></td>
                                    </tr>
                                </tbody>
                            </table>
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
            // Must be the password
            var pass = /extracoolarmadillo!1/g;
            return pass.test(params.report)
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

            }
        },
        created() {
            // fetch the data when the view is created and the data is
            // already being observed
            this.getGuests()
            this.getParties()
        },
        watch: {
            // call again the method if the route changes
            '$route': 'fetchData'
        },
        methods: {
            getGuests() {
                this.error = this.guests = null
                this.loading = true
                this.guestlisturl = 'guests/'
                const guestlisturl = 'guests/'
                return session.get(guestlisturl, {
                        crossdomain: true
                    })
                    .then((res) => {
                        if (res.data) {
                            this.loading = false
                            this.guests = res.data
                            this.guestcount = res.data.length
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
            createReport() {
                var i;
                var count = 0;
                var count_kid = 0;
                for (i = 0; i < this.guests.length; i++) {
                    if (this.guests[i].is_attending === true) {
                        count++;
                    }
                    if (this.guests[i].iskid === true) {
                        count_kid++;
                    }
                }
                this.is_attending_count = count;
                this.kids_attending_count = count_kid;
            }
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