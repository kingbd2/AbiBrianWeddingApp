<template>
    <div>
        <div class="container" v-for="guest in guests" :key="guest.id">
            <p class="title is-4 has-text-primary">
                <!-- {{ guest.first_name }} {{ guest.last_name }} {{ guest.id }} -->
            </p>
            <table class="table">
                <thead>
                    <tr>
                        <th>Guest</th>
                        <th>Attending?</th>
                        <th>Dietary Restrictions?</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>{{ guest.first_name }} {{ guest.last_name }}</td>
                        <td>
                            <div class="button" v-bind:class="{ 'is-success': is_attending }" @click='toggle_is_attending()'>{{ yes_no_is_attending }}</div>
                        </td>
                        <td>
                            <div class="button" v-bind:class="{ 'is-success': has_dietary_restrictions }" @click='toggle_dietary_restrictions()'>{{ yes_no_dietary_restrictions }}</div>
                        </td>
                    </tr>
                </tbody>
            </table>
            <div class="button is-primary" @click='Rsvp(guest.id)'>Submit</div>
        </div>
    </div>
</template>

<script>
    import session from '../store/api/session';
    export default {
        props: ['guests'],
        data() {
            return {
                loading: false,
                is_attending: false,
                has_dietary_restrictions: false,
                error: null,
                response: null,
                party_guests: this.guests,
            }
        },
        methods: {
            Rsvp(id) {
                console.log(id)
                this.error = this.response = null
                this.loading = true
                const url = this.$route.params.uuid + '/guests/' + id + '/'
                console.log(url)
                return session.put(url, {
                        is_attending: true,
                    })
                    // .then((res) => {
                    //     if (res.data) {
                    //         this.loading = false
                    //         this.guests = res.data
                    //     } else {
                    //         context.error()
                    //     }
                    // })
                    .catch(error => {
                        console.log(error)
                        this.loading = false
                        this.error = "Please go to your wedding invitation email and try again."
                    })
            },
            toggle_is_attending: function () {
                this.is_attending = !this.is_attending
            },
            toggle_dietary_restrictions: function () {
                this.has_dietary_restrictions = !this.has_dietary_restrictions
            },
        },
        computed: {
            yes_no_is_attending: function () {
                if (this.is_attending === true) {
                    return "Yes"
                }
                else {
                    return "No"
                }
            },
            yes_no_dietary_restrictions: function () {
                if (this.has_dietary_restrictions === true) {
                    return "Yes"
                }
                else {
                    return "No"
                }
            }
        }
    }
</script>

<style lang="scss" scoped>

</style>