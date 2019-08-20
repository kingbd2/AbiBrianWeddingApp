<template>
  <div>
    <!-- <div class="container"> -->
    <section class="hero is-primary is-fullheight is-background">
      <div class="hero-head">
        <header>
          <div class="container">
            <div class="section">
              <div class="has-text-centered">
                <h1 class="title is-1 is-spaced has-text-info">Abiella & Brian are getting married!</h1>
                
                <h2 class="subtitle is-4 has-text-info">September 1st, 2019</h2>
                
                <h3 class="p is-4 has-text-info">Wildflowers Farm</h3>
                <h3 class="p is-4 has-text-info">42338 Fruit Ridge Line, St. Thomas, ON</h3>
              </div>
              <div class="container has-background-primary">
                <h1 class="shuttle-heading is-size-4 has-text-white has-text-weight-bold">Wedding Day Shuttle Information</h1>
                <ul class="is-size-6 has-text-white">
                  <li>2:30PM - 87 Tetherwood Blvd. Shuttle departs</li>
                  <li>2:45PM - Delta Armouries Shuttle departs</li>
                  <li>2:45PM - Windermere Manor Shuttle departs</li>
                  <li>10:30PM - Delta Armouries, Windermere Manor and 87 Tetherwood Blvd.</li>
                  <li>12:30AM - Delta Armouries, Windermere Manor and 87 Tetherwood Blvd.</li>
                </ul>
              </div>
              
            </div>
          </div>
        </header>
      </div>
    </section>

    <section class="hero is-fullheight is-primary is-background">
      <div class="hero-body">
        <div class="container has-text-centered">
          <div class="columns is-vcentered">
            <div class="column is-5">
              <figure class="image">
                <img src="../assets/images/front.png" style="border-radius:50%" alt="Description">
              </figure>
            </div>
            <div class="column is-6 is-offset-1">
              <div class="has-text-centered">
                <h1 class="title is-1 is-spaced has-text-info">We are very excited to celebrate with you!</h1>
                <h4 class="p is-4 has-text-info">Time until marriage:</h4>
                <h4 class="subtitle is-3 has-text-info">
                  <Countdown class="has-text-info" deadline="September 1, 2019"></Countdown>
                </h4>
              </div>
              <br>
            </div>
          </div>
        </div>
      </div>
    </section>

    <div v-if="showMap === true">
      <section class="hero is-small is-primary is-background">
        <div class="hero-body">
          <div class="container">
            <h1 class="title is-2 has-text-success">Our Wedding</h1>
            <p class="has-text-info">September 1st, 2019</p>
            <p class="has-text-info">Ceremony starts at 4:00 pm</p>
            <p class="has-text-info">Attire: Formal</p>
            <div class="columns is-vcentered">
              <div class="column is-one-half">
                <h1 class="title is-4 has-text-success">Ceremony and Reception</h1>
                <a href="https://wildflowers.farm/weddings">
                  <h3 class="button is-primary">Wildflowers Farm</h3>
                </a>
                <p class="has-text-info">42338 Fruit Ridge Line, St Thomas, Ontario, Canada N5P 3S9</p>
                </br>
                <p class="has-text-info">Come celebrate with us as we unite the Schneider-Friedman-King clans! The
                  wedding will take place at Wildflower Tea Farm in St. Thomas. Dress code is cocktail chic, and the
                  ceremony and cockails will be outside, weather permitting, so choose footwear accordingly. Plenty of
                  parking is availabe on-site, but should you prefer not to drive, we have shuttles leaving from the
                  Schneider-Friedman home, Delta Armories Downtown London, and the Windermere Manor. Check back here for
                  exact times.
                </p>
                </br>
                <p class="has-text-info">Schedule of Events (subject to change):</p>
                <ul class="has-text-info">
                  <li>
                    <p class="has-text-info">3:30 pm - Arrive at Wildflowers Tea Farm and enjoy a cool drink while you
                      wander the grounds</p>
                  </li>
                  <li>
                    <p class="has-text-info">4:00 pm - Ceremony </p>
                  </li>
                  <li>
                    <p class="has-text-info">4:45 pm - Cocktails</p>
                  </li>
                  <li>
                    <p class="has-text-info">6:00 pm - Dinner and Dancing</p>
                  </li>
                  <li>
                    <p class="has-text-info">12:30 am - Last Shuttle Leaves</p>
                  </li>
                </ul>
                </br>
                <p class="has-text-info has-text-weight-bold">To RSVP, use the link in the email you received from
                  abiella.and.brian@gmail.com. Please RSVP by July 15th, 2019. </p>
              </div>
              <div class="column">
                <location-map v-bind:center="[-80.44, 43.10]"></location-map>
              </div>
            </div>
            </br>
          </div>
        </div>
      </section>
    </div>

    <div v-else>
      <section class="hero is-small is-primary is-background">
        <div class="hero-body">
          <div class="container">
            <h1 class="title is-2 has-text-success">Our Wedding</h1>
            <p class="has-text-info">September 1st, 2019</p>
            <p class="has-text-info">Ceremony starts at 4:00 pm</p>
            <p class="has-text-info">Attire: Formal</p>
            <div class="columns is-vcentered">
              <div class="column is-one-half">
                <h1 class="title is-4 has-text-success">Ceremony and Reception</h1>
                <a href="https://wildflowers.farm/weddings">
                  <h3 class="button is-primary">Wildflowers Farm</h3>
                </a>
                <p class="has-text-info">42338 Fruit Ridge Line, St Thomas, Ontario, Canada N5P 3S9</p>
                </br>
                <p class="has-text-info">Come celebrate with us as we unite the Schneider-Friedman-King clans! The
                  wedding will take place at Wildflower Tea Farm in St. Thomas. Dress code is cocktail chic, and the
                  ceremony and cockails will be outside, weather permitting, so choose footwear accordingly. Plenty of
                  parking is availabe on-site, but should you prefer not to drive, we have shuttles leaving from the
                  Schneider-Friedman home, Delta Armories Downtown London, and the Windermere Manor. Check back here for
                  exact times.
                </p>
                </br>
                <p class="has-text-info">Schedule of Events (subject to change):</p>
                <ul class="has-text-info">
                  <li>
                    <p class="has-text-info">3:30 pm - Arrive at Wildflowers Tea Farm and enjoy a cool drink while you
                      wander the grounds</p>
                  </li>
                  <li>
                    <p class="has-text-info">4:00 pm - Ceremony </p>
                  </li>
                  <li>
                    <p class="has-text-info">4:45 pm - Cocktails</p>
                  </li>
                  <li>
                    <p class="has-text-info">6:00 pm - Dinner and Dancing</p>
                  </li>
                  <li>
                    <p class="has-text-info">12:30 am - Last Shuttle Leaves</p>
                  </li>
                </ul>
                </br>
                <p class="has-text-info has-text-weight-bold">To RSVP, use the link in the email you received from
                  abiella.and.brian @ gmail.com. Please RSVP by July 15th, 2019. </p>
              </div>
              <div class="column">
                <iframe
                  src="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d2931.112544048068!2d-81.2022724!3d42.7225086!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0xf8dd3f88028a4425!2sWildflowers+Farm!5e0!3m2!1sen!2sca!4v1560112295041!5m2!1sen!2sca"
                  width="600" height="450" frameborder="0" style="border:0" allowfullscreen></iframe>
              </div>
            </div>
            </br>
          </div>
        </div>
      </section>
    </div>

  </div>
</template>

<script>
  import Countdown from '../components/Countdown'
  import LocationMap from '../components/LocationMap'

  export default {
    components: {
      Countdown,
      LocationMap,
    },
    data: function () {
      return {
        showMap: 'false'
      }
    },
    mounted: function () {
      if (!mapboxgl.supported()) {
        this.showMap = false;
      } else {
        this.showMap = true;
      }
    }
  }
</script>

<style lang="scss" scoped>
  @import url('https://fonts.googleapis.com/css?family=Karla|Source+Serif+Pro');

  .title {
    font-family: 'Source Serif Pro', serif;
    padding-top: 10%;
    padding-bottom: 2%;
  }

  .subtitle {
    font-family: 'Karla', sans-serif;
    padding-bottom: 2%;
  }

  p {
    font-family: 'Karla', sans-serif;
  }

  .button {
    margin-bottom: 5%;
  }

  .subtitle.quote {
    padding-top: 2%;
  }

  .articles {
    padding-bottom: 5%;
    padding-top: 5%;
  }

  .container {
    margin-top: 5%;
  }

  .hero.is-primary.is-background {
    background: linear-gradient(rgba(255, 255, 255, .5), rgba(255, 255, 255, .99)), url('https://b0rtdg.bn.files.1drv.com/y4mUKhWv84jRu2sffpC_unLOD1mj7KsVbvKBnvKcXsgvHA54Vf4f1An1wG31t6yJnqKDYP3aUclf-b4s3bbD8JpmKMVY73vGJesWbp09zpMh96z1JPEb_1nS8jpCuXWn8uIArzw3I6iTShKuhnqcx9sxmfCogjKxNQI7fmzmnzVB_fKT_3L-7wwN4IpSBsJLJPkM_OwVjGIfbJJPnz4W4ahEg?width=1500&height=2000&cropmode=none') no-repeat center center fixed;
    -webkit-background-size: cover;
    -moz-background-size: cover;
    -o-background-size: cover;
    background-size: cover;
    image-rendering: -webkit-optimize-contrast;
    // -webkit-filter: grayscale(100%);
    /* Chrome, Safari, Opera */
    // filter: grayscale(100%);
  }

  .hero.is-info.is-background {
    background: linear-gradient(rgba(255, 255, 255, .9), rgba(255, 255, 255, .1)), url('../assets/images/front.png') no-repeat center center fixed;
    -webkit-background-size: cover;
    -moz-background-size: cover;
    -o-background-size: cover;
    background-size: cover;
    image-rendering: -webkit-optimize-contrast;
    // -webkit-filter: grayscale(100%);
    /* Chrome, Safari, Opera */
    // filter: grayscale(100%);
  }

  li {
    margin-bottom: 0.5%;
  }
  .shuttle-heading{
    margin-bottom: 1%;
  }

  .container .has-background-primary{
    padding-left: 10%;
    padding-top: 2%;
    padding-bottom: 2%;
  }
</style>