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
                        </br>
                        <p class="subtitle is-6 has-text-info has-text-weight-bold">{{ details.dates }}</p>
                        <p class="subtitle is-6 has-text-info has-text-weight-bold">{{ details.price }}</p>
                        <p class="subtitle is-6 has-text-info">{{ details.bookby }}</p>
                        <p class="subtitle is-6 has-text-info">{{ details.location }}</p>
                        <p class="subtitle is-6 has-text-info">{{ details.transportation }}</p>
                        <p class="subtitle is-6 has-text-info">{{ details.bookhere }}</p>
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

<style>

</style>