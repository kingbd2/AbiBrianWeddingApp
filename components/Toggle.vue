<template>
    <div>
        <div class="button" v-bind:class="{ 'is-success': is_attending }" @click='toggle_is_attending()'
            v-on:click="emitToParent">Yes</div>
        <div class="button" v-bind:class="{ 'is-success': !is_attending }" @click='toggle_is_attending()'
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
                error: null,
                response: null,
                guest_details: this.guest,
                event_type: this.eventType,
                has_submitted: false,
                has_changed: false,
            }
        },
        methods: {
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
            emitToParent(event) {
                this.$emit('childToParent', [this.guest.id, this.event_type, this.is_attending])
            }
        }
    }
</script>

<style>

</style>