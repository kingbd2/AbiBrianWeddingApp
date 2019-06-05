<template>
    <div>
        <div class="card large">
            <div class="card-image">
                <figure class="image">
                    <img src="https://images.unsplash.com/photo-1475778057357-d35f37fa89dd?dpr=1&auto=compress,format&fit=crop&w=1920&h=&q=80&cs=tinysrgb&crop="
                        alt="Image">
                </figure>
            </div>
            <div class="card-content">
                <div class="media">
                    <!-- <div class="media-left">
                        <figure class="image is-96x96">
                            <img src="https://i.imgsafe.org/a4/a4bb9acc5e.jpeg" alt="Image">
                        </figure>
                    </div> -->
                    <div class="media-content">
                        <p class="title is-4 no-padding has-text-primary">{{ details.title }}</p>
                        <p>{{ details.dates }}</p>
                        <p class="subtitle is-6 has-text-info">{{ details.price }}</p>
                        <p class="subtitle is-6 has-text-info">{{ details.bookby }}</p>
                        <p class="subtitle is-6 has-text-info">{{ details.location }}</p>
                        <p class="subtitle is-6 has-text-info">{{ details.transportation }}</p>
                        <p class="subtitle is-6 has-text-info">{{ details.bookhere }}</p>
                        <p class="subtitle is-6 has-text-info">{{ details.info }}</p>
                    </div>
                </div>
                <div class="content">
                    {{ details.title }}
                    <div class="background-icon"><span class="icon-twitter"></span></div>
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