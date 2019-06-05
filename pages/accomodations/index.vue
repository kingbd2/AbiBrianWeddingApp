<template>
    <div>
        <section class="hero is-primary is-background">
            <div class="hero-body">
                <div class="container">
                    <!-- Cards -->
                    <div class="row columns">
                        <div class="column is-one-third" v-for="item in this.contents" :key="item.id">
                       
                            <accomodation-card :place="item"></accomodation-card>
                        </div>
                    </div>
                    <!-- End Developers -->
                </div>
            </div>
        </section>
    </div>
</template>

<script>
    import AccomodationCard from '~/components/AccomodationCard';
    export default {
        components: {
            AccomodationCard
        },
        data() {
            return {
                contents: [{
                        title: 'Room Block at The Delta Armouries',
                        dates: 'Friday August 30 - Monday September 2, 2019',
                        price: '$160-$180/ night',
                        bookby: 'Friday July 19, 2019',
                        location: '325 Dundas St, London, ON N6B 1T9 (40 minute drive to Wedding Venue, 15 minute drive to Schneider-Friedma house)',
                        transportation: 'Transportation will be provided from the hotel to and from the wedding by bus.',
                        website: '',
                        bookhere: 'https://www.marriott.com/event-reservations/reservation-link.mi?id=1550782452374&key=GRP&app=resvlink',
                        info: ''
                    },
                    {
                        title: 'Room Block at The Windermere Manor',
                        dates: 'Friday August 30 - Monday September 2, 2019',
                        price: '$140-$160/ night; includes free parking and breakfast each morning',
                        bookby: 'Friday July 30, 2019',
                        location: '200 Collip Cir, London, ON N6G 4X8 (45 minute drive to Wedding Venue, 5 minute drive to Schneider-Friedman house)',
                        transportation: 'Transportation will be provided from Windermere Manor to and from the wedding by bus.',
                        website: 'https://www.windermeremanor.com/',
                        bookhere: 'Call (519) 858-1391 and reference the “Schneider-Friedman/ King Offsite Wedding”',
                        info: ''
                    },
                    {
                        title: 'Port Stanley Accommodations',
                        dates: '',
                        price: '',
                        bookby: '',
                        location: '',
                        transportation: '',
                        website: '',
                        bookhere: '',
                        info: '*These vary in prices and we will not be providing transportation to the venue. Uber and taxis available /nKettle Creek Inn: http://www.kettlecreekinn.com/ /nInn on the harbour: http://innontheharbour.net/ /nThe windjammer Inn: https://www.thewindjammerinn.com/ /nThe telegraph house: http://www.telegraphhouse.com/index.php/Dining/Index'
                    },
                ],
                loading: false,
                guests: null,
                error: null
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
        background: linear-gradient(rgba(255, 255, 255, .6), rgba(255, 255, 255, .99)), url('../../assets/images/background-grey.png') no-repeat center center fixed;
        -webkit-background-size: cover;
        -moz-background-size: cover;
        -o-background-size: cover;
        background-size: cover;
        image-rendering: -webkit-optimize-contrast;
        // -webkit-filter: grayscale(100%);
        /* Chrome, Safari, Opera */
        // filter: grayscale(100%);
    }
</style>