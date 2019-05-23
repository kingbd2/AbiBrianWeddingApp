<template>
    <div>
        <div class="container" v-for="guest in guests" :key="guest.id">
            <p class="title is-4 has-text-primary">
                {{ guest.first_name }} {{ guest.last_name }}
            </p>
            <div class="button" @click='toggle()'>Open/Close</div>
            <div class="button" @click='Rsvp()'>Submit</div>
            <p class="title is-4 has-text-primary">
                {{ is_attending }}
            </p>
            <div class="control">
                <label class="radio">
                    <input type="radio" name="answer">
                    Yes
                </label>
                <label class="radio">
                    <input type="radio" name="answer">
                    No
                </label>
            </div>
        </div>
    </div>
</template>

<script>
    import session from '../store/api/session';
    export default {
        props: ['guests'],
        data() {
            return {
                loading: false,
                is_attending: false,
                error: null,
                response: null,
            }
        },
        methods: {
            Rsvp() {
                this.error = this.response = null
                this.loading = true
                const url = this.$route.params.uuid + '/guests/'
                console.log(url)
                return session.put(url, {
                        id: 1,
                        is_attending: true,
                        // lastName: 'Flintstone'
                    })
                    // .then((res) => {
                    //     if (res.data) {
                    //         this.loading = false
                    //         this.guests = res.data
                    //     } else {
                    //         context.error()
                    //     }
                    // })
                    .catch(error => {
                        console.log(error)
                        this.loading = false
                        this.error = "Please go to your wedding invitation email and try again."
                    })
            },
            toggle: function () {
                this.is_attending = !this.is_attending
            },
        }
    }
</script>

<style lang="scss" scoped>

</style>