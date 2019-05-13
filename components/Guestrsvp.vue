<template>
    <div>
        <div class="container" v-for="guest in guests" :key="guest.id">
            <p class="title is-4 has-text-primary">
                {{ guest.first_name }} {{ guest.last_name }}
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
    export default {
        props: ['guests'],
        data() {
            return {
                loading: false,
                response: null,
                error: null
            }
        },
        methods: {
            Rsvp() {
                this.error = this.response = null
                this.loading = true
                const url = this.$route.params.uuid + '/guests'
                console.log(url)
                return session.get(url)
                    .then((res) => {
                        if (res.data) {
                            this.loading = false
                            this.guests = res.data
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
    }
</script>

<style lang="scss" scoped>

</style>