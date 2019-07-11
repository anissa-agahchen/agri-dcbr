<template>
  <v-container grid-list-md text-xs-center>
    <v-layout row wrap>
      <v-card-title primary-title>
        <div>
          <h2>Profile</h2>
        </div>
      </v-card-title>
      <v-flex xs12>
        <v-card flat>
          <v-form v-model="valid">
            <v-container>
              <!--Name Section  -->
              <v-layout mx-2 mt-2>
                <h4>Name</h4>
              </v-layout>
              <v-layout row wrap mx-2>
                <v-flex xs12 md4>
                  <v-text-field v-model="firstname" :rules="nameRules" label="First name" required></v-text-field>
                </v-flex>
                <v-flex xs12 md4>
                  <v-text-field v-model="middlename" label="Middle name (optional)"></v-text-field>
                </v-flex>

                <v-flex xs12 md4>
                  <v-text-field v-model="lastname" :rules="nameRules" label="Last name" required></v-text-field>
                </v-flex>
              </v-layout>

              <!-- Home address section  -->
              <v-layout row mt-5 mx-2>
                <h4>Home Address</h4>
              </v-layout>
              <v-layout row wrap mx-2>
                <v-flex xs12 md4>
                  <v-text-field
                    v-model="streetNumber"
                    :rules="streetNumberRules"
                    label="Street number"
                    required
                  ></v-text-field>
                </v-flex>
                <v-flex xs12 md4 lg6>
                  <v-text-field v-model="aptNumber" label="Apt/Suite" required></v-text-field>
                </v-flex>
                <v-flex xs12 md4>
                  <v-text-field
                    v-model="streetName"
                    :rules="nameRules"
                    label="Street name"
                    required
                  ></v-text-field>
                </v-flex>
                <v-flex xs12 md4>
                  <v-text-field v-model="city" :rules="nameRules" label="City" required></v-text-field>
                </v-flex>
                <v-flex xs12 md4>
                  <v-text-field
                    v-model="postalCode"
                    :rules="nameRules"
                    label="Postal Code"
                    required
                  ></v-text-field>
                </v-flex>
                <v-flex xs12 md4>
                  <v-checkbox
                    v-model="homeAsOperation"
                    :label="`My home address is also my operation address`"
                  ></v-checkbox>
                  <!-- <label for="homeAsOperation">My home address is also my operation address</label> -->
                  <!-- <input type="checkbox" v-model="homeAsOperation" /> -->
                </v-flex>
              </v-layout>

              <!-- contact info  -->
              <v-layout row mt-5 mx-2>
                <h4>Contact</h4>
              </v-layout>
              <v-layout row mx-2>
                <!-- email -->
                <v-flex xs12 md4 lg6>
                  <v-text-field v-model="email" :rules="emailRules" label="E-mail" required></v-text-field>
                </v-flex>
                <!-- phone number -->
                <v-flex xs12 md4 lg6>
                  <v-text-field v-model="phone" :mask="mask" label="Phone"></v-text-field>
                </v-flex>
              </v-layout>
              <v-layout mx-2 mt-5>
                <subheader>What is the best way to contact you?</subheader>
              </v-layout>
              <v-layout mx-2>
                <v-radio-group v-model="commType" row>
                  <v-radio label="E-mail" value="Email"></v-radio>
                  <v-radio label="Mail" value="Mail"></v-radio>
                </v-radio-group>
              </v-layout>
            </v-container>
          </v-form>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>
<script>
export default {
  data: () => ({
    valid: false,
    firstname: "",
    lastname: "",
    middlename: "",
    streetnumber: "",
    aptNumber: "",
    streetName: "",
    postalCode: "",
    city: "",
    homeAsOperation: "",
    email: "",
    mask: "",
    phone: "",
    commType: "",
    nameRules: [
      v => !!v || "Name is required",
      v => v.length <= 50 || "Name must be less than 50 characters"
    ],
    email: "",
    emailRules: [
      v => !!v || "E-mail is required",
      v => /.+@.+/.test(v) || "E-mail must be valid"
    ],
    streetNumber: "",
    streetNumberRules: [v => !!v || "Street number is required"]

    //numberRules: [v => v.|| "Enter a valid number"]
  })
};
</script>
