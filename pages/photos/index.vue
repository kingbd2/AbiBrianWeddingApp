<template>
    <div>
        <section class="hero is-fullheight is-primary is-background">
            <div class="hero-body">
                <div class="container has-text-centered">
                    <div class="columns is-multiline">
                        <div class="column is-one-quarter-desktop is-half-tablet" v-for="photo in images" :key="photo.id">
                        <photo-card :photo="photo"></photo-card>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </div>
</template>

<script>
    import PhotoCard from '~/components/PhotoCard';
    export default {
        components: {
            PhotoCard
        },
        data: function () {
            return {
                images: [
                    {
                        caption: 'Brian and Abi',
                        url: 'https://bersdg.bn.files.1drv.com/y4m8PSFJlUOUdYOgiMQ5QyQHmi7yu0t7Hoa1Y2IEZtqQGuzZazUbDqguq83H6CxIU6vSfxjrYFuT_BTH4VYyIMflHCTlx9xUrVHNfk29YzT8rZJoC-6jXFJA9ZbFkYCStMU2DQKppJvLZSgbgTHefltJdNffRXUcDym_obdkefaXayShcVqwYx_2TUppjflc72lvXty3_5Hur8E_nmsc72-cg?width=640&height=427&cropmode=none',
                    },
                    {
                        caption: 'Brian and Abi AGAIN',
                        url: 'https://b0rldg.bn.files.1drv.com/y4mjEgv7U-YShZxhuJGHcJq570FGnpqtH_jbTDJc2YkIw5HzIp2Oc_uHBR2HqfA-H_KXitQQHgXmWp5jH9GfwMIEg3Fn0U55lS8ZUxGSdZ-Nv3UQjnnbyZgCHTMGgpqayG045cevXad1xeSDcTFVupt1aYowxr9sKCPN2yKbthO-lmdUiyR25tO1tsTLhF4aC-W7g2fqZMdNUat-4D4ZOyc9A?width=640&height=427&cropmode=none',
                    },
                    {
                        caption: 'You guessed it...Brian and Abi',
                        url: 'https://b0rodg.bn.files.1drv.com/y4mYueL9h-jsf__MkfbcUJD7ZrH9z1TqKRJJvYDXgaiLXVoagqbvmSq4yDZF1F3s75Vjk-EZnwiQhpZ1gWLLz4MUcRd5uLHCYzvesMSJLMiunBlQhH-CpBxJ9Wu94oh6D41fjiqSHVn_brGGVZB7rqq-ZMxEBmCn3XvnL7I5jfI_NQTISvmExlxQZ4cpGnGO349FxAQAI1TLhxrc4mjZzlhIw?width=640&height=427&cropmode=none',
                    },
                    {
                        caption: 'Awwww',
                        url: 'https://bersdg.bn.files.1drv.com/y4m8PSFJlUOUdYOgiMQ5QyQHmi7yu0t7Hoa1Y2IEZtqQGuzZazUbDqguq83H6CxIU6vSfxjrYFuT_BTH4VYyIMflHCTlx9xUrVHNfk29YzT8rZJoC-6jXFJA9ZbFkYCStMU2DQKppJvLZSgbgTHefltJdNffRXUcDym_obdkefaXayShcVqwYx_2TUppjflc72lvXty3_5Hur8E_nmsc72-cg?width=640&height=427&cropmode=none',
                    },
                    {
                        caption: 'Brian and Abi',
                        url: 'https://bersdg.bn.files.1drv.com/y4m8PSFJlUOUdYOgiMQ5QyQHmi7yu0t7Hoa1Y2IEZtqQGuzZazUbDqguq83H6CxIU6vSfxjrYFuT_BTH4VYyIMflHCTlx9xUrVHNfk29YzT8rZJoC-6jXFJA9ZbFkYCStMU2DQKppJvLZSgbgTHefltJdNffRXUcDym_obdkefaXayShcVqwYx_2TUppjflc72lvXty3_5Hur8E_nmsc72-cg?width=640&height=427&cropmode=none',
                    },
                    {
                        caption: 'Brian and Abi',
                        url: 'https://bersdg.bn.files.1drv.com/y4m8PSFJlUOUdYOgiMQ5QyQHmi7yu0t7Hoa1Y2IEZtqQGuzZazUbDqguq83H6CxIU6vSfxjrYFuT_BTH4VYyIMflHCTlx9xUrVHNfk29YzT8rZJoC-6jXFJA9ZbFkYCStMU2DQKppJvLZSgbgTHefltJdNffRXUcDym_obdkefaXayShcVqwYx_2TUppjflc72lvXty3_5Hur8E_nmsc72-cg?width=640&height=427&cropmode=none',
                    },
                    {
                        caption: 'Brian and Abi',
                        url: 'https://bersdg.bn.files.1drv.com/y4m8PSFJlUOUdYOgiMQ5QyQHmi7yu0t7Hoa1Y2IEZtqQGuzZazUbDqguq83H6CxIU6vSfxjrYFuT_BTH4VYyIMflHCTlx9xUrVHNfk29YzT8rZJoC-6jXFJA9ZbFkYCStMU2DQKppJvLZSgbgTHefltJdNffRXUcDym_obdkefaXayShcVqwYx_2TUppjflc72lvXty3_5Hur8E_nmsc72-cg?width=640&height=427&cropmode=none',
                    },
                    {
                        caption: 'Brian and Abi',
                        url: 'https://bersdg.bn.files.1drv.com/y4m8PSFJlUOUdYOgiMQ5QyQHmi7yu0t7Hoa1Y2IEZtqQGuzZazUbDqguq83H6CxIU6vSfxjrYFuT_BTH4VYyIMflHCTlx9xUrVHNfk29YzT8rZJoC-6jXFJA9ZbFkYCStMU2DQKppJvLZSgbgTHefltJdNffRXUcDym_obdkefaXayShcVqwYx_2TUppjflc72lvXty3_5Hur8E_nmsc72-cg?width=640&height=427&cropmode=none',
                    },
                ]
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

    img {
        -webkit-filter: grayscale(100%);
        /* Chrome, Safari, Opera */
        filter: grayscale(100%);
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