<template>
    <div class="card">
        <div class="card-image">
            <figure class="image is-3by2">
                <img :src="photo.url" alt="Brian and Abi">
            </figure>
            <div class="card-content is-overlay is-clipped">
                <span class="tag is-info">
                    {{ photo.caption }}
                </span>
            </div>
        </div>
        <footer class="card-footer">
            <a class="card-footer-item">
                {{ photo.caption }}
            </a>
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