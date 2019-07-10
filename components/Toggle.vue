<template>
    <div>
        <div class="button" v-bind:class="{ 'is-success': is_attending_yes }" @click='toggle_is_attending_yes()'
            v-on:click="emitToParent">Yes</div>
        <div class="button" v-bind:class="{ 'is-success': is_attending_no }" @click='toggle_is_attending_no()'
            v-on:click="emitToParent">No
        </div>
    </div>
</template>

<script>
    export default {
        props: ['guest', 'eventType'],
        data() {
            return {
                is_attending: false,
                is_attending_yes: false,
                is_attending_no: false,
                error: null,
                response: null,
                guest_details: this.guest,
                event_type: this.eventType,
                has_submitted: false,
                has_changed: false,
            }
        },
        methods: {
            toggle_is_attending_yes: function () {
                this.is_attending_no = false
                this.is_attending_yes = !this.is_attending_yes
                this.has_submitted = false
                this.has_changed = true
                if (this.is_attending_no === false & this.is_attending_yes === true ){
                    this.is_attending = true
                } else {
                    this.is_attending = false
                }
            },
            toggle_is_attending_no: function () {
                this.is_attending_yes = false
                this.is_attending_no = !this.is_attending_no
                this.has_submitted = false
                this.has_changed = true
                if (this.is_attending_no === true & this.is_attending_yes === false ){
                    this.is_attending = false
                }
            },
            emitToParent(event) {
                this.$emit('childToParent', [this.guest.id, this.event_type, this.is_attending])
            }
        },
    }
</script>

<style>

</style>