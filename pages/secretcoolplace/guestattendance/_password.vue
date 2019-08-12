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
                            <div class="button is-info is-large" @click="createReport()">Generate Report of Attendance:
                            </div>
                            <div class="box">
                                <div class="columns">
                                    <div class="column">
                                        <div class="has-text-info has-text-weight-bold">Guests attending:
                                        </div>
                                        <div class="has-text-info">{{ is_attending_count }} /
                                            {{ guestcount }}
                                        </div>
                                    </div>
                                    <div class="column">
                                        <div class="has-text-info has-text-weight-bold">Attending Shabbat:
                                        </div>
                                        <div class="has-text-info">{{ attending_shabbat_count }} /
                                            {{ guestcount }}</div>
                                    </div>
                                    <div class="column">
                                        <div class="has-text-info has-text-weight-bold">Attending brunch:
                                        </div>
                                        <div class="has-text-info">{{ attending_brunch_count }} / {{ guestcount }}</div>

                                    </div>
                                    <div class="column">
                                        <div class="has-text-info has-text-weight-bold">Attending wedding rehearsal:
                                        </div>
                                        <div class="has-text-info">{{ attending_wedding_rehearsal_count }} /
                                            {{ guestcount }}</div>
                                    </div>
                                    <div class="column">
                                        <div class="has-text-info has-text-weight-bold">Attending rehearsal dinner:
                                        </div>
                                        <div class="has-text-info">{{ attending_rehearsal_dinner_count }}
                                            / {{ guestcount }}</div>
                                    </div>
                                </div>
                            </div>
                            <div class="card large sticky">
                                <div class="card-content">
                                    <div class="media">
                                        <div class="media-content">
                                            <div class="columns has-text-primary">
                                                <div class="column">
                                                    <div>Number</div>
                                                </div>
                                                <div class="column">
                                                    <div>Name</div>
                                                </div>
                                                <div class="column">
                                                    <div>Attending Wedding?</div>
                                                </div>
                                                <div class="column">
                                                    <div>Attending Shabbat?</div>
                                                </div>
                                                <div class="column">
                                                    <div>Attending Wedding Rehearsal?</div>
                                                </div>
                                                <div class="column">
                                                    <div>Attending Rehearsal Dinner?</div>
                                                </div>
                                                <div class="column">
                                                    <div>Attending Brunch?</div>
                                                </div>
                                                <div class="column">
                                                    <div>Dietary Restrictions?</div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div v-for="item in guest_list" :key="item.id">
                                <guest-attendance-card :guest="item"></guest-attendance-card>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </div>

</template>

<script>
    import _ from 'lodash';
    import GuestChangeCard from '../../../components/GuestChangeCard';
    import GuestAttendanceCard from '../../../components/GuestAttendanceCard';
    import session from '../../../store/api/session';
    export default {
        components: {
            GuestChangeCard,
            GuestAttendanceCard,
        },
        validate({
            params
        }) {
            // Must be the password
            var pass = /EjCPkUFKe0ZLhr8GR2wMhNGoO3rIANpD3uqmyykWd9aBRvnwmGD456anu8yq/g;
            return pass.test(params.password)
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
                attending_shabbat_count: 0,
                attending_wedding_rehearsal_count: 0,
                attending_rehearsal_dinner_count: 0,
                attending_brunch_count: 0,

            }
        },
        created() {
            // fetch the data when the view is created and the data is
            // already being observed
            this.getGuests()
            // this.getParties()
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
            // getParties() {
            //     this.error = this.party = null
            //     this.loading = true
            //     this.partylisturl = 'parties/'
            //     const partylisturl = 'parties/'
            //     return session.get(partylisturl, {
            //             crossdomain: true
            //         })
            //         .then((res) => {
            //             if (res.data) {
            //                 this.loading = false
            //                 this.party = res.data
            //             } else {
            //                 context.error()
            //             }
            //         })
            //         .catch(error => {
            //             console.log(error)
            //             this.loading = false
            //             this.error = "Please go to your wedding invitation email and try again."
            //         })
            // },
            createReport() {
                var i;
                var count = 0;
                // var count_kid = 0;
                var count_shabbat = 0;
                var count_wedding_rehearsal = 0;
                var count_rehearsal_dinner = 0;
                var count_brunch = 0;

                for (i = 0; i < this.guests.length; i++) {
                    if (this.guests[i].is_attending === true) {
                        count++;
                    }
                    // if (this.guests[i].iskid === true) {
                    //     count_kid++;
                    // }
                    if (this.guests[i].is_attending_shabbat === true) {
                        count_shabbat++;
                    }
                    if (this.guests[i].is_attending_wedding_rehearsal === true) {
                        count_wedding_rehearsal++;
                    }
                    if (this.guests[i].is_attending_rehearsal_dinner === true) {
                        count_rehearsal_dinner++;
                    }
                    if (this.guests[i].is_attending_brunch === true) {
                        count_brunch++;
                    }
                }
                this.is_attending_count = count;
                // this.kids_attending_count = count_kid;
                this.attending_shabbat_count = count_shabbat;
                this.attending_rehearsal_dinner_count = count_rehearsal_dinner;
                this.attending_wedding_rehearsal_count = count_wedding_rehearsal;
                this.attending_brunch_count = count_brunch;
            }
        },
        computed: {
            guest_list: function () {
                return _.orderBy(this.guests, 'id')
            }
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

    .sticky {
        position: sticky;
        z-index:999;
        top: 0;
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