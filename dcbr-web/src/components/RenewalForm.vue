<template>
  <v-layout>
    <v-container grid-list-md text-xs-center>
      <v-layout row wrap>
        <v-card-title primary-title>
          <div>
            <h2>Renewal</h2>
          </div>
        </v-card-title>
        <v-flex xs12>
          <v-card flat>
            <v-form v-model="valid">
              <v-container>
                <!--Name Section  -->
                <v-layout mx-2 mt-2>
                  <h4>Operator's Name</h4>
                </v-layout>
                <v-layout row wrap mx-2>
                  <v-flex xs12 md4>
                    <v-text-field
                      v-model="firstName"
                      :rules="nameRules"
                      label="First name"
                      name="firstName"
                      required
                    ></v-text-field>
                  </v-flex>
                  <v-flex xs12 md4>
                    <v-text-field
                      v-model="middleName"
                      :rules="middleNameRules"
                      label="Middle name (optional)"
                      name="middleName"
                    ></v-text-field>
                  </v-flex>

                  <v-flex xs12 md4>
                    <v-text-field
                      v-model="lastName"
                      :rules="nameRules"
                      label="Last name"
                      name="lastName"
                      required
                    ></v-text-field>
                  </v-flex>
                </v-layout>

                <v-layout mx-2 mt-2>
                  <h4>Registration Number</h4>
                </v-layout>
                <v-layout row wrap mx-2>
                  <v-flex xs12 md4>
                    <v-text-field
                      :rules="registrationNumberRules"
                      v-model="registrationNumber"
                      label="Reg #"
                      name="registrationNumber"
                      required
                    ></v-text-field>
                  </v-flex>
                  <v-flex xs12 md4>
                    <DatePicker />
                  </v-flex>
                </v-layout>
              </v-container>
            </v-form>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
  </v-layout>
</template>
<script>

import DatePicker from "@/components/DatePicker";
import { mapState } from "vuex";
export default {
  components: {
    DatePicker
  },
  data: () => ({
    valid: false,
    mask: "",
    nameRules: [
      v => !!v || "Name is required",
      v => v.length <= 50 || "Name must be less than 50 characters"
    ],
    registrationNumberRules: [
      v => !!v || "Registration number is required",
      v => v.length <= 50 || "Registration number must be less than 50 characters"
    ],
    middleNameRules: [
      v => v.length <= 50 || "Middle name must be less than 50 characters"
    ]
  }),
  computed: {
    ...mapState({
      renewal: state => state.renewal
    }),
    firstName: {
      // getter
      get() {
        return this.$store.getters["renewal/firstName"];
      },
      // setter
      set(value) {
        console.log(value);
        this.$store.dispatch("renewal/firstName", value);
      }
    },
    middleName: {
      // getter
      get() {
        return this.$store.getters["renewal/middleName"];
      },
      // setter
      set(value) {
        console.log(value);
        this.$store.dispatch("renewal/middleName", value);
      }
    },
    lastName: {
      // getter
      get() {
        return this.$store.getters["renewal/lastName"];
      },
      // setter
      set(value) {
        console.log(value);
        this.$store.dispatch("renewal/lastName", value);
      }
    },
    registrationNumber: {
      // getter
      get() {
        return this.$store.getters["renewal/registrationNumber"];
      },
      // setter
      set(value) {
        console.log(value);
        this.$store.dispatch("renewal/registrationNumber", value);
      }
    }
  }
};
</script>