<template>
    <div>
        <div class="card large">
            <div class="card-image">
                <figure class="image">
                    <img :src="details.image" alt="Image">
                </figure>
            </div>
            <div class="card-content">
                <div class="media">
                    <div class="media-content">
                        <p class="title is-4 no-padding has-text-primary">{{ details.title }}</p>
                        <!-- </br> -->
                        <p class="is-size-6 has-text-info has-text-weight-bold" v-if="details.dates">{{ details.dates }}</p>
                        <p class="is-size-6 has-text-info has-text-weight-bold" v-if="details.price">{{ details.price }}</p>
                        <p class="is-size-6 has-text-info" v-if="details.bookby">{{ details.bookby }}</p>
                        <p class="is-size-6 has-text-info" v-if="details.location">{{ details.location }}</p>
                        <p class="is-size-6 has-text-info" v-if="details.transportation">{{ details.transportation }}</p>
                        <p class="is-size-6 has-text-info" v-if="details.bookhere">{{ details.bookhere }}</p>
                        <div v-for="item in details.info" :key="item.id">
                            <div v-if="item.isLink === false">
                                <div class="is-6 has-text-info"> {{ item.name }}</div>
                                </br>
                            </div>
                            <div v-else>
                                <a class="subtitle is-6" :href="item.url">
                                    <div class="is-6 has-text-primary"> {{ item.name }}</div>
                                </a>
                                </br>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        props: ['place'],
        data: function () {
            return {
                details: this.place
            }
        }

    }
</script>

<style lang="scss" scoped>
    p {
        padding-bottom: 4%;
    }

</style>