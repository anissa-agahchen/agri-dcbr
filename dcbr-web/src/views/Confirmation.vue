
<template>
  <v-layout>
    <v-flex ma-5 xs9 sm12>
      <v-card class="grey lighten-4">
        <v-container fill-height fluid>
          <v-layout fill-height>
            <v-flex xs12 class="text-md-center" flexbox>
              <span class="headline green--text">Congratulations!</span>
              <br />
              <span
                class="subheadline"
              >You are now a registerred operator/seller in the province of Brtish Columbia</span>
              <br />
              <span
                class="subheadline"
              >An email notification has been sent to your email along with your registration certificate and standard of care act</span>
            </v-flex>
          </v-layout>
        </v-container>

        <v-card-title>
          <div>
            <span class="grey--text">Your Registration Number:</span>
            <br />
            <span class="subheading">DG-253-672</span>
            <br />
          </div>
        </v-card-title>
        <v-card-title>
          <div>
            <span class="grey--text">Renewal date :</span>
            <br />
            <span class="subheading">Oct, 21, 2020</span>
            <br />
          </div>
        </v-card-title>
        <v-card-title>
          <div>
            <span class="grey--text">Your status as an operator/seller:</span>
            <br />
            <span class="success--text subheading">Active</span>
            <br />
          </div>
        </v-card-title>
        <v-card-actions>
          <v-layout justify-center />
          <v-flex>
            <v-btn flat color="primary">go to my profile</v-btn>
          </v-flex>
        </v-card-actions>
      </v-card>
    </v-flex>
  </v-layout>
</template>