<template>
    <div>
        <div class="card large">
            <div class="card-content">
                <div class="media">
                    <div class="media-content">
                        <div class="columns">
                            <div class="column">
                                <div>{{ guest.id }}</div>
                            </div>
                            <div class="column">
                                <div>{{ guest.first_name }} {{ guest.last_name }}</div>
                            </div>
                            <div class="column">
                                <div v-if="guest.is_attending===true">
                                    <div class="has-text-weight-bold has-text-primary">Yes!</div>
                                </div>
                                <div v-else>
                                    <div class="">No</div>
                                </div>
                            </div>
                            <div class="column">
                                <div v-if="guest.is_attending_shabbat===true">
                                    <div class="has-text-weight-bold has-text-primary">Yes!</div>
                                </div>
                                <div v-else>
                                    <div class="">No</div>
                                </div>
                            </div>
                            <div class="column">
                                <div v-if="guest.is_attending_wedding_rehearsal===true">
                                    <div class="has-text-weight-bold has-text-primary">Yes!</div>
                                </div>
                                <div v-else>
                                    <div class="">No</div>
                                </div>
                            </div>
                            <div class="column">
                                <div v-if="guest.is_attending_rehearsal_dinner===true">
                                    <div class="has-text-weight-bold has-text-primary">Yes!</div>
                                </div>
                                <div v-else>
                                    <div class="">No</div>
                                </div>
                            </div>
                            <div class="column">
                                <div v-if="guest.is_attending_brunch===true">
                                    <div class="has-text-weight-bold has-text-primary">Yes!</div>
                                </div>
                                <div v-else>
                                    <div class="">No</div>
                                </div>
                            </div>

                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    </div>
</template>

<script>
    import Dropdown from './Dropdown';
    import session from '../store/api/session';
    export default {
        components: {
            Dropdown
        },
        props: ['guest'],
        data: function () {
            return {
                details: this.guest,
                error: null,
                loading: false,
                has_submitted: false,
                has_changed: false,
            }
        },
        methods: {
            Submit(id) {
                this.error = this.response = null
                this.loading = true
                const GUEST_URL = '/b76224a7-fb0e-40c3-8dd3-cc46ec482079/guests/' + id + '/'
                return session.put(GUEST_URL, {
                        group: this.details.group,
                        iskid: this.details.iskid,
                        shabbat: this.details.shabbat,
                        brunch: this.details.brunch,
                        rehearsal_dinner: this.details.rehearsal_dinner,
                        wedding_rehearsal: this.details.wedding_rehearsal
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
            toggle_iskid: function () {
                this.details.iskid = !this.details.iskid
                this.has_submitted = false
                this.has_changed = true
            },
            toggle_shabbat: function () {
                this.details.shabbat = !this.details.shabbat
                this.has_submitted = false
                this.has_changed = true
            },
            toggle_brunch: function () {
                this.details.brunch = !this.details.brunch
                this.has_submitted = false
                this.has_changed = true
            },
            toggle_wedding_rehearsal: function () {
                this.details.wedding_rehearsal = !this.details.wedding_rehearsal
                this.has_submitted = false
                this.has_changed = true
            },
            toggle_rehearsal_dinner: function () {
                this.details.rehearsal_dinner = !this.details.rehearsal_dinner
                this.has_submitted = false
                this.has_changed = true
            },

            changekid(payload) {
                this.details.iskid = payload
            },
            changeshabbat(payload) {
                this.details.shabbat = payload
            },
            changebrunch(payload) {
                this.details.brunch = payload
            },
            changerehearsaldinner(payload) {
                this.details.rehearsal_dinner = payload
            },
            changeweddingrehearsal(payload) {
                this.details.wedding_rehearsal = payload
            }
        }

    }
</script>

<style lang="scss" scoped>
    p {
        padding-bottom: 4%;
    }
</style>