<template>
    <div>
        <div class="card large">
            <div class="card-content">
                <div class="media">
                    <div class="media-content">
                        <div class="columns">
                            <div class="column is-1">
                                <div>{{ details.id }}</div>
                            </div>
                            <div class="column">
                                
                                <div><input class="input" type="text" placeholder="Event name"
                                        v-model="details.date"></div>
                            </div>
                            <div class="column is-2">
                                <div><input class="input" type="text" placeholder="Event name"
                                        v-model="details.event_name">
                                </div>
                            </div>
                            <div class="column">
                                <textarea class="textarea" type="text" placeholder="Details"
                                    v-model="details.details"></textarea>
                            </div>
                            <div class="column">
                                <div>{{ details.location_id }}</div>
                            </div>

                            <div class="column">
                                <div>
                                    <div class="button is-primary" @click="Submit(details.id)">Submit</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
            <!-- <div class="button is-primary" @click="Submit(item.id)">Submit changes</div> -->
    </div>
</template>

<script>
    import Dropdown from './Dropdown';
    import session from '../store/api/session';
    export default {
        components: {
            Dropdown
        },
        props: ['event'],
        data: function () {
            return {
                details: this.event,
                error: null,
                loading: false,
                events: null,
            }
        },
        methods: {
            Submit(id) {
                this.error = this.response = null
                this.loading = true
                console.log(id)
                const EVENT_URL = '/events/' + id + '/'
                return session.put(EVENT_URL, {
                        date: this.details.date,
                        end_time: this.details.end_time,
                        start_time: this.details.start_time,
                        event_name: this.details.event_name,
                        details: this.details.details,
                        location_id: this.details.location_id,

                    })
                    .then((res) => {
                        if (res.data) {
                            this.has_submitted = true
                            this.has_changed = false
                            this.loading = false
                            this.events = res.data
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
    p {
        padding-bottom: 4%;
    }
</style>