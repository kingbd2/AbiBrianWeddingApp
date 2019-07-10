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
                                <div>{{ guest.party }}</div>
                            </div>
                            <!-- <div class="column">
                                <div><input class="input" type="text" placeholder="Group" v-model="guest.group">
                                </div>
                            </div> -->

                            <div class="column">
                                <!-- <dropdown :value="guest.iskid" @child-to-parent="changekid"></dropdown> -->
                                <div class="button" v-bind:class="{ 'is-success': details.has_responded }"
                                    @click='toggle_has_responded()'>Has responded?</div>
                            </div>
                            <!-- <div class="column">
                                <div v-if="guest.is_attending===true">
                                    <div class="has-text-weight-bold has-text-primary">Yes!</div>
                                </div>
                                <div v-else>
                                    <div class="">No</div>
                                </div>
                            </div>
                            <div class="column">
                                <div v-if="guest.has_dietary_restrictions===true">
                                    <div class="has-text-weight-bold has-text-danger">Yes:
                                        {{ guest.dietary_restrictions }}</div>
                                </div>
                                <div v-else>
                                    <div class="">No</div>
                                </div>

                            </div> -->
                            <div class="column">
                                <!-- <dropdown :value="guest.iskid" @child-to-parent="changekid"></dropdown> -->
                                <div class="button" v-bind:class="{ 'is-success': details.iskid }"
                                    @click='toggle_iskid()'>Is kid?</div>
                            </div>
                            <div class="column">
                                <!-- <dropdown :value="guest.shabbat" @child-to-parent="changeshabbat"></dropdown> -->
                                <div class="button" v-bind:class="{ 'is-success': details.shabbat }"
                                    @click='toggle_shabbat()'>Shabbat</div>
                            </div>

                            <div class="column">
                                <!-- <dropdown :value="guest.wedding_rehearsal" @child-to-parent="changeweddingrehearsal"></dropdown> -->
                                <div class="button" v-bind:class="{ 'is-success': details.wedding_rehearsal }"
                                    @click='toggle_wedding_rehearsal()'>Wedding Rehearsal</div>
                            </div>
                            <div class="column">
                                <!-- <dropdown :value="guest.rehearsal_dinner" @child-to-parent="changerehearsaldinner"></dropdown> -->
                                <div class="button" v-bind:class="{ 'is-success': details.rehearsal_dinner }"
                                    @click='toggle_rehearsal_dinner()'>Rehearsal Dinner</div>
                            </div>
                            <div class="column">
                                <!-- <dropdown :value="guest.shabbat" @child-to-parent="changeshabbat"></dropdown> -->
                                <div class="button" v-bind:class="{ 'is-success': details.brunch }"
                                    @click='toggle_brunch()'>Brunch</div>
                            </div>
                            <div class="column">

                                <div class="button is-primary" @click="Submit(guest.id)">Submit</div>

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
                        wedding_rehearsal: this.details.wedding_rehearsal,
                        has_responded: this.details.has_responded
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
            toggle_has_responded: function () {
                this.details.has_responded = !this.details.has_responded
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
            },
            changehasresponded(payload) {
                this.details.has_responded = payload
            }
        }

    }
</script>

<style lang="scss" scoped>
    p {
        padding-bottom: 4%;
    }
</style>