<template>
  <v-app class="grey lighten-4">
    <Navbar />
    <v-stepper flat>
      <v-stepper-header>
        <v-stepper-step complete editable step="1">Registration</v-stepper-step>

        <v-divider></v-divider>

        <v-stepper-step step="2">Payment($0)</v-stepper-step>

        <v-divider></v-divider>

        <v-stepper-step step="3">Review & submit</v-stepper-step>
      </v-stepper-header>
    </v-stepper>

    <v-content class="mx-4 mb-4 my-4">
      <v-container fluid>
        <v-stepper non-linear v-model="e6" vertical>
          <v-stepper-step editable :complete="e6 > 1" step="1">Profile</v-stepper-step>
          <v-stepper-content step="1">
            <Profile ref="profile" />
          </v-stepper-content>

          <v-stepper-step editable :complete="e6 > 2" step="2">Operation Details</v-stepper-step>
          <v-stepper-content step="2">
            <OperationDetails ref="operationdetails" />
          </v-stepper-content>

          <v-stepper-step editable :complete="e6 > 3" step="3">Operation Locations</v-stepper-step>

          <v-stepper-content step="3">
            <!-- <v-layout mt-4>
              <subheader>Do you have additional operation locations?</subheader>
            </v-layout>
            <v-radio-group v-model="row" row>
              <v-radio label="Yes" value="radio-1"></v-radio>
              <v-radio label="No" value="radio-2"></v-radio>
            </v-radio-group>-->
            <!-- <OperationLocation ref="operationlocation" /> -->
            <v-card-title primary-title>
              <h2>Operation Location(s)</h2>
            </v-card-title>

            <!-- <div v-for="(child, index) in children">
              <component :is="child" :key="child.name" v-bind:number="index+1"></component>
            </div>-->

            <div v-for="(child, index) in children">
              <OperationLocation ref="operationlocation{{index+1}}" v-bind:number="index+1" />
            </div>

            <v-btn @click.native="addLocation()">
              <v-btn-text>Add</v-btn-text>
              <v-icon dark>add</v-icon>
            </v-btn>

            <v-btn @click.native="removeLocation()">
              <v-btn-text>Remove</v-btn-text>
              <v-icon dark>remove</v-icon>
            </v-btn>

            <!-- <button @click="addLocation()">Add Another</button> -->
          </v-stepper-content>

          <v-stepper-step editable :complete="e6 > 4" step="4">Animal Identification</v-stepper-step>
          <AnimalIdentification ref="animalidentification" />
          <!-- <v-stepper-content step="4">
            <AnimalIdentification/>
          </v-stepper-content>-->

          <v-stepper-step editable :complete="e6 > 5" step="5">Breeding Details</v-stepper-step>
          <BreedingDetails ref="breedingdetails" />
          <!-- <v-stepper-content step="5">
            <BreedingDetails/>
          </v-stepper-content>-->
        </v-stepper>

        <v-btn
          large
          block
          round
          mt-5
          class="blue darken-4 white--text"
          @click.native="createOperator"
        >Submit</v-btn>
      </v-container>
    </v-content>
    <Footer />
  </v-app>
</template>


<script>
import Navbar from "@/components/Navbar";
import OperationDetails from "@/components/OperationDetails";
import Profile from "@/components/Profile";
import OperationLocation from "@/components/OperationLocation";
//import OpLocation2 from "@/components/OpLocation2";
import AnimalIdentification from "@/components/AnimalIdentification";
import BreedingDetails from "@/components/BreedingDetails";
import Footer from "@/components/Footer";
import axios from "axios";

export default {
  name: "App",
  components: {
    Navbar,
    Profile,
    OperationDetails,
    OperationLocation,
    //OpLocation2,
    // Vet,
    AnimalIdentification,
    BreedingDetails,
    Footer
  },
  data() {
    return {
      e6: 1,
      errors: [],
      children: []
    };
  },
  methods: {
    createOperator() {
      console.log("Submit clicked");
      axios
        .post("http://localhost:8080/api/operator/", {
          // for localhost, use "http://localhost:8080/api/operator"
          // before deploying to Openshift, use "/api/operator"
          first_name: this.$refs.profile.firstname,
          middle_name: this.$refs.profile.middlename,
          last_name: this.$refs.profile.lastname,
          comm_pref: this.$refs.profile.commType,
          phone_num: this.$refs.profile.phone,
          email_address: this.$refs.profile.email,
          operation_type: this.$refs.operationdetails.operationType,
          operation_name: this.$refs.operationdetails.operationName,
          operation_URL: this.$refs.operationdetails.opWebsite,

          addresses: [
            {
              type: "PRI",
              street_num: this.$refs.profile.streetNumber,
              suite: this.$refs.profile.aptNumber,
              street_name: this.$refs.profile.streetName,
              city: this.$refs.profile.city,
              postal_code: this.$refs.profile.postalCode
            }
          ],
          associations: [
            {
              assoc_name: this.$refs.operationdetails.assocName,
              membership_num: this.$refs.operationdetails.assocMembership,
              assoc_URL: this.$refs.operationdetails.assocWebsite
            }
          ],
          risk_factor_animals: [
            {
              num_dogs_intact: this.$refs.breedingdetails.femaleDogNum,
              num_litter_whelped: this.$refs.breedingdetails.littersWhelped,
              num_cats_intact: this.$refs.breedingdetails.femaleIntactCat,
              num_litter_queened: this.$refs.breedingdetails.littersQueened,
              num_dog_sold: this.$refs.breedingdetails.dogsSold,
              num_dog_transferred: this.$refs.breedingdetails.dogsTransferred,
              num_dog_traded: this.$refs.breedingdetails.dogsTraded,
              num_dog_leased: this.$refs.breedingdetails.dogsLeased,
              num_cat_sold: this.$refs.breedingdetails.catsSold,
              num_cat_transferred: this.$refs.breedingdetails.catsTransferred,
              num_cat_traded: this.$refs.breedingdetails.catsTraded,
              num_cat_leased: this.$refs.breedingdetails.catsLeased
            }
          ],
          risk_factor_operations: [
            {
              accidental_breeding: this.$refs.operationdetails.accident,
              num_workers: this.$refs.operationdetails.numWorkers,
              animal_type: this.$refs.operationdetails.animalType,
              num_breeds_dogs: this.$refs.operationdetails.numDogBreeds,
              num_breeds_cats: this.$refs.operationdetails.numCatBreeds,
              has_vet: this.$refs.operationdetails.hasVet,
              has_perm_id: this.$refs.animalidentification.hasId,
              perm_id_type: this.$refs.animalidentification.idType,
              perm_id_other: this.$refs.animalidentification.otherId
            }
          ]
        })
        .then(response => {})
        .catch(e => {
          this.errors.push(e);
        });
    },
    addLocation() {
      // <OperationLocations ref="operationlocations" />;
      // this.children.push(OperationLocation);
      this.children.push(OperationLocation);
    },
    removeLocation() {
      // <OperationLocations ref="operationlocations" />;
      // this.children.push(OperationLocation);
      this.children.pop();
    }
  }
};
</script>

