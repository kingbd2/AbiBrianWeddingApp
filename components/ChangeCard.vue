<template>
    <div>
        <div class="card large">
            <div class="card-content">
                <div class="media">
                    <div class="media-content">
                        <div class="columns">
                            <div class="column is-1">
                                <div>{{ guest.id }}</div>
                            </div>
                            <div class="column">
                                <div>{{ guest.first_name }} {{ guest.last_name }}</div>
                            </div>
                            <div class="column">
                                <div>{{ guest.party }}</div>
                            </div>
                            <div class="column is-2">
                                <div><input class="input" type="text" placeholder="Group" v-model="guest.group">
                                </div>
                            </div>
                            <div class="column">
                                <div>{{ guest.is_attending }}</div>
                            </div>
                            <div class="column">
                                <div>{{ guest.has_dietary_restrictions }} {{ guest.dietary_restrictions }}</div>
                            </div>
                            <div class="column">
                                <dropdown :value="guest.iskid" @child-to-parent="changekid"></dropdown>
                                <!-- <div>{{ guest.iskid }}</div> -->
                            </div>
                            <div class="column">
                                <dropdown :value="guest.brunch" @child-to-parent="changebrunch"></dropdown>
                                <!-- <div>{{ guest.brunch }}</div> -->
                            </div>
                            <div class="column">
                                <dropdown :value="guest.shabbat" @child-to-parent="changeshabbat"></dropdown>
                            </div>
                            <div class="column">
                                <dropdown :value="guest.rehearsal_dinner" @child-to-parent="changerehearsal"></dropdown>
                            </div>
                            <div class="column">
                                <div>
                                    <div class="button is-primary" @click="Submit(guest.id)">Submit</div>
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
                        rehearsal_dinner: this.details.rehearsal

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
            changekid(payload) {
                this.details.iskid = payload
            },
            changeshabbat(payload) {
                this.details.shabbat = payload
            },
            changebrunch(payload) {
                this.details.brunch = payload
            },
            changerehearsal(payload) {
                this.details.rehearsal = payload
            }
        }

    }
</script>

<style lang="scss" scoped>
    p {
        padding-bottom: 4%;
    }
</style>