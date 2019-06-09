<template>
    <div>

        <div v-if="error" class="error">
            {{ error }}
        </div>

        <div class="card large">
            <div class="card-content">
                <div class="media">
                    <div class="media-content">
                        <h1 class="title is-4 no-padding has-text-primary">{{ guest.first_name }} {{ guest.last_name }}
                        </h1>
                        <div class="columns">
                            <div class="column">
                                <p class="no-padding has-text-info">Attending?</p>
                                <div class="button" v-bind:class="{ 'is-success': is_attending }"
                                    @click='toggle_is_attending()'>{{ yes_no_is_attending }}</div>
                                    <div class="button" v-bind:class="{ 'is-success': !is_attending }"
                                    @click='toggle_is_attending()'>{{ yes_no_is_attending }}</div>
                            </div>
                            <div class="column">
                                <p class="no-padding has-text-info">Any dietary restrictions?</p>
                                <div class="button" v-bind:class="{ 'is-success': has_dietary_restrictions }"
                                    @click='toggle_dietary_restrictions()'>{{ yes_no_dietary_restrictions }}</div>
                            </div>
                        </div>

                        </br>
                        <div v-if="has_dietary_restrictions === true">
                            <input class="input" type="text" placeholder="Please provide your dietary restriction."
                                v-model="dietary_restrictions">
                        </div>
                        <div v-else>
                            <input class="input" type="text" placeholder="Please provide your dietary restriction."
                                disabled>
                        </div>
                        </br>
                        <div v-if="has_changed === true" class="success">
                            <div class="button is-primary" @click='Rsvp(guest.id)'>Submit</div>
                            <div class="p has-text-weight-bold has-text-success">Please submit your changes.</div>
                        </div>
                        <div v-else>
                            <!-- <div class="p has-text-primary">Please submit your changes.</div> -->
                            <div class="button is-primary" disabled>Submit</div>
                        </div>
                        <div v-if="has_submitted === true" class="success">
                            <div class="p has-text-weight-bold has-text-success">Thanks for letting us know!</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- <div v-if="guest" class="content">
            <div class="card">
                <header class="card-header">
                    <p class="card-header-title">
                        Component
                    </p>
                    <a href="#" class="card-header-icon" aria-label="more options">
                        <span class="icon">
                            <i class="fas fa-angle-down" aria-hidden="true"></i>
                        </span>
                    </a>
                </header>
                <div class="card-content">
                    <div class="content">
                        <table class="table">
                            <thead>
                                <tr>
                                    <th>Guest</th>
                                    <th>Attending?</th>
                                    <th>Dietary Restrictions?</th>
                                    <th v-if="has_dietary_restrictions === true">
                                        Dietary Restrictions Details
                                    </th>

                                    <th v-else class="has-text-light">
                                        Dietary Restrictions Details
                                    </th>
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
                                            @click='toggle_dietary_restrictions()'>{{ yes_no_dietary_restrictions }}
                                        </div>
                                    </td>

                                    <td v-if="has_dietary_restrictions === true">

                                        <input class="input" type="text"
                                            placeholder="Please provide your dietary restriction."
                                            v-model="dietary_restrictions">
                                    <td v-else>
                                        <input class="input" type="text"
                                            placeholder="Please provide your dietary restriction." disabled>
                                    </td>

                                </tr>
                            </tbody>
                        </table>
                        <div v-if="has_changed === true" class="success">
                            <div class="button is-primary" @click='Rsvp(guest.id)'>Submit</div>
                            <div class="p has-text-weight-bold has-text-success">Please submit your changes.</div>
                        </div>
                        <div v-else>
                            <div class="button is-primary" disabled>Submit</div>
                        </div>
                        <div v-if="has_submitted === true" class="success">
                            <div class="p has-text-weight-bold has-text-success">Thanks for letting us know!</div>
                        </div>
                    </div>
                </div>
            </div>
        </div> -->

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
                return session.get(STATUS_URL, {
                        crossdomain: true
                    })
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