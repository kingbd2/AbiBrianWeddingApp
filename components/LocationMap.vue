<template>
    <div>
        <script src='https://api.tiles.mapbox.com/mapbox-gl-js/v0.51.0/mapbox-gl.js'></script>
        <link href='https://api.tiles.mapbox.com/mapbox-gl-js/v0.51.0/mapbox-gl.css' rel='stylesheet' />
        <mapbox access-token="pk.eyJ1Ijoia2luZ2JkMiIsImEiOiJjam96MDIxOGQwNDQzM3BwOTBja2ExbmRwIn0.F1hx0bbEkNrblMCKVOQM5A"
            @map-load="mapLoaded" :map-options="{
          style: 'mapbox://styles/mapbox/light-v9',
          center: [-80.44, 43.10],
          zoom: 7
        }" :geolocate-control="{
  show: true,
  position: 'top-left'
}" :scale-control="{
  show: true,
  position: 'top-left'
}" :fullscreen-control="{
  show: true,
  position: 'top-left'
}">
        </mapbox>

    </div>
</template>

<script>
    import Mapbox from 'mapbox-gl-vue';

    export default {
        name: 'LocationMap',
        components: {
            'mapbox': Mapbox,
        },
        methods: {
            mapLoaded(map) {
                map.addLayer({
                    'id': 'points',
                    'type': 'symbol',
                    'source': {
                        'type': 'geojson',
                        'data': {
                            'type': 'FeatureCollection',
                            'features': [{
                                    'type': 'Feature',
                                    'geometry': {
                                        'type': 'Point',
                                        'coordinates': [-81.19, 42.72]
                                    },
                                    'properties': {
                                        'title': 'Wildflowers Farm',
                                        'icon': 'circle'
                                    }
                                },
                                // {
                                //     'type': 'Feature',
                                //     'geometry': {
                                //         'type': 'Point',
                                //         'coordinates': [-122.414, 37.776]
                                //     },
                                //     'properties': {
                                //         'title': 'Mapbox SF',
                                //         'icon': 'harbor'
                                //     }
                                // }
                            ]
                        }
                    },
                    'layout': {
                        'icon-image': '{icon}-15',
                        'text-field': '{title}',
                        'text-font': ['Open Sans Semibold', 'Arial Unicode MS Bold'],
                        'text-offset': [0, 0.6],
                        'text-anchor': 'top'
                    }
                });
            },

        }

    }
</script>

<style lang="scss" scoped>
    #map {
        width: 100%;
        height: 400px;
    }
</style>