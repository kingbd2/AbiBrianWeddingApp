<template>
    <div>
        <div class="column">
            <div v-for="guest in party_guests" :key="guest.id">
                <p class="has-text-info">Will {{ guest.first_name }} be attending? </p>
                <toggle :guest="guest" :eventType="event_type" v-on:childToParent="onChildClick"></toggle>
            </div>

        </div>
        <p class="has-text-primary has-text-weight-bold">Please click "Yes" or "No" for each guest and press the button
            below to submit your response.</p>
        <div v-if="started === true" class="success">
            <div class="button is-primary" disabled>Select an option for each guest above</div>
        </div>

        <div v-else-if="has_changed === true" class="success">

            <div class="button is-primary" @click='RsvpGuests()'>Click here to submit your
                response.</div>
        </div>
        <div v-else>
            <div class="button is-primary" disabled>Thanks for letting us know!</div>
        </div>

    </div>
</template>

<script>
    import session from '../store/api/session';
    import Toggle from '~/components/Toggle';
    export default {
        props: ['guest', 'eventType'],
        components: {
            Toggle
        },
        data() {
            return {
                started: true,
                id: this.guest.id,
                loading: false,
                is_attending: false,
                error: null,
                response: null,
                party_guests: this.guest,
                event_type: this.eventType,
                has_submitted: false,
                has_changed: false,
                test: '',
                has_responded_brunch: false,
                has_responded_shabbat: false,
                has_responded_rehearsal_dinner: false,
                has_responded_wedding_rehearsal: false,
            }
        },
        mounted: function () {
            this.GET_EVENT_TYPE();
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
            EventRsvp(i, id) {
                this.error = this.response = null
                this.loading = true
                const RSVP_URL = this.$route.params.uuid + '/guests/' + id + '/'
                if (this.has_responded_brunch === true) {
                    return session.put(RSVP_URL, {
                            is_attending_brunch: this.party_guests[i].is_attending_brunch,
                            has_responded_brunch: this.has_responded_brunch,

                        })
                        .then((res) => {
                            if (res.data) {
                                this.started = false
                                this.has_submitted = true
                                this.has_changed = false
                                this.loading = false
                            } else {
                                context.error()
                            }
                        })
                        .catch(error => {
                            console.log(error)
                            this.loading = false
                            this.error = "Please go to your wedding invitation email and try again."
                        })
                } else if (this.has_responded_shabbat === true) {
                    return session.put(RSVP_URL, {
                            is_attending_shabbat: this.party_guests[i].is_attending_shabbat,
                            has_responded_shabbat: this.has_responded_shabbat,
                        })
                        .then((res) => {
                            if (res.data) {
                                this.started = false
                                this.has_submitted = true
                                this.has_changed = false
                                this.loading = false
                            } else {
                                context.error()
                            }
                        })
                        .catch(error => {
                            console.log(error)
                            this.loading = false
                            this.error = "Please go to your wedding invitation email and try again."
                        })
                } else if (this.has_responded_rehearsal_dinner === true) {
                    return session.put(RSVP_URL, {
                            is_attending_rehearsal_dinner: this.party_guests[i].is_attending_rehearsal_dinner,
                            has_responded_rehearsal_dinner: this.has_responded_rehearsal_dinner,
                        })
                        .then((res) => {
                            if (res.data) {
                                this.started = false
                                this.has_submitted = true
                                this.has_changed = false
                                this.loading = false
                            } else {
                                context.error()
                            }
                        })
                        .catch(error => {
                            console.log(error)
                            this.loading = false
                            this.error = "Please go to your wedding invitation email and try again."
                        })
                } else {
                    return session.put(RSVP_URL, {
                            is_attending_wedding_rehearsal: this.party_guests[i].is_attending_wedding_rehearsal,
                            has_responded_wedding_rehearsal: this.has_responded_wedding_rehearsal,
                        })
                        .then((res) => {
                            if (res.data) {
                                this.started = false
                                this.has_submitted = true
                                this.has_changed = false
                                this.loading = false
                            } else {
                                context.error()
                            }
                        })
                        .catch(error => {
                            console.log(error)
                            this.loading = false
                            this.error = "Please go to your wedding invitation email and try again."
                        })
                }
            },
            RsvpGuests() {
                var i;
                for (i = 0; i < this.party_guests.length; i++) {
                    this.EventRsvp(i, this.party_guests[i].id)
                }

            },
            GET_EVENT_TYPE() {
                if (this.event_type === 'brunch') {
                    this.has_responded_brunch = true
                } else if (this.event_type === 'shabbat') {
                    this.has_responded_shabbat = true
                } else if (this.event_type === 'rehearsal_dinner') {
                    this.has_responded_rehearsal_dinner = true
                } else {
                    this.has_responded_wedding_rehearsal = true
                }
            },


            onChildClick: function (value) {
                this.has_changed = true
                this.started = false
                var i;
                // console.log(value[0])

                if (this.event_type === "wedding_rehearsal") {
                    for (i = 0; i < this.party_guests.length; i++) {
                        if (value[0] === this.party_guests[i].id) {
                            if (value[2] === true) {
                                this.party_guests[i].is_attending_wedding_rehearsal = true
                            } else {
                                this.party_guests[i].is_attending_wedding_rehearsal = false
                            }
                        }
                    }
                } else if (this.event_type === "brunch") {
                    for (i = 0; i < this.party_guests.length; i++) {
                        if (value[0] === this.party_guests[i].id) {
                            if (value[2] === true) {
                                this.party_guests[i].is_attending_brunch = true
                            } else {
                                this.party_guests[i].is_attending_brunch = false
                            }
                        }
                    }
                } else if (this.event_type === "rehearsal_dinner") {
                    for (i = 0; i < this.party_guests.length; i++) {
                        if (value[0] === this.party_guests[i].id) {
                            if (value[2] === true) {
                                this.party_guests[i].is_attending_rehearsal_dinner = true
                            } else {
                                this.party_guests[i].is_attending_rehearsal_dinner = false
                            }
                        }
                    }
                } else if (this.event_type === "shabbat") {
                    for (i = 0; i < this.party_guests.length; i++) {
                        if (value[0] === this.party_guests[i].id) {
                            if (value[2] === true) {
                                this.party_guests[i].is_attending_shabbat = true
                            } else {
                                this.party_guests[i].is_attending_shabbat = false
                            }
                        }
                    }
                }
            }
            // emitToParent(event) {
            //     this.$emit('childToParent', this.guest.id)
            // }
        },
    }
</script>

<style lang="scss" scoped>
    p.has-text-info {
        padding-top: 3%;
    }
</style>