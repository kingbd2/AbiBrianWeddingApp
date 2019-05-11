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

            <h1 class="title">
                We're getting married!
            </h1>
            <h2 class="subtitle">
                And we want to celebrate with you.
            </h2>
            <ul>
                <li>
                    {{ guests.name }}
                </li>
            </ul>
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
    import session from '../../store/api/session';
    export default {
        components: {},
        
        asyncData(context){
            return session.get('76774464-c666-47ca-85fb-758f18b90588')
            .then((res)=>{
                if(res.data){
                    return { guests: res.data }
                }else{
                    context.error()
                }
            })
        },
        async fetch({
            store,
            query
        }) {
            // store.state.uuid = query.uuid
            // let {
            //     data
            // } = await axios.get('http://192.168.0.21:8000/api/v1/')
            // store.commit('setStars', data)
        },
        mounted() {
            console.log(this.$route.params.uuid);
        }
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