<template>
    <div>
            <h1 class="title is-4 no-padding has-text-primary">{{ guest.first_name }} {{ guest.last_name }}
            </h1>
            <div class="columns">
                <div class="column">
                    <p class="no-padding has-text-info">Is {{ guest.first_name }} attending?</p>
                    <div class="button" v-bind:class="{ 'is-success': is_attending_yes }"
                        @click='toggle_is_attending_yes()' v-on:click="emitToParent">Yes</div>
                    <div class="button" v-bind:class="{ 'is-success': is_attending_no }"
                        @click='toggle_is_attending_no()'>No</div>
                </div>
                <div class="column">
                    <p class="no-padding has-text-info">Any dietary restrictions?</p>
                    <div class="button" v-bind:class="{ 'is-success': has_dietary_restrictions_yes }"
                        @click='toggle_dietary_restrictions_yes()'>Yes</div>
                    <div class="button" v-bind:class="{ 'is-success': has_dietary_restrictions_no }"
                        @click='toggle_dietary_restrictions_no()'>No</div>
                </div>
                <div class="column"></div>
            </div>
            </br>

            <div v-if="has_dietary_restrictions === true">
                <input class="input" type="text" placeholder="Please provide your dietary restriction."
                    v-model="dietary_restrictions">
            </div>
            <div v-else>
                <input class="input" type="text" placeholder="Please provide your dietary restriction." disabled>
            </div>
            </br>
            <div v-if="started === true" class="success">
                <div class="button is-primary" disabled>Select an option for each guest above</div>
            </div>
            <div v-else-if="has_changed === true" class="success">
                <div class="button is-primary" @click='Rsvp(guest.id)'>Click here to submit
                    {{ guest.first_name }}'s response.</div>
            </div>
            <div v-else>
                <div class="button is-primary" disabled>Thanks for letting us know!</div>
            </div>
        </div>
</template>

<script>
    import session from '../store/api/session';
    export default {
        props: ['guest'],
        data() {
            return {
                started: true,
                id: this.guest.id,
                loading: false,
                is_attending_yes: false,
                is_attending_no: false,
                is_attending: false,
                has_dietary_restrictions: false,
                has_dietary_restrictions_yes: false,
                has_dietary_restrictions_no: false,
                dietary_restrictions: '',
                error: null,
                response: null,
                party_guests: this.guests,
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
                        dietary_restrictions: this.dietary_restrictions,
                        has_responded: true
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
                        dietary_restrictions: this.dietary_restrictions,
                        has_responded: true,

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
            toggle_is_attending_yes: function () {
                this.is_attending_no = false
                this.started = false
                this.is_attending_yes = !this.is_attending_yes
                this.has_submitted = false
                this.has_changed = true
                if (this.is_attending_no === false & this.is_attending_yes === true) {
                    this.is_attending = true
                } else {
                    this.is_attending = false
                }
            },
            toggle_is_attending_no: function () {
                this.is_attending_yes = false
                this.started = false
                this.is_attending_no = !this.is_attending_no
                this.has_submitted = false
                this.has_changed = true
                if (this.is_attending_no === true & this.is_attending_yes === false) {
                    this.is_attending = false
                }
            },
            toggle_dietary_restrictions_yes: function () {
                this.has_dietary_restrictions_no = false
                this.started = false
                this.has_dietary_restrictions_yes = !this.has_dietary_restrictions_yes
                this.has_submitted = false
                this.has_changed = true
                if (this.has_dietary_restrictions_no === false & this.has_dietary_restrictions_yes === true) {
                    this.has_dietary_restrictions = true
                } else {
                    this.has_dietary_restrictions = false
                }
            },
            toggle_dietary_restrictions_no: function () {
                this.has_dietary_restrictions_yes = false
                this.started = false
                this.has_dietary_restrictions_no = !this.has_dietary_restrictions_no
                this.has_submitted = false
                this.has_changed = true
                if (this.has_dietary_restrictions_no === true & this.has_dietary_restrictions_yes === false) {
                    this.has_dietary_restrictions = false
                }
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