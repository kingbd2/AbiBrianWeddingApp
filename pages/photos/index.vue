<template>
    <div>
        <section class="hero is-fullheight is-primary is-background">
            <div class="hero-body">
                <div class="container has-text-centered">
                    <div class="columns is-multiline">
                        <div class="column is-one-quarter-desktop is-half-tablet" v-for="photo in images"
                            :key="photo.id">
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
                        caption: "Brian and Abiella's first hockey game!",
                        url: 'https://bkrudg.bn.files.1drv.com/y4mtQQsxCJ2P6dIdKK304ptwW7pqCfBFNUKy2Y0JP7-xOvYTWTD9NRaTLuBYOli8ow0x8GRSYWErMBGOJFqwQ6Y4xI0pQ_-I-IZDSipDEkCAx3ph4WAPsyKhSrqA0Ypk8N8c1b2SOar5rlWbkKc8w7-4CsxfUagUB0RM7WKMsi2_bgFvTjDjqpcER6t52Zbg9CsHtap1R0w3ST5u8EYql1muQ?width=495&height=660&cropmode=none',
                    },
                    {
                        caption: "Eating Naples pizza...yum!",
                        url: 'https://yurldg.bn.files.1drv.com/y4mK2YDMlYcqfVfsdnu2DN-SmockXgL6wnpR5ErQa3HWapGTCclXm9HUbRlcmBVA9w0u4sEYtcTYbonkkGo1MBwEueP9ZzcI0Sn-BB9BmGI4WX14or57u0QCwrzecsmu318SA1bZV_S4k8iC4vTkHTmm_I-MXisV6s8Zz7yG6Tces0SgBb4-YX7QsusOM1si4AtSMZqNvKngdORMrAGYOAyxQ?width=495&height=660&cropmode=none',
                    },
                    {
                        caption: "In Italy",
                        url: 'https://bkrsdg.bn.files.1drv.com/y4mkojOI82YtOaOHCZfi9uGbAPt39n2-orkQavfolMGj0XUtorUrHhVKtLBreiG3dhUYDr8jOwamArOEqbb9qWXYTI0ieNksm5GzNZuD5CQCTSAdIHk2Hq-AYXm8h1DZV56P56H-U81v3Sgz82Gxj44yQcE-4_8LjeLc0xRBTHD0x-e0qVJReqNnmXHSG6_vRZQjAw1ID5B-fqyHaaPVJ_60A?width=495&height=660&cropmode=none',
                    },
                    {
                        caption: "Jon Snow and Queen Danaerys",
                        url: 'https://bkrndg.bn.files.1drv.com/y4mc7pLRe00cGhZAFy6IHhMqRJ-pmh1e9nev_6qS82TG9EuhIwrsL96Th7_wpOnzEjgCOp5Xy1_jJ3eY8BbEmNxxBmSjWDZTyaZHvZv_4P6RbSLDFC6dSz4BENyTdXbsGonWa9mo3dZZ5MhXZ5wUc6zt24aowylFQIkAI-A3OLYgI_bCnXaemXsW5_gHuF6S5NOPGjSwqA9PcSDbRcu3I1Cpw?width=495&height=660&cropmode=none',
                    },




                    {
                        caption: 'Engagement photoshoot',
                        url: 'https://b0rmdg.bn.files.1drv.com/y4mfrS3OPLPYUDjFhgExusEGSNvC6_hlO-CNdGNyaxzwBuhEAkqXl4MDmxJlKoca5D0GcD41TplKrb37TyTVkfh-cdIM75N6ZTjpJPKK1Nq5f5iECx2fXRxbapAYMGsRm-aWVDRakXH9mPf5Ne2vKCsLzhzjmylq8bMyklNk90StKfsjKmQAvqDNpf0tfvU_zVNtxtcudfHaMoBpjrU2zcHSQ?width=640&height=427&cropmode=none',
                    },
                    {
                        caption: 'With the family in Costa Rica',
                        url: 'https://bkrqdg.bn.files.1drv.com/y4msaK7VzJ8gX9_ukEb2wt7utShs_FpwqpU0G0rV6JTZyD6408aQtjXsYrgh6QHvZso_T2HRjCbUQ2qLVv2zkgTYTFb1dNtfGTX6nRsvfYz-rRbqzea9xWM4_QeeNKnyorFr2ooL1ibdxzEzKDvuP_9hE84ScJw5s5JA0BCLhF2HUGC-vD5X5ORvX9JR-8WPBUHeE6fvJO_DeqnpfY1hKYBPA?width=660&height=440&cropmode=none',
                    },
                    {
                        caption: 'At our engagement party',
                        url: 'https://yurodg.bn.files.1drv.com/y4mIDLbokKVns0tRmg_UKvC4HUzDmDNnafZk6Dc4xpWRNNgp92AoGtkUhB_BVzyVHWR2PNqpCRZT8G1lmFxlykIX1KHpdsDEQ3mnN0XRcOZvjvUERnKJqydCRFAIS7bIfs83ue8KHYzDoITI1WbveMPEbakG0_EnTAngDP0mXFrGeAMHi8-RxKj915OaNTllEM257bKYmhxP_u0hMc64vv6yg?width=660&height=495&cropmode=none',
                    },
                    {
                        caption: 'Enjoying the cottage',
                        url: 'https://bkrmdg.bn.files.1drv.com/y4mndR6lqud24Wd7xHmS9v3xnRtnrJAR-cvUG4qsFseYf6_0hpSAoUB8_Rgrb1Sh9HVCOPV19IzaR0aVfCaKVv-mghxlZen49POFkXhLnk-AD6aR3b2Gy1UvBNjIO4dTp_itkqEkylRHSZR1fG8BLtcbTKU9p9r_fw8ubL3lwUm9vvYwzWXftFkGa8ob8bK5Vga0PnVqEiFGS4cjvsuSYuIxg?width=1280&height=960&cropmode=none',
                    },




                    {
                        caption: 'Brian and Abiella',
                        url: 'https://bersdg.bn.files.1drv.com/y4m8PSFJlUOUdYOgiMQ5QyQHmi7yu0t7Hoa1Y2IEZtqQGuzZazUbDqguq83H6CxIU6vSfxjrYFuT_BTH4VYyIMflHCTlx9xUrVHNfk29YzT8rZJoC-6jXFJA9ZbFkYCStMU2DQKppJvLZSgbgTHefltJdNffRXUcDym_obdkefaXayShcVqwYx_2TUppjflc72lvXty3_5Hur8E_nmsc72-cg?width=640&height=427&cropmode=none',
                    },
                    {
                        caption: 'Brian and Abiella AGAIN',
                        url: 'https://b0rldg.bn.files.1drv.com/y4mjEgv7U-YShZxhuJGHcJq570FGnpqtH_jbTDJc2YkIw5HzIp2Oc_uHBR2HqfA-H_KXitQQHgXmWp5jH9GfwMIEg3Fn0U55lS8ZUxGSdZ-Nv3UQjnnbyZgCHTMGgpqayG045cevXad1xeSDcTFVupt1aYowxr9sKCPN2yKbthO-lmdUiyR25tO1tsTLhF4aC-W7g2fqZMdNUat-4D4ZOyc9A?width=640&height=427&cropmode=none',
                    },
                    {
                        caption: 'You guessed it...Brian and Abiella',
                        url: 'https://b0rodg.bn.files.1drv.com/y4mYueL9h-jsf__MkfbcUJD7ZrH9z1TqKRJJvYDXgaiLXVoagqbvmSq4yDZF1F3s75Vjk-EZnwiQhpZ1gWLLz4MUcRd5uLHCYzvesMSJLMiunBlQhH-CpBxJ9Wu94oh6D41fjiqSHVn_brGGVZB7rqq-ZMxEBmCn3XvnL7I5jfI_NQTISvmExlxQZ4cpGnGO349FxAQAI1TLhxrc4mjZzlhIw?width=640&height=427&cropmode=none',
                    },
                    {
                        caption: 'Engaged!',
                        url: 'https://b0rudg.bn.files.1drv.com/y4mZ2cdB59uD7TG-CNAvIB8Zm8gX_I9ewZGUqYyhBz1195vooE8JIjrezE7X7MVwEGuxAsvrD5IFy9GaCqkyaxG-vAv5NN9FFklmwfrjbGZQq3fBaUDP2Bw-cr4so9cJPBaEymTZs8kXco9uOpRMN6r1_WowFr5XYgPXG58rFyoPpNrCXEnWYy3-ApAt1XjwFpJeC5J3ISD21rHpiHJVPBMQg?width=660&height=496&cropmode=none',
                    },



                    {
                        caption: "Cycling the Tuli",
                        url: 'https://yurpdg.bn.files.1drv.com/y4mHxxxC_Nfs-yYCmY1U4T8ewDR_FVktBBAh_DPYlG8s6dEJjTCvut6B-VcknaxCmd0JnpTs2BJKlaz6I1AbbY3ubixji_vHLJEbPuD9dSwOf7QbSF7HJPwvOmbTWsLDrGzgdWna1rQWfnj_Ms3vQBNKocWVt0c9V9oN0QrfjgqzZ2ZHsD-o7KskMgix2ja8EBRbuaHFqfIXjOC33uzCjEOQg?width=660&height=495&cropmode=none',
                    },
                    {
                        caption: 'Brian, Peter, Brenda, and Lucy',
                        url: 'https://z88yhq.bn.files.1drv.com/y4mBnpUFtZX8rRuilBZbM1T6c9J3xP4SDjI1pPcz5GoufJv5Ite8k-6GyqyieyPp5ryz_GMsQFeF5-_K0nx32urxpyieIfMCS23-jVr-jH2Y2bnJx3JB2f6oMT2QizfHChnGtSjJRLMqeYlixFywjhaloH0L-ZgoGSXBdKc5KCjqIqfHp2tzWGMuiGPnwC4XqrGsvIyUZjTAtH7dz2-fN7o7Q?width=1024&height=680&cropmode=none',
                    },
                    {
                        caption: 'Abiella cycling in Amsterdam',
                        url: 'https://x4jqsg.dm.files.1drv.com/y4m2lYMD6YD5bHVhm22UOUuqnu0o1lDFeEnGetcinuTwG-GDUNs6My2uPnD0Pg27VB-aLUKLonenKp0SNm1jXeVoiaic07vTB7Z0tuq-rYxOKSh0vQTHHquvtcUgkv4mzy0VJt7NNTNZpxiUtmcbD-zj6_5aHDfdRgCHKHTy4LrmiQf7zSen0ZnYzae6t9AdLKA3kUTPGysuNoCJwkBHB9z-w?width=1024&height=576&cropmode=none',
                    },
                    {
                        caption: 'Clive and Abiella cycling the Tuli',
                        url: 'https://jbszva.dm.files.1drv.com/y4m3mPuAdNwYrcQLdmkbOKA3Sk17Z1GO4s_UaXdoJ32gjJvJvQkzvIIsiacrz8jK7mcSJ1GedQxGps4MWbKQu9HDCqkOJxusDLY5Utu_j3pRfSkdiR34V0J4SqoqHZK0paOugctafc0OWTsJ79ssYzpvYEFQ25PcdQxhhlyOuPsn8J_5vGcP23dRaFyJIadYge3qvNGyOqt1ZJcYbD8W7uRaw?width=1024&height=576&cropmode=none',
                    },



                    {
                        caption: 'Hiking in Capri',
                        url: 'https://bkrrdg.bn.files.1drv.com/y4mO_PoL6fwnq1bLh9v9-Z-2IeegXsMcsyHTQwQDQGP8ymyDnmY6shWiTk45QbIDtP98ibuRdbcXePpTF-yZxoS1Hps1Pvl-MawbuWgjV7D8WAItHNe7NIdbaiQ8-sBnj1OxlbUS_8XHs5Xtm2tJvN3JFPFA9N7OlidXrR5ndfOlgPLvfqC7TnH93wJWlpGpaWbd4clIoLPHg8CXFAxAo2LtQ?width=495&height=660&cropmode=none',
                    },
                    {
                        caption: 'Hiking in Capri',
                        url: 'https://bkrpdg.bn.files.1drv.com/y4mGbUf0MYzFf4ICYvh2mR6SOFREOvbMieZYIiaZ3XiRu_yaxsdXxHTHC0z9gPXM_Zzz1rsItMWEpJdy2KT26P7Oz0DFqpkzlj9JqOwxeM-7ecMiik5tpVTvv4UIYqx9vLER8jDyyIlKxqC0oGMQwCpgf9iZoLgR5Nsy9aLkbRaHO3POalvJ8WDvLgW5gRacn11gnmO1JBJzyoPgoKMDVEXcQ?width=495&height=660&cropmode=none',
                    },
                    {
                        caption: 'Caprese salad - the best salad!',
                        url: 'https://yurndg.bn.files.1drv.com/y4m0m9hNhNzsJuBteQdsZOYocOh2ZaRe22P7GsHr79rUN52B0Du6kRAIpt2wPO5pjLD7oRhsu7_PYU8t6SPew8BDpR_voUNBWGEiwEoDGJzzW1caTP93g4M1ockUAnTXWUmw3m3omnOn8hzw0xj6cPu7Z01fNixUZBletH0385z09l0007LcorgjK7ONxj6eSdcDK6hhA6-XgkjLIVwDhoxcg?width=495&height=660&cropmode=none',
                    },
                    {
                        caption: 'Enjoying a cappucino',
                        url: 'https://yurmdg.bn.files.1drv.com/y4mgnE7oXL8YgXzui_4Fh_ZrJFZQLRkK-9gVyO2vNCsP5vo1gl7cGbtHCgsoCOmLHNDo78PD67Pm8JX6XcN1lHAjiWX51Fb67ApgJSG0Xvowhyi5gQ1pmF61Sd-PvZXqR0hFafi5QGK1GYCRCz7Npm7vuv_TXfbY0c3VnVhLb08p20KsOs49TzZ7yxEMY2UvhCW-w3fw77K5rEU1Z2PpYpD2g?width=495&height=660&cropmode=none',
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