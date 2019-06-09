<template>
    <div>
        <section class="hero is-primary is-background">
            <div class="hero-body">
                <div class="container">
                    <div class="row columns">
                        <div class="column is-one-third" v-for="item in this.contents" :key="item.id">
                            <accomodation-card :place="item"></accomodation-card>
                        </div>
                    </div>
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
                        image: 'https://b0rpdg.bn.files.1drv.com/y4mfQabRRxvKhQvPdd-JModeroBznhEtku1ZkgeCkC439Opose7EFtABV1CNCiHYiWVYJKC0b891d--sje8-UMrcN-tpehltcjc5oS7h4hRvdN4hUABf6SPnVdoRRUvzNqhYteYAfW_GBnOr4x3qz6S55Zn6wEXO4P6DGTmP86n56FaNb36GZDjkQDjPlU9RTb9aeimuld18kMK_Wu15xpJdA?width=660&height=463&cropmode=none',
                        dates: 'Dates: Friday August 30 - Monday September 2, 2019',
                        price: '$160-$180/ night',
                        bookby: 'Book by: Friday July 19, 2019',
                        location: '325 Dundas St, London, ON N6B 1T9 (40 minute drive to Wedding Venue, 15 minute drive to Schneider-Friedma house)',
                        transportation: 'Transportation will be provided from the hotel to and from the wedding by bus.',
                        website: '',
                        bookhere: '',
                        info: [{ 
                            name: 'Book here.',
                            url: 'https://www.marriott.com/event-reservations/reservation-link.mi?id=1550782452374&key=GRP&app=resvlink',
                            isLink: true,
                        },]
                    },
                    {
                        title: 'Room Block at The Windermere Manor',
                        image: 'https://b0rqdg.bn.files.1drv.com/y4mOlIzW4Ely2iFLUi2tNQNyLNDs2yq7B3qpbh7N-vyVuI2n_YtbcN_ZDGg9PkoeGN1MQqO7Yuc3t1KvxMX8Cua_-IGMjX037ZWNbZpN16gQ0qBRU9OgruUWghe1xqDVWlMoanDhdPc9ey78MPjvsKZn4PY-fv2uogOUrC0sOPsZK_JoAZuekvBa6yHwTy64EXwo26OPyDg7mB6J8f-iW81Sw?width=550&height=279&cropmode=none',
                        dates: 'Dates: Friday August 30 - Monday September 2, 2019',
                        price: '$140-$160/ night; includes free parking and breakfast each morning',
                        bookby: 'Book by: Friday July 30, 2019',
                        location: '200 Collip Cir, London, ON N6G 4X8 (45 minute drive to Wedding Venue, 5 minute drive to Schneider-Friedman house)',
                        transportation: 'Transportation will be provided from Windermere Manor to and from the wedding by bus.',
                        website: 'https://www.windermeremanor.com/',
                        bookhere: 'Call (519) 858-1391 and reference the “Schneider-Friedman/ King Offsite Wedding”',
                        info: ''
                    },
                    {
                        title: 'Port Stanley Accommodations',
                        image: 'https://b0rrdg.bn.files.1drv.com/y4mcDl7S2E1jlQEh5DWGzfKXeaWEsFuXst71aJAvpO0NRzz2pBMkLpY16AwktfyU8y6pBs9sK9rCjPcW-WxxP472Uq6WuzDZgFNmz_Zx5UdaGgOnBZ_vnnLGGsQWywIsbD3FVKzMK0ozPIwFtqMGB4LbeUfUaAb-L6WuVGVWkSNAZrscJkR_WMfKOSNjmDXoiVKCIJr0iXiYHKCI3MXestcLQ?width=550&height=366&cropmode=none',
                        dates: '',
                        price: '',
                        bookby: '',
                        location: '',
                        transportation: '',
                        website: '',
                        bookhere: '',
                        info: [{ 
                            name: '*These vary in prices and we will not be providing transportation to the venue. Uber and taxis available.',
                            url: '',
                            isLink: false,
                        },
                        { 
                            name: 'Kettle Creek Inn',
                            url: 'http://www.kettlecreekinn.com/',
                            isLink: true,
                        },
                        { 
                            name: 'Inn on the Harbour',
                            url: 'http://innontheharbour.net/',
                            isLink: true,
                        },
                        { 
                            name: 'The Windjammer Inn',
                            url: 'https://www.thewindjammerinn.com/',
                            isLink: true,
                        },
                        { 
                            name: 'The Telegraph House',
                            url: 'http://www.telegraphhouse.com/index.php/Dining/Index',
                            isLink: true,
                        },
                        ]
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
        background: linear-gradient(rgba(255, 255, 255, .6), rgba(255, 255, 255, .99)), url('https://b0rtdg.bn.files.1drv.com/y4mUKhWv84jRu2sffpC_unLOD1mj7KsVbvKBnvKcXsgvHA54Vf4f1An1wG31t6yJnqKDYP3aUclf-b4s3bbD8JpmKMVY73vGJesWbp09zpMh96z1JPEb_1nS8jpCuXWn8uIArzw3I6iTShKuhnqcx9sxmfCogjKxNQI7fmzmnzVB_fKT_3L-7wwN4IpSBsJLJPkM_OwVjGIfbJJPnz4W4ahEg?width=1500&height=2000&cropmode=none') no-repeat center center fixed;
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