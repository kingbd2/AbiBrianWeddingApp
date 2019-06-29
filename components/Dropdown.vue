<template>
    <div class="dropdown" :class="{'is-active': isActive}" @click="toggleActive(), emitToParent()">
        <div class="dropdown-trigger">
            <button class="button" :class="{'is-success': response}" aria-haspopup="true" aria-controls="dropdown-menu">
                <span>{{ response }}</span>
                <span class="icon is-small">
                    <i class="fas fa-angle-down" aria-hidden="true"></i>
                </span>
            </button>
        </div>
        <div class="dropdown-menu" id="dropdown-menu" role="menu">
            <div class="dropdown-content">
                <div class="dropdown-item" @click="response=true">
                    true
                </div>
                <div class="dropdown-item" @click="response=false">
                    false
                </div>
                
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        props: ['value'],
        data() {
            return {
                isActive: false,
                response: this.value
            }
        },
        methods: {
            toggleActive() {
                this.isActive = !this.isActive
            },
            emitToParent(event) {
                this.$emit('child-to-parent', this.response)
            }

        }
    }
</script>

<style>

</style>