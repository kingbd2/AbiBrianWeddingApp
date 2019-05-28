<template>
    <div>
        <div v-if="error" class="error">
            {{ error }}
        </div>


        <div v-if="guest" class="content">
            <table class="table">
                <thead>
                    <tr>
                        <th>Guest</th>
                        <th>Attending?</th>
                        <th>Dietary Restrictions?</th>
                        <div v-if="has_dietary_restrictions === true" class="success">
                        <th>
                            Dietary Restrictions Details</th></div>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>{{ guest.first_name }} {{ guest.last_name }}</td>
                        <td>
                            <div class="button" v-bind:class="{ 'is-success': is_attending }"
                                @click='toggle_is_attending()'>{{ yes_no_is_attending }}</div>
                        </td>
                        <td>
                            <div class="button" v-bind:class="{ 'is-success': has_dietary_restrictions }"
                                @click='toggle_dietary_restrictions()'>{{ yes_no_dietary_restrictions }}</div>
                        </td>
                        
                        <td>
                            <div v-if="has_dietary_restrictions === true" class="success">
                            <input class="input" type="text" placeholder="Please provide your dietary restriction."
                                v-model="dietary_restrictions">
                            </div>
                        </td>
                    </tr>
                </tbody>
            </table>

            <div v-if="has_changed === true" class="success">
                <div class="button is-primary" @click='Rsvp(guest.id)'>Submit</div>
                Please submit your changes.
            </div>
        </div>
        <div v-if="has_submitted === true" class="success">
            Thanks for letting us know!
        </div>
    </div>

</template>

<script>
    import session from '../store/api/session';
    export default {
        props: ['guest'],
        data() {
            return {
                id: this.guest.id,
                loading: false,
                is_attending: false,
                has_dietary_restrictions: false,
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
                return session.get(STATUS_URL)
                    .then((res) => {
                        if (res.data) {
                            this.has_dietary_restrictions = res.data.has_dietary_restrictions
                            this.dietary_restrictions = res.data.dietary_restrictions
                            this.is_attending = res.data.is_attending
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