<template>
    <div class="card">
        <div class="card-image">
            <figure class="image">
                <img :src="photo.url" alt="Brian and Abi's photos"/>
            </figure>
            <!-- <div class="card-content is-overlay is-clipped">
                <span class="tag is-info">
                    {{ photo.caption }}
                </span>
            </div> -->
        </div>
        <footer class="card-footer">
            <div class="card-footer-item">
                {{ photo.caption }}
            </div>
        </footer>
    </div>
</template>

<script>
    export default {
        props: ['photo'],
        data: function () {
            return {
                image: this.photo
            }
        }

    }
</script>

<style>

</style>