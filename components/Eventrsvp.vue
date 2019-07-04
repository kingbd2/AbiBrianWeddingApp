<template>
    <div>

        <div class="column">
            <p class="no-padding has-text-info">Will you be attending?</p>
            <div class="button" v-bind:class="{ 'is-success': is_attending }" @click='toggle_is_attending()'
                v-on:click="emitToParent">Yes</div>
            <div class="button" v-bind:class="{ 'is-success': !is_attending }" @click='toggle_is_attending()'>No</div>
        </div>


        <div v-if="has_changed === true" class="success">
            <div class="button is-primary" @click='Rsvp(guest.id)'>Click here to submit {{ guest.first_name }}'s
                response.</div>
        </div>
        <div v-else>
            <div class="button is-primary" disabled>Thanks for letting us know!</div>
        </div>


    </div>
</template>

<script>
    import session from '../store/api/session';
    export default {
        props: ['guest', 'eventType'],
        data() {
            return {
                id: this.guest.id,
                loading: false,
                is_attending: false,
                has_dietary_restrictions: false,
                dietary_restrictions: '',
                error: null,
                response: null,
                party_guests: this.guest,
                event_type: this.eventType,
                has_submitted: false,
                has_changed: false,
            }
        },
        mounted: function () {
            this.GET_STATUS();
        },
        methods: {
            GET_STATUS() {

                this.has_submitted = false
                this.error = this.response = null
                this.loading = true
                const STATUS_URL = this.$route.params.uuid + '/guests/' + this.id + '/'
                return session.get(STATUS_URL, {
                        crossdomain: true
                    })
                    .then((res) => {
                        if (res.data) {
                            this.has_dietary_restrictions = res.data.has_dietary_restrictions
                            this.dietary_restrictions = res.data.dietary_restrictions
                            this.is_attending = res.data.is_attending
                            this.has_changed = true
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
            Rsvp(id) {
                this.error = this.response = null
                this.loading = true
                const RSVP_URL = this.$route.params.uuid + '/guests/' + id + '/'
                return session.put(RSVP_URL, {
                        is_attending: this.is_attending,
                        has_dietary_restrictions: this.has_dietary_restrictions,
                        dietary_restrictions: this.dietary_restrictions

                    })
                    .then((res) => {
                        if (res.data) {
                            this.has_submitted = true
                            this.has_changed = false
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
            submitComment(id) {
                this.error = this.response = null
                this.loading = true
                const RSVP_URL = this.$route.params.uuid + '/guests/' + id + '/'
                return session.put(RSVP_URL, {
                        is_attending: this.is_attending,
                        has_dietary_restrictions: this.has_dietary_restrictions,
                        dietary_restrictions: this.dietary_restrictions

                    })
                    .then((res) => {
                        if (res.data) {
                            this.has_submitted = true
                            this.has_changed = false
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
            toggle_is_attending: function () {
                this.is_attending = !this.is_attending
                this.has_submitted = false
                this.has_changed = true
            },
            toggle_dietary_restrictions: function () {
                this.has_dietary_restrictions = !this.has_dietary_restrictions
                this.has_submitted = false
                this.has_changed = true
            },
            emitToParent(event) {
                this.$emit('childToParent', this.guest.id)
            }
        },
        computed: {
            yes_no_is_attending: function () {
                if (this.is_attending === true) {
                    return "Yes"
                } else {
                    return "No"
                }
            },
            yes_no_dietary_restrictions: function () {
                if (this.has_dietary_restrictions === true) {
                    return "Yes"
                } else {
                    return "No"
                }
            }
        }
    }
</script>

<style lang="scss" scoped>

</style>